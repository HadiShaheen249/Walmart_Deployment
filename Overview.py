import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title="Walmart Sales Forecast", page_icon="🛒", layout="wide")

# دلوقتي الـ sidebar هيكون فاضي
with st.sidebar:
    pass

# عرض العنوان الرئيسي
st.title("Walmart Sales Forecasting")
st.write("Welcome to the Walmart Sales Forecasting !")

# عرض الصورة
image = Image.open("dataset-cover.jpeg")
st.image(image,  use_container_width=True)

# عرض الوصف بشكل مُنظم
st.subheader("Problem:")
st.write("""
There are many seasons that sales are significantly higher or lower than averages. If the company does not know about these seasons, it can lose too much money. Predicting future sales is one of the most crucial plans for a company. Sales forecasting gives an idea to the company for arranging stocks, calculating revenue, and deciding to make a new investment. Another advantage of knowing future sales is that achieving predetermined targets from the beginning of the seasons can have a positive effect on stock prices and investors' perceptions. Also, not reaching the projected target could significantly damage stock prices, conversely. And, it will be a big problem especially for Walmart as a big company.
""")

st.subheader("Aim:")
st.write("""
My aim in this project is to build a model which predicts sales of the stores. With this model, Walmart authorities can decide their future plans which is very important for arranging stocks, calculating revenue and deciding to make new investment or not.
""")


# باقي الكود بتاعك (تحميل البيانات وغيره) هيكون هنا
data = pd.read_csv(r'data.csv')
