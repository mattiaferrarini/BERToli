import json
import random
import sys

def split_json(input_path, train_ratio=0.90, val_ratio=0.05):
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    random.seed(42)
    indices = list(range(len(data)))
    random.shuffle(indices)

    n = len(data)
    n_train = int(n * train_ratio)
    n_val = int(n * val_ratio)

    train_idx = indices[:n_train]
    val_idx = indices[n_train:n_train+n_val]
    test_idx = indices[n_train+n_val:]

    train = [data[i] for i in train_idx]
    val = [data[i] for i in val_idx]
    test = [data[i] for i in test_idx]

    def out_path(suffix):
        if input_path.endswith('.json'):
            return input_path[:-5] + f'_{suffix}.json'
        return input_path + f'_{suffix}'

    train_path = out_path('train')
    val_path = out_path('val')
    test_path = out_path('test')

    with open(train_path, 'w', encoding='utf-8') as f:
        json.dump(train, f, ensure_ascii=False, indent=2)
    with open(val_path, 'w', encoding='utf-8') as f:
        json.dump(val, f, ensure_ascii=False, indent=2)
    with open(test_path, 'w', encoding='utf-8') as f:
        json.dump(test, f, ensure_ascii=False, indent=2)

    print(f"Train size: {len(train)} ({train_path})")
    print(f"Validation size: {len(val)} ({val_path})")
    print(f"Test size: {len(test)} ({test_path})")

if __name__ == "__main__":
    if len(sys.argv) not in [2, 4]:
        print("Usage: python splitter.py <input_json> [<train_ratio> <val_ratio>]")
        print("Example: python splitter.py data.json 0.8 0.1")
        sys.exit(1)
    input_json = sys.argv[1]
    if len(sys.argv) == 4:
        train_ratio = float(sys.argv[2])
        val_ratio = float(sys.argv[3])
        if train_ratio + val_ratio > 1.0:
            print("Error: train_ratio + val_ratio must be <= 1.0")
            sys.exit(1)
        split_json(input_json, train_ratio, val_ratio)
    else:
        split_json(input_json)