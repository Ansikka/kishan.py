# import streamlit as st
# from datetime import datetime

# # Language Support
# LANGUAGE_DATA = {
#     "Hindi": {
#         "welcome": "कृषि मित्र में आपका स्वागत है!",
#         "task": "आज का कार्य:",
#     },
#     "English": {
#         "welcome": "Welcome to KrishiMitra!",
#         "task": "Today's Task:",
#     },
#     "Bangoli": {
#         "welcome": "কৃষিমিত্রতে আপনাকে স্বাগতম!",
#         "task": "আজকের কাজ:",
#     }
# }

# TASKS = [
#     "Check soil moisture levels",
#     "Irrigate tomato crops",
#     "Spray pesticide for aphids",
#     "Harvest brinjal",
#     "Apply organic fertilizer to field"
# ]

# # Select language
# lang = st.selectbox("Choose Language", options=["English", "Hindi", "Bangoli"])
# st.title(LANGUAGE_DATA[lang]["welcome"])

# # Show today's task
# today = datetime.now().day
# if today % 2 == 0:
#     st.write(f"📝 {LANGUAGE_DATA[lang]['task']} {TASKS[today % len(TASKS)]}")
# else:
#     st.write("✅ No task for today.")

# import streamlit as st
# from datetime import datetime

# # ------------------ BhashaBuddy - Language Support ------------------
# LANGUAGE_DATA = {
#     "Hindi": {
#         "welcome": "कृषि मित्र में आपका स्वागत है!",
#         "today_task": "आज के लिए आपका कार्य:",
#         "no_task": "आज कोई विशेष कार्य नहीं है।",
#         "price_info": "मंडी मूल्य जानकारी:",
#         "disease_detected": "फसल रोग का पता चला:",

#         "govt_scheme": "सरकारी योजना विवरण:",
#         "choose_scheme": "योजना का नाम दर्ज करें:",
#         "choose_image": "छवि फ़ाइल नाम दर्ज करें:",
#     },
#     "English": {
#         "welcome": "Welcome to KrishiMitra!",
#         "today_task": "Your task for today:",
#         "no_task": "No specific task for today.",
#         "price_info": "Mandi price information:",
#         "disease_detected": "Crop disease detected:",
#         "govt_scheme": "Government scheme details:",
#         "choose_scheme": "Enter scheme name:",
#         "choose_image": "Enter image file name:",
#     },
#     "Bangoli": {
#         "welcome": "কৃষিমিত্রতে আপনাকে স্বাগতম!",
#         "today_task": "আজকের কাজ:",
#         "no_task": "আজ কোন নির্দিষ্ট কাজ নেই।",
#         "price_info": "মন্ডির মূল্য তথ্য:",
#         "disease_detected": "ফসলের রোগ সনাক্ত হয়েছে:",
#         "govt_scheme": "সরকারি প্রকল্প বিবরণ:",
#         "choose_scheme": "প্রকল্পের নাম লিখুন:",
#         "choose_image": "ছবির ফাইল নাম লিখুন:",
#     }
# }

# # ------------------ Farming Tasks ------------------
# TASKS = [
#     "Check soil moisture levels",
#     "Irrigate tomato crops",
#     "Spray pesticide for aphids",
#     "Harvest brinjal",
#     "Apply organic fertilizer to field"
# ]

# # ------------------ Mock Data ------------------
# MANDI_PRICES = {
#     "wheat": "₹2200/qtl",
#     "rice": "₹1800/qtl",
#     "mustard": "₹5500/qtl"
# }

# CROP_DISEASES = {
#     "image1.jpg": "Blight disease in potato",
#     "image2.jpg": "Rust in wheat leaves"
# }

# GOVT_SCHEMES = {
#     "PM-KISAN": "Rs. 6000 per year to eligible farmers",
#     "PMFBY": "Crop insurance at nominal premium rates",
#     "Soil Health Card": "Free soil testing and nutrient advice"
# }

# # ------------------ App UI ------------------
# st.set_page_config(page_title="KrishiMitra", page_icon="🌾")

# lang = st.sidebar.selectbox("🌐 Choose Language", options=["English", "Hindi", "Bangoli"])
# st.title(LANGUAGE_DATA[lang]["welcome"])

# # 1. Task Section
# st.subheader("📝 " + LANGUAGE_DATA[lang]["today_task"])
# today = datetime.now().day
# if today % 2 == 0:
#     task = TASKS[today % len(TASKS)]
#     st.success(task)
# else:
#     st.warning(LANGUAGE_DATA[lang]["no_task"])

# # 2. Mandi Prices
# st.subheader("📈 " + LANGUAGE_DATA[lang]["price_info"])
# for crop, price in MANDI_PRICES.items():
#     st.write(f"**{crop.capitalize()}**: {price}")

# # 3. Crop Disease Detection
# st.subheader("🌾 " + LANGUAGE_DATA[lang]["disease_detected"])
# image_name = st.text_input(LANGUAGE_DATA[lang]["choose_image"], value="image1.jpg")
# result = CROP_DISEASES.get(image_name, "No disease detected")
# st.info(result)

# # 4. Govt Scheme
# st.subheader("🏛 " + LANGUAGE_DATA[lang]["govt_scheme"])
# scheme_name = st.text_input(LANGUAGE_DATA[lang]["choose_scheme"], value="PM-KISAN")
# scheme_info = GOVT_SCHEMES.get(scheme_name, "Scheme not found")
# st.write(scheme_info)


# KrishiMitra: AI-Powered Daily Companion for Farmers (Streamlit Version)

# import streamlit as st
# from datetime import datetime

# # ------------------ BhashaBuddy - Language Support ------------------
# LANGUAGE_DATA = {
#     "Hindi": {
#         "welcome": "कृषि मित्र में आपका स्वागत है!",
#         "today_task": "आज के लिए आपका कार्य:",
#         "no_task": "आज कोई विशेष कार्य नहीं है।",
#         "price_info": "मंडी मूल्य जानकारी:",
#         "disease_detected": "फसल रोग का पता चला:",
#         "govt_scheme": "सरकारी योजना विवरण:",
#         "weather": "आज का मौसम:",
#         "chat": "किसान सहायक चैटबॉट",
#         "ask_question": "कोई प्रश्न पूछें"
#     },
#     "English": {
#         "welcome": "Welcome to KrishiMitra!",
#         "today_task": "Your task for today:",
#         "no_task": "No specific task for today.",
#         "price_info": "Mandi price information:",
#         "disease_detected": "Crop disease detected:",
#         "govt_scheme": "Government scheme details:",
#         "weather": "Today's Weather:",
#         "chat": "Farmer Help Chatbot",
#         "ask_question": "Ask a question"
#     },
#     "Bangoli": {
#         "welcome": "কৃষিমিত্রতে আপনাকে স্বাগতম!",
#         "today_task": "আজকের কাজ:",
#         "no_task": "আজ কোন নির্দিষ্ট কাজ নেই।",
#         "price_info": "মন্ডির মূল্য তথ্য:",
#         "disease_detected": "ফসলের রোগ সনাক্ত হয়েছে:",
#         "govt_scheme": "সরকারি প্রকল্প বিবরণ:",
#         "weather": "আজকের আবহাওয়া:",
#         "chat": "চাষি সহায়তা চ্যাটবট",
#         "ask_question": "একটি প্রশ্ন জিজ্ঞাসা করুন"
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
#     "mustard": "₹5500/qtl"
# }

# GOVT_SCHEMES = {
#     "PM-KISAN": "Rs. 6000 per year to eligible farmers",
#     "PMFBY": "Crop insurance at nominal premium rates",
#     "Soil Health Card": "Free soil testing and nutrient advice"
# }

# # ------------------ UI ------------------
# st.set_page_config(page_title="KrishiMitra", layout="centered")

# lang = st.selectbox("Choose Language", options=["English", "Hindi", "Bangoli"])
# st.title(LANGUAGE_DATA[lang]["welcome"])

