> Research proposal | 20 November 2026 | V2.0 | Design only, not tested outcomes.

# GoldenAudit-RAG: Evidence-Accountable and Professionally Bounded Agentic AI for Information Systems and Financial Auditing

*Full Research Proposal V2.0 | 20 November 2026 | Principal Investigator: Saeid Homayoun | University of Gävle, Sweden | Status: preregistration-ready research design; not empirical findings*

## Executive summary and abstract

This project will investigate whether large language models (LLMs) supplemented with retrieval-augmented generation (RAG), independent evidence verification, and coordinated specialist agents produce more defensible decisions in information systems (IS) and artificial-intelligence (AI) auditing than LLMs alone. Previous research demonstrates that LLM performance on professional-accounting assessments can be strong, but selecting the correct response is not equivalent to making a standards-conformant, evidence-grounded and properly authorized audit judgment (Eulerich et al., 2024; Commerford et al., 2022). The study contributes GoldenAudit-RAG, a provenance-controlled and independently adjudicated benchmark with domain, time, jurisdiction, evidence and decision-authorization metadata.

The empirical design comprises a staged 60-case blinded expert-adjudication pilot and, conditional on feasibility and reviewer agreement, a prospective 400-case evaluation. Four matched systems will be compared: closed-book LLM (A0), hybrid lexical–semantic RAG (A1), RAG with an independent verifier (A2), and specialist multi-agent RAG with professional authorization gates (A3). An optional graph-augmented RAG arm (A4) will be treated as a separate extension. The preregistered primary outcome is the proportion of responses achieving a supported and professionally authorized conclusion, as determined by blinded independent audit experts. Secondary outcomes include authority-citation validity, evidence recall, material unsupported claims, abstention calibration, unsafe actions and cost/latency. This work will join the existing AuditGold programme with POMELO evidence passports, DARWIN claim auditing, CAM/KAM, ICFR, ESG assurance and forensic-audit stress tests while explicitly separating proprietary research data from public replication code.

## 1. Motivation, gap and research objective

Professional auditing is a high-stakes information-processing activity: an answer must not only be directionally correct but also cite an applicable source, distinguish facts from assumptions, identify contradicting evidence, respect version and jurisdiction, and stop short of actions requiring a licensed professional. Yet conventional LLM benchmarks frequently prioritize multiple-choice accuracy or generic text similarity. CyberMetric shows that RAG-generated questions can support domain evaluation in cybersecurity (Tihanyi et al., 2024). ObliQA/RIRAG demonstrates large-scale regulatory question-to-evidence alignment (Gokhan et al., 2024). RAGAS and ARES provide component-level evaluation methods, but their automatic metrics are not substitutes for qualified auditor adjudication (Es et al., 2024; Saad-Falcon et al., 2024).

The central research gap is the absence, within the research materials surveyed, of an independently gold-adjudicated cross-domain assessment explicitly combining evidence provenance, authority version, human authorization boundaries and comparative multi-agent performance for IS auditing and financial audit judgments. This is a proposed novelty claim to be systematically tested against a full literature and artifact review before manuscript submission, not an assertion that no similar framework exists.

Objective O1: design original audit scenarios and an expert-approved answer/rubric protocol. O2: compare retrieval and agentic configurations under matched experimental conditions. O3: explain failures and heterogeneity using theory-grounded mechanisms. O4: release reproducible code and rights-cleared examples while protecting confidential source data and gold holdouts.

## 2. Theoretical foundation and testable mechanisms

Delegation theory: agentic systems expand delegated task execution and coordination, creating new questions about who may interpret evidence, override recommendations and authorize conclusions. Baird and Maruping (2021, MIS Quarterly) provide a foundation for distinguishing delegation of information gathering from delegation of final audit responsibility. Prediction: explicit evidence contracts and authorization boundaries reduce unsafe completions, while too many agents may increase coordination overhead.

Professional skepticism and evidence contradiction: audit evidence must be evaluated rather than accepted merely because an AI system generated it. Commerford et al. (2022, Journal of Accounting Research) demonstrate that audit judgments can differ when contradictory evidence comes from AI versus human specialists. Prediction: independent verifier/counter-evidence modules improve handling of conflicts and reduce unsupported final conclusions.

