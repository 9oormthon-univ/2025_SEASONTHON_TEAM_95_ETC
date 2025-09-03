from transformers import pipeline

# Ateeqq 모델 로드
model_ateeqq = pipeline("image-classification", model="Ateeqq/ai-vs-human-image-detector")

def predict_ateeqq(image_path: str):
    results = model_ateeqq(image_path)
    return {r["label"].lower(): round(r["score"] * 100, 2) for r in results}
