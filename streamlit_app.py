import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Campaign Agent", layout="centered")

st.title("🚀 AI Campaign & Creative Generator")

product = st.text_input("Product / Brand")
audience = st.text_input("Target Audience")
platform = st.selectbox("Platform", ["Instagram", "Facebook", "Google Ads", "LinkedIn"])
tone = st.selectbox("Ad Tone", ["Luxury", "Casual", "Aggressive", "Minimal"])

if st.button("Generate Campaign"):
    prompt = f"""
    You are an AI marketing agent.

    Create a high-converting ad campaign.

    Product: {product}
    Audience: {audience}
    Platform: {platform}
    Tone: {tone}

    Output:
    1. 3 Headlines (high CTR)
    2. Ad Copy
    3. Call to Action
    4. Campaign Strategy (budget + targeting idea)
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    st.subheader("📢 Campaign Output")
    st.write(response.output[0].content[0].text)
