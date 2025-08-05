import streamlit as st

if 'total' not in st.session_state:
    st.session_state.total = 0
if 'continue_shopping' not in st.session_state:
    st.session_state.continue_shopping = True

price_list = {
    "Phones": {"Samsung": 45000, "Vivo": 25000, "Oppo": 35000, "Realme": 20000, "Apple": 145000},
    "Earphones": {"Noise": 1000, "Boat": 2000, "Samsung": 3000, "OnePlus": 4000, "iPhone": 5000},
    "AC": {"Samsung": 60000, "GENERAL": 35000, "Haier": 40000, "BlueStar": 50000, "VOLTUS": 40000},
    "Fridge": {"Samsung": 65000, "Godrej": 35000, "Whirlpool": 45000, "Bluestar": 50000, "LG": 95000},
    "EV Bikes": {"Chetak": 150000, "Ola": 120000, "Ather": 200000, "Tata iQ": 75000, "Revolt": 175000}
}


st.title("📱 Electronic Device Management System")

if st.session_state.continue_shopping:
    category = st.selectbox("🔘 Select a category:", list(price_list.keys()))
    brand = st.selectbox(f"Select a brand from {category}:", list(price_list[category].keys()))
    price = price_list[category][brand]

    if st.button("🛒 Add to Cart"):
        st.session_state.total += price
        st.success(f"✅ {brand} added to cart! Current Total: ₹{st.session_state.total}")

    cont = st.radio("Do you want to continue shopping?", ("Yes", "No"))
    if cont == "No":
        st.session_state.continue_shopping = False
else:
    st.subheader("🧾 Final Bill")
    st.success(f"Your total bill is ₹{st.session_state.total}")
    st.balloons()
    if st.button("🔄 Start New Purchase"):
        st.session_state.total = 0
        st.session_state.continue_shopping = True
