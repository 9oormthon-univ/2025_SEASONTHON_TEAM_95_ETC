from transformers import pipeline

# Mirage 모델 로드
detector_mirage = pipeline("image-classification", model="prithivMLmods/Mirage-Photo-Classifier")

def predict_mirage(image):
    results = detector_mirage(image)
    return results
