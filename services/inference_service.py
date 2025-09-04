from models.detector_ateeqq import predict_ateeqq
from models.detector_smogy import predict_smogy
from utils.image_utils import load_image
from utils.calc_utils import cross_validate
from services.chatgpt_service import analyze_with_gpt

def run_inference(image_url: str):
    image = load_image(image_url)

    res1 = predict_ateeqq(image)
    res2 = predict_smogy(image)

    merged = cross_validate(res1, res2)

    summary = analyze_with_gpt(
        {"model1": res1, "model2": res2,
         "final_decision": merged["final_decision"],
         "confidence": merged["confidence"]},
        image_url
    )

    return {
        "status": "success",
        "image_url": image_url,
        "results": {
            "cross_validation": {"AI": merged["AI"], "Real": merged["Real"]},
            "final_decision": merged["final_decision"],
            "confidence": merged["confidence"],
            "summary": summary
        }
    }
