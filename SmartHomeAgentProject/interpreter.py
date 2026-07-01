import google.generativeai as genai
from config import API_KEY, MODEL_NAME

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(model_name=MODEL_NAME)

def interpret_input_with_gemini(input_text):
    prompt = (
        f"Aşağıdaki kullanıcı komutunu mantıksal bir gerçek olarak temsil et.\n"
        f"Geçerli gerçekler şunlardır:\n"
        f"cold_weather, hot_weather, no_one_home, dark_room, bright_room, "
        f"sleep_time, wake_time, wake_up_time, hot_enough, cold_enough, "
        f"leaving_home, arriving_home\n"
        f"KOMUT: '{input_text}'\n"
        f"Sadece bu gerçeklerden biri olarak tek bir Python tanımlayıcı döndür."
    )

    response = model.generate_content(prompt)
    fact = response.text.strip().replace("`", "").replace("'", "").split("\n")[0]
    return fact
