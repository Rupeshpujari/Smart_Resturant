import json
import random
import streamlit as st
import qrcode
import io
import pandas as pd

# ---- Load Menu ----
with open("menu.json", "r") as f:
    menu = json.load(f)

# ---- Load Users ----
with open("users.json", "r") as f:
    users = json.load(f)

# ---- Page Config ----
st.set_page_config(page_title="Smart Restaurant", layout="centered")

# ---- Custom CSS ----
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    position: relative;
    z-index: 0;
}
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: url("https://images.unsplash.com/photo-1504674900247-0877df9cc836") no-repeat center center fixed;
    background-size: cover;
    filter: blur(3px);
    z-index: -1;
}
.block-container {
    background: rgba(255, 255, 255, 0.35);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    padding: 30px;
    border-radius: 25px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.25);
    border: 1px solid rgba(255,255,255,0.3);
}
h1 {
    font-size: 2.8rem !important;
    color: #ff7043 !important;
    font-weight: 900;
    text-align: center;
    text-shadow: 1px 1px 5px rgba(0,0,0,0.3);
}
h2, h3, h4, h5, h6, p, label {
    color: #222 !important;
    font-weight: 600;
}
.stButton>button {
    background-color: #ff7043 !important;
    color: white !important;
    border-radius: 12px;
    padding: 10px 25px;
    font-weight: bold;
    border: none;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background-color: #ff5722 !important;
    transform: scale(1.05);
}
.stSelectbox, .stNumberInput>div>input {
    background-color: rgba(255,255,255,0.85) !important;
    border-radius: 10px;
    padding: 5px;
    color: #222 !important;
}
.stAlert {
    border-radius: 15px !important;
}
</style>
""", unsafe_allow_html=True)

# ---- Session State Init ----
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "order_started" not in st.session_state:
    st.session_state.order_started = False
if "total_bill" not in st.session_state:
    st.session_state.total_bill = 0
if "order_items" not in st.session_state or st.session_state.order_items is None:
    st.session_state.order_items = []
if "allocated_tables" not in st.session_state:
    st.session_state.allocated_tables = set()
if "table_number" not in st.session_state:
    st.session_state.table_number = None
if "transaction_id" not in st.session_state:
    st.session_state.transaction_id = None

# ---- LOGIN PAGE ----
if not st.session_state.logged_in:
    st.markdown('<h1>🔐 Staff Login</h1>', unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_clicked = st.button("Login")
    
    if login_clicked:
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"✅ Welcome {username}! You are logged in.")
        else:
            st.error("❌ Invalid username or password!")

# ---- MAIN APP ----
if st.session_state.logged_in:
    # Logout button
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.order_started = False
        st.session_state.total_bill = 0
        st.session_state.order_items = []
        st.session_state.table_number = None
        st.experimental_rerun = None  # remove old rerun call
        st.info("🔓 You have been logged out.")
    else:
        # Main Header
        st.markdown(f'<h1>🍽 Welcome {st.session_state.username} to the Smart Restaurant!</h1>', unsafe_allow_html=True)

        # ---- Step 1: Takeaway or Dine-in ----
        if not st.session_state.order_started:
            choice = st.radio("What are you looking for today?", ["Takeaway", "Dine-in"])
            if st.button("Confirm Selection"):
                if choice == "Dine-in":
                    available_tables = set(range(1, 16)) - st.session_state.allocated_tables
                    if available_tables:
                        st.session_state.table_number = random.choice(list(available_tables))
                        st.session_state.allocated_tables.add(st.session_state.table_number)
                        # st.success(f"✅ Your table number is: {st.session_state.table_number}")
                    else:
                        st.error("❌ Sorry, all tables are currently occupied!")
                st.session_state.order_started = True

        # Show table number
        if st.session_state.table_number:
            st.info(f"🍴 Your Table Number: {st.session_state.table_number}")

        # ---- Step 2: Menu Selection ----
        st.subheader("📖 Menu")
        dish1 = st.selectbox("Select Category", [""] + list(menu.keys()))
        dish2 = st.selectbox("Select Sub-Category", [""] + (list(menu[dish1].keys()) if dish1 else []))
        dish3 = st.selectbox("Select Dish Type", [""] + (list(menu[dish1][dish2].keys()) if dish1 and dish2 else []))
        dish4 = st.selectbox("Select Item", [""] + (list(menu[dish1][dish2][dish3].keys()) if dish1 and dish2 and dish3 else []))
        quantity = st.number_input("Quantity", min_value=1, value=1)

        # ---- Step 3: Add to Order ----
        if st.button("Add to Order"):
            if dish1 and dish2 and dish3 and dish4 and quantity > 0:
                final_item = menu[dish1][dish2][dish3][dish4]
                price = final_item * quantity
                st.session_state.total_bill += price
                st.session_state.order_items.append([
                    len(st.session_state.order_items) + 1,
                    f"{dish4} - {dish3}",
                    quantity,
                    price
                ])
                st.success(f"Added {quantity} x {dish4} → ₹{price}")
                st.info(f"💰 Current Bill: ₹{st.session_state.total_bill}")

        # ---- Step 4: Current Order Table ----
        if st.session_state.order_items:
            st.subheader("🛒 Current Order")
            df = pd.DataFrame(st.session_state.order_items, columns=["No.", "Item", "Qty", "Price (₹)"])
            df = df.set_index("No.")
            st.table(df)
            st.write(f"💰 Subtotal: ₹{st.session_state.total_bill}")

        # ---- Step 5: Checkout ----
        if st.session_state.order_items and st.button("Checkout"):
            if st.session_state.table_number:
                st.info(f"🍴 Table Number: {st.session_state.table_number}")
            gst_rate = 0.05
            gst_amount = round(st.session_state.total_bill * gst_rate, 2)
            final_amount = st.session_state.total_bill + gst_amount
            st.session_state.transaction_id = random.randint(100000, 1500000)

            st.success("🧾 Final Bill")
            st.write(f"Subtotal: ₹{st.session_state.total_bill}")
            st.write(f"GST (5%): ₹{gst_amount}")
            st.write(f"✅ Total Payable: ₹{final_amount}")
            st.write(f"🔖 Transaction ID: {st.session_state.transaction_id}")

            # QR Code
            order_summary = {
                "table": st.session_state.table_number,
                "items": st.session_state.order_items,
                "subtotal": st.session_state.total_bill,
                "gst": gst_amount,
                "total": final_amount,
                "transaction_id": st.session_state.transaction_id
            }
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(json.dumps(order_summary))
            qr.make(fit=True)
            qr_image = qr.make_image(fill_color="black", back_color="white")
            buf = io.BytesIO()
            qr_image.save(buf)
            buf.seek(0)
            st.image(buf, caption="📲 Scan for your Bill", use_container_width=True)

