# 🤖 Gemini AI Chatbot

Streamlit을 이용해 배포한 구글 Gemini 챗봇입니다.

## 🚀 바로가기
[내 앱 주소 링크 클릭](https://myaichatbot-73dujbtnsqhbls8gcthltq.streamlit.app/)

## 📌 주요 기능
- **실시간 대화:** Gemini 2.5 Flash 모델과의 빠른 대화
- **대화 기록:** 대화 중 내용이 유지됨
- **반응형 UI:** 모바일과 PC 어디서나 접속 가능

## ⚙️ 설정 방법
1. [Google AI Studio](https://aistudio.google.com/)에서 API Key를 발급받습니다.
2. Streamlit Cloud의 `Advanced Settings` -> `Secrets`에 아래 내용을 입력합니다.
   ```toml
   GEMINI_API_KEY = "당신의_API_키"
