import base64
import requests
from io import BytesIO
from PIL import Image

def load_image(input_data: str):
    if input_data.startswith("http"):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/115.0 Safari/537.36"
        }
        response = requests.get(input_data, headers=headers, timeout=10)
        response.raise_for_status()  # HTTP 에러 시 예외 발생
        return Image.open(BytesIO(response.content))

    elif input_data.startswith("data:image"):
        base64_data = input_data.split(",")[1]
        return Image.open(BytesIO(base64.b64decode(base64_data)))
    else:
        raise ValueError("지원하지 않는 이미지 형식입니다.")
