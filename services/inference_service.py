from models.detector_ateeqq import predict_ateeqq
from models.detector_smogy import predict_smogy
from models.detector_mirage import predict_mirage
from utils.image_utils import load_image
from utils.calc_utils import cross_validate
from services.chatgpt_service import analyze_with_gpt
import json

def run_inference(image_url: str):
    image = load_image(image_url)


    res1 = predict_ateeqq(image)
    res2 = predict_smogy(image)
    res3 = predict_mirage(image)

    # 세 모델 결과 교차 검증
    merged = cross_validate(res1, res2, res3)


    summary_json = analyze_with_gpt(
        {"model1": res1, "model2": res2, "model3": res3,
         "final_decision": merged["final_decision"],
         "confidence": merged["confidence"]},
        image_url
    )

    summary_data = json.loads(summary_json)

    return {
        "status": "success",
        "image_url": image_url,
        "results": {
            "cross_validation": {"AI": merged["AI"], "Real": merged["Real"]},
            "final_decision": merged["final_decision"],
            "confidence": merged["confidence"],
            "conclusion": summary_data.get("conclusion"),
            "evidence": summary_data.get("evidence")
        }
    }
