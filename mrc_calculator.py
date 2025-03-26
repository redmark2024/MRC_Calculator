import streamlit as st

def calculate_total_income(initial_income, increase_per_day, days):
    total_income = 0
    for day in range(days):
        total_income += initial_income + day * increase_per_day
    return total_income


st.set_page_config(page_title="MRC Calculator", page_icon="💰", layout="centered")


st.markdown("""
    <h1 style="color:#4CAF50; text-align:center;">MRC Calculator</h1>
    <p style="color:#1E88E5; text-align:center;">Welcome to the <strong>MRC Calculator</strong>. This app calculates your total income over a period of 30, 60, or 90 days.  
    You can adjust your initial income and daily income increase, and the app will give you the total earnings in <strong>Rupees</strong>.</p>
""", unsafe_allow_html=True)


st.markdown("<hr>", unsafe_allow_html=True)


initial_income = st.number_input("Enter initial income (first day) in Rupees:", min_value=0, value=20, step=1)
increase_per_day = st.number_input("Enter the increase in income per day in Rupees:", min_value=0, value=1, step=1)


if st.button("Calculate Total Income"):
    # Calculate total income after 30, 60, and 90 days
    income_30_days = calculate_total_income(initial_income, increase_per_day, 30)
    income_60_days = calculate_total_income(initial_income, increase_per_day, 60)
    income_90_days = calculate_total_income(initial_income, increase_per_day, 90)

   
    st.markdown("<h3 style='color:#FF5733;'>Total Income Calculations</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#D32F2F;'>Total income after 30 days will be: <strong>₹{income_30_days}</strong> Rupees</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#D32F2F;'>Total income after 60 days will be: <strong>₹{income_60_days}</strong> Rupees</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#D32F2F;'>Total income after 90 days will be: <strong>₹{income_90_days}</strong> Rupees</p>", unsafe_allow_html=True)

    
    st.markdown("<hr>", unsafe_allow_html=True)

   
    st.markdown("<p style='color:#8E24AA;'>Thank you for using the MRC Calculator!</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:#8E24AA;'>You can adjust the values to see how the total income changes.</p>", unsafe_allow_html=True)


st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='color:#2196F3; text-align:center;'>Made with ❤ by RedMark | MRC Calculator</p>", unsafe_allow_html=True)