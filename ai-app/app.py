import streamlit as st
from openai import OpenAI

# 初始化
client = OpenAI(api_key="YOUR_API_KEY")

st.title("🌍 Civilization Decision AI")

# 输入
country = st.text_input("Enter Country")

if st.button("Analyze") and country:
    
    # 读取Prompt
    with open("prompt.txt", "r", encoding="utf-8") as f:
        prompt_template = f.read()

    prompt = prompt_template.replace("{{USER_INPUT}}", country)

    # 调用AI
    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "You are a structured decision engine"},
            {"role": "user", "content": prompt}
        ]
    )

    result = response.choices[0].message.content

    st.subheader("Result")
    st.code(result, language="json")
