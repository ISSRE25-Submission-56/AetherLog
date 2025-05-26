import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score


def precision(y_true, y_pred):
    
    return precision_score(y_true, y_pred, average='macro')


def recall(y_true, y_pred):
    
    return recall_score(y_true, y_pred, average='macro')


def f1(y_true, y_pred):
    
    return f1_score(y_true, y_pred, average='macro')


def accuracy(y_true, y_pred):
    
    return accuracy_score(y_true, y_pred)


def evaluate_classification_metrics(y_true, y_pred):
    
    metrics = {
        'precision': precision(y_true, y_pred),
        'recall': recall(y_true, y_pred),
        'f1': f1(y_true, y_pred),
        'accuracy': accuracy(y_true, y_pred)
    }
    return metrics


def mean_average_precision_at_k(y_true, y_pred, k=5):
   
    map_score = 0.0
    for true, pred in zip(y_true, y_pred):
        
        relevant = 0
        precision_at_k = 0.0
        for i, p in enumerate(pred[:k]):
            if p in true:
                relevant += 1
                precision_at_k += relevant / (i + 1)
        if relevant > 0:
            map_score += precision_at_k / relevant
    return map_score / len(y_true) if len(y_true) > 0 else 0.0


def calculate_confusion_matrix(y_true, y_pred):
   
    cm = np.zeros((len(set(y_true)), len(set(y_pred))), dtype=int)
    for true, pred in zip(y_true, y_pred):
        cm[true][pred] += 1
    return cm


def evaluate_classification_performance(y_true, y_pred):
    
    metrics = evaluate_classification_metrics(y_true, y_pred)
    cm = calculate_confusion_matrix(y_true, y_pred)

    results = {
        'metrics': metrics,
        'confusion_matrix': cm
    }
    return results
