"""Deterministic, dependency-free BM25 lexical retrieval baseline (NOT an LLM)."""
import math
import re
from collections import Counter

def tokenize(text):
    return re.findall(r"[a-z0-9]+", str(text).lower())

def bm25(query, docs, k=3, k1=1.5, b=0.75):
    """Return top k [(score, doc)] ordered by decreasing BM25 score."""
    if not docs:
        return []
    tokens = [tokenize(d["text"]) for d in docs]
    counts = [Counter(t) for t in tokens]
    avgdl = sum(map(len, tokens)) / len(docs)
    qterms = set(tokenize(query))
    scores = []
    for idx, doc in enumerate(docs):
        score = 0.0
        for term in qterms:
            df = sum(1 for counter in counts if counter[term] > 0)
            idf = math.log(1 + (len(docs) - df + 0.5) / (df + 0.5))
            tf = counts[idx][term]
            denom = tf + k1 * (1 - b + b * len(tokens[idx]) / max(avgdl, 1e-9))
            if tf:
                score += idf * tf * (k1 + 1) / denom
        scores.append((score, doc))
    return sorted(scores, key=lambda t: (-t[0], t[1]["source_id"]))[:k]