Information-processing and bounded rationality: standard-specific, time-sensitive retrieval may reduce search costs while increasing exposure to noisy or outdated passages. The net effect depends on case complexity, evidence quality, authority hierarchy and whether the answer requires multiple linked claims. Prediction: gains should be larger on verifiable, high-complexity cases but can disappear when retrieval is corrupted.

Design-science contribution: GoldenAudit-RAG will operationalize the construct 'defensible professional AI assistance' as a multidimensional outcome: substantive correctness, evidence support, authority validity, appropriate uncertainty, and authorization. Artifact evaluation and falsification, rather than technical functionality alone, are required for claims of usefulness.

## 3. Research questions and preregistered hypotheses

RQ1. Does retrieval improve evidence-supported and professionally authorized audit decisions? H1: A1 (hybrid RAG) attains a higher mean proportion of supported-and-authorized conclusions than A0 (closed-book LLM) on the sealed adjudicated holdout.

RQ2. Does independent verification improve reliability? H2: A2 yields a lower invalid-authority-citation rate and materially unsupported-claim rate than A1, controlling for task family and model budget.

RQ3. Do specialist agents create value beyond a single verifier? H3a: A3 outperforms A2 on complex cross-domain cases involving three or more distinct evidence relationships. H3b: A3 uses more tokens and has higher median latency; the study will report the reliability–cost frontier rather than assume unconditional superiority.

RQ4. Are version- and jurisdiction-aware systems more robust? H4: explicitly conditioned retrieval has a smaller performance deterioration on out-of-time or conflicted-authority cases than otherwise equivalent unconditioned retrieval.

RQ5. Can agentic audit systems abstain appropriately? H5: an explicit professional-authorization gate increases appropriate abstention and decreases unauthorized final-action completions on intentionally insufficient-evidence scenarios, without an unbounded increase in incorrect abstentions.

Exploratory analyses: effects by information-systems-control type, CISA competency family, AAIA competency family, CAM/ICFR, ESG assurance, IFRS and forensic evidence; complexity interactions; and the degree of agreement between automated metrics and independent audit experts. These are exploratory unless added to preregistration before holdout release.

## 4. Existing project assets and intellectual contribution

The existing AuditGold private preregistration reports 3,207 provisional candidate cases (V1 32; V2 75; V3 100; V4 3,000), including a previously prepared blind 60-case reviewer package. These numbers describe a candidate inventory, NOT independent human-certified gold answers. As of the source protocol dated 17 November 2026, no completed coder adjudication or model-comparison results are documented; an expert-approved gold set therefore must not be claimed at present.

Existing GoldenAudit-RAG technical assets comprise a deterministic BM25 lexical-retrieval demonstration, original synthetic example passages, evaluator gates that reject provisional labels, a Kaggle-ready notebook, and a Hugging Face Space template. Automated GitHub CI tests passed for this starter code. No end-to-end LLM or multi-agent experimental performance has yet been established, and a code prototype must not be conflated with construct validity.

## 5. Sample, task taxonomy and authority data

Pilot P0: retain the EXISTING blinded 60-case candidate package as recorded in AuditGold—20 CAM, 20 ICFR and 20 mixed-credential cases—subject to screening for applicability, source rights and duplicate templates. For the distinct IS/AI-audit expansion, add new cases prospectively rather than silently substituting or reclassifying the original P0 sample. The target P1 benchmark of 400 expert-adjudicated cases is a conditional design goal, not an achieved sample.

Proposed P1 domain allocation (total = 400 if resources permit): 150 IS audit cases across five CISA competency families (30 each); 90 AI auditing cases across three AAIA competency families (30 each); 80 CAM and ICFR cases (40 each); 40 ESG assurance cases; 20 IFRS judgment cases; 20 forensic accounting cases. The allocations ensure sufficient domain representation but are not claimed to reproduce the actual ISACA exam distribution. The ISACA public outline is a human-facing taxonomy reference only; no ISACA content enters any AI tool, retriever or training corpus without explicit written permission.

