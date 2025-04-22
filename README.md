## 📊 SSC&Damage submission details May to Jan'25 

### 🔍 Overview
**SSC&Damage submission details May to Jan'25 ** ek Streamlit-based web application hai jo WD (Warehouse Distributor) codes ke basis par claims data ko visualize karta ha. Yeh application users ko unke claims ka status dekhne, aur 'Not Received' claims ke liye details submit karne ki suvidha deta ha.

### 🚀 Features
- WD Code ke basis par claims data filter kana- 'Received', 'Not Received', aur 'All' tabs ke through data visualizaton- 'Not Received' claims ke liye actual claim amount aur supporting documents submit kana- Submitted data ko local Excel file mein update karna (Note: Streamlit Cloud par file writing operations limited hote han)

### 🛠️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Satendra1207/SND-Claims-App.git
   cd SND-Claims-App
   ```

2. **Install dependencies:**

   Ensure that you have Python installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   ```bash
   streamlit run streamlit_app.py
   ```

### 📁 Project Structure

```
SND-Claims-App/
├── streamlit_app.py
├── SSC_and_Atta_Damage_Claims.xlsx
├── requirements.txt
└── README.md
```

### 📌 Nots

- Ensure that the `SSC_and_Atta_Damage_Claims.xlsx` file is present in the same directory as `streamlit_ap.py.
- When deploying on Streamlit Cloud, be aware that writing to local files may not be suppred. Consider using alternative storage solutions for persistentdata.
