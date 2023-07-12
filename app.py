import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_excel('Diwali Sales Data.xlsx')

st.set_page_config(page_title='Sales Dashboard',
                   page_icon=':bar_chart:', layout="wide")

# SIDEBAR----------
st.sidebar.header(":pushpin: FILTER")


State = st.sidebar.multiselect("SELECT THE STATE", options=df["State"].unique(),
                               default=df["State"].unique()
                               )


df.selection = df.query("State== @State")


# MAINPAGE-----
st.header(":bar_chart: Sales Analysis")
st.markdown("##")

# TOP KPI'S
total_orders = int(df.selection["Orders"].sum())
total_amount = int(df.selection["Amount"].sum())

col1, col2 = st.columns(2)
with col1:
    st.write(":shopping_bags: Total Orders ")
    st.subheader(total_orders)
with col2:
    st.write(":heavy_dollar_sign: Total Amount ")
    st.write(f"{total_amount} Rupees")
st.markdown("---")


tabs = ['Product Category', 'Gender', 'Age Group',
        'States', 'Marital Status', 'Occupation']

active_tab = st.sidebar.radio("ANALYSIS BASED ON", tabs)


if active_tab == "Product Category":
    # PRODUCT VS ORDERS [BAR CHART]

    product_order = df.selection.groupby(['Product_Category'], as_index=False)[
        'Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

    fig_product_order = px.bar(
        product_order,
        y="Product_Category",
        x="Orders",
        orientation="h",
        width=500,
        height=400,

    )


# PRODUCT CATEGORY VS AMOUNT [BAR CHART]

    product_amount = df.selection.groupby(['Product_Category'], as_index=False)[
        'Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

    fig_product_sales = px.bar(
        product_amount,
        y="Product_Category",
        x="Amount",
        orientation="h",
        width=500,
        height=400,
    )

    cola, colb = st.columns(2)
    with cola:
        st.write("PRODUCT CATEGORY VS ORDERS")
        st.plotly_chart(fig_product_order)
    with colb:
        st.write("PRODUCT CATEGORY VS AMOUNT")
        st.plotly_chart(fig_product_sales)


elif active_tab == "Gender":

    # COUNT OF ORDERS BY GENDER

    orders_sales_gender = df.selection.groupby(['Gender'], as_index=False)[
        'Orders'].sum().sort_values(by='Orders', ascending=False)

    fig1 = px.pie(orders_sales_gender,
                  names="Gender",
                  values="Orders",
                  width=400,
                  height=400,


                  )


# AMOUNT OF SALES BY GENDER

    amount_sales_gender = df.selection.groupby(['Gender'], as_index=False)[
        'Amount'].sum().sort_values(by='Amount', ascending=False)

    fig2 = px.pie(
        amount_sales_gender,
        names="Gender",
        values="Amount",
        width=400,
        height=400,


    )

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("GENDER VS ORDERS")
        st.plotly_chart(fig1)
    with col2:
        st.subheader("GENDER VS AMOUNT")
        st.plotly_chart(fig2)


elif active_tab == "Age Group":

    # AGE GROUP BY ORDERS

    age_orders = df.selection.groupby(['Age Group'], as_index=False)[
        'Orders'].sum().sort_values(by='Orders', ascending=False)
    fig3 = px.bar(age_orders,
                  x="Age Group",
                  y="Orders",
                  orientation="v", height=300, width=400
                  )


# AGE GROUP BY AMOUNT

    age_amount = df.selection.groupby(['Age Group'], as_index=False)[
        'Amount'].sum().sort_values(by='Amount', ascending=False)
    fig4 = px.bar(age_amount,
                  x="Age Group",
                  y="Amount",
                  orientation="v", height=300, width=400
                  )

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("COUNT OF ORDERS BY AGE GROUP")
        st.plotly_chart(fig3)
    with col4:
        st.subheader("AMOUNT OF SALES BY AGE GROUP")
        st.plotly_chart(fig4)


elif active_tab == "States":
    # STATES BY ORDERS

    state_orders = df.selection.groupby(['State'], as_index=False)[
        'Orders'].sum().sort_values(by='Orders', ascending=False)
    fig5 = px.bar(state_orders, x='State', y='Orders',
                  orientation='v', height=300, width=400)

    # STATES BY AMOUNT

    state_amount = df.selection.groupby(['State'], as_index=False)[
        'Amount'].sum().sort_values(by='Amount', ascending=False)
    fig6 = px.bar(state_amount, x='State', y='Amount',
                  orientation='v', height=300, width=400)

    col5, col6 = st.columns(2)
    with col5:
        st.subheader("COUNT OF ORDERS BY STATE")
        st.plotly_chart(fig5)
    with col6:
        st.subheader("AMOUNT OF SALES BY STATE")
        st.plotly_chart(fig6)


elif active_tab == "Marital Status":
    # marrital status BY ORDERS

    marry_orders = df.selection.groupby(['Marital_Status'], as_index=False)[
        'Orders'].sum().sort_values(by='Orders', ascending=False)
    fig7 = px.pie(marry_orders, names='Marital_Status',
                  values='Orders', width=400, height=400)

    # marrital status BY AMOUNT

    marry_amount = df.selection.groupby(['Marital_Status'], as_index=False)[
        'Amount'].sum().sort_values(by='Amount', ascending=False)
    fig8 = px.pie(marry_amount, names='Marital_Status',
                  values='Amount', width=400, height=400)

    col7, col8 = st.columns(2)
    with col7:
        st.subheader("ORDERS BY  MARITAL STATUS")
        st.plotly_chart(fig7)
    with col8:
        st.subheader("AMOUNT BY MARITAL STATUS")
        st.plotly_chart(fig8)
    st.subheader(" '1' = Married")
    st.subheader(" '0' = Unmarried")


elif active_tab == "Occupation":
    # OCCUPATION BY ORDERS

    occu_orders = df.selection.groupby(['Occupation'], as_index=False)[
        'Orders'].sum().sort_values(by='Orders', ascending=False)
    fig9 = px.bar(occu_orders, x='Occupation',
                  y='Orders', orientation='v', width=400, height=300)

    # OCCUPATION BY AMOUNT

    occu_amount = df.selection.groupby(['Occupation'], as_index=False)[
        'Amount'].sum().sort_values(by='Amount', ascending=False)
    fig10 = px.bar(occu_amount, x='Occupation',
                   y='Amount', orientation='v', width=400, height=300)

    col9, col10 = st.columns(2)
    with col9:
        st.subheader("ORDERS BY OCCUPATION")
        st.plotly_chart(fig9)
    with col10:
        st.subheader("AMOUNT BY OCCUPATION")
        st.plotly_chart(fig10)
