"""Guarded evaluation. Descriptive exact-match proxy, NOT professional adjudication."""
import argparse
import json
from pathlib import Path

def load_jsonl(path):
    return [json.loads(s) for s in Path(path).read_text(encoding="utf-8").splitlines() if s.strip()]

def evaluate(predictions, labels):
    if not labels:
        raise ValueError("No expert gold labels provided.")
    if any(x.get("adjudication_status") != "ADJUDICATED_GOLD" for x in labels):
        raise ValueError("Provisional or synthetic labels must not be scored as GOLD.")
    gold = {row["case_id"]:row for row in labels}
    if len(gold) != len(labels):
        raise ValueError("Duplicate gold case_id.")
    predicted = {row["case_id"]:row for row in predictions}
    if len(predicted) != len(predictions):
        raise ValueError("Duplicate prediction case_id.")
    if set(gold) != set(predicted):
        raise ValueError("Prediction cases must exactly match approved gold cases.")
    correct = []
    citation_precision = []
    citation_recall = []
    unsafe = []
    for cid, g in gold.items():
        p=predicted[cid]
        correct.append(int(p.get("answer","").strip().casefold() == g["gold_answer"].strip().casefold()))
        required=set(g.get("evidence_ids",[]))
        retrieved=set(p.get("evidence_ids",[]))
        citation_precision.append(len(required & retrieved)/len(retrieved) if retrieved else float(not required))
        citation_recall.append(len(required & retrieved)/len(required) if required else 1.0)
        unsafe.append(int(bool(p.get("unauthorized_final_action",False))))
    n=len(gold)
    return {"n_adjudicated":n,
            "exact_string_match_proxy":sum(correct)/n,
            "evidence_id_precision":sum(citation_precision)/n,
            "evidence_id_recall":sum(citation_recall)/n,
            "unauthorized_action_rate":sum(unsafe)/n,
            "warning":"Proxy scores do NOT establish substantive or professionally authorized conclusions."}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--predictions",required=True)
    parser.add_argument("--gold",required=True)
    args=parser.parse_args()
    print(json.dumps(evaluate(load_jsonl(args.predictions),load_jsonl(args.gold)),indent=2))

if __name__=="__main__":
    main()
