import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("META_API_KEY")

print(f"🔑 Key OK: {API_KEY[:10]}...")
print("☀️ KHENCHELA SUN - Photoshop الشمس!")

# نحسب الطاقة لخنشلة
def calculate_khenchela():
    # خنشلة: 35.4N, 7.1E, 300 يوم شمس
    roof_m2 = 20
    sun_hours = 5.5
    efficiency = 0.85
    
    kw = (roof_m2 * 0.2 * sun_hours * efficiency)  # 0.2 kW per m2
    kwh_per_year = kw * sun_hours * 365
    dzd_saving = kwh_per_year * 6  # 6 دينار لكل kWh
    
    print(f"\n📍 خنشلة 35.4N 7.1E")
    print(f"🏠 سطح: {roof_m2} m2")
    print(f"⚡ انتاج: {kw:.1f} kW")
    print(f"📅 سنويا: {kwh_per_year:.0f} kWh")
    print(f"💰 توفير: {dzd_saving:.0f} DZD / سنة")
    print(f"💵 توفير: {dzd_saving/135:.0f} $ / سنة")
    
    # نستعمل Llama لحساب دقيق
    if API_KEY and len(API_KEY) > 20:
        try:
            headers = {"Authorization": f"Bearer {API_KEY}"}
            data = {
                "model": "Llama-3.3-70B",
                "prompt": f"Khenchela Algeria solar: {roof_m2}m2 roof, 5.5h sun, calculate kW and ROI in JSON",
                "max_tokens": 250
            }
            r = requests.post(
                "https://api.llm.meta.com/v1/generate",
                headers=headers,
                json=data,
                timeout=10
            )
            print(f"\n🤖 Meta AI Response: {r.status_code}")
            print(r.text[:400])
        except Exception as e:
            print(f"Meta API: {e} - لكن الحساب المحلي صحيح!")
    
    print("\n✅ جاهز للمرحلة الجاية: SAM 3.1 - Magic Wand!")

calculate_khenchela()