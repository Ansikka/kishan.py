import streamlit as st
from datetime import datetime

# ------------------ BhashaBuddy - Language Support ------------------
LANGUAGE_DATA = {
    "Hindi": {
        "welcome": "कृषि मित्र में आपका स्वागत है!",
        "today_task": "आज के लिए आपका कार्य:",
        "no_task": "आज कोई विशेष कार्य नहीं है।",
        "price_info": "मंडी मूल्य जानकारी:",
        "disease_detected": "फसल रोग का पता चला:",
        "govt_scheme": "सरकारी योजना विवरण:",
        "weather": "आज का मौसम:",
        "chat": "किसान सहायक चैटबॉट",
        "ask_question": "कोई प्रश्न पूछें"
    },
    "English": {
        "welcome": "Welcome to KrishiMitra!",
        "today_task": "Your task for today:",
        "no_task": "No specific task for today.",
        "price_info": "Mandi price information:",
        "disease_detected": "Crop disease detected:",
        "govt_scheme": "Government scheme details:",
        "weather": "Today's Weather:",
        "chat": "Farmer Help Chatbot",
        "ask_question": "Ask a question"
    },
    "Bangoli": {
        "welcome": "কৃষিমিত্রতে আপনাকে স্বাগতম!",
        "today_task": "আজকের কাজ:",
        "no_task": "আজ কোন নির্দিষ্ট কাজ নেই।",
        "price_info": "মন্ডির মূল্য তথ্য:",
        "disease_detected": "ফসলের রোগ সনাক্ত হয়েছে:",
        "govt_scheme": "সরকারি প্রকল্প বিবরণ:",
        "weather": "আজকের আবহাওয়া:",
        "chat": "চাষি সহায়তা চ্যাটবট",
        "ask_question": "একটি প্রশ্ন জিজ্ঞাসা করুন"
    }
}

TASKS = [
    "Check soil moisture levels",
    "Irrigate tomato crops",
    "Spray pesticide for aphids",
    "Harvest brinjal",
    "Apply organic fertilizer to field"
]

MANDI_PRICES = {
    "wheat": "₹2200/qtl",
    "rice": "₹1800/qtl",
    "mustard": "₹5500/qtl"
}

GOVT_SCHEMES = {
    "PM-KISAN": "Rs. 6000 per year to eligible farmers",
    "PMFBY": "Crop insurance at nominal premium rates",
    "Soil Health Card": "Free soil testing and nutrient advice"
}

# ------------------ UI ------------------
st.set_page_config(page_title="KrishiMitra", layout="centered")

lang = st.selectbox("Choose Language", options=["English", "Hindi", "Bangoli"])
st.title(LANGUAGE_DATA[lang]["welcome"])

# ------------------ Task Suggestion ------------------
today = datetime.now().day
if today % 2 == 0:
    st.subheader(LANGUAGE_DATA[lang]['today_task'])
    st.success(TASKS[today % len(TASKS)])
else:
    st.info(LANGUAGE_DATA[lang]['no_task'])

# ------------------ Mandi Prices ------------------
st.subheader(LANGUAGE_DATA[lang]['price_info'])
for crop, price in MANDI_PRICES.items():
    st.write(f"👉 **{crop.title()}**: {price}")

# ------------------ Government Schemes ------------------
st.subheader(LANGUAGE_DATA[lang]['govt_scheme'])
scheme = st.selectbox("Select Scheme", list(GOVT_SCHEMES.keys()))
st.write(f"📋 {GOVT_SCHEMES[scheme]}")

# ------------------ Crop Disease Detection ------------------
st.subheader(LANGUAGE_DATA[lang]['disease_detected'])
image = st.file_uploader("Upload Crop Image", type=["jpg", "jpeg", "png"])
if image:
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.warning("🧪 Simulated Result: Blight detected in tomato leaves")

# ------------------ Weather Forecast (Simulated) ------------------
st.subheader(LANGUAGE_DATA[lang]['weather'])
location = st.text_input("Enter Your Village or District Name")
if location:
    st.info(f"📍 Simulated Weather for **{location}**: 35°C, Clear Sky, Wind 10 km/h")

# ------------------ Farmer Chatbot (Simulated) ------------------
st.subheader(LANGUAGE_DATA[lang]['chat'])
query = st.text_input(LANGUAGE_DATA[lang]["ask_question"])
if query:
    st.success("🤖 Chatbot: Please use neem-based pesticides for aphids.")

# import streamlit as st
# from datetime import datetime
# import streamlit.components.v1 as components

