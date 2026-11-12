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

## Step 7 — See what your .env actually calls things

Your `.env` does **not** hold a single connection URL. It holds `DB_TYPE=mysql` and the rest split
across separate variables. That is normal; we just need their names.

Paste this one line. **It prints variable NAMES only, never values** — nothing secret appears:

```
grep -o '^[A-Za-z_]*' ~/Documents/"Cargo Sales"/cargo-sales-app/backend/.env | sort -u
```

**You should see** a list like `DB_HOST`, `DB_NAME`, `DB_PASSWORD`, `DB_PORT`, `DB_TYPE`,
`DB_USER` — possibly with other unrelated names mixed in.

**Send me that list.** It is safe to paste into chat: names, no values.

---

## Step 8 — Build the connection string without ever displaying your password

Once the names are confirmed, paste this **whole block** at once (it is one unit, unlike the other
steps). It reads the `.env`, assembles the URL, and prints it back **with the password masked**:

```
set -a; source ~/Documents/"Cargo Sales"/cargo-sales-app/backend/.env; set +a
export CSI_DB_URL="mysql+pymysql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT:-3306}/${DB_NAME}"
echo "${CSI_DB_URL/:$DB_PASSWORD@/:********@}"
```

**You should see** one line like:

```
mysql+pymysql://csi_readonly:********@some-host.com:3306/csi_production
```

Check that the user, host and database name look right. **If any part is blank** — you see `//:` or
`@:3306/` with nothing between — the variable names differ from the guess. Send me the step 7 list
and I will give you the corrected block.

**Note the `mysql+pymysql://` prefix.** That is not a typo; it tells SQLAlchemy to use the PyMySQL
driver you installed in step 6.

**Use the read-only user.** If `.env` holds an admin account, swap `${DB_USER}` and
`${DB_PASSWORD}` for the read-only credentials. Nothing here writes, but the read-only user is what
makes that a guarantee rather than a promise.

**This lasts only until you close Terminal.** To keep it, paste:

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
