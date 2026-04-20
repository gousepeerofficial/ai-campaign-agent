import streamlit as st
from openai import OpenAI

# Safe API key loading
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Campaign Agent", layout="centered")

st.title("🚀 AI Campaign & Creative Generator")
st.write("Generate high-converting ad creatives and campaign strategies using AI.")

st.markdown("---")
st.subheader("📥 Input Details")

product = st.text_input("Product / Brand")
audience = st.text_input("Target Audience")
platform = st.selectbox("Platform", ["Instagram", "Facebook", "Google Ads", "LinkedIn"])
tone = st.selectbox("Ad Tone", ["Luxury", "Casual", "Aggressive", "Minimal"])

if st.button("Generate Campaign"):
    if not product or not audience:
        st.warning("Please fill all fields")
    else:
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

        try:
            response = client.responses.create(
                model="gpt-4o-mini",
                input=prompt
            )

            # Safer output extraction
            output_text = response.output[0].content[0].text

            st.markdown("---")
            st.subheader("📊 Campaign Results")
            st.success("✅ AI Generated Campaign Strategy")
            st.write(output_text)

        except Exception as e:
            st.error(f"Error: {e}")