# # ------------------ Task Suggestion ------------------
# today = datetime.now().day
# if today % 2 == 0:
#     st.subheader(LANGUAGE_DATA[lang]['today_task'])
#     st.success(TASKS[today % len(TASKS)])
# else:
#     st.info(LANGUAGE_DATA[lang]['no_task'])

# # ------------------ Mandi Prices ------------------
# st.subheader(LANGUAGE_DATA[lang]['price_info'])
# for crop, price in MANDI_PRICES.items():
#     st.write(f"👉 **{crop.title()}**: {price}")

# # ------------------ Government Schemes ------------------
# st.subheader(LANGUAGE_DATA[lang]['govt_scheme'])
# scheme = st.selectbox("Select Scheme", list(GOVT_SCHEMES.keys()))
# st.write(f"📋 {GOVT_SCHEMES[scheme]}")

# # ------------------ Crop Disease Detection ------------------
# st.subheader(LANGUAGE_DATA[lang]['disease_detected'])
# image = st.file_uploader("Upload Crop Image", type=["jpg", "jpeg", "png"])
# if image:
#     st.image(image, caption="Uploaded Image", use_column_width=True)
#     st.warning("🧪 Simulated Result: Blight detected in tomato leaves")

# # ------------------ Weather Forecast (Simulated) ------------------
# st.subheader(LANGUAGE_DATA[lang]['weather'])
# location = st.text_input("Enter Your Village or District Name")
# if location:
#     st.info(f"📍 Simulated Weather for **{location}**: 35°C, Clear Sky, Wind 10 km/h")

# # ------------------ Farmer Chatbot (Simulated) ------------------
# st.subheader(LANGUAGE_DATA[lang]['chat'])
# query = st.text_input(LANGUAGE_DATA[lang]["ask_question"])
# if query:
#     st.success("🤖 Chatbot: Please use neem-based pesticides for aphids.")
import streamlit as st
from datetime import datetime

# ------------------ BhashaBuddy - Language Support ------------------
LANGUAGE_DATA = {
    "Hindi": {
        "welcome": "\U0001F33E कृषि मित्र में आपका स्वागत है!",
        "today_task": "\U0001F4CB आज के लिए आपका कार्य:",
        "no_task": "\u26A0\ufe0f आज कोई विशेष कार्य नहीं है।",
        "price_info": "\U0001F4B8 मंडी मूल्य जानकारी:",
        "disease_detected": "\U0001F33F फसल रोग का पता चला:",
        "govt_scheme": "\U0001F4CA सरकारी योजना विवरण:",
        "weather": "\u2600\ufe0f आज का मौसम:",
        "chat": "\U0001F916 किसान सहायक चैटबॉट",
        "ask_question": "कोई प्रश्न पूछें"
    },
    "English": {
        "welcome": "\U0001F33E Welcome to KrishiMitra!",
        "today_task": "\U0001F4CB Your task for today:",
        "no_task": "\u26A0\ufe0f No specific task for today.",
        "price_info": "\U0001F4B8 Mandi price information:",
        "disease_detected": "\U0001F33F Crop disease detected:",
        "govt_scheme": "\U0001F4CA Government scheme details:",
        "weather": "\u2600\ufe0f Today's Weather:",
        "chat": "\U0001F916 Farmer Help Chatbot",
        "ask_question": "Ask a question"
    },
    "Bangoli": {
        "welcome": "\U0001F33E কৃষিমিত্রতে আপনাকে স্বাগতম!",
        "today_task": "\U0001F4CB আজকের কাজ:",
        "no_task": "\u26A0\ufe0f আজ কোন নির্দিষ্ট কাজ নেই।",
        "price_info": "\U0001F4B8 মন্ডির মূল্য তথ্য:",
        "disease_detected": "\U0001F33F ফসলের রোগ সনাক্ত হয়েছে:",
        "govt_scheme": "\U0001F4CA সরকারি প্রকল্প বিবরণ:",
        "weather": "\u2600\ufe0f আজকের আবহাওয়া:",
        "chat": "\U0001F916 চাষি সহায়তা চ্যাটবট",
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
    "maize": "₹1700/qtl",
    "barley": "₹1600/qtl",
    "soybean": "₹4800/qtl",
    "cotton": "₹6600/qtl",
    "groundnut": "₹5500/qtl",
    "sugarcane": "₹340/qtl",
    "potato": "₹1200/qtl",
    "onion": "₹900/qtl",
    "tomato": "₹1100/qtl"
}

GOVT_SCHEMES = {
    "PM-KISAN": "₹6000 per year to eligible farmers in three installments.",
    "PMFBY": "Pradhan Mantri Fasal Bima Yojana: Crop insurance at nominal premium rates.",
    "Soil Health Card": "Provides soil nutrient status and recommendations for balanced use of fertilizers.",
    "KCC": "Kisan Credit Card: Short-term credit to farmers for cultivation expenses at low interest.",
    "eNAM": "National Agriculture Market: Unified national market for agricultural commodities.",
    "RKVY": "Rashtriya Krishi Vikas Yojana: Funds to support agricultural infrastructure and innovation.",
    "PUSA Krishi": "Access to agri-tech solutions from ICAR-PUSA for higher productivity.",
    "Agri Infrastructure Fund": "₹1 Lakh Cr fund for building warehouses, cold storage and processing units.",
    "Atma Nirbhar Krishi": "Promotes self-reliance in agriculture with reforms in APMC, contract farming.",
    "PM Kusum": "Subsidy for installing solar pumps and grid-connected renewable power systems for irrigation."
}

# ------------------ UI ------------------
st.set_page_config(page_title="KrishiMitra", layout="centered")
st.markdown("""
    <style>
    .main {
        background-color: #f6fff4;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 0.5em 1em;
    }
    .stTextInput>div>input {
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

lang = st.selectbox("Choose Language / भाषा चुनें / ভাষা নির্বাচন করুন", options=["English", "Hindi", "Bangoli"])
st.title(LANGUAGE_DATA[lang]["welcome"])

# ------------------ Task Suggestion ------------------
st.markdown("---")
today = datetime.now().day
if today % 2 == 0:
    st.subheader(LANGUAGE_DATA[lang]['today_task'])
    st.success(f"✅ {TASKS[today % len(TASKS)]}")
else:
    st.info(LANGUAGE_DATA[lang]['no_task'])

# ------------------ Mandi Prices ------------------
st.markdown("---")
st.subheader(LANGUAGE_DATA[lang]['price_info'])
for crop, price in MANDI_PRICES.items():
    st.markdown(f"- **{crop.title()}**: {price}")

# ------------------ Government Schemes ------------------
st.markdown("---")
st.subheader(LANGUAGE_DATA[lang]['govt_scheme'])
scheme = st.selectbox("Select Scheme", list(GOVT_SCHEMES.keys()))
st.info(f"📋 {GOVT_SCHEMES[scheme]}")

# ------------------ Crop Disease Detection ------------------
st.markdown("---")
st.subheader(LANGUAGE_DATA[lang]['disease_detected'])
image = st.file_uploader("Upload Crop Image", type=["jpg", "jpeg", "png"])
if image:
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.warning("🧪 Simulated Result: Blight detected in tomato leaves")

# ------------------ Weather Forecast (Simulated) ------------------
st.markdown("---")
st.subheader(LANGUAGE_DATA[lang]['weather'])
location = st.text_input("Enter Your Village or District Name")
if location:
    st.info(f"📍 Simulated Weather for **{location}**: 35°C, Clear Sky, Wind 10 km/h")

# ------------------ Farmer Chatbot (Simulated) ------------------
st.markdown("---")
st.subheader(LANGUAGE_DATA[lang]['chat'])
query = st.text_input(LANGUAGE_DATA[lang]["ask_question"])
if query:
    st.success("🤖 Chatbot: Please use neem-based pesticides for aphids.")

