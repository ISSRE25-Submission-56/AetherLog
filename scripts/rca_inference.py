import os
import json
import logging
import argparse
import openai
from config_parser import load_config, merge_args_with_config
from entity_recall import recall_entities
from rca_prompt import generate_rca_prompt
from llm_inference import get_llm_response
from evaluation import evaluate

logger = logging.getLogger('AetherLog')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

def rca_inference(config):
    test_logs_file = os.path.join(config['output_dir'], 'test_logs.jsonl')
    
    with open(test_logs_file, 'r') as f:
        test_logs = [json.loads(line) for line in f]
    
    logger.info(f"Loaded {len(test_logs)} test logs from {test_logs_file}")

    recall_output_file = os.path.join(config['output_dir'], 'recall_results.json')
    with open(recall_output_file, 'r') as f:
        recall_results = json.load(f)
    
    logger.info(f"Loaded entity recall results from {recall_output_file}")
    
    if config['rca_prompt']['use_openai_api']:
        openai.api_key = os.getenv(config['rca_prompt']['openai']['api_key_env'])
    
    rca_results = []
    
    for log in test_logs:
        log_id = log.get('id', 'unknown')
        log_text = log.get('text', '')
        
        # Step 1: Recall top K related entities based on the log
        top_k_entities = recall_entities(log_text, recall_results, top_k=config['entity_recall']['top_k'])
        
        # Step 2: Generate RCA prompt
        rca_prompt = generate_rca_prompt(log_text, top_k_entities, config)
        
        # Step 3: Get RCA response from LLM
        rca_response = get_llm_response(rca_prompt, config)
        
        # Step 4: Save the results
        rca_results.append({
            'log_id': log_id,
            'log_text': log_text,
            'top_k_entities': top_k_entities,
            'rca_response': rca_response
        })
    
    rca_output_file = os.path.join(config['output_dir'], 'rca_results.jsonl')
    with open(rca_output_file, 'w') as f:
        for result in rca_results:
            f.write(json.dumps(result) + '\n')
    
    logger.info(f"Saved RCA results to {rca_output_file}")

    eval_metrics = evaluate(rca_results, config)
    eval_output_file = os.path.join(config['output_dir'], 'eval_metrics.json')
    
    with open(eval_output_file, 'w') as f:
        json.dump(eval_metrics, f, indent=4)
    
    logger.info(f"Saved evaluation metrics to {eval_output_file}")

def main():
    parser = argparse.ArgumentParser(description="AetherLog RCA Inference")
    parser.add_argument('--config', type=str, default='configs/config.yaml', help='Path to the configuration YAML file')
    args = parser.parse_args()
    
    config = load_config(args.config)
    config = merge_args_with_config(args, config)

    rca_inference(config)

if __name__ == "__main__":
    main()
