import json
from tqdm import tqdm

def preprocess_logs(input_file, output_file):

    with open(input_file) as f:
        data = json.load(f)

    processed = []
    for entry in tqdm(data):
        if 'message' in entry:
            processed.append({'msg': entry['message']})

    with open(output_file, 'w') as f:
        json.dump(processed, f, indent=2)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='raw')
    parser.add_argument('--output', required=True, help='preprocess')
    args = parser.parse_args()
    preprocess_logs(args.input, args.output)