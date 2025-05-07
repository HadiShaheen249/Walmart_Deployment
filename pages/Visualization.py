import streamlit as st
import plotly.express as px 
import pandas as pd

# Load data
sales_by_year = pd.read_csv("sales_by_year.csv")
sales_by_month = pd.read_csv("sales_by_month.csv")
sales_by_store_size = pd.read_csv("sales_by_store_size.csv")
sales_by_dept = pd.read_csv("sales_by_dept.csv")
store_type_counts = pd.read_csv("store_type_counts.csv")

# Clean and prepare sales_by_month
sales_by_month['Month'] = sales_by_month['Month'].astype(int)
sales_by_month['MonthName'] = sales_by_month['Month'].apply(lambda x: pd.to_datetime(str(x), format='%m').strftime('%B'))
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
sales_by_month['MonthName'] = pd.Categorical(sales_by_month['MonthName'], categories=month_order, ordered=True)
sales_by_month = sales_by_month.sort_values('MonthName')

# Summary metrics
most_selling_store_id = sales_by_store_size.groupby('Store')['Weekly_Sales'].sum().idxmax()
most_selling_store = f"Store {most_selling_store_id}"
store_20_type = sales_by_store_size[sales_by_store_size['Store'] == 20]['Size'].iloc[0]
most_selling_department = sales_by_dept.sort_values(by='Weekly_Sales', ascending=False).iloc[0]['Dept']
most_selling_month = sales_by_month.sort_values(by='Weekly_Sales', ascending=False).iloc[0]['Month']
most_selling_month_name = pd.to_datetime(str(int(most_selling_month)), format='%m').strftime('%B')
most_selling_holiday = "Thanksgiving"

# Header
st.markdown("<h2 style='text-align: center;'>Sales Analysis Summary</h2>", unsafe_allow_html=True)

# Summary boxes
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<h4 style='font-size: 12px;'>Most Selling Store</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 22px;'>{most_selling_store}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 22px;'>Size: {store_20_type}</p>", unsafe_allow_html=True)

with col2:
    st.markdown("<h4 style='font-size: 12px;'>Most Selling Department</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 22px;'>{int(most_selling_department)}</p>", unsafe_allow_html=True)

with col3:
    st.markdown("<h4 style='font-size: 12px;'>Most Selling Month</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 22px;'>{most_selling_month_name}</p>", unsafe_allow_html=True)

with col4:
    st.markdown("<h4 style='font-size: 12px;'>Most Selling Holiday</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 22px;'>{most_selling_holiday}</p>", unsafe_allow_html=True)

st.markdown("---")

# Plot 1: Pie chart for store types
fig_store_types = px.pie(
    store_type_counts,
    names='Type',
    values='Count',
    title='Weekly Sales by Store Type',
    color_discrete_sequence=px.colors.qualitative.Set1
)

# Plot 2: Sales by Year
fig_sales_by_year = px.bar(
    sales_by_year,
    x='Year',
    y='Weekly_Sales',
    title='Weekly Sales by Year',
    color_discrete_sequence=px.colors.sequential.Plasma
)

# Plot 3: Sales by Store and Size
fig_store_size_sales = px.bar(
    sales_by_store_size,
    x='Store',
    y='Weekly_Sales',
    color='Size',
    title='Weekly Sales by Store and Size',
    barmode='group'
)

# Plot 4: Sales by Month
fig_sales_by_month = px.bar(
    sales_by_month,
    x='MonthName',
    y='Weekly_Sales',
    title='Weekly Sales by Month',
    color_discrete_sequence=px.colors.sequential.Plasma
)

# Plot 5: Sales by Department
fig_sales_by_dept = px.bar(
    sales_by_dept,
    x='Dept',
    y='Weekly_Sales',
    title='Weekly Sales by Department',
    color_discrete_sequence=px.colors.sequential.Oranges
)

# Show 
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_store_types, use_container_width=True)
with col2:
    st.plotly_chart(fig_sales_by_year, use_container_width=True)

# Plot 3: Sales by Store and Size
st.plotly_chart(fig_store_size_sales, use_container_width=True)

# Plot 4: Sales by Month
st.plotly_chart(fig_sales_by_month, use_container_width=True)

# Plot 5: Sales by Department
st.plotly_chart(fig_sales_by_dept, use_container_width=True)