Case attributes: case_id, template_family, domain, subdomain, source_origin, authority_id, document_version, effective_date, reporting_period, jurisdiction, controls/assertions, answerability_class, missing_evidence_flag, contradictory_evidence_flag, complexity, gold_reference_answer, gold_evidence_ids, expert_scorer_ids, adjudication_state, license_status and leakage_group. Audit facts should be presented as synthetic or authorized de-identified scenarios with minimal personal or confidential material.

Potential source classes (not presumed free to redistribute): original fictional audit-control policies; properly licensed standards and professional guidance; permitted public SEC and PCAOB material; rights-reviewed NIST AI RMF and Cybersecurity Framework materials; original controls and redacted case narratives. Maintain a source-rights ledger recording version, jurisdiction, redistribution restrictions, expiration and exact paragraph locator. 'Publicly readable' does not equal 'licensed for model ingestion or public release'.

## 6. Golden-answer creation, human reliability and contamination controls

Two independent qualified audit/IS/AI-audit reviewers will first read a question without the candidate model answer or other reviewer's scoring. For every case they will specify answerable/conditionally answerable/not answerable; governing authority and version; minimum sufficient evidence; a conditional reference answer; contradictory facts; and the action that cannot be delegated to AI. Reviewers will score accuracy (0–2), authority reasoning (0–2), evidence traceability (0–2), uncertainty handling (0–2), and professional action authorization (0–2), yielding a 0–10 substantive rubric. Record unsafe-action and fabricated-citation binary flags separately.

A third adjudicator resolves substantive disagreement. Store both original ratings, reviewer professional background, authority IDs and resolution rationales; publish item-level labels only where intellectual-property clearance allows. Report raw agreement, pairwise weighted kappa where meaningful and Krippendorff's alpha across rating dimensions with bootstrap intervals. Cases not reaching a documented adjudication standard remain PROVISIONAL_UNADJUDICATED and are excluded from the primary endpoint.

Prevent contamination by (i) separating cases by source-document cluster AND semantic template family, (ii) withholding all gold answers and rubrics from RAG corpora, (iii) freezing an independent holdout before prompts are tuned, (iv) checking overlapping paraphrases and duplicated source passages, and (v) separating retrieval indexes from annotation storage. Keep access logs and source hashes. If holdout answers are disclosed or inspected for tuning, withdraw the case from the locked holdout.

## 7. System architecture and experimental comparison

Input case → authorization and rights screening → standards/version locator → hybrid lexical BM25 and dense retrieval with optional reranking → draft response with evidence spans → specialist counter-evidence verifier → human decision boundary → structured output and evidence passport → blind benchmark evaluation. POMELO supplies version-controlled evidence passports and professional decision DAGs; DARWIN supplies falsification and claim-review gates; cross-domain agent modules provide specialist analysis but are never permitted to sign an audit report.

A0 = base LLM without retrieval; A1 = same base LLM with hybrid RAG; A2 = A1 plus independent critique/verifier model with fixed prompt and budget; A3 = orchestrated specialist agents (IS controls, cyber/AI, financial auditing, standards/provenance, skeptic/verifier) with evidence contracts and escalation rules. A4 = optional graph-enhanced retrieval and will not be folded into confirmatory H1 testing after results are observed.

Control framework: freeze model family and version, inference parameters, retrieval corpus version, authority cut-off date, instruction templates, maximum context, token cap, available tools and run environment. Randomize order of arm execution per case. Report all refusals, run failures, timeouts and empty retrievals. Additional analysis can stratify model families but should not pool them as independent replications of the same treatment.

No final opinion, assurance statement, fraud finding or filing may be issued autonomously. If critical evidence is missing or contradictory, the system must explicitly abstain or request qualified human review. Retrieved content must be treated as evidence data rather than executable instructions; evaluate prompt-injection robustness.

## 8. Outcomes, model specifications and five research tables

Primary dependent variable: SupportedAuthorized_ia = 1 if a blinded adjudicator determines that response a to case i is substantively correct, supported by dated clause-specific sources, appropriately qualified and within the authorized professional action boundary; otherwise 0. This composite requires satisfying all four conditions, not a weighted average of generic LLM judge scores.

