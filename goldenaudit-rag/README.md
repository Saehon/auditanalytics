# GoldenAudit-RAG — evidence-accountable AI for auditing

**Status (2026-11-19): RESEARCH STARTER — not a validated exam-prep model, not a qualified audit assistant.**

Research lead: Saeid Homayoun, University of Gävle.

## Research question

Can retrieval, independent verification and multi-agent coordination improve **supported and professionally authorized** audit decisions beyond answer-choice accuracy? This public workspace contains only original synthetic demonstration materials. It is not an ISACA affiliate and contains no copied CISA/AAIA exam bank, proprietary working papers or protected golden answers.

## Research components

- **Expert gold:** original CISA-competency / AI-audit scenarios, independently reviewed under a blinded two-coder plus adjudicator protocol.
- **Arms:** A0 matched closed-book LLM; A1 hybrid RAG; A2 RAG + independent verifier; A3 multi-agent RAG; optional A4 GraphRAG.
- **Outcomes:** supported and authorized conclusion (primary), evidence recall@k, citation precision, faithfulness, abstention and unsafe-action rates, cost, latency, robustness.
- **Protections:** licence registry, version-locked standards, private sealed gold holdout, source-family split, no model answers in retrieval index.
- **Cross-project links:** [PROJECT_REGISTRY.md](PROJECT_REGISTRY.md); full research design [RESEARCH_FRAMEWORK.md](RESEARCH_FRAMEWORK.md).

## Public runnable starter (stdlib, no external LLM API)

```bash
python goldenaudit-rag/src/run_demo.py
python -m unittest discover -s goldenaudit-rag/tests -v
```

The demo executes a deterministic **BM25 retrieval baseline** on five clearly synthetic source passages. It **does not** call an LLM or certify an expert Golden Q&A benchmark. The evaluator refuses provisional labels.

Google Drive private project folder: https://drive.google.com/drive/folders/1UQw3FrYbuc3rsOnv-6BhCIl0V6NiCzee

Research framework: https://docs.google.com/document/d/1XKQ8zV18zUTA0uhy1ne8Lyaznrs6aQ-9b3sPtXLBaa4/edit

Deployment templates: [Hugging Face](huggingface/README.md) and [Kaggle](kaggle/README.md). These are **templates only**; no dataset/model/Space/Notebook has been uploaded to those platforms.
