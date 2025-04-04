import streamlit as st # type: ignore
from PIL import Image

st.set_page_config(page_title="The Living Office", layout="wide")

# Load local background image
bg_image_path = "assets/greenhouse_bg.jpg"
st.image(bg_image_path, use_column_width=True, caption="🌿 Welcome to The Living Office")

st.markdown("### This isn’t a funnel. It’s a frequency mirror.")
st.markdown("Step into a space where business becomes rhythm, and strategy breathes with soul.")

if st.button("Begin Resonance Mapping"):
    st.session_state.page = "assessment"

if "page" in st.session_state and st.session_state.page == "assessment":
    st.markdown("## 🎧 Resonance Mapping Assessment")

    rhythm = st.radio("What’s your current rhythm?", [
        "I’m moving but out of sync",
        "I feel paused or stuck",
        "I’m in flow, just seeking refinement"
    ])

    st.markdown("### 🪞 Resonance Reflection")
    if rhythm == "I’m moving but out of sync":
        st.success("🔍 Your rhythm is calling for realignment. Let’s explore where the dissonance lives.")
    elif rhythm == "I feel paused or stuck":
        st.info("🌒 This is your rest note. Let’s uncover what wants to grow next.")
    elif rhythm == "I’m in flow, just seeking refinement":
        st.warning("🌿 Beautiful. Let’s sculpt the subtleties of your groove.")

    st.markdown("---")
    st.markdown("### 🎼 Resonance Profile Teaser")
    st.write("“Your structure is strong — now, let’s tune your frequency.”")

    col1, col2 = st.columns(2)
    with col1:
        st.button("📅 Book a Sound Check")
    with col2:
        st.button("📖 Learn More About Your Rhythm Strategy")
