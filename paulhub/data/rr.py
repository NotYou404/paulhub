import json
from pathlib import Path
from typing import Optional


def increment_rickroll(origin: Optional[str] = None):
    if origin is None:
        origin = "null"

    path = Path(__file__).parent / "rrs.json"
    if not path.exists():
        with open(path, "w", encoding="utf-8") as fp:
            fp.write("{}")

    content = json.loads(path.read_text("utf-8"))
    if origin in content:
        content[origin] += 1
    else:
        content[origin] = 1
    with open(path, "w", encoding="utf-8") as fp:
        json.dump(content, fp)
