from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_with_gpt(results, image_url):
    prompt = f"""
    두 개의 AI 판별 모델 결과:
    - 모델1: {results['model1']}
    - 모델2: {results['model2']}
    교차 검증 결과: {results['final_decision']} (Confidence: {results['confidence']})

    위 결과를 바탕으로, 왜 Real인지/왜 Fake인지 간단히 1줄로 설명해 주세요.
    """

    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role": "system", "content": "당신은 AI 생성 이미지 판별 전문가입니다."},
            {"role": "user", "content": prompt},
            {"role": "user", "content": f"이미지 URL: {image_url}"}
        ]
    )

    return response.choices[0].message.content.strip()