# # ------------------ Voice Support ------------------
# def speak_text(text):
#     js = f"""
#     <script>
#     var msg = new SpeechSynthesisUtterance("{text}");
#     window.speechSynthesis.speak(msg);
#     </script>
#     """
#     components.html(js)

# # ------------------ BhashaBuddy - Language Support ------------------
# LANGUAGE_DATA = {
#     "Hindi": {
#         "welcome": "\U0001F33E कृषि मित्र में आपका स्वागत है!",
#         "today_task": "\U0001F4CB आज के लिए आपका कार्य:",
#         "no_task": "⚠️ आज कोई विशेष कार्य नहीं है।",
#         "price_info": "\U0001F4B8 मंडी मूल्य जानकारी:",
#         "disease_detected": "\U0001F33F फसल रोग का पता चला:",
#         "govt_scheme": "\U0001F4CA सरकारी योजना विवरण:",
#         "weather": "☀️ आज का मौसम:",
#         "chat": "\U0001F916 किसान सहायक चैटबॉट",
#         "ask_question": "कोई प्रश्न पूछें"
#     },
#     "English": {
#         "welcome": "\U0001F33E Welcome to KrishiMitra!",
#         "today_task": "\U0001F4CB Your task for today:",
#         "no_task": "⚠️ No specific task for today.",
#         "price_info": "\U0001F4B8 Mandi price information:",
#         "disease_detected": "\U0001F33F Crop disease detected:",
#         "govt_scheme": "\U0001F4CA Government scheme details:",
#         "weather": "☀️ Today's Weather:",
#         "chat": "\U0001F916 Farmer Help Chatbot",
#         "ask_question": "Ask a question"
#     },
#     "Bangoli": {
#         "welcome": "\U0001F33E কৃষিমিত্রতে আপনাকে স্বাগতম!",
#         "today_task": "\U0001F4CB আজকের কাজ:",
#         "no_task": "⚠️ আজ কোন নির্দিষ্ট কাজ নেই।",
#         "price_info": "\U0001F4B8 মন্ডির মূল্য তথ্য:",
#         "disease_detected": "\U0001F33F ফসলের রোগ সনাক্ত হয়েছে:",
#         "govt_scheme": "\U0001F4CA সরকারি প্রকল্প বিবরণ:",
#         "weather": "☀️ আজকের আবহাওয়া:",
#         "chat": "\U0001F916 চাষি সহায়তা চ্যাটবট",
#         "ask_question": "একটি প্রশ্ন জিজ্ঞাসা করুন"
#     },