Other dependent variables: QuestionAccuracy (0/1), CitationPrecision (valid cited source IDs / cited IDs), EvidenceRecall@5, Faithfulness (manual expert and separately automated RAGAS/ARES), UnsupportedMaterialClaims (count), ProperAbstention (0/1), UnauthorizedAction (0/1), LatencySeconds, Tokens, CostUSD and ReviewerOverride (0/1). Missing values must be flagged; do not replace unknown cost with zero.

Independent variables: TreatmentArm indicators A0/A1/A2/A3; treatment-specific version gate (0/1); verifier (0/1); multiagent (0/1); retrieval k; and preregistered interaction with case complexity. Controls: case difficulty, domain, answerability class, source age, authority jurisdiction, evidence count, source-document cluster, model family/version, text length and session order. Pairing by identical case is central to identification.

Confirmatory equation (generalized linear mixed model): logit{Pr(SupportedAuthorized_ia = 1)} = alpha + beta1*A1 + beta2*A2 + beta3*A3 + gamma*CaseCharacteristics_i + u_template(i) + u_authority(i) + e_ia. Interpret A2 and A3 versus A1/A2 using prespecified linear contrasts; when arm and verifier are collinear, do NOT include separate redundant arm and verifier regressors. Conduct sensitivity analyses using conditional case-fixed-effects logit and paired permutation/bootstrap methods.

Produce five nonfabricated journal-style tables after genuine model runs: Table 1 scenario/source descriptive statistics and adjudication; Table 2 domain-balanced arm outcomes with denominators; Table 3 primary paired effects and mixed-effects logit with 95% intervals; Table 4 robustness, out-of-time and negative-control tests; Table 5 failure taxonomy, authorization, cost and latency frontier. A correlation matrix for eligible continuous measures is a supplementary appendix, not a substitute for the primary paired design. Tables must retain sample sizes, units and missingness.

Pre-specify H1 as the primary test and use Holm familywise error adjustment for secondary confirmatory contrasts. Report effect sizes, cluster bootstrap confidence intervals by template family, calibration and McNemar-style paired checks when appropriate. Conduct simulation-based power planning only after the 60-case adjudication pilot produces plausible baseline risks and within-case correlations. Do not assert statistical power from 400 cases without estimating these inputs.

## 9. Robustness, falsification and independent validation

Robustness set: unseen time periods; obsolete versus current authority; two competing jurisdictions; insufficient evidence/should-abstain; intentionally inserted malicious retrieval instructions; adversarial paraphrases; dense-only/BM25-only ablations; top-k sensitivity; missed source passages; long-context truncation; model-temperature perturbations; agent-count ablation; and leave-domain-out transfer. Human evaluators remain blind to treatment arm. External assessment by qualified practitioners is encouraged after internal reliability is established.

Falsification and hard stops: any response that (a) invents a specific legal or standards clause, (b) issues an unsupported assurance conclusion, (c) attributes fraud without evidence, (d) authorizes unapproved audit signing or filing, or (e) suppresses material contradictory evidence is recorded as a critical failure regardless of aggregate accuracy. Version/gov controls must produce auditable failure logs.

## 10. Cross-project integration and nonduplication

AuditGold: retained private candidate registry, blind scoring, gold-label adjudication and separate publication scope. POMELO IFRS Intelligence Fabric: stable source authority core, evidence passports, normative professional DAG, source-version checks. DARWIN V9 / KIWI CAM: claim audit, risk-response alignment, falsification and confidence gating. ICFR/SOX 404: assertions, control evidence and material-weakness boundary conditions. ESG multi-agent: materiality and assurance provenance. FinAuditAgentBench / JMIS: research framework for delegation, agent orchestration and decision authority. Forensic research: red-flag interpretation versus legally supportable conclusions. MACEI/SME: optional later external-validity test cases, never recycled from proprietary sample data without rights clearance.

