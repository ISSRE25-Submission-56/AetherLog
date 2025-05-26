from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json

model = SentenceTransformer('BigLog')

def align_entities(entities, threshold=0.8):

    embeddings = model.encode(entities)
    sim_matrix = cosine_similarity(embeddings)
    used = set()
    groups = {}
    for i, ent in enumerate(entities):
        if i in used:
            continue
        group = [ent]
        used.add(i)
        for j in range(i+1, len(entities)):
            if j not in used and sim_matrix[i][j] >= threshold:
                group.append(entities[j])
                used.add(j)
        groups[ent] = group
    return groups

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    with open(args.input) as f:
        data = json.load(f)
    entities = [x['msg'] for x in data]
    grouped = align_entities(entities)

    with open(args.output, 'w') as f:
        json.dump(grouped, f, indent=2)