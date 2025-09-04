from transformers import pipeline

# 전역에서 모델 로드
detector_ateeqq = pipeline("image-classification", model="Ateeqq/ai-vs-human-image-detector")

def predict_ateeqq(image):
    return detector_ateeqq(image)
