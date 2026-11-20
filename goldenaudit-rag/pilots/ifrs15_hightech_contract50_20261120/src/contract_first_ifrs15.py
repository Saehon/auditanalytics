#!/usr/bin/env python3
"""CUAD 50-document *candidate* screen: does not issue IFRS conclusions.

Input: independently obtained CUAD v1 SQuAD-style JSON, e.g. CUADv1.json.
The 50 requested are selected only from ACTUAL parsed documents; no padding.
The caller must verify high-tech sector, issuer role, date, source rights,
original SEC exhibit and applicable GAAP before treating a candidate as
an IFRS 15 contract. Never use gold labels in retrieval experiment inputs.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, re
from collections import Counter
from pathlib import Path

POSITIVE = {'software','subscription','saas','technology','platform','data hosting',
 'licensing','licence','license','maintenance','implementation','integration',
 'reseller','distributor','development','royalty','customer','support','cloud'}
NEGATIVE = {'employment','severance','consulting employment','stock option',
 'promissory note','credit agreement','loan agreement','indemnification'}
STAGES = {
 'S1_CONTRACT': [r'customer', r'agreement', r'contract',r'consideration'],
 'S2_PERFORMANCE_OBLIGATIONS': [r'license',r'licence',r'subscription',r'services?',r'maintenance',r'implementation',r'hosting'],
 'S3_TRANSACTION_PRICE': [r'fees?',r'pricing',r'royalt',r'consideration',r'rebate',r'variable'],
 'S4_ALLOCATION': [r'allocation',r'stand.?alone',r'bundl',r'component',r'separate'],
 'S5_RECOGNITION': [r'acceptance',r'control',r'deliver',r'completion',r'milestone',r'over time']}

def extract_contracts(j):
    data=j.get('data')
    if not isinstance(data,list): raise ValueError('Expected CUAD SQuAD JSON data list')
    seen={}
    for entry in data:
        title=entry.get('title','').strip()
        paras=entry.get('paragraphs',[])
        text='\n'.join(x.get('context','') for x in paras if isinstance(x,dict)).strip()
        if not title or not text: continue
        sha=hashlib.sha256(text.encode()).hexdigest()
        key=sha # dedup identical contracts even if title differs
        if key in seen: continue
        seen[key]={'title':title,'text':text,'sha':sha}
    return list(seen.values())

def score(title,text):
    t=title.lower(); body=text[:25000].lower()
    found=[]
    score=0
    for p in sorted(POSITIVE):
        if p in t:score+=4;found.append('TITLE:'+p)
        elif p in body:score+=1;found.append('BODY:'+p)
    negatives=[p for p in NEGATIVE if p in t]
    if negatives:score-=20
    return score,found,negatives

def screen(records,n=50):
    if n<1:raise ValueError('n must be >=1')
    ranked=[]
    for r in records:
        points,hits,neg=score(r['title'],r['text'])
        if points<=0:continue
        stages={k:sum(bool(re.search(p,r['text'],re.I)) for p in patterns)
                for k,patterns in STAGES.items()}
        ranked.append({'source_title':r['title'],'contract_text_sha256':r['sha'],
           'technology_relevance_heuristic':points,'detected_terms':';'.join(hits),
           'exclusion_indicators':';'.join(neg),'contract_evidence_length':len(r['text']),
           'source_contract_verified':'CUAD_CONTEXT_PARSED_ONLY',
           'company_is_high_tech':'UNVERIFIED','issuer_customer_seller_role':'UNKNOWN',
           'applicable_gaap':'NOT_ESTABLISHED','IFRS15_scope':'HUMAN_REVIEW_REQUIRED',
           'original_SEC_exhibit':'NOT_VERIFIED','cam_issuer_year_match':'NOT_VERIFIED',
           'icfr_issuer_year_match':'NOT_VERIFIED','cyber_evidence':'NOT_VERIFIED',
           'risk_status':'QUESTION_FOR_REVIEW','human_coded':'NO',
           **{'term_count_'+k:v for k,v in stages.items()}})
    ranked.sort(key=lambda r:(-r['technology_relevance_heuristic'],r['source_title'],r['contract_text_sha256']))
    return ranked[:n],len(ranked)

def run(source,out,n=50):
    source=Path(source);out=Path(out);out.mkdir(parents=True,exist_ok=True)
    j=json.loads(source.read_text(encoding='utf-8'))
    universe=extract_contracts(j)
    rows,n_eligible=screen(universe,n)
    file=out/'50_contract_candidate_register.csv'
    if rows:
        with file.open('w',newline='',encoding='utf-8') as f:
            writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    status={'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'input_unique_contexts':len(universe),'keyword_eligible':n_eligible,
            'target':n,'screened_candidate_rows':len(rows),
            'high_tech_issuer_validated':0,'IFRS15_applicability_verified':0,
            'original_exhibits_verified':0,'CAM_matches_verified':0,'ICFR_matches_verified':0,
            'pilot_status':'CANDIDATE_TEXT_SCREEN_ONLY',
            'caution':'CUAD legal annotations are NOT IFRS 15 gold labels; no audit opinions or revenue numbers can be inferred.'}
    (out/'50_contract_status.json').write_text(json.dumps(status,indent=2)+'\n',encoding='utf-8')
    return status

def main():
    p=argparse.ArgumentParser();p.add_argument('--cuad-json',required=True)
    p.add_argument('--out',default='reports/cuad_50');p.add_argument('--n',type=int,default=50)
    a=p.parse_args(); print(json.dumps(run(a.cuad_json,a.out,a.n),indent=2))
if __name__=='__main__':main()
