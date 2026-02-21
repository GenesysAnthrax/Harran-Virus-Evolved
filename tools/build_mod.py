#!/usr/bin/env python3
"""Builds the Harran Virus Evolved mod override files from a balance profile."""
from __future__ import annotations

import json
from pathlib import Path
from string import Template

ROOT = Path(__file__).resolve().parents[1]
MOD_ROOT = ROOT / "mods" / "HarranVirusEvolved"
PROFILE_PATH = MOD_ROOT / "profiles" / "default.profile.json"
TEMPLATE_DIR = MOD_ROOT / "data" / "templates"
OUTPUT_DIR = MOD_ROOT / "generated"

TEMPLATES = {
    "zombie_stats.xml.tpl": "zombie_stats.xml",
    "special_abilities.xml.tpl": "special_abilities.xml",
    "spawn_rules.xml.tpl": "spawn_rules.xml",
}


def load_profile(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def flatten(profile: dict) -> dict:
    values: dict[str, str] = {}

    def walk(prefix: str, data: object) -> None:
        if isinstance(data, dict):
            for key, value in data.items():
                walk(f"{prefix}_{key}" if prefix else key, value)
        else:
            values[prefix.upper()] = str(data)

    walk("", profile)
    return values


def render_templates(values: dict[str, str]) -> list[Path]:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    for source_name, output_name in TEMPLATES.items():
        source_path = TEMPLATE_DIR / source_name
        output_path = OUTPUT_DIR / output_name

        text = source_path.read_text(encoding="utf-8")
        rendered = Template(text).safe_substitute(values)
        output_path.write_text(rendered, encoding="utf-8")
        written.append(output_path)

    return written


def main() -> None:
    profile = load_profile(PROFILE_PATH)
    values = flatten(profile)
    written = render_templates(values)
    print("Generated files:")
    for path in written:
        print(f" - {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
