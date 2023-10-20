from pathlib import Path
from typing import Any

import tomllib

DEFAULTS = {"include_source_dir_in_test_path": True}


def parse_pyproject_toml(path: str) -> dict[str, Any]:
    with Path(path).open("rb") as f:
        pyproject_toml = tomllib.load(f)
    config: dict[str, Any] = pyproject_toml.get("tool", {}).get("autopytest", {})

    return {**DEFAULTS, **config}
