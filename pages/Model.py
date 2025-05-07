import streamlit as st
import pandas as pd
import pickle
import os

# تحميل النموذج من ملف محلي على GitHub repo
MODEL_PATH = "best_model.pkl"

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"حدث خطأ أثناء تحميل النموذج: {e}")
    st.stop()

# تحميل البيانات لاستخدام القيم الفعلية
DATA_PATH = "data.csv"
if not os.path.exists(DATA_PATH):
    st.error("ملف البيانات غير موجود: تأكد من رفع data.csv في نفس المجلد.")
    st.stop()

data = pd.read_csv(DATA_PATH)
unique_depts = sorted(data['Dept'].unique())
unique_stores = sorted(data['Store'].unique())

# استخراج القيم الدنيا والعليا لكل متغير
min_size, max_size = int(data['Size'].min()), int(data['Size'].max())
min_markdown, max_markdown = float(data['Total_MarkDown'].min()), float(data['Total_MarkDown'].max())
min_econ, max_econ = float(data['Economic_Index'].min()), float(data['Economic_Index'].max())

st.markdown("<h2 style='text-align: center;'>Sales Prediction Model</h2>", unsafe_allow_html=True)
st.markdown("---")

# نموذج الإدخال
with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        store = st.selectbox("Select Store", unique_stores)
        dept = st.selectbox("Select Department", unique_depts)
        store_type = st.selectbox("Store Type", ['A', 'B', 'C'])

    with col2:
        is_holiday = st.radio("Is Holiday?", ['No', 'Yes'])

        store_size = st.slider("Store Size", min_size, max_size, value=min_size, step=1000)
        markdown = st.slider("Total MarkDown", min_markdown, max_markdown, value=min_markdown, step=0.1)
        econ_index = st.slider("Economic Index", min_econ, max_econ, value=min_econ, step=0.1)

    # زر التنبؤ
    submitted = st.form_submit_button("Predict")

# التنبؤ عند الضغط
if submitted:
    try:
        is_holiday_bool = 1 if is_holiday == 'Yes' else 0
        type_encoded = {'A': 0, 'B': 1, 'C': 2}[store_type]

        input_data = pd.DataFrame({
            'Store': [store],
            'Dept': [dept],
            'IsHoliday': [is_holiday_bool],
            'Type': [type_encoded],
            'Size': [store_size],
            'Total_MarkDown': [markdown],
            'Economic_Index': [econ_index],
        })

        prediction = model.predict(input_data)[0]
        st.success(f"Predicted Weekly Sales: ${prediction:,.2f}")

    except Exception as e:
        st.error(f"Prediction failed: {e}")