#     "Punjabi": {
#         "welcome": "\U0001F33E ਕ੍ਰਿਸ਼ੀ ਮਿਤਰ ਵਿੱਚ ਤੁਹਾਡਾ ਸੁਆਗਤ ਹੈ!",
#         "today_task": "\U0001F4CB ਅੱਜ ਲਈ ਤੁਹਾਡਾ ਕੰਮ:",
#         "no_task": "⚠️ ਅੱਜ ਕੋਈ ਵਿਸ਼ੇਸ਼ ਕੰਮ ਨਹੀਂ ਹੈ।",
#         "price_info": "\U0001F4B8 ਮੰਡੀ ਮੁੱਲ ਜਾਣਕਾਰੀ:",
#         "disease_detected": "\U0001F33F ਫਸਲ ਦੀ ਬਿਮਾਰੀ ਦੀ ਪਛਾਣ ਹੋਈ:",
#         "govt_scheme": "\U0001F4CA ਸਰਕਾਰੀ ਯੋਜਨਾ ਵੇਰਵਾ:",
#         "weather": "☀️ ਅੱਜ ਦਾ ਮੌਸਮ:",
#         "chat": "\U0001F916 ਕਿਸਾਨ ਸਹਾਇਤਾ ਚੈਟਬੌਟ",
#         "ask_question": "ਇੱਕ ਸਵਾਲ ਪੁੱਛੋ"
#     },
#     "Bhojpuri": {
#         "welcome": "\U0001F33E कृषिमित्र में रउआ स्वागत बा!",
#         "today_task": "\U0001F4CB आज के काम:",
#         "no_task": "⚠️ आज कवनो खास काम नइखे।",
#         "price_info": "\U0001F4B8 मंडी के दाम जानकारी:",
#         "disease_detected": "\U0001F33F फसल के बीमारी पाइल गइल:",
#         "govt_scheme": "\U0001F4CA सरकारी योजना विवरण:",
#         "weather": "☀️ आज के मौसम:",
#         "chat": "\U0001F916 किसान मदद चैटबॉट",
#         "ask_question": "कोई सवाल पूछीं"
#     },
#     "Tamil": {
#         "welcome": "\U0001F33E கிருஷிமித்ராவிற்கு வரவேற்கிறோம்!",
#         "today_task": "\U0001F4CB இன்றைய உங்கள் வேலை:",
#         "no_task": "⚠️ இன்றைக்கு சிறப்பு வேலை இல்லை.",
#         "price_info": "\U0001F4B8 மண்டி விலை தகவல்:",
#         "disease_detected": "\U0001F33F பயிர் நோய் கண்டறியப்பட்டது:",
#         "govt_scheme": "\U0001F4CA அரசு திட்ட விவரங்கள்:",
#         "weather": "☀️ இன்றைய வானிலை:",
#         "chat": "\U0001F916 விவசாய உதவி சந்தை",
#         "ask_question": "ஒரு கேள்வி கேளுங்கள்"
#     },
#     "Telugu": {
#         "welcome": "\U0001F33E కృషిమిత్రా కు స్వాగతం!",
#         "today_task": "\U0001F4CB ఈరోజు మీ పని:",
#         "no_task": "⚠️ ఈ రోజు ప్రత్యేకమైన పని లేదు.",
#         "price_info": "\U0001F4B8 మండీ ధరల సమాచారం:",
#         "disease_detected": "\U0001F33F పంట వ్యాధి గుర్తించబడింది:",
#         "govt_scheme": "\U0001F4CA ప్రభుత్వం పథక వివరాలు:",
#         "weather": "☀️ ఈరోజు వాతావరణం:",
#         "chat": "\U0001F916 రైతు సహాయ చాట్బాట్",
#         "ask_question": "ప్రశ్నను అడగండి"
#     },
#     "Odia": {
#         "welcome": "\U0001F33E କୃଷିମିତ୍ରକୁ ସ୍ୱାଗତ!",
#         "today_task": "\U0001F4CB ଆଜିର କାର୍ଯ୍ୟ:",
#         "no_task": "⚠️ ଆଜି କୌଣସି ବିଶେଷ କାର୍ଯ୍ୟ ନାହିଁ।",
#         "price_info": "\U0001F4B8 ମଣ୍ଡି ଦର ସୂଚନା:",
#         "disease_detected": "\U0001F33F ପାଣିଗଛ ରୋଗ ଚିହ୍ନଟ:",
#         "govt_scheme": "\U0001F4CA ସରକାରୀ ଯୋଜନା ବିବରଣୀ:",
#         "weather": "☀️ ଆଜିର ପାଣିପାଗ:",
#         "chat": "\U0001F916 କୃଷକ ସାହାଯ୍ୟ ଚ୍ୟାଟ୍ବଟ୍",
#         "ask_question": "ପ୍ରଶ୍ନ ପଚାରନ୍ତୁ"
#     },
#     "Chhattisgarhi": {
#         "welcome": "\U0001F33E कृषिमित्र मं आपमन ला स्वागत हे!",
#         "today_task": "\U0001F4CB आज के काम हे:",
#         "no_task": "⚠️ आज कोनो खास काम नइ हे।",
#         "price_info": "\U0001F4B8 मंडी के भाव जानकारी:",
#         "disease_detected": "\U0001F33F फसल मं रोग मिलिस:",
#         "govt_scheme": "\U0001F4CA सरकारी योजना के जानकारी:",
#         "weather": "☀️ आज के मौसम:",
#         "chat": "\U0001F916 किसान सहायता चैटबॉट",
#         "ask_question": "कोनो सवाल पूछव"
#     }

# }

# TASKS = [
#     "Check soil moisture levels",
#     "Irrigate tomato crops",
#     "Spray pesticide for aphids",
#     "Harvest brinjal",
#     "Apply organic fertilizer to field"
# ]

# MANDI_PRICES = {
#     "wheat": "₹2200/qtl",
#     "rice": "₹1800/qtl",
#     "mustard": "₹5500/qtl",
#     "maize": "₹1700/qtl",
#     "barley": "₹1600/qtl",
#     "soybean": "₹4800/qtl",
#     "cotton": "₹6600/qtl",
#     "groundnut": "₹5500/qtl",
#     "sugarcane": "₹340/qtl",
#     "potato": "₹1200/qtl",
#     "onion": "₹900/qtl",
#     "tomato": "₹1100/qtl"
# }
# GOVT_SCHEMES = {
#     "PM-KISAN": "₹6000 per year to eligible farmers in three installments.",
#     "PMFBY": "Pradhan Mantri Fasal Bima Yojana: Crop insurance at nominal premium rates.",
#     "Soil Health Card": "Provides soil nutrient status and recommendations for balanced use of fertilizers.",
#     "KCC": "Kisan Credit Card: Short-term credit to farmers for cultivation expenses at low interest.",
#     "eNAM": "National Agriculture Market: Unified national market for agricultural commodities.",
#     "RKVY": "Rashtriya Krishi Vikas Yojana: Funds to support agricultural infrastructure and innovation.",
#     "PUSA Krishi": "Access to agri-tech solutions from ICAR-PUSA for higher productivity.",
#     "Agri Infrastructure Fund": "₹1 Lakh Cr fund for building warehouses, cold storage and processing units.",
#     "Atma Nirbhar Krishi": "Promotes self-reliance in agriculture with reforms in APMC, contract farming.",
#     "PM Kusum": "Subsidy for installing solar pumps and grid-connected renewable power systems for irrigation."
# }
# # ------------------ UI ------------------
# st.set_page_config(page_title="KrishiMitra", layout="centered")
# st.markdown("""
#     <style>
#     .main {
#         background-color: #f6fff4;
#     }
#     .stButton>button {
#         background-color: #4CAF50;
#         color: white;
#         border-radius: 10px;
#         padding: 0.5em 1em;
#     }
#     .stTextInput>div>input {
#         border-radius: 8px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# lang = st.selectbox("Choose Language / भाषा चुनें / ভাষা নির্বাচন করুন", options=["English", "Hindi", "Bangoli","Punjabi","Chhatishgharh","odia","Tamil","Telgu","Bhojpuri"])
# st.title(LANGUAGE_DATA[lang]["welcome"])
# if st.button("🔊 Speak Welcome"):
#     speak_text(LANGUAGE_DATA[lang]["welcome"])

# # ------------------ Task Suggestion ------------------
# st.markdown("---")
# today = datetime.now().day
# if today % 2 == 0:
#     st.subheader(LANGUAGE_DATA[lang]['today_task'])
#     task = TASKS[today % len(TASKS)]
#     st.success(f"✅ {task}")
#     if st.button("🔊 Speak Task"):
#         speak_text(task)
# else:
#     st.info(LANGUAGE_DATA[lang]['no_task'])
#     if st.button("🔊 Speak Info"):
#         speak_text(LANGUAGE_DATA[lang]['no_task'])

# # ------------------ Mandi Prices ------------------
# st.markdown("---")
# st.subheader(LANGUAGE_DATA[lang]['price_info'])
# price_text = ""
# for crop, price in MANDI_PRICES.items():
#     st.markdown(f"- **{crop.title()}**: {price}")
#     price_text += f"{crop.title()} {price}. "
# if st.button("🔊 Speak Prices"):
#     speak_text(price_text)

# # ------------------ Government Schemes ------------------
# st.markdown("---")
# st.subheader(LANGUAGE_DATA[lang]['govt_scheme'])
# scheme = st.selectbox("Select Scheme", list(GOVT_SCHEMES.keys()))
# st.info(f"📋 {GOVT_SCHEMES[scheme]}")
# if st.button("🔊 Speak Scheme"):
#     speak_text(GOVT_SCHEMES[scheme])

# # ------------------ Crop Disease Detection ------------------
# st.markdown("---")
# st.subheader(LANGUAGE_DATA[lang]['disease_detected'])
# image = st.file_uploader("Upload Crop Image", type=["jpg", "jpeg", "png"])
# if image:
#     st.image(image, caption="Uploaded Image", use_column_width=True)
#     st.warning("🧪 Simulated Result: Blight detected in tomato leaves")
#     if st.button("🔊 Speak Detection Result"):
#         speak_text("Blight detected in tomato leaves")

# # ------------------ Weather Forecast (Simulated) ------------------
# st.markdown("---")
# st.subheader(LANGUAGE_DATA[lang]['weather'])
# location = st.text_input("Enter Your Village or District Name")
# if location:
#     weather_report = f"Simulated Weather for {location}: 35°C, Clear Sky, Wind 10 km/h"
#     st.info(f"📍 {weather_report}")
#     if st.button("🔊 Speak Weather"):
#         speak_text(weather_report)

# # ------------------ Farmer Chatbot (Simulated) ------------------
# st.markdown("---")
# st.subheader(LANGUAGE_DATA[lang]['chat'])
# query = st.text_input(LANGUAGE_DATA[lang]["ask_question"])
# if query:
#     reply = "Please use neem-based pesticides for aphids."
#     st.success(f"🤖 Chatbot: {reply}")
#     if st.button("🔊 Speak Chatbot Reply"):
#         speak_text(reply)