Novelty separation: GoldenAudit-RAG's focal dependent variable is the defensibility of model-generated audit assistance and evidence traceability, not prediction of CAM topics, future misstatement, financial performance or ESG valuation. Any shared benchmark cases or outputs with the existing AuditGold/ISF and JMIS manuscripts must be transparently cross-referenced, and results cannot be represented as independent new datasets if reused.

## 11. Work packages, deliverables and 12-month schedule

WP1 (months 1–2): legal/authority ledger, literature novelty review, preserve and audit the AuditGold 3,207 candidate inventory; freeze original 60-case blind packet. Deliverables: provenance inventory, de-duplication report, IRB/ethics assessment where relevant, completed preregistration.

WP2 (months 2–4): recruit two qualified blind expert coders and an adjudicator, adjudicate pilot, estimate reviewer agreement and rubric reliability, refine case-writing manual. Deliverables: 60-case independently checked reference set or explicit failure-to-validate report; sample-size simulation inputs.

WP3 (months 3–6): implement versioned hybrid retrieval and LLM baselines; code A0/A1 and standardized logs; lock evaluation splits. Deliverables: stable code, unit tests, data dictionary and baseline run logs.

WP4 (months 5–8): implement verifier and multi-agent A2/A3; generate hard negative and out-of-time cases, log failures, rights-check the expanded sample. Deliverables: verifier/agent ablation and design checkpoint.

WP5 (months 8–10): conditional 400-case expert benchmark if reviewer/rights gates permit; preregister analysis and run sealed paired evaluation. Deliverables: five empirical tables only if observations exist, uncertainty estimates, robustness, cost-quality analysis and incident register.

WP6 (months 10–12): manuscript and supplementary methods, public rights-cleared synthetic/approved data, reproducibility package, independent technical review and journal fit audit. Deliverables: submission-ready draft and read-only release. Where 400 cases are not feasible, publish an explicitly bounded pilot rather than imply the full benchmark was completed.

## 12. Resources, ethics, rights and reproducibility

Team: principal investigator for scientific design and audit domain validity; two independent qualified auditors/coders; third adjudicator; research assistant for source inventory; ML engineer for retrieval/evaluation; methodological reviewer for mixed-effects inference. Document conflicts of interest and professional qualifications. Secure compute should isolate model-generated drafts from sealed labels. Anticipated expenditure categories: staff hours, professional adjudication, compute/API tokens, secure data storage, publication and conference dissemination; detailed monetary budget remains to be costed.

Research governance: preserve immutable source hashes, copyright/license register, GDPR and trade-secret screening, data minimization, model-card disclosures, code environment and version pins, red-team logs, and documented human sign-off. ISACA's current terms restrict using ISACA content in AI tools or grounding/training AI systems; consequently, the project will not ingest or redistribute ISACA protected material without express permission, and cannot present itself as ISACA-approved or as providing authentic examination questions.

Reproducibility package: frozen requirements/environment, deterministic seeds, public synthetic fixture, schema validator, data-rights tests, benchmark split generator (excluding confidential gold), standardized A0–A3 runner interface, run logs and manifest of result hashes, expert scoring manual, analysis script for the five empirical tables, automated CI. Public Hugging Face and Kaggle resources are planned mirrors only until publishing permissions and credentials are available.

## 13. Expected theoretical, practical and methodological contributions

Theory: refine IS delegation theory for audit assistance by distinguishing delegated search/reasoning from nondelegable sign-off; provide empirical tests of evidence-based professional skepticism and of governance controls on agentic information processing. Practice: establish auditable evidence trails, escalation boundaries and measurable failure classes for IS audit and AI assurance, with potential educational use of original non-ISACA scenarios. Method: provide a domain-grounded multi-treatment benchmark with independent blind experts, temporal validity checks, explicit source licensing and reproducible code beyond question-answer accuracy.

Potential outlets after empirical validation and novelty audit: Journal of Management Information Systems or MIS Quarterly for organizational delegation/control mechanisms; Journal of Information Systems or International Journal of Accounting Information Systems for audit-system design and evidence; Auditing: A Journal of Practice & Theory for practitioner judgment/assurance. FT50/AJG4 placement is an aspiration subject to journal-specific fit and the ranking edition used, not an acceptance or editorial guarantee.

