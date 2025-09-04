from transformers import pipeline

detector_smogy = pipeline("image-classification", model="Smogy/SMOGY-Ai-images-detector")

def predict_smogy(image):
    return detector_smogy(image)
