# Wistia Latest Medias Script

This repository contains a small script `wistia_lastest.sh.py` that fetches the latest media items from the Wistia API.

Setup

1. Copy the example env into `.env` and add your Wistia API token:

```bash
cp .env.example .env
# then edit .env and set WISTIA_TOKEN to your real token
```

2. Create and activate a virtualenv (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Usage

- Print full JSON:

```bash
python3 wistia_lastest.sh.py
```

- Print summary (created | hashed_id | name):

```bash
python3 wistia_lastest.sh.py --summary --limit 5
```

Notes

- `.env` is ignored via `.gitignore`. Keep secrets out of version control.
- The script reads `WISTIA_TOKEN` from the environment; using a `.env` file is convenient for local development.

# Wistia-API-Test
