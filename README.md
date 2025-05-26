**🌾 KrishiMitra – Empowering Indian Farmers with AI & Language Support
KrishiMitra is a smart,multilingual Streamlit web application designed to assist farmers in India!!
By providing crucial daily support—crop care tips, mandi prices, government schemes, disease detection, weather updates, and a friendly chatbot.
With BhashaBuddy farmers can use the app in their native languages, making the platform more inclusive and empowering!!
**
🚀 Features
🌐 BhashaBuddy – Language Support
Supports 9+ Indian languages with localized translations:

English, Hindi, Bengali, Punjabi, Bhojpuri, Tamil, Telugu, Odia, Chhattisgarhi

More languages can be added with ease.

📅 Smart Daily Task Assistant
Suggests personalized agricultural tasks based on the day and farming season, such as:

Irrigation reminders

Fertilizer application

Pest control alerts

Harvest schedules

📈 Mandi Price Updates
Shows updated and localized market rates (mandi prices) for essential crops:

Wheat, Rice, Mustard, Sugarcane, Maize, etc.

Custom pricing data can be integrated from APIs.

🧬 Crop Disease Detection (Simulated)
Upload crop images and get instant simulated feedback (future: integrate with ML models for real detection). Example:

"Blight detected in tomato leaves"

“Powdery mildew on brinjal”

🌤 Weather Forecast (Simulated)
Location-based simulated weather update feature:

Temperature

Sky condition

Wind speed

Can be linked to real-time weather APIs (e.g., OpenWeatherMap).

🧾 Government Scheme Info
Provides details about popular central schemes:

PM-KISAN

PMFBY (Fasal Bima Yojana)

Soil Health Card

KCC (Kisan Credit Card)

Future: Add regional schemes per state.

🤖 Farmer Chatbot
Simulated AI chatbot answers basic agri-related queries in the selected language.

Example: "Which fertilizer to use for tomatoes?"

🔊 Voice Instructions (Coming Soon)
In development: Integration of text-to-speech for voice navigation and feedback in local languages.

🛠 Tech Stack
Layer	Tools Used
Frontend	Streamlit (Python)
Backend	Python
NLP/Language	Multilingual Dictionary (BhashaBuddy)
Future ML Use	TensorFlow / OpenCV for disease detection
UI Enhancements	Custom CSS & Emojis
Hosting	Streamlit Community Cloud / GitHub Pages (coming soon)

💡 Use Cases
Indian Farmers: Especially those in rural regions unfamiliar with English.

Agri Startups: Can integrate this as a demo or public utility feature.

Government & NGOs: Use as awareness tools to spread scheme-related information.

🚧 Future Enhancements
✅ Real-time disease detection with ML

✅ Voice support in all languages

✅ Mandi price & weather via live API

✅ Chatbot using LLMs for better answers

✅ Push notifications & SMS alerts

🔗 How to Run Locally
Clone the Repository

bash
Copy
Edit
git clone https://github.com/Ansikka/kishan.py
cd krishimitra
Install Requirements

bash
Copy
Edit
pip install -r requirements.txt
Run App

bash
Copy
Edit
streamlit run krishimitra.py
📂 Project Structure
bash
Copy
Edit
krishimitra/
├── krishimitra.py        # Main Streamlit App
├── requirements.txt
├── README.md
└── assets/               # Images, crop samples, etc.
🙌 Contributors
Made with 💚 by Anshika Sharma and open for contributions!

