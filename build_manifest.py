#!/usr/bin/env python3
"""Génère le manifest JSON pour up-functions à partir des métadonnées PHPDoc/JSdoc."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, List, Optional

BASE_DIR = Path(__file__).parent
MANIFEST_PATH = BASE_DIR / "manifest.json"
SOURCE_GLOBS = [
    "inc/**/*.php",
    "inc/**/*.js",
]

DOC_PATTERN = re.compile(r"/\*\*(.*?)\*/", re.DOTALL)
FIELD_PATTERN = re.compile(r"^([A-Za-zÀ-ÖØ-öø-ÿ'`\- ]+)\s*:\s*(.+)$")


def _read_doc_fields(content: str) -> Dict[str, str]:
    match = DOC_PATTERN.search(content)
    if not match:
        return {}

    block = match.group(1)
    fields: Dict[str, str] = {}
    for raw_line in block.splitlines():
        line = raw_line.strip().lstrip("* ").strip()
        if not line or line.startswith("@"):
            continue
        field_match = FIELD_PATTERN.match(line)
        if not field_match:
            continue
        key = field_match.group(1).strip().lower()
        value = field_match.group(2).strip()
        fields[key] = value
    return fields


def _build_entry(path: Path, fields: Dict[str, str]) -> Optional[Dict[str, object]]:
    rel_path = path.relative_to(BASE_DIR)
    slug = path.stem

    description = fields.get("description") or fields.get("description ")
    if not description:
        # Fallback: short sentence from filename
        description = f"Module {slug.replace('-', ' ')}"

    # Name derived from description (first sentence) or slug capitalised
    name = fields.get("nom")
    if not name:
        name = description.split(".")[0].strip().capitalize()
        if not name:
            name = slug.replace('-', ' ').title()

    category_raw = fields.get("catégorie") or fields.get("categorie") or "Modules"
    categories: List[str] = [c.strip() for c in re.split(r",|/|;", category_raw) if c.strip()]
    if not categories:
        categories = ["Modules"]

    version = fields.get("version") or "1.0.0"

    # Installer: on copie par défaut sous functions/<...>
    if rel_path.suffix == ".php":
        file_key = "php"
    elif rel_path.suffix == ".js":
        file_key = "script"
    else:
        file_key = "file"

    install_path = "functions/" + str(rel_path.parent).replace("\\", "/")

    entry = {
        "slug": slug,
        "name": name,
        "description": description,
        "version": version,
        "categories": categories,
        "files": {
            file_key: str(rel_path).replace("\\", "/"),
        },
        "install": {
            file_key: install_path,
        },
    }

    return entry


def collect_entries() -> List[Dict[str, object]]:
    entries: List[Dict[str, object]] = []
    for pattern in SOURCE_GLOBS:
        for path in BASE_DIR.glob(pattern):
            if path.name.startswith("."):
                continue
            if path.is_dir():
                continue
            content = path.read_text(encoding="utf-8")
            fields = _read_doc_fields(content)
            entry = _build_entry(path, fields)
            if entry:
                entries.append(entry)
    entries.sort(key=lambda e: e["slug"])  # type: ignore[index]
    return entries


def build_manifest(entries: List[Dict[str, object]]) -> Dict[str, object]:
    return {
        "patterns": entries,
    }


def main() -> None:
    entries = collect_entries()
    manifest = build_manifest(entries)
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Manifest généré avec {len(entries)} entrées → {MANIFEST_PATH}")


if __name__ == "__main__":
    main()
