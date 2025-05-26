import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm

def recall_entities(log_text, recall_results, top_k=5):
   
    log_vector = vectorize_log_text(log_text)
    
    entity_embeddings = recall_results.get('entity_embeddings', {})
    entities = list(entity_embeddings.keys())
    embeddings = np.array(list(entity_embeddings.values()))
    similarities = cosine_similarity([log_vector], embeddings).flatten()
    
    top_k_idx = np.argsort(similarities)[-top_k:][::-1]
    top_k_entities = [entities[idx] for idx in top_k_idx]
    
    return top_k_entities

def vectorize_log_text(log_text):

    np.random.seed(42)
    return np.random.rand(512)

def load_recall_results(recall_output_file):
   
    with open(recall_output_file, 'r') as f:
        recall_results = json.load(f)
    return recall_results

def main():
   
    recall_output_file = 'outputs/recall_results.json'
    
    recall_results = load_recall_results(recall_output_file)
    
    test_logs = [
        {"id": 1, "text": "Connection timeout error during database query."},
        {"id": 2, "text": "CPU utilization exceeds threshold in server node."},
    ]
    
    for log in test_logs:
        log_id = log['id']
        log_text = log['text']
        
        top_k_entities = recall_entities(log_text, recall_results, top_k=5)
        
        print(f"Log ID: {log_id}, Top-K Entities: {top_k_entities}")

if __name__ == "__main__":
    main()
