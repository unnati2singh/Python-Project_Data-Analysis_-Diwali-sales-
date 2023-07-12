import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_excel('Diwali Sales Data.xlsx')

st.set_page_config(page_title='Sales Dashboard',
                   page_icon=':bar_chart:', layout="wide")

# SIDEBAR----------
st.sidebar.header("Filter")


State = st.sidebar.multiselect("Select The State", options=df["State"].unique(),
                               default=df["State"].unique()
                               )


df.selection = df.query("State== @State")

st.dataframe(df.selection)


# MAINPAGE-----
st.title(":bar_chart: Sales Analysis")
st.markdown("##")

# TOP KPI'S
total_orders = int(df.selection["Orders"].sum())
total_amount = int(df.selection["Amount"].sum())

col1, col2 = st.columns(2)
with col1:
    st.subheader("Total Orders ")
    st.subheader(total_orders)
with col2:
    st.subheader("Total Amount ")
    st.subheader(f"{total_amount} Rupees")
st.markdown("---")

# PRODUCT VS ORDERS [BAR CHART]

product_order = df.groupby(['Product_Category'], as_index=False)[
    'Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

fig_product_order = px.bar(
    product_order,
    y="Product_Category",
    x="Orders",
    orientation="h",
)


# PRODUCT CATEGORY VS AMOUNT [BAR CHART]

product_amount = df.groupby(['Product_Category'], as_index=False)[
    'Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

fig_product_sales = px.bar(
    product_amount,
    y="Product_Category",
    x="Amount",
    orientation="h",
)


left_column, right_column = st.columns(2)

with left_column:
    st.subheader("PRODUCT CATEGORY VS ORDERS")
    st.plotly_chart(fig_product_order)

with right_column:
    st.subheader("PRODUCT CATEGORY VS AMOUNT")
    st.plotly_chart(fig_product_sales)

# COUNT OF ORDERS BY GENDER

orders_sales_gender = df.groupby(['Gender'], as_index=False)[
    'Orders'].sum().sort_values(by='Orders', ascending=False)

fig1 = px.bar(orders_sales_gender,
              x="Gender",
              y="Orders",
              orientation="v",
              )


# AMOUNT OF SALES BY GENDER

amount_sales_gender = df.groupby(['Gender'], as_index=False)[
    'Amount'].sum().sort_values(by='Amount', ascending=False)

fig2 = px.bar(
    amount_sales_gender,
    x="Gender",
    y="Amount",
    orientation='v',
)


col1, col2 = st.columns(2)
with col1:
    st.subheader("COUNT OF ORDERS BY GENDER")
    st.plotly_chart(fig1)
with col2:
    st.subheader("AMOUNT OF SALES VS GENDER")
    st.plotly_chart(fig2)

# AGE GROUP BY ORDERS

age_orders = df.groupby(['Age Group'], as_index=False)[
    'Orders'].sum().sort_values(by='Orders', ascending=False)
fig3 = px.bar(age_orders,
              x="Age Group",
              y="Orders",
              orientation="v",
              )


# AGE GROUP BY AMOUNT

age_amount = df.groupby(['Age Group'], as_index=False)[
    'Amount'].sum().sort_values(by='Amount', ascending=False)
fig4 = px.bar(age_amount,
              x="Age Group",
              y="Amount",
              orientation="v",
              )


col3, col4 = st.columns(2)
with col3:
    st.subheader("COUNT OF ORDERS BY AGE GROUP")
    st.plotly_chart(fig3)
with col4:
    st.subheader("AMOUNT OF SALES BY AGE GROUP")
    st.plotly_chart(fig4)

tabs = ['Product Category', 'Gender', 'Age Group']
active_tab = st.sidebar.radio("select tab", tabs)


if active_tab == "Product Category":
    # PRODUCT VS ORDERS [BAR CHART]
    st.subheader("Sales Analysis by Product Category ")

    product_order = df.groupby(['Product_Category'], as_index=False)[
        'Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

    fig_product_order = px.bar(
        product_order,
        y="Product_Category",
        x="Orders",
        orientation="h",
    )


# PRODUCT CATEGORY VS AMOUNT [BAR CHART]

    product_amount = df.groupby(['Product_Category'], as_index=False)[
        'Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

    fig_product_sales = px.bar(
        product_amount,
        y="Product_Category",
        x="Amount",
        orientation="h",
    )

    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader("PRODUCT CATEGORY VS ORDERS")
        st.plotly_chart(fig_product_order)

    with right_column:
        st.subheader("PRODUCT CATEGORY VS AMOUNT")
        st.plotly_chart(fig_product_sales)


elif active_tab == "Gender":
    st.subheader("Sales Analysis by Gender ")
    # COUNT OF ORDERS BY GENDER

    orders_sales_gender = df.groupby(['Gender'], as_index=False)[
        'Orders'].sum().sort_values(by='Orders', ascending=False)

    fig1 = px.bar(orders_sales_gender,
                  x="Gender",
                  y="Orders",
                  orientation="v",
                  )


# AMOUNT OF SALES BY GENDER

    amount_sales_gender = df.groupby(['Gender'], as_index=False)[
        'Amount'].sum().sort_values(by='Amount', ascending=False)

    fig2 = px.bar(
        amount_sales_gender,
        x="Gender",
        y="Amount",
        orientation='v',
    )

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("COUNT OF ORDERS BY GENDER")
        st.plotly_chart(fig1)
    with col2:
        st.subheader("AMOUNT OF SALES VS GENDER")
        st.plotly_chart(fig2)

elif active_tab == "Age Group":
    st.subheader("Sales Analysis by Age Group ")
    # AGE GROUP BY ORDERS

    age_orders = df.groupby(['Age Group'], as_index=False)[
        'Orders'].sum().sort_values(by='Orders', ascending=False)
    fig3 = px.bar(age_orders,
                  x="Age Group",
                  y="Orders",
                  orientation="v",
                  )


# AGE GROUP BY AMOUNT

    age_amount = df.groupby(['Age Group'], as_index=False)[
        'Amount'].sum().sort_values(by='Amount', ascending=False)
    fig4 = px.bar(age_amount,
                  x="Age Group",
                  y="Amount",
                  orientation="v",
                  )

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("COUNT OF ORDERS BY AGE GROUP")
        st.plotly_chart(fig3)
    with col4:
        st.subheader("AMOUNT OF SALES BY AGE GROUP")
        st.plotly_chart(fig4)
