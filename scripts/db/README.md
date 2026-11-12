# Running database exports locally

**Why this exists.** CSI's production database is reachable only from Ethan's machine. The agent
team runs in the cloud. Rather than exposing the database to the network, the two are connected
through this repository: **scripts are committed here, run locally against the database, and their
aggregated outputs are committed back.**

Production credentials never leave the local machine. For a system holding decedent and family
data (`CLAUDE.md §7.2`), that is the design, not a workaround.

## The loop

```
  write a script here  ──▶  run it locally  ──▶  output to data/derived/  ──▶  commit + push
         ▲                   (reads the DB)         (aggregated only)              │
         └──────────────────────────────────────────────────────────────────────────┘
                              agents read data/derived/, never the DB
```

## One-time setup on the local machine

```bash
git clone <this repo>                 # alongside cargo-sales-app, not inside it
cd CSI-Side-Projects
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-db.txt
```

Then set the connection string **in the shell, never in a file**:

```bash
export CSI_DB_URL='postgresql://readonly_user:...@host:5432/dbname'
```

Put that line in `~/.zshrc` if it should persist. **Do not** put it in `.env`, and do not commit it
(`CLAUDE.md §8`: no credentials in code, config only).

Use the **read-only** user. Every script here opens a read-only connection and none issues a write,
but the database user is the backstop that makes that guarantee real rather than aspirational.

## Running one

```bash
python scripts/db/export_bookings_monthly.py
git add data/derived/ && git commit -m "Refresh monthly bookings export" && git push
```

Agents then read `data/derived/`. They never see the database and never need to.

## Rules for scripts in this directory

1. **Aggregate before it leaves the database.** `GROUP BY` in SQL, not a filter in pandas after a
   full table lands in memory. Row-level operational data should not be written to disk at all
   unless a specific analysis needs it, and then only to `data/raw/` (gitignored).
2. **Never select a name column.** Decedent and family names appear in operational tables
   (`§7.2` lists where). Select the columns you need by name; never `SELECT *`.
3. **Read-only.** No `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`. If a script needs to write,
   it does not belong here.
4. **Idempotent.** Same input, same output. Safe to re-run.
5. **Every output gets a `.meta.json`** — source, row count, script version, run timestamp, and
   any columns deliberately dropped.
6. **Log row counts in and out.** Unexplained row loss is a bug (`§8`).

## If the backend already has a query helper

`cargo-sales-app/backend` has its own helper and venv. If it is easier to use it, a script can be
run from there instead — the important part is that **the output lands in this repo's
`data/derived/` and gets committed.** The loop is what matters, not the driver.
