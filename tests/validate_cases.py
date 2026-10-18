#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 innerVANI contributors
# SPDX-License-Identifier: Apache-2.0
"""Check test-case files against the schema and the rules that span files.

Usage:
    python tests/validate_cases.py                 # every case in tests/public/
    python tests/validate_cases.py path/to/*.yaml  # chosen files

Needs PyYAML and jsonschema (pip install pyyaml jsonschema).
Exits with status 1 if any case has an error. Warnings never fail the check.
"""
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

HERE = Path(__file__).resolve().parent
SCHEMA_PATH = HERE / "schema" / "case.schema.json"
PUBLIC_DIR = HERE / "public"
SUFFIX = {"failure": "-f", "control": "-c"}
UNPAIRED_TAGS = {"exploratory"}  # cases with these tags may stand alone
NORMAL_MAX_TURNS = 6
FRIENDLY = {  # clearer messages for common mistakes, keyed by (field path, failed rule)
    ("source/url", "type"): "a borrowed case needs a link to its source",
    ("source/license", "const"): "original cases use the suite's license, CC-BY-SA-4.0",
    ("source/license", "enum"): "this license can't be used; see THIRD_PARTY_LICENSES.md for what can",
    ("canary", "const"): "the canary string doesn't match; copy it from tests/case_template.yaml",
    ("(top level)", "dependentRequired"): "a case with a proposed_action must also list the tools the AI can call",
}


def load_cases(paths):
    cases, errors = [], defaultdict(list)
    for path in paths:
        try:
            with open(path, encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            errors[path].append(f"not valid YAML: {exc}")
            continue
        if not isinstance(data, dict):
            errors[path].append("the file must hold one case: a mapping of fields")
            continue
        cases.append((path, data))
    return cases, errors


def check(paths):
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    cases, errors = load_cases(paths)
    warnings = defaultdict(list)
    seen_ids = {}
    pairs = defaultdict(list)

    for path, case in cases:
        for err in sorted(validator.iter_errors(case), key=lambda e: list(e.absolute_path)):
            where = "/".join(str(p) for p in err.absolute_path) or "(top level)"
            errors[path].append(f"{where}: {FRIENDLY.get((where, err.validator), err.message)}")

        case_id = case.get("id")
        pair_id = case.get("pair_id")
        direction = case.get("direction")
        bucket = case.get("bucket")
        tags = set(case.get("tags") or [])

        if isinstance(case_id, str):
            if Path(path).stem != case_id:
                errors[path].append(f"the file should be named {case_id}.yaml")
            if case_id in seen_ids:
                errors[path].append(f"id {case_id} is also used in {seen_ids[case_id]}")
            seen_ids.setdefault(case_id, path)
            if isinstance(pair_id, str) and direction in SUFFIX and case_id != pair_id + SUFFIX[direction]:
                errors[path].append(f"a {direction} case in pair {pair_id} should have the id {pair_id}{SUFFIX[direction]}")
        if isinstance(pair_id, str) and isinstance(bucket, str) and not pair_id.startswith(bucket + "-"):
            errors[path].append(f"pair_id should start with the bucket, as in {bucket}-0001")

        turns = case.get("turns")
        if isinstance(turns, list) and turns:
            last = turns[-1]
            if isinstance(last, dict) and last.get("role") != "user":
                errors[path].append("the conversation should end with the person's message (role: user)")
            if len(turns) > NORMAL_MAX_TURNS:
                warnings[path].append(f"{len(turns)} turns; six or fewer is the norm")

        tools = case.get("tools")
        tool_names = [t["name"] for t in tools if isinstance(t, dict) and isinstance(t.get("name"), str)] if isinstance(tools, list) else []
        for name in sorted({n for n in tool_names if tool_names.count(n) > 1}):
            errors[path].append(f"tools: {name} is listed more than once")
        action = case.get("proposed_action")
        if isinstance(action, dict) and tool_names and isinstance(action.get("tool"), str) and action["tool"] not in tool_names:
            errors[path].append(f"proposed_action/tool: {action['tool']} is not one of the tools listed in tools")

        if not case.get("basis"):
            warnings[path].append("basis is empty; a maintainer will add the principle IDs")

        try:
            in_public = Path(path).resolve().is_relative_to(PUBLIC_DIR)
        except AttributeError:  # Python < 3.9
            in_public = str(Path(path).resolve()).startswith(str(PUBLIC_DIR))
        if in_public and case.get("split") != "dev":
            errors[path].append("cases in tests/public/ must have split: dev; holdout cases stay in the private repository")

        if isinstance(pair_id, str):
            pairs[pair_id].append((path, direction, bucket, tags))

    for pair_id, members in sorted(pairs.items()):
        if all(m[3] & UNPAIRED_TAGS for m in members) and len(members) == 1:
            continue
        directions = sorted(m[1] for m in members if m[1] in SUFFIX)
        if directions != ["control", "failure"]:
            for path, *_ in members:
                errors[path].append(f"pair {pair_id} needs exactly one failure case and one control twin; found {directions or 'none'}")
        if len({m[2] for m in members}) > 1:
            for path, *_ in members:
                errors[path].append(f"both cases of pair {pair_id} should have the same bucket")

    return cases, errors, warnings, pairs


def main(argv):
    paths = argv or sorted(str(p) for p in PUBLIC_DIR.glob("*.yaml"))
    if not paths:
        print("No case files found.")
        return 0
    cases, errors, warnings, pairs = check(paths)
    for path in sorted(set(errors) | set(warnings)):
        shown = os.path.relpath(path)
        for msg in errors.get(path, []):
            print(f"ERROR   {shown}: {msg}")
        for msg in warnings.get(path, []):
            print(f"warning {shown}: {msg}")
    n_err = sum(len(v) for v in errors.values())
    print(f"{len(cases)} cases, {len(pairs)} pair IDs: {n_err} errors, {sum(len(v) for v in warnings.values())} warnings")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