## 14. Quality gates, decision rules and present status

G0 Design/gateway: scientific questions, rights register, public-safe repository, documented baseline—not an empirical result (CURRENTLY AVAILABLE). G1 Source and label gate: written rights status and adequate independent adjudicator agreement. G2 Model gate: reproduced A0–A3 code and valid source timestamps. G3 Statistical gate: true paired results, confidence intervals and blind analysis without leakage. G4 Release gate: secure gold handling, plagiarism/license review and independent replication. G5 Publication gate: resolved novelty and journal appropriateness.

Current known status at 20 November 2026: project folder, project-wide registry and research framework exist in Google Drive; existing public GitHub synthetic baseline and CI pass. There is no confirmed completed expert gold labeling, authenticated LLM head-to-head empirical run, Hugging Face upload, Kaggle upload or arXiv submission. This proposal is a plan for those activities and must not be cited as completed evidence.

## References (verified scholarly and primary sources; APA-oriented)

Baird, A., & Maruping, L. M. (2021). The next generation of research on IS use: A theoretical framework of delegation to and from agentic IS artifacts. MIS Quarterly, 45(1), 315–341. https://aisel.aisnet.org/misq/vol45/iss1/12/

Commerford, B. P., Dennis, S. A., Joe, J. R., & Ulla, J. W. (2022). Man versus machine: Complex estimates and auditor reliance on artificial intelligence. Journal of Accounting Research, 60(1), 171–201. https://doi.org/10.1111/1475-679X.12407

Eulerich, M., Sanatizadeh, A., Vakilzadeh, H., & Wood, D. A. (2024). Is it all hype? ChatGPT’s performance and disruptive potential in the accounting and auditing industries. Review of Accounting Studies, 29(3), 2318–2349. https://doi.org/10.1007/s11142-024-09833-9

Es, S., James, J., Espinosa Anke, L., & Schockaert, S. (2024). RAGAs: Automated evaluation of retrieval augmented generation. Proceedings of EACL 2024 System Demonstrations, 150–158. https://doi.org/10.18653/v1/2024.eacl-demo.16

Saad-Falcon, J., Khattab, O., Potts, C., & Zaharia, M. (2024). ARES: An automated evaluation framework for retrieval-augmented generation systems. NAACL 2024, 338–354. https://aclanthology.org/2024.naacl-long.20/

Tihanyi, N., Ferrag, M. A., Jain, R., Bisztray, T., & Debbah, M. (2024). CyberMetric: A benchmark dataset based on retrieval-augmented generation for evaluating LLMs in cybersecurity knowledge. IEEE International Conference on Cyber Security and Resilience (CSR). https://arxiv.org/abs/2402.07688

Gokhan, T., Wang, K., Gurevych, I., & Briscoe, T. (2024). RIRAG: Regulatory information retrieval and answer generation. arXiv:2409.05677. https://arxiv.org/abs/2409.05677

ISACA. (n.d.). CISA exam content outline (competency information only; not AI training material). https://www.isaca.org/credentialing/cisa/cisa-exam-content-outline

ISACA. (n.d.). Advanced in AI Audit (AAIA) exam content outline (competency information only; not AI training material). https://www.isaca.org/credentialing/aaia/aaia-exam-content-outline

ISACA. (2026, June 22). Terms of use, sections 2.6 and related content restrictions. https://www.isaca.org/terms-of-use

Public source-code workspace: https://github.com/Saehon/auditanalytics/tree/main/goldenaudit-rag


---

## Repository implementation and provenance

- [Runnable original synthetic research starter](../README.md)
- [Cross-project public registry](../PROJECT_REGISTRY.md)
- [Research framework](../RESEARCH_FRAMEWORK.md)
- [Kaggle notebook template](../kaggle/goldenaudit_rag_synthetic_demo.ipynb)
- [Hugging Face Space template](../huggingface/SPACE_README.md)

**Publication status**: a proposal, NOT experimental results, validated Golden Answers, an ISACA-approved app, or a peer-reviewed manuscript.
