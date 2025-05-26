import json
import argparse

PROMPT_TEMPLATE = """
You are an expert Root Cause Analysis (RCA) assistant. Analyze the following fault log and the associated contextual entities to infer the root cause.

[Log Summary]
{summary}

[Related Entities]
{entities}

Please identify the root cause and explain your reasoning.
"""

def construct_prompt(summary_file, entity_file, output_file):

    with open(summary_file) as f:
        summary_data = json.load(f)
    log_summary = "\n".join([item['msg'] for item in summary_data])

    with open(entity_file) as f:
        entity_data = json.load(f)
    entity_list = "\n".join(entity_data)

    prompt = PROMPT_TEMPLATE.format(summary=log_summary, entities=entity_list)

    with open(output_file, 'w') as f:
        json.dump({"prompt": prompt}, f, indent=2)

    print("\nPrompt written to", output_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--summary', required=True)
    parser.add_argument('--entity', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    construct_prompt(args.summary, args.entity, args.output)