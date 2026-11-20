#!/usr/bin/env python3
"""Recompute public descriptive counts; no LLM, legal test, or audit conclusion."""
import csv,json,collections
from pathlib import Path
root=Path(__file__).resolve().parent
rows=list(csv.DictReader((root/"qualitative_coding.csv").open(encoding="utf-8",newline="")))
assert len(rows)==12 and len({x["unit_id"] for x in rows})==12
allowed={"ISSUER_ASSERTION","ISSUER_POSITION","REGULATORY_COMMENT","ANALYST_INFERENCE"}
assert all(x["epistemic_status"] in allowed for x in rows)
out={"units":len(rows),"by_theme":dict(sorted(collections.Counter(x["second_order_theme"] for x in rows).items())),"by_speaker":dict(sorted(collections.Counter(x["speaker"] for x in rows).items())),"human_adjudication":"NOT RUN","model_experiments":"NOT RUN"}
expected=json.loads((root/"pilot_summary_public.json").read_text())
assert out["by_theme"]==expected["theme_counts"]
print(json.dumps(out,indent=2))
