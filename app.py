import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Marseille Beach Rentals",
    page_icon="🏖️",
    layout="centered",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* Hero header */
.hero {
    background: linear-gradient(135deg, #0077b6 0%, #00b4d8 50%, #90e0ef 100%);
    border-radius: 18px;
    padding: 2.5rem 2rem 2rem 2rem;
    margin-bottom: 2rem;
    text-align: center;
    box-shadow: 0 8px 32px rgba(0,119,182,0.25);
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2.6rem;
    font-weight: 900;
    color: #fff;
    margin: 0 0 0.3rem 0;
    letter-spacing: -0.5px;
    text-shadow: 0 2px 8px rgba(0,0,0,0.15);
}
.hero p {
    color: rgba(255,255,255,0.88);
    font-size: 1.05rem;
    margin: 0;
}

/* Section labels */
.section-label {
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: #0077b6;
    margin-bottom: 0.15rem;
    margin-top: 0.5rem;
}

/* Summary card */
.summary-card {
    background: linear-gradient(135deg, #f0f9ff 0%, #e0f7fa 100%);
    border: 2px solid #00b4d8;
    border-radius: 14px;
    padding: 1.6rem 1.8rem;
    margin-top: 1rem;
}
.summary-card h3 {
    font-family: 'Playfair Display', serif;
    color: #0077b6;
    font-size: 1.35rem;
    margin: 0 0 1rem 0;
}
.summary-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.45rem 0;
    border-bottom: 1px dashed #b2ebf2;
    font-size: 0.97rem;
    color: #1a1a2e;
}
.summary-row:last-of-type {
    border-bottom: none;
}
.summary-total {
    margin-top: 0.9rem;
    padding-top: 0.9rem;
    border-top: 2.5px solid #0077b6;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 1.25rem;
    font-weight: 700;
    color: #0077b6;
    font-family: 'Playfair Display', serif;
}

/* Beach badge */
.beach-badge {
    display: inline-block;
    background: #0077b6;
    color: white;
    border-radius: 20px;
    padding: 0.25rem 0.9rem;
    font-size: 0.88rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    margin-bottom: 0.3rem;
}

/* Success banner */
.success-banner {
    background: linear-gradient(90deg, #06d6a0, #00b4d8);
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    color: white;
    text-align: center;
    font-size: 1.05rem;
    font-weight: 600;
    margin-top: 1rem;
    box-shadow: 0 4px 16px rgba(6,214,160,0.3);
}

/* Sticker price tags */
.price-tag {
    background: #fff3cd;
    border: 1.5px solid #ffc107;
    border-radius: 8px;
    padding: 0.15rem 0.55rem;
    font-size: 0.82rem;
    font-weight: 600;
    color: #856404;
    margin-left: 0.4rem;
}

/* Hide Streamlit branding */
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ── Data ───────────────────────────────────────────────────────────────────────
BEACHES = {
    "Plage des Catalans 🏖️": {"zone": "1er arr.", "emoji": "🐠"},
    "Plage du Prophète 🌊": {"zone": "8e arr.", "emoji": "🌊"},
    "Plage de la Pointe Rouge 🎣": {"zone": "8e arr.", "emoji": "⛵"},
    "Plage de Bonneveine 🌴": {"zone": "9e arr.", "emoji": "🌴"},
    "Plage de la Vieille Chapelle ⛪": {"zone": "9e arr.", "emoji": "🏄"},
    "Plage de Corbières 🪸": {"zone": "16e arr.", "emoji": "🪸"},
}

EQUIPMENT = {
    "☂️ Beach Umbrella": {"price_hour": 3.0, "price_day": 12.0, "icon": "☂️"},
    "🪑 Beach Chair": {"price_hour": 2.0, "price_day": 8.0, "icon": "🪑"},
    "🏖️ Sun Lounger (Transat)": {"price_hour": 4.0, "price_day": 15.0, "icon": "🏖️"},
    "🎪 Beach Tent (2-person)": {"price_hour": 5.0, "price_day": 20.0, "icon": "🎪"},
}

DURATION_UNIT = ["Hours", "Full Days"]

# ── Session state init ─────────────────────────────────────────────────────────
if "booking_confirmed" not in st.session_state:
    st.session_state.booking_confirmed = False
if "last_booking" not in st.session_state:
    st.session_state.last_booking = None

# ── Hero ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>🌊 Marseille Beach Rentals</h1>
    <p>Enjoy the sun without the hassle — affordable gear, right on the beach</p>
</div>
""", unsafe_allow_html=True)

# ── Main form ──────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">📍 Choose Your Beach</div>', unsafe_allow_html=True)
selected_beach = st.selectbox(
    "Beach",
    options=list(BEACHES.keys()),
    label_visibility="collapsed",
)

st.markdown('<div class="section-label" style="margin-top:1.2rem">🏄 Select Equipment</div>', unsafe_allow_html=True)
st.caption("Prices shown per hour / per full day")

selected_items = {}
cols = st.columns(2)
for i, (item_name, item_data) in enumerate(EQUIPMENT.items()):
    with cols[i % 2]:
        checked = st.checkbox(
            f"{item_name}  \n"
            f"**€{item_data['price_hour']:.0f}/hr** · **€{item_data['price_day']:.0f}/day**",
            key=f"item_{item_name}",
        )
        if checked:
            qty = st.number_input(
                f"Qty for {item_data['icon']}",
                min_value=1, max_value=10, value=1,
                key=f"qty_{item_name}",
            )
            selected_items[item_name] = qty

st.markdown('<div class="section-label" style="margin-top:1.2rem">⏱️ Rental Duration</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])
with col1:
    unit = st.radio("Duration unit", DURATION_UNIT, label_visibility="collapsed")
with col2:
    if unit == "Hours":
        duration = st.slider("Number of hours", min_value=1, max_value=12, value=3)
        duration_label = f"{duration} hour{'s' if duration > 1 else ''}"
    else:
        duration = st.slider("Number of days", min_value=1, max_value=7, value=1)
        duration_label = f"{duration} day{'s' if duration > 1 else ''}"

# ── Price calculation ──────────────────────────────────────────────────────────
def calc_price(item_name, qty, unit, duration):
    data = EQUIPMENT[item_name]
    unit_price = data["price_hour"] if unit == "Hours" else data["price_day"]
    return unit_price * qty * duration

line_items = []
total = 0.0
for item_name, qty in selected_items.items():
    subtotal = calc_price(item_name, qty, unit, duration)
    total += subtotal
    line_items.append((item_name, qty, subtotal))

# ── Live summary ───────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown('<div class="section-label">🧾 Booking Summary</div>', unsafe_allow_html=True)

if not selected_items:
    st.info("👆 Select at least one piece of equipment above to see your summary.")
else:
    beach_info = BEACHES[selected_beach]

    rows_html = ""
    for item_name, qty, subtotal in line_items:
        rows_html += f"""
        <div class="summary-row">
            <span>{item_name} × {qty}</span>
            <span>€{subtotal:.2f}</span>
        </div>"""

    st.markdown(f"""
    <div class="summary-card">
        <h3>📋 Your Rental</h3>
        <div class="summary-row">
            <span>📍 Beach</span>
            <span><strong>{selected_beach.split(" ")[0]} {selected_beach.split(" ")[1] if len(selected_beach.split(" ")) > 1 else ""}</strong> — {beach_info['zone']}</span>
        </div>
        <div class="summary-row">
            <span>⏱️ Duration</span>
            <span><strong>{duration_label}</strong></span>
        </div>
        {rows_html}
        <div class="summary-total">
            <span>Total</span>
            <span>€{total:.2f}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    # ── Confirm booking button ─────────────────────────────────────────────────
    if st.button("✅ Confirm Booking", type="primary", use_container_width=True):
        st.session_state.booking_confirmed = True
        st.session_state.last_booking = {
            "beach": selected_beach,
            "items": line_items,
            "duration": duration_label,
            "total": total,
        }

    if st.session_state.booking_confirmed and st.session_state.last_booking:
        b = st.session_state.last_booking
        st.markdown(f"""
        <div class="success-banner">
            🎉 Booking confirmed! Your gear will be ready at <strong>{b['beach'].split('�')[0].strip()}</strong>
            for <strong>{b['duration']}</strong> — Total: <strong>€{b['total']:.2f}</strong> 🌞
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔄 New Booking", use_container_width=True):
            st.session_state.booking_confirmed = False
            st.session_state.last_booking = None
            st.rerun()

# ── Footer ──────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#90a4ae; font-size:0.82rem;'>"
    "🌊 Marseille Beach Rentals · Profitez de la mer sans vous ruiner ☀️"
    "</p>",
    unsafe_allow_html=True,
)
