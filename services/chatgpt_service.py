from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_with_gpt(results, image_url):
    prompt = f"""
    세 개의 AI 판별 모델 결과:
    - 모델1: {results['model1']}
    - 모델2: {results['model2']}
    - 모델3: {results['model3']}
    교차 검증 결과: {results['final_decision']} (Confidence: {results['confidence']})

    당신은 이미지 판별 전문가입니다.
    이미지를 분석하여 다음 두 가지를 반드시 JSON 형태로 작성해주세요:

    1. "conclusion": 최종 결론 (예의 있게 1줄, 예: "판단이 불확실합니다. 추가적인 확인이 필요합니다.")
    2. "evidence": 주요 근거를 2~3개 bullet 형식 리스트 (픽셀, 피부 질감, 배경, 조명, 메타데이터 등 구체적인 요소)

    주의:
    - 모델의 퍼센트나 교차검증 수치는 언급하지 마세요.
    - 이미지 자체의 시각적 특징을 근거로 설명하세요.
    - JSON만 반환하세요.
    """

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "당신은 AI 생성 이미지 판별 전문가입니다."},
            {"role": "user", "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": image_url}}
            ]}
        ],
        response_format={ "type": "json_object" }
    )

    return response.choices[0].message.content
