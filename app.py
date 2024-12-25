import streamlit as st
import pickle
import numpy as np


model_path = "my_model.pkl"  
with open(model_path, "rb") as file:
    model = pickle.load(file)


diagnosis_map = {
    0: "Depressiya",
    1: "Bipolyar buzilish",
    2: "Tashvish buzilishi",
    3: "Obsessiv-kompulsiv buzilish (OKB)",
    4: "Post-travmatik stress buzilishi (PTSB)",
    5: "Shizofreniya",
    6: "Chegara shaxs buzilishi",
    7: "Ruhiy buzilish aniqlanmadi"
}


st.title("Ruhiy buzilishlarni bashorat qilish ilovasi")


st.header("Ma'lumotlarni kiriting:")


value_map = {
    "Yig‘ilish": ["Doimiy", "Ba'zan", "Kamdan-kam"],
    "Yuqori kayfiyat": ["Doimiy", "Ko‘pincha", "Kamdan-kam"],
    "Charchash": ["Doimiy", "Ba'zan", "Hech qachon"],
    "Uyqu buzilishi": ["Ba'zan", "Ko‘pincha", "Hech qachon"],
    "Kayfiyat o‘zgarishi": ["HA", "YO‘Q"],
    "O‘z joniga qasd qilish fikrlari": ["HA", "YO‘Q"],
    "Tajovuzkor javob": ["HA", "YO‘Q"],
    "Ortacha fikrlash": ["HA", "YO‘Q"],
    "Ovqatlanish buzilishi": ["HA", "YO‘Q"],
    "Galutsinatsiyalar": ["HA", "YO‘Q"],
    "Impulsiv xatti-harakatlar": ["HA", "YO‘Q"],
    "Past o‘zini baholash": ["HA", "YO‘Q"],
    "Stress darajasi": ["Yuqori", "O‘rtacha", "Past"],
    "Energiya darajasi": ["Yuqori", "O‘rtacha", "Past"],
    "Diqqat darajasi": ["Yuqori", "O‘rtacha", "Past"],
    "Motivatsiya darajasi": ["Yuqori", "O‘rtacha", "Past"],
    "Tashvish darajasi": ["Yuqori", "O‘rtacha", "Past"]
}


sadness = st.selectbox("Yig‘ilish", value_map["Yig‘ilish"])
euphoric = st.selectbox("Yuqori kayfiyat", value_map["Yuqori kayfiyat"])
exhausted = st.selectbox("Charchash", value_map["Charchash"])
sleep_dissorder = st.selectbox("Uyqu buzilishi", value_map["Uyqu buzilishi"])
mood_swing = st.selectbox("Kayfiyat o‘zgarishi", value_map["Kayfiyat o‘zgarishi"])
suicidal_thoughts = st.selectbox("O‘z joniga qasd qilish fikrlari", value_map["O‘z joniga qasd qilish fikrlari"])
aggressive_response = st.selectbox("Tajovuzkor javob", value_map["Tajovuzkor javob"])
overthinking = st.selectbox("Ortacha fikrlash", value_map["Ortacha fikrlash"])
eating_disorder = st.selectbox("Ovqatlanish buzilishi", value_map["Ovqatlanish buzilishi"])
hallucinations = st.selectbox("Galutsinatsiyalar", value_map["Galutsinatsiyalar"])
impulsive_behavior = st.selectbox("Impulsiv xatti-harakatlar", value_map["Impulsiv xatti-harakatlar"])
low_self_esteem = st.selectbox("Past o‘zini baholash", value_map["Past o‘zini baholash"])
stress = st.selectbox("Stress darajasi", value_map["Stress darajasi"])
energy_level = st.selectbox("Energiya darajasi", value_map["Energiya darajasi"])
focus_level = st.selectbox("Diqqat darajasi", value_map["Diqqat darajasi"])
motivation_level = st.selectbox("Motivatsiya darajasi", value_map["Motivatsiya darajasi"])
anxiety_level = st.selectbox("Tashvish darajasi", value_map["Tashvish darajasi"])


if st.button("Natijani ko'rsat"):
    
    input_data = [
        value_map["Yig‘ilish"].index(sadness),
        value_map["Yuqori kayfiyat"].index(euphoric),
        value_map["Charchash"].index(exhausted),
        value_map["Uyqu buzilishi"].index(sleep_dissorder),
        value_map["Kayfiyat o‘zgarishi"].index(mood_swing),
        value_map["O‘z joniga qasd qilish fikrlari"].index(suicidal_thoughts),
        value_map["Tajovuzkor javob"].index(aggressive_response),
        value_map["Ortacha fikrlash"].index(overthinking),
        value_map["Ovqatlanish buzilishi"].index(eating_disorder),
        value_map["Galutsinatsiyalar"].index(hallucinations),
        value_map["Impulsiv xatti-harakatlar"].index(impulsive_behavior),
        value_map["Past o‘zini baholash"].index(low_self_esteem),
        value_map["Stress darajasi"].index(stress),
        value_map["Energiya darajasi"].index(energy_level),
        value_map["Diqqat darajasi"].index(focus_level),
        value_map["Motivatsiya darajasi"].index(motivation_level),
        value_map["Tashvish darajasi"].index(anxiety_level)
    ]

    
   input_data = np.array(input_data).reshape(1, -1)
    
    prediction = model.predict(input_data)
    
    diagnosis_result = diagnosis_map.get(prediction[0], "Noma'lum diagnoz")
    
    # Ajoyib ko'rinishdagi natija
    st.markdown(f"""
    <style>
        .result {{
            background-color: #F1F1F1;
            padding: 20px;
            border-radius: 10px;
            font-size: 20px;
            font-weight: bold;
            color: #2C3E50;
            border: 2px solid #3498DB;
        }}
        .result-header {{
            font-size: 24px;
            color: #3498DB;
            margin-bottom: 15px;
        }}
    </style>
    <div class="result">
        <div class="result-header">Bashoratlangan diagnoz:</div>
        <p>{diagnosis_result}</p>
    </div>
    """, unsafe_allow_html=True)
