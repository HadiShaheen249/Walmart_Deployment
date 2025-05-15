# 🛒 Walmart Sales Forecasting & Deployment

This project presents a complete machine learning pipeline for forecasting weekly sales for Walmart stores. It includes everything from data exploration to model deployment using Streamlit.

🔗 **Live App**: [Click here to try the Streamlit App](https://walmartdeployment-dseasayw7hve4vjb5py9uf.streamlit.app/)

---

## 📌 Problem Statement

Walmart's sales fluctuate significantly during certain times of the year (e.g., holidays, Black Friday). Not forecasting those correctly may lead to overstocking, lost revenue, or customer dissatisfaction. This project aims to build a reliable model to forecast store sales and help decision-makers plan better for inventory, promotions, and investment.

---

## 🎯 Objectives

- Predict **weekly sales** based on historical data, promotions, holidays, and other features.
- Provide insights into **sales trends** across stores and departments.
- Build an interactive **Streamlit application** for real-time sales forecasting.

---

## 🧩 System Workflow

📂 Raw Data (train.csv, features.csv, stores.csv)                                       
↓                              
🧹 Data Cleaning & Preprocessing                      
↓                               
📊 Exploratory Data Analysis (EDA)                     
↓             
🛠️ Feature Engineering            
↓          
🤖 Model Training (Random Forest, XGBoost, Linear Regression)            
↓          
✅ Model Evaluation        
↓        
💾 Model Saving (joblib)          
↓           
🚀 Streamlit Deployment           


---

## 🔍 Key Insights

- **Department 92** has the highest average sales.  
- **Store 20** and **Store 4** are top performers overall.  
- Holiday weeks (47–51) like **Christmas**, **Black Friday**, and **Thanksgiving** show sales spikes.  
- **Sales in January** drop significantly due to heavy spending in Nov-Dec.  
- Features like **CPI**, **Unemployment**, **Fuel Price**, and **Temperature** showed no significant correlation with weekly sales.

---

## 🧠 Models Used

- ✅ **Final Model**: Random Forest Regressor (selected for its balance between accuracy and training speed).
- 🔍 Also Tested:
  - Linear Regression (low accuracy)
  - Decision Tree (overfitting)
  - XGBoost (very accurate but slower to train)

---

## 🚀 Deployment

Built with **Streamlit** to provide a live, browser-based prediction app.

🧠 Users can:
- Input store number, department, and week info
- Predict weekly sales using the trained model

🔗 **Try it here**:  
👉 [Streamlit App](https://walmartdeployment-dseasayw7hve4vjb5py9uf.streamlit.app/)

---

## 💻 Technologies Used

- Python
- Pandas, NumPy
- Seaborn, Matplotlib
- Scikit-learn
- XGBoost
- Streamlit
- VS Code

---

## 👤 Author

**Hadi Shaheen**  
📧 Email: [ hadishaheen736@gmail.com ]  
📁 Repo: [GitHub - Walmart_Deployment](https://github.com/HadiShaheen249/Walmart_Deployment)

---

## 📎 License

This project was developed as part of the **DEPI Initiative** (Digital Egypt Professional Initiative) by the **Ministry of Communications and Information Technology – Egypt**.
