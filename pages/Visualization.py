import streamlit as st
import plotly.express as px
import pandas as pd

# Load the data
data = pd.read_csv(r'data.csv')

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Get the value counts of store types
store_type_counts = data['Type'].value_counts()

# Calculate sales by year
sales_by_year = data.groupby(data['Date'].dt.year)['Weekly_Sales'].sum().reset_index()

# Summary calculations
most_selling_store_id = data.groupby('Store')['Weekly_Sales'].sum().idxmax()
most_selling_store = f"Store {most_selling_store_id}"
store_20_type = data[data['Store'] == 20]['Type'].iloc[0]
most_selling_department = data.groupby('Dept')['Weekly_Sales'].sum().idxmax()

# Most selling month
monthly_sales = data.groupby(data['Date'].dt.month)['Weekly_Sales'].sum()
most_selling_month_num = monthly_sales.idxmax()
most_selling_month = pd.to_datetime(most_selling_month_num, format='%m').strftime('%B')

# Set most selling holiday manually
most_selling_holiday = "Thanksgiving"

# Title
st.markdown("<h2 style='text-align: center;'>Sales Analysis Summary</h2>", unsafe_allow_html=True)

# Summary boxes
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"<h4 style='font-size: 12px;'>Most Selling Store</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 22px;'>{most_selling_store}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 22px;'>Type: {store_20_type}</p>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<h4 style='font-size: 12px;'>Most Selling Department</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 22px;'>{most_selling_department}</p>", unsafe_allow_html=True)

with col3:
    st.markdown(f"<h4 style='font-size: 12px;'>Most Selling Month</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 22px;'>{most_selling_month}</p>", unsafe_allow_html=True)

with col4:
    st.markdown(f"<h4 style='font-size: 12px;'>Most Selling Holiday</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 22px;'>{most_selling_holiday}</p>", unsafe_allow_html=True)

st.markdown("---")

# Create the plots using plotly with a layout similar to the image

# Pie chart
fig_store_types = px.pie(
    store_type_counts,
    names=store_type_counts.index,
    values=store_type_counts,
    title='Weekly Sales by Store Type',
    color_discrete_sequence=px.colors.qualitative.Pastel
)
fig_store_types.update_layout(
    margin=dict(l=20, r=20, t=50, b=10),
    legend=dict(
        orientation="v",
        yanchor="top",
        y=0.8,
        xanchor="left",
        x=1
    ),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='black',
    title_font_size=20,
)


# Bar chart
fig_sales_by_year = px.bar(
    sales_by_year,
    x='Date',
    y='Weekly_Sales',
    title='Weekly Sales by Year',
    color_discrete_sequence=px.colors.sequential.Plasma
)
fig_sales_by_year.update_layout(
    margin=dict(l=20, r=20, t=50, b=10),
    xaxis_title="Year",
    yaxis_title="Total Sales",
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='black',
    title_font_size=20,
)

# Create the grouped bar chart
fig_store_size_sales = px.bar(
    data,
    x='Store',
    y='Weekly_Sales',
    color='Size',
    title='Weekly Sales by Store and Size',
    barmode='group'  # To group bars by size
)
fig_store_size_sales.update_layout(
    margin=dict(l=20, r=20, t=50, b=10),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='black',
    title_font_size=20,
)

# Create the bar chart for weekly sales by month
monthly_sales = data.groupby(data['Date'].dt.month)['Weekly_Sales'].sum().reset_index()
monthly_sales['Month'] = monthly_sales['Date'].apply(lambda x: pd.to_datetime(x, format='%m').strftime('%B'))

fig_sales_by_month = px.bar(
    monthly_sales,
    x='Month',
    y='Weekly_Sales',
    title='Weekly Sales by Month',
    color_discrete_sequence=px.colors.sequential.Plasma
)
fig_sales_by_month.update_layout(
    margin=dict(l=20, r=20, t=50, b=10),
    xaxis_title="Month",
    yaxis_title="Total Sales",
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='black',
    title_font_size=20,
)


# Create the grouped bar chart for weekly sales by holiday and store type
fig_holiday_store_sales = px.bar(
    data,
    x='IsHoliday',
    y='Weekly_Sales',
    color='Type',
    title='Weekly Sales by Holiday and Store Type',
    barmode='group'
)
fig_holiday_store_sales.update_layout(
    margin=dict(l=20, r=20, t=50, b=10),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='black',
    title_font_size=20,
)


# Display the plots in Streamlit
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_store_types, use_container_width=True)
with col2:
    st.plotly_chart(fig_sales_by_year, use_container_width=True)
st.plotly_chart(fig_store_size_sales, use_container_width=True)
st.plotly_chart(fig_sales_by_month, use_container_width=True)
st.plotly_chart(fig_holiday_store_sales, use_container_width=True)
st.plotly_chart(fig_holiday_store_sales, use_container_width=True)
