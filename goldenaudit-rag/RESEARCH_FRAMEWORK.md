# GoldenAudit-RAG — research design, preregistration V1

## Rationale and provenance
Original extension of the user's **AuditGold** programme (32 V1, 75 V2, 100 V3, 3,000 V4 = 3,207 **provisional**, not gold-adjudicated cases). A prepared blind 60-case adjudication pilot exists; no scored expert gold evaluation or actual model efficacy is claimed here. Avoid duplicate research claims and reuse original data only under legal/data rights.

## Mechanism
Licensed dated sources → document-level and clause-level indexing → lexical/dense hybrid retrieval → optional relation graph → grounded LLM → separate verifier/counter-evidence review → professional authorization/abstention gate → independent gold evaluation → evidence passport, immutable run log and error review.

## Preregistered hypotheses
H1. Hybrid RAG > matched LLM-only on proportion of supported and authorized conclusions.
H2. A verifier reduces invalid citations, unsupported material claims and unauthorized final actions relative to RAG without verification.
H3a. Specialist multi-agent RAG improves accuracy for cross-domain complex cases; H3b. multi-agent orchestration increases cost/latency.
H4. Standard-version/jurisdiction-aware retrieval reduces out-of-time generalization loss relative to retrieval without those constraints.
Exploratory: CAM/ICFR versus IT/cyber/ESG cases have different error profiles; no causal mediation claims without identification.

## Human expert benchmark (private)
- Cases: original, permission-cleared, dated and version-controlled. Do not copy ISACA exam questions or licensed text.
- 60-case *planned* double-blind pilot, 2 qualified independent coders per case and 3rd adjudicator; scale toward 400 only after agreement/reliability and coverage review.
- Status rules: PROVISIONAL_UNADJUDICATED is not GOLD. Gold answer, answerability, citation spans, jurisdiction, effective date, evidence contradiction and risk boundaries require adjudication.
- Split scenario families AND originating authorities into development, validation and sealed holdout; screen paraphrase near-duplicates and benchmark contamination.
- Redact protected evidence and licensed excerpts in public releases; retain raw judgment and adjudication records privately.

## Controlled experiment
A0 LLM-only; A1 BM25 + vector RAG; A2 A1 + independently prompted verifier; A3 multiple specialist agents with evidence contracts and human gate; A4 optional GraphRAG. Same model/prompt schema, clock, standard versions and budget where feasible; log exceptions. Randomize case and arm order; prespecify holdout and failures.

## Primary and secondary outcomes
Primary: Y=1 only if a blinded expert panel confirms substantive correctness, verified evidence, appropriate uncertainty and professional authorization. Otherwise 0.
Secondary: item accuracy, retrieval recall@5, evidence/citation precision, hallucinated authority rate, proper abstention, unsafe action, cost, latency, robustness and token usage.
Inference: paired cluster bootstrap by scenario family; mixed-effects logistic models accounting for domain/difficulty, family and source, prespecified H1 primary contrast and Holm correction for additional tests. No fabricated descriptive/regression/significance tables.

## Quality assurance and stop rules
No unsupported audit opinion, false fraud allegation, invented clause, unauthorized filing/signature or hiding contradicting evidence. If the authority is absent or expired, response MUST indicate uncertainty and escalate to a qualified auditor. Prompt-injection tests may use malicious retrieved text as attack data, never as instruction.

## Related programmes
AuditGold: expert question construction; POMELO: IFRS evidence passport, professional decision DAG; DARWIN V9: claim/falsification audit; CAM/KAM: narrative risk and evidence; ICFR: deficiencies and assertions; ESG: assurance and materiality; JMIS multi-agent FinAuditAgentBench: delegated actions, human authorization; forensic: fraud-risk classification versus proof.

## External reproducibility anchors (check licenses)
- CyberMetric: https://github.com/cybermetric/CyberMetric ; Tihanyi et al. IEEE CSR (2024) https://arxiv.org/abs/2402.07688
- RegNLP ObliQA: https://github.com/RegNLP/ObliQADataset ; https://huggingface.co/datasets/RegNLP/ObliQA
- RAGAS: Es et al. (2024) https://aclanthology.org/2024.eacl-demo.16/
- ARES: https://arxiv.org/abs/2311.09476
- UK Inspect Evals CyberMetric implementation: https://ukgovernmentbeis.github.io/inspect_evals/evals/cybermetric/index.html
- ISACA terms: https://www.isaca.org/terms-of-use

## Milestone register (no performance claims)
M0 design / links / synthetic retrieval prototype; M1 permissioned corpus + expert adjudication; M2 matched RAG evaluation; M3 verifier/agent ablation; M4 blinded holdout + robustness; M5 manuscript + full reproduction materials.
