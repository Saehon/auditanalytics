"""GoldenAudit-RAG synthetic retrieval Space. Not an LLM or official ISACA app."""
import math
import re
from collections import Counter
import gradio as gr

DOCUMENTS = [
    {"id":"SYN-IS-01","text":"Original synthetic internal policy: revoke employee access when employment ends, and document independent review."},
    {"id":"SYN-AI-02","text":"Original synthetic AI policy: deployment requires version recording, evaluation evidence and human approval."},
    {"id":"SYN-ICFR-03","text":"Original synthetic internal control: a missing reconciliation is a deficiency indicator requiring further audit evaluation."},
    {"id":"SYN-ESG-04","text":"Original synthetic ESG assurance: check the reporting date, standard version, assurance scope and traceable evidence."},
    {"id":"SYN-CAM-05","text":"Original synthetic auditor reporting: a critical audit matter does not itself establish fraud or misstatement."},
]
def tokens(s):
    return re.findall(r"[a-z0-9]+", s.lower())

def retrieve(question):
    t=[tokens(d["text"]) for d in DOCUMENTS]
    avg=sum(len(x) for x in t)/len(t)
    hits=[]
    for i,d in enumerate(DOCUMENTS):
        score=0.0
        freq=Counter(t[i])
        for term in set(tokens(question)):
            df=sum(term in x for x in t)
            idf=math.log(1+(len(t)-df+0.5)/(df+0.5))
            f=freq[term]
            if f:
                score+=idf*f*2.5/(f+1.5*(0.25+0.75*len(t[i])/avg))
        hits.append((score,d))
    hits.sort(key=lambda pair:(-pair[0],pair[1]["id"]))
    return "\n\n".join(f"**{d['id']}** • BM25={s:.3f}\n\n{d['text']}" for s,d in hits[:3])

with gr.Blocks(title="GoldenAudit-RAG — Synthetic Evidence Retrieval") as demo:
    gr.Markdown("# GoldenAudit-RAG — Synthetic Evidence Retriever\n**Prototype only:** lexical BM25 over five original, fictional documents. No LLM, expert-approved gold answers, live standards or certification content.")
    question=gr.Textbox(label="Ask a control/evidence question",value="What evidence is needed for AI model deployment?")
    answer=gr.Markdown()
    question.submit(retrieve,inputs=question,outputs=answer)
    gr.Button("Retrieve synthetic evidence").click(retrieve,inputs=question,outputs=answer)
if __name__=="__main__":
    demo.launch()
