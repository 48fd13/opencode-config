#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load_config(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        raise RuntimeError(f"failed to parse {path.name}: {exc}")


def extract_prompt_paths(value) -> list[str]:
    paths: list[str] = []
    if isinstance(value, dict):
        for nested in value.values():
            paths.extend(extract_prompt_paths(nested))
    elif isinstance(value, list):
        for nested in value:
            paths.extend(extract_prompt_paths(nested))
    elif isinstance(value, str):
        match = re.fullmatch(r"\{file:(.+)\}", value.strip())
        if match:
            paths.append(match.group(1))
    return paths


def main() -> int:
    errors: list[str] = []

    required_paths = [
        ROOT / "opencode.json",
        ROOT / "AGENTS.md",
        ROOT / ".opencode" / "agents",
        ROOT / ".opencode" / "skills",
        ROOT / ".opencode" / "skills" / "repo-bootstrap" / "SKILL.md",
    ]

    for path in required_paths:
        if not path.exists():
            errors.append(f"missing required path: {path.relative_to(ROOT)}")

    config_path = ROOT / "opencode.json"
    if config_path.exists():
        try:
            config = load_config(config_path)
            prompt_paths = extract_prompt_paths(config.get("agent", {}))
            for prompt_path in sorted(set(prompt_paths)):
                full_path = ROOT / prompt_path
                if not full_path.exists():
                    errors.append(
                        f"prompt file not found: {prompt_path} (from opencode.json)"
                    )
        except RuntimeError as exc:
            errors.append(str(exc))

    if errors:
        print("OpenCode setup check failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OpenCode setup check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
