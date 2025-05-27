import json
import argparse

PROMPT_TEMPLATE = """
Instruction: Based on the following failure
case and associated entities, identify
the root cause.
Failure Summary: [summary of new log]
Related Entities: [Top-3 entities]
Similarity Scores: [Cosine similarity scores
of the top-3 entities]
Guidance:
- If any entity has a high similarity score,
consider selecting its associated root
cause.
- If all scores are relatively low, reason
based on inter-entity relationships and
failure context to infer a new root
cause.
- If a novel root cause is inferred, also
suggest a new entity and its potential
relationship to the existing KG.
- Then, extract key entities and
relationships in the form of (Head
Entity, Relation, Tail Entity) based on
the inferred root cause and failure
context.
Output:
Root Cause: [Inferred or selected root cause
]
Knowledge Triples:
(Head Entity 1, Relation 1, Tail Entity 1)
(Head Entity 2, Relation 2, Tail Entity 2)
...
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
