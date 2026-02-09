import streamlit as st
import google.generativeai as genai

# 페이지 설정
st.set_page_config(page_title="My_free_little_chat", page_icon="🤖")
st.title("🤖 내가 만든 무료 Gemini 챗봇")

# API 키 설정(보안을 위해 뒤에서 처리)
api_key=st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

# 대화 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 대화 내용 화면에 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력창
if prompt := st.chat_input("메시지를 입력하세요: "):
    # 사용자 메시지 표시 및 저장
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI 응답 생성
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})

