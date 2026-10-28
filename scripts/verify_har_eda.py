"""2026-10-28 정리 시 추가한 제한 재현 도구. 과거 팀 코드와 별개."""
import argparse
import json
from datetime import date
from pathlib import Path
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score


def main():
    parser = argparse.ArgumentParser(description="HAR EDA RF baseline verification")
    parser.add_argument("--data-dir", type=Path, default=Path("data/har"))
    parser.add_argument("--output", type=Path, default=Path("results/har_eda_current.json"))
    args = parser.parse_args()
    frame = pd.read_csv(args.data_dir / "data01_train.csv").drop(columns="subject")
    features = frame.drop(columns="Activity")
    labels = LabelEncoder().fit_transform(frame["Activity"])
    x_train, x_valid, y_train, y_valid = train_test_split(features, labels, test_size=0.2, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(x_train, y_train)
    predictions = model.predict(x_valid)
    result = {
        "run_date": date.today().isoformat(), "sklearn_version": sklearn.__version__,
        "training_rows": len(x_train), "validation_rows": len(x_valid),
        "accuracy": accuracy_score(y_valid, predictions),
        "confusion_matrix": confusion_matrix(y_valid, predictions).tolist(),
        "important_top5": [features.columns[i] for i in model.feature_importances_.argsort()[::-1][:5]],
        "scope": "Current EDA RF validation only; not historical hierarchical DNN reproduction",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
