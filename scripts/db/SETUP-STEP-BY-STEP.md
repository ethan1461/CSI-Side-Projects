# Database exports — step by step

Written to be followed exactly, in order, without deciding anything.

**Do one step at a time.** Copy the command, paste it, press Enter, read what comes back, then go
to the next step. Where a step says "you should see", check that you see roughly that before
continuing. If you don't, stop and send me what you got instead.

---

## Step 1 — Open Terminal

Press **Cmd + Space**, type `Terminal`, press Enter. A window with a text prompt opens.

Everything below is typed into that window.

---

## Step 2 — Go to the folder that holds your projects

Copy and paste this one line, press Enter:

```
cd ~/Documents/"Cargo Sales"
```

Then paste this, press Enter:

```
pwd && ls
```

**You should see** a path ending in `Cargo Sales`, and a list that includes `cargo-sales-app`.

If you get `No such file or directory`, your folder is somewhere else. Run `ls ~/Documents` and
tell me what you see.

---

## Step 3 — Download the agent repo next to it

One line, press Enter:

```
git clone https://github.com/ethan1461/CSI-Side-Projects.git
```

**You should see** several lines ending in something like `Resolving deltas: 100% ... done.`

If it asks for a username and password, stop — you need GitHub set up on the command line and I'll
walk you through that separately.

---

## Step 4 — Go into it and switch to the right branch

**This step matters.** All the work is on a branch, not on `main`. Skip it and the scripts
won't be there.

Paste these two lines one at a time:

```
cd CSI-Side-Projects
```

```
git checkout claude/csi-agent-team-setup-cs9rwk
```

**You should see** `Switched to a new branch 'claude/csi-agent-team-setup-cs9rwk'` or
`branch set up to track ...`.

Now check the scripts arrived:

```
ls scripts/db
```

**You should see** four files: `README.md`, `SETUP-STEP-BY-STEP.md`, `_conn.py`,
`export_bookings_monthly.py`.

---

## Step 5 — Build a private Python environment for this folder

This keeps these packages from interfering with anything else on your machine.

Paste this one line, press Enter:

```
python3 -m venv .venv
```

Nothing visible happens. That's correct — it takes a few seconds and prints nothing.

Then paste this, press Enter:

```
source .venv/bin/activate
```

**You should see** your prompt change so it now starts with `(.venv)`.

**That `(.venv)` prefix matters.** If you close Terminal and come back later, you must run
`cd ~/Documents/"Cargo Sales"/CSI-Side-Projects` and then `source .venv/bin/activate` again before
running any script. If the prefix isn't there, the script won't find its packages.

---

## Step 6 — Install the packages

First, open the requirements file to pick your database driver:

```
open -e requirements-db.txt
```

TextEdit opens. You'll see two driver lines near the bottom:

```
psycopg[binary]>=3.1   # PostgreSQL
# PyMySQL>=1.1         # MySQL / MariaDB
```

- **If your database is PostgreSQL** — change nothing. Close the window.
- **If it's MySQL or MariaDB** — put a `#` at the start of the `psycopg` line, and delete the `#`
  from the start of the `PyMySQL` line. Save with **Cmd + S**, then close.

Not sure which you have? Step 7 will tell you — your connection string starts with `postgresql://`
or `mysql://`. Come back and fix this after if needed.

Now install, one line:

```
pip install -r requirements-db.txt
```

**You should see** a lot of scrolling and then `Successfully installed ...` at the end.

---

## Step 7 — Find your database connection string

It's already on your machine, in the backend's environment file. Paste this one line:

```
grep -i "database_url\|db_url\|postgres\|mysql" ~/Documents/"Cargo Sales"/cargo-sales-app/backend/.env
```

**You should see** one or more lines containing something shaped like:

```
postgresql://someuser:somepassword@some-host.com:5432/somedatabase
```

Copy **just that URL part** — from `postgresql://` (or `mysql://`) to the end. Not the
`DATABASE_URL=` prefix, and no quotes.

**Use the read-only user** if there's more than one. You said you have read-only credentials — that
is the one to use here. Nothing in these scripts writes, but the read-only user is what makes that
a guarantee rather than a promise.

---

## Step 8 — Tell the script where the database is

Paste this, but **replace everything between the quotes** with the URL you just copied:

```
export CSI_DB_URL='postgresql://readonly_user:password@host:5432/dbname'
```

**Keep the single quotes.** They protect characters in the password.

Nothing visible happens. That's correct.

Check it took:

```
echo $CSI_DB_URL
```

**You should see** your URL printed back.

**This lasts only until you close Terminal.** To make it permanent, paste this one line — it
appends the same line to your shell startup file:

```
echo "export CSI_DB_URL='$CSI_DB_URL'" >> ~/.zshrc
```

**Never put this URL in a file inside the repo, and never commit it.**

---

## Step 9 — Run the export

```
python scripts/db/export_bookings_monthly.py
```

**If it works**, you'll see three lines like:

```
rows in from database: 57
rows out to db-bookings-monthly.csv: 57
wrote db-bookings-monthly.meta.json
```

**If you get an error mentioning a table or column** — `csi_bookings`, `registration_date`,
`status_id`, `hidden` — that's expected and not your fault. I wrote that query from a screenshot and
have never seen your real schema. **Send me the error and I'll fix the file.**

**If you get `CSI_DB_URL is not set`** — Terminal was closed and reopened. Redo step 8.

---

## Step 10 — Send the result back to me

Three lines, one at a time:

```
git add data/derived/
```

```
git commit -m "Refresh monthly bookings export"
```

```
git push
```

**You should see** output ending in something like `main -> ...` or
`claude/csi-agent-team-setup-cs9rwk -> claude/csi-agent-team-setup-cs9rwk`.

Done. I can now read that data, and the database itself never left your machine.

---

## Every time after this

Four lines:

```
cd ~/Documents/"Cargo Sales"/CSI-Side-Projects
source .venv/bin/activate
git pull
python scripts/db/export_bookings_monthly.py
```

Then the three `git` lines from Step 10.

Say which question you want answered and I'll write a new script into `scripts/db/`. You `git pull`,
run it, push. You never write SQL and I never see the database.
