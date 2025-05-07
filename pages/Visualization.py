import streamlit as st
import pandas as pd
import plotly.express as px

# Load the summarized data
summary_data = pd.read_csv("visualization_summary_for_streamlit.csv")

# Set page config
st.set_page_config(layout="wide")
st.title("📊 Walmart Sales Visualization (Optimized)")

# Most selling info
st.markdown("### 📌 Summary Insights")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Most Selling Store", f"Store {int(summary_data['most_selling_store'][0])}")
col1.metric("Store Type", summary_data['store_20_type'][0])

col2.metric("Most Selling Dept", f"Dept {int(summary_data['most_selling_dept'][0])}")
col3.metric("Most Selling Month", summary_data['most_selling_month'][0])
col4.metric("Most Selling Holiday", summary_data['most_selling_holiday'][0])

st.markdown("---")

# Pie chart - Store Type Distribution
store_type_df = summary_data[['store_type_A', 'store_type_B', 'store_type_C']].melt(var_name='Type', value_name='Sales')
store_type_df['Type'] = store_type_df['Type'].str[-1]

fig_pie = px.pie(
    store_type_df,
    names='Type',
    values='Sales',
    title="Sales Distribution by Store Type",
    color_discrete_sequence=px.colors.qualitative.Pastel
)
st.plotly_chart(fig_pie, use_container_width=True)

# Bar chart - Sales by Year
year_sales_df = summary_data[['sales_2010', 'sales_2011', 'sales_2012']].melt(var_name='Year', value_name='Sales')
year_sales_df['Year'] = year_sales_df['Year'].str.extract(r'(\d{4})')

fig_year = px.bar(
    year_sales_df,
    x='Year',
    y='Sales',
    title="Total Sales by Year",
    color='Sales',
    color_continuous_scale='Plasma'
)
st.plotly_chart(fig_year, use_container_width=True)

# Bar chart - Monthly Sales
months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
monthly_sales = summary_data[[f'sales_{month}' for month in months]].melt(var_name='Month', value_name='Sales')
monthly_sales['Month'] = monthly_sales['Month'].str.replace('sales_', '')
monthly_sales['Month'] = pd.Categorical(monthly_sales['Month'], categories=months, ordered=True)
monthly_sales = monthly_sales.sort_values('Month')

fig_month = px.bar(
    monthly_sales,
    x='Month',
    y='Sales',
    title='Monthly Sales',
    color='Sales',
    color_continuous_scale='Plasma'
)
st.plotly_chart(fig_month, use_container_width=True)

# Store and Size grouped bar chart
store_size_df = summary_data[['store_id', 'store_size', 'store_sales']]
fig_store_size = px.bar(
    store_size_df,
    x='store_id',
    y='store_sales',
    color='store_size',
    title='Store Sales by Size',
    labels={'store_id': 'Store', 'store_sales': 'Sales', 'store_size': 'Size'},
    barmode='group'
)
st.plotly_chart(fig_store_size, use_container_width=True)

# Holiday vs Non-Holiday by Store Type
holiday_df = summary_data[['holiday_type_A', 'holiday_type_B', 'holiday_type_C',
                           'nonholiday_type_A', 'nonholiday_type_B', 'nonholiday_type_C']]

holiday_data = []
for status in ['holiday', 'nonholiday']:
    for store_type in ['A', 'B', 'C']:
        value = holiday_df[f"{status}_type_{store_type}"][0]
        holiday_data.append({'Holiday': status.capitalize(), 'Type': store_type, 'Sales': value})

holiday_df_final = pd.DataFrame(holiday_data)

fig_holiday = px.bar(
    holiday_df_final,
    x='Holiday',
    y='Sales',
    color='Type',
    barmode='group',
    title="Sales by Holiday Status and Store Type"
)
st.plotly_chart(fig_holiday, use_container_width=True)
