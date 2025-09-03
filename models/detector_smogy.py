from transformers import pipeline

# Smogy 모델 로드
model_smogy = pipeline("image-classification", model="Smogy/SMOGY-Ai-images-detector")

def predict_smogy(image_path: str):
    results = model_smogy(image_path)
    return {r["label"].lower(): round(r["score"] * 100, 2) for r in results}
