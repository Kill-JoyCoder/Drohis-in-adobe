import numpy as np

def rank_sections(sections, section_embs, task_emb, top_n=10):
    scores = np.dot(section_embs, task_emb)
    top_idx = np.argsort(scores)[::-1][:top_n]
    ranked_sections = []
    for rank, idx in enumerate(top_idx, 1):
        s = dict(sections[idx])
        s['importance_rank'] = rank
        s['score'] = float(scores[idx])
        ranked_sections.append(s)
    return ranked_sections
