# GoldenAudit × DARWIN–POMELO — IFRS 15 High-Tech Contract-First AOS Pilot V0.5

**Status: documentary pilot executed, 50 contract pilot NOT RUN (no raw CUAD corpus).**

## What is verified
- Three user-Drive SEC company correspondence files retrieved and reviewed: Lightspeed, Cloudera, National Instruments.
- 10 provisional, source-located analytic units, stored as paraphrases rather than full document content.
- Full retrieved text frequency checks in `reports/real_sec_text_counts.csv`.
- 12/12 offline Python code tests on synthetic fixture pass.
- A 12-page AOS-oriented working manuscript with methodological boundaries and source links.

## What is NOT verified
- No original customer-contract text retrieved for these cases.
- Zero of the target 50 CUAD high-tech customer agreements were parsed locally.
- No CAM or ICFR firm-year joined; no control effectiveness, material weakness, revenue misstatement or six-capital loss established.
- No LLM A0–A4 evaluation, expert adjudication or real ERP/SIEM tests.

## Source selection and replication
Primary 50 candidate source: original CUAD SQuAD JSON from [The Atticus Project](https://github.com/The-Atticus-Project/cuad), 510 commercial agreements with 41 **legal** clause categories. GitHub repository includes retrieval/evaluation code, but source legal labels do not certify IFRS 15 compliance. Mirror: https://www.kaggle.com/datasets/konradb/atticus-open-contract-dataset-aok-beta (licence and overlaps should be verified).

```
python -m unittest discover -s tests -v
python src/contract_first_ifrs15.py --cuad-json /path/to/CUADv1.json --out reports/cuad_50 --n 50
```

Never submit a 50-case result without the real, deduplicated source sample and explicit human verification. If fewer than 50 candidates are supported, record the shortfall.  The full case study should keep IFRS 15 separate from US GAAP ASC 606 issuers.

## Cross-project boundary
The existing separate AOS contract→CAM→ICFR manuscript explores documentary risk translation. This pilot instead centers on IFRS 15 high-tech contract interpretation and agentic professional decision rights; publication as an independent paper requires distinct cases, theory and human practitioner observations to avoid duplicate contributions.

## Public release policy
Safe public contents: original scripts, test fixture clearly labeled SYNTHETIC, source file accession numbers, summary counts and paraphrased coding metadata. Do not publish original private Drive sources, original third-party contracts, licensed IFRS text, confidential client records or unadjudicated Golden Q&A keys.
