import base64
import requests
from io import BytesIO
from PIL import Image

def load_image(input_data: str):
    if input_data.startswith("http"):
        return Image.open(requests.get(input_data, stream=True).raw)
    elif input_data.startswith("data:image"):
        base64_data = input_data.split(",")[1]
        return Image.open(BytesIO(base64.b64decode(base64_data)))
    else:
        raise ValueError("지원하지 않는 이미지 형식입니다.")
