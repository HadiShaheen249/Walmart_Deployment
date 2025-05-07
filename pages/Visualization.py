import streamlit as st
import plotly.express as px 
import pandas as pd

# Load data
sales_by_year = pd.read_csv("sales_by_year.csv")
sales_by_month = pd.read_csv("sales_by_month.csv")
sales_by_store_size = pd.read_csv("sales_by_store_size.csv")
sales_by_dept = pd.read_csv("sales_by_dept.csv")
store_type_counts = pd.read_csv("store_type_counts.csv")
holiday_sales = pd.read_csv("holiday_sales_by_type.csv")

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
most_selling_department = sales_by_dept.sort_values(by='Weekly_Sales', ascending=False).iloc[0]['Dept']
most_selling_month = sales_by_month.sort_values(by='Weekly_Sales', ascending=False).iloc[0]['Month']
most_selling_month_name = pd.to_datetime(str(int(most_selling_month)), format='%m').strftime('%B')
most_selling_holiday = "Thanksgiving"
top_store_type = store_type_counts.sort_values(by='Count', ascending=False).iloc[0]['Type']
store_a_percentage = store_type_counts[store_type_counts['Type'] == 'A']['Count'].iloc[0] / store_type_counts['Count'].sum() * 100

# Header
st.markdown("<h2 style='text-align: center;'>Sales Analysis Summary</h2>", unsafe_allow_html=True)

# Summary boxes
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("<h4 style='font-size: 12px;'>Most Selling Store</h4>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 22px;'>{most_selling_store}</p>", unsafe_allow_html=True)

with col2:
    st.markdown("<h4 style='font-size: 12px;'>Most Selling Department</h4>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 22px;'>{int(most_selling_department)}</p>", unsafe_allow_html=True)

with col3:
    st.markdown("<h4 style='font-size: 12px;'>Most Selling Month</h4>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 22px;'>{most_selling_month_name}</p>", unsafe_allow_html=True)

with col4:
    st.markdown("<h4 style='font-size: 12px;'>Most Selling Holiday</h4>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 22px;'>{most_selling_holiday}</p>", unsafe_allow_html=True)

with col5:
    st.markdown("<h4 style='font-size: 12px;'>Top Store Type</h4>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 22px;'>Type {top_store_type}</p>", unsafe_allow_html=True)

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
    color_discrete_sequence=px.colors.sequential.Aggrnyl
)

# Plot 5: Sales by Department
fig_sales_by_dept = px.bar(
    sales_by_dept,
    x='Dept',
    y='Weekly_Sales',
    title='Weekly Sales by Department',
    color_discrete_sequence=px.colors.sequential.Oranges
)

# Plot 6: Holiday Sales by Store Type
fig_holiday_sales = px.bar(
    holiday_sales,
    x='Holiday_Name',
    y='Weekly_Sales',
    color='Type',
    barmode='group',
    title='Weekly Sales by Store Type During Holidays',
    category_orders={'Holiday_Name': ['Thanksgiving', 'Super_Bowl', 'Labor_Day', 'Christmas']},
    color_discrete_sequence=px.colors.qualitative.Set1
)

# Show plots
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig_store_types, use_container_width=True)
    st.markdown(f"**Insight:** Store Type A has the highest sales share, contributing approximately **{store_a_percentage:.1f}%** of the total. This indicates that Type A stores play a major role in overall performance.")

with col2:
    st.plotly_chart(fig_sales_by_year, use_container_width=True)
    st.markdown("**Insight:** Sales were relatively consistent over the three years, but the highest sales were recorded in **2010**, suggesting a strong market or seasonal push that year.")

# Additional plots
st.plotly_chart(fig_store_size_sales, use_container_width=True)
st.markdown("**Insight:** Store size has a clear impact on weekly sales. The store with the highest sales is **Store 20**, which also has the largest size. This suggests that investing in larger store formats could be beneficial.")

st.plotly_chart(fig_sales_by_month, use_container_width=True)
st.markdown("**Insight:** The highest sales are observed in **December**, which aligns with the **Christmas** season when customers are more likely to purchase gifts and seasonal items.")

st.plotly_chart(fig_sales_by_dept, use_container_width=True)
st.markdown("**Insight:** Department **92** has the highest weekly sales among all departments. Focusing on this department and understanding its drivers could help boost total sales further.")

st.plotly_chart(fig_holiday_sales, use_container_width=True)
st.markdown("**Insight:** **Thanksgiving** leads all holidays in weekly sales, especially for **Store Type A**, showing its importance in planning seasonal strategies.")
