import json
from sklearn.metrics import precision_score, recall_score, f1_score

def evaluate(pred_file, gold_file):
    with open(pred_file) as f:
        preds = json.load(f)
    with open(gold_file) as f:
        gts = json.load(f)

    y_true = [gt['root_cause'] for gt in gts]
    y_pred = [pred['root_cause'] for pred in preds]

    p = precision_score(y_true, y_pred, average='macro', zero_division=0)
    r = recall_score(y_true, y_pred, average='macro', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='macro', zero_division=0)

    print("Precision: {:.4f}".format(p))
    print("Recall: {:.4f}".format(r))
    print("F1-score: {:.4f}".format(f1))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--pred', required=True)
    parser.add_argument('--gold', required=True)
    args = parser.parse_args()

    evaluate(args.pred, args.gold)
