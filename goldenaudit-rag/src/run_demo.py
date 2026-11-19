"""Synthetic retrieval demonstration: no commercial questions, no LLM."""
import json
from pathlib import Path
from retrieval import bm25

ROOT = Path(__file__).resolve().parents[1]
def load_jsonl(path):
    return [json.loads(row) for row in path.read_text(encoding="utf-8").splitlines() if row.strip()]

def run():
    docs = load_jsonl(ROOT / "data" / "demo_corpus.jsonl")
    questions = load_jsonl(ROOT / "data" / "demo_questions.jsonl")
    for q in questions:
        hits = bm25(q["question"], docs, k=3)
        print(json.dumps({"case_id":q["case_id"],
                          "predicted_source_ids":[d["source_id"] for _,d in hits],
                          "note":"SYNTHETIC_DEMO_NOT_GOLD"}))
if __name__ == "__main__":
    run()
