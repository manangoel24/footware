import streamlit as st
from image_gen import generate_shoe_image
from agents import ShoeAdvisorAgent


st.set_page_config(page_title="AI Shoe Advisor", layout="centered")
st.title("👟 How to Choose the Right Shoes — Powered by AI")
st.markdown("Let this AI assistant help you find shoes based on comfort, purpose, durability, and more.")

# Input form
with st.form("shoe_form"):
    purpose = st.selectbox("What will you use the shoes for?", ["Running", "Casual Wear", "Formal Events", "Hiking", "Sports", "Daily Use"])
    comfort = st.select_slider("How important is comfort to you?", options=["Low", "Medium", "High"])
    durability = st.select_slider("Expected durability?", options=["6 months", "1 year", "2+ years"])
    style = st.text_input("What kind of style are you looking for? (e.g. minimal, sporty, classic)")
    brand_pref = st.text_input("Any preferred brands? (optional)")
    submitted = st.form_submit_button("Get My Shoe Recommendation")

if submitted:
    with st.spinner("Thinking about your perfect pair..."):
        advisor = ShoeAdvisorAgent()
        advice = advisor.recommend(
            purpose=purpose,
            comfort=comfort,
            durability=durability,
            style=style,
            brand=brand_pref
        )
        st.subheader("Personalized Recommendation")
        st.markdown(advice)

        # Generate shoe concept image (optional)
        st.subheader("Visual Preview")
        prompt = f"A {comfort.lower()} comfort {style} shoe for {purpose.lower()} use, modern look"
        image_url = generate_shoe_image(prompt)
        if image_url:
            st.image(image_url, caption="AI-Generated Shoe Design", use_column_width=True)
