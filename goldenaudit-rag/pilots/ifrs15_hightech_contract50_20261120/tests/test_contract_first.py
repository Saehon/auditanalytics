import unittest,sys,json,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from contract_first_ifrs15 import extract_contracts,score,screen,run
class ContractFirstTests(unittest.TestCase):
 def setUp(self):
  self.source=ROOT/'data/SYNTHETIC_test_only_cuad_shape.json';self.j=json.loads(self.source.read_text())
 def test_extracts_synthetic(self):self.assertEqual(len(extract_contracts(self.j)),3)
 def test_no_padding_to_50(self):
  with tempfile.TemporaryDirectory() as t:
   r=run(self.source,t,50);self.assertLess(r['screened_candidate_rows'],50)
 def test_gaap_not_assumed(self):
  r,n=screen(extract_contracts(self.j),50);self.assertTrue(all(x['applicable_gaap']=='NOT_ESTABLISHED' for x in r))
 def test_no_invented_cam_matches(self):
  r,_=screen(extract_contracts(self.j));self.assertTrue(all(x['cam_issuer_year_match']=='NOT_VERIFIED' for x in r))
 def test_no_invented_ifrs_gold(self):
  r,_=screen(extract_contracts(self.j));self.assertTrue(all(x['IFRS15_scope']=='HUMAN_REVIEW_REQUIRED' for x in r))
 def test_title_score(self):self.assertGreater(score('Cloud software license agreement','Basic subscription service')[0],0)
 def test_employment_penalty(self):self.assertLess(score('Employment agreement','Software training')[0],1)
 def test_sha_dedup(self):
  j=dict(self.j);j['data']=j['data']+[j['data'][0]]
  self.assertEqual(len(extract_contracts(j)),3)
 def test_reject_missing_list(self):
  with self.assertRaises(ValueError):extract_contracts({'data':{}})
 def test_reject_nonpositive_n(self):
  with self.assertRaises(ValueError):screen([],0)
 def test_status_no_claim_of_inference(self):
  with tempfile.TemporaryDirectory() as t:
   r=run(self.source,t,50);self.assertEqual(r['pilot_status'],'CANDIDATE_TEXT_SCREEN_ONLY')
 def test_reject_numeric_risk_claim(self):
  r,_=screen(extract_contracts(self.j));self.assertTrue(all(x['risk_status']=='QUESTION_FOR_REVIEW' for x in r))
if __name__=='__main__':unittest.main()
