from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

print("TOKEN:", TOKEN)  # ← Shu qatorni vaqtincha qo‘shing, tekshirish uchun
