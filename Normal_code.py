import json
import random
import streamlit as st
import qrcode
from PIL import Image
import io

# Load menu
with open("menu.json", "r") as f:
    menu = json.load(f)

st.set_page_config(page_title="Smart Restaurant", layout="centered")
st.title("🍽 Welcome to the Smart Restaurant!")

# Initialize session state
if "order_started" not in st.session_state:
    st.session_state.order_started = False
if "total_bill" not in st.session_state:
    st.session_state.total_bill = 0
if "order_items" not in st.session_state:
    st.session_state.order_items = []
if "allocated_tables" not in st.session_state:
    st.session_state.allocated_tables = set()  # track assigned tables
if "table_number" not in st.session_state:
    st.session_state.table_number = None

# Step 1: Takeaway or Dine-in
if not st.session_state.order_started:
    choice = st.radio("What are you looking for today?", ["Takeaway", "Dine-in"])
    
    if st.button("Confirm Selection"):  # Add this button
        if choice == "Dine-in":
            available_tables = set(range(1, 16)) - st.session_state.allocated_tables
            if available_tables:
                st.session_state.table_number = random.choice(list(available_tables))
                st.session_state.allocated_tables.add(st.session_state.table_number)
                st.success(f"✅ Your table number is: {st.session_state.table_number}")
            else:
                st.error("❌ Sorry, all tables are currently occupied!")
        st.session_state.order_started = True
        st.rerun()  # Add this to refresh the page

# Always show table number if allocated
if st.session_state.table_number:
    st.info(f"🍴 Your Table Number: {st.session_state.table_number}")

st.subheader("Menu")

# Step 2: Dish selection dropdowns
dish1 = st.selectbox("Select Category", [""] + list(menu.keys()))
dish2 = st.selectbox(
    "Select Sub-Category", 
    [""] + (list(menu[dish1].keys()) if dish1 else [])
)
dish3 = st.selectbox(
    "Select Dish Type", 
    [""] + (list(menu[dish1][dish2].keys()) if dish1 and dish2 else [])
)
dish4 = st.selectbox(
    "Select Item", 
    [""] + (list(menu[dish1][dish2][dish3].keys()) if dish1 and dish2 and dish3 else [])
)

quantity = st.number_input("Quantity", min_value=1, value=1)

# Step 3: Add to order button
if st.button("Add to Order"):
    if dish4 and quantity > 0:
        final_item = menu[dish1][dish2][dish3][dish4]
        if isinstance(final_item, dict):
            price = final_item.get("Price", 0) * quantity
        else:
            price = final_item * quantity

        st.session_state.total_bill += price
        st.session_state.order_items.append(f"{quantity} x {dish4} → {price}")
        st.success(f"Added {quantity} x {dish4} → {price}")
        st.info(f"💰 Current Bill: {st.session_state.total_bill}")

# Step 4: Show current order
if st.session_state.order_items:
    st.subheader("🛒 Current Order")
    for item in st.session_state.order_items:
        st.write(item)
    st.write(f"💰 Total: {st.session_state.total_bill}")

# Step 5: Checkout
if st.session_state.order_items and st.button("Checkout"):
    if st.session_state.table_number:
        st.info(f"🍴 Table Number: {st.session_state.table_number}")
    st.success(f"🧾 Final Bill = {st.session_state.total_bill}")

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(f"Total Bill: {st.session_state.total_bill}")
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")
    buf = io.BytesIO()
    qr_image.save(buf)
    buf.seek(0)
    st.image(buf, caption="Scan for your Bill", use_container_width=True)
