import json
import os
import numpy as np

def save_json(data, filepath):

    os.makedirs(os.path.dirname(filepath), exist_ok=True) 
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Data saved to {filepath}")

def load_json(filepath):
   
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"Data loaded from {filepath}")
    return data

def save_numpy_array(data, filepath):
   
    os.makedirs(os.path.dirname(filepath), exist_ok=True)  
    np.save(filepath, data)
    print(f"Array saved to {filepath}")

def load_numpy_array(filepath):
    
    data = np.load(filepath)
    print(f"Array loaded from {filepath}")
    return data

def save_text(data, filepath):
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)  
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(data)
    print(f"Text saved to {filepath}")

def load_text(filepath):
   
    with open(filepath, 'r', encoding='utf-8') as f:
        data = f.read()
    print(f"Text loaded from {filepath}")
    return data

def save_pickle(data, filepath):
   
    import pickle
    os.makedirs(os.path.dirname(filepath), exist_ok=True)  
    with open(filepath, 'wb') as f:
        pickle.dump(data, f)
    print(f"Data saved as pickle to {filepath}")

def load_pickle(filepath):
    
    import pickle
    with open(filepath, 'rb') as f:
        data = pickle.load(f)
    print(f"Data loaded from pickle file {filepath}")
    return data
