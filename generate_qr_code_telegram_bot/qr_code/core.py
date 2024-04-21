import qrcode
import io
from base64 import b64encode
from settings import settings
from PIL import Image
from typing import Optional

async def generate_qr_code(message:str) -> Optional[io.BytesIO]:
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(message)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img = img.resize((settings.QR_IMAGE_BOX_SIZE, settings.QR_IMAGE_BOX_SIZE), Image.Resampling.BOX)

        #save the physical image:
        img.save("qr.png")
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)  # Reset buffer position to the beginning

        return buffer

    except Exception as e:
        print("Error generating QR code: ", e)
        return None

if __name__ == '__main__':
    import asyncio
    message = "https://hrekov.com/"
    res = asyncio.run(generate_qr_code(message))
    print(res)