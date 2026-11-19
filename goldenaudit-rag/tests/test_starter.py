"""Tests for synthetic retrieval and the evaluation gold-label guard."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from retrieval import bm25
from evaluate import evaluate

class TestStarter(unittest.TestCase):
    def test_retrieval(self):
        docs=[{"source_id":"a","text":"revoke employee access after departure"},
              {"source_id":"b","text":"financial reporting and audit accounting"}]
        self.assertEqual(bm25("employee access revoke",docs,1)[0][1]["source_id"],"a")
    def test_no_gold_leakage(self):
        with self.assertRaises(ValueError):
            evaluate([{"case_id":"1","answer":"yes"}],
                     [{"case_id":"1","gold_answer":"yes",
                       "adjudication_status":"PROVISIONAL_UNADJUDICATED"}])
    def test_approved_label_proxy_only(self):
        out=evaluate([{"case_id":"1","answer":"escalate","evidence_ids":["a"]}],
                     [{"case_id":"1","gold_answer":"escalate","evidence_ids":["a"],
                       "adjudication_status":"ADJUDICATED_GOLD"}])
        self.assertEqual(out["exact_string_match_proxy"],1.0)

if __name__=="__main__":
    unittest.main()
