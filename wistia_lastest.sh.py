#!/usr/bin/env python3
import os
import sys
import json
import argparse
from typing import Any, List

import requests

from dotenv import load_dotenv

load_dotenv()


def fetch_latest_medias(token: str, limit: int) -> List[Any]:
    url = "https://api.wistia.com/v1/medias.json"
    params = {
        "sort_by": "created",
        "sort_direction": "desc",
        "per_page": limit,
        "page": 1,
    }
    headers = {"Authorization": f"Bearer {token}"}

    resp = requests.get(url, params=params, headers=headers, timeout=30)
    if resp.status_code != 200:
        raise RuntimeError(
            f"Wistia API error {resp.status_code}: {resp.text.strip()}"
        )

    data = resp.json()
    if not isinstance(data, list):
        raise RuntimeError(f"Unexpected response shape: {type(data)}")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch latest Wistia medias.")
    parser.add_argument("--limit", type=int, default=10, help="How many to fetch (default 10)")
    parser.add_argument("--summary", action="store_true", help="Print a concise summary instead of full JSON")
    parser.add_argument("--json", action="store_true", help="Force full JSON output (default if --summary not set)")
    args = parser.parse_args()

    token = os.environ.get("WISTIA_TOKEN", "").strip()
    if not token:
        print("Error: set WISTIA_TOKEN environment variable.", file=sys.stderr)
        print('Example: export WISTIA_TOKEN="YOUR_TOKEN"', file=sys.stderr)
        return 2

    medias = fetch_latest_medias(token, args.limit)

    if args.summary:
        for m in medias:
            created = m.get("created", "")
            hashed_id = m.get("hashed_id", "")
            name = m.get("name", "")
            print(f"{created} | {hashed_id} | {name}")
        return 0

    # Default: print full JSON
    print(json.dumps(medias, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())