import streamlit as st
from google import genai
from google.genai import types

from prompts import SYSTEM_PROMPT


st.set_page_config(
    page_title="SnapStudy",
    page_icon="📚"
)


st.title("📚 SnapStudy")
st.caption("Upload your study material and ask questions about it.")


GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]


@st.cache_resource
def get_gemini_client():
    return genai.Client(api_key=GEMINI_API_KEY)


gemini_client = get_gemini_client()


if "chat" not in st.session_state:
    st.session_state.chat = gemini_client.chats.create(
        model="gemini-3.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT
        )
    )


uploaded_file = st.file_uploader(
    "📷 Upload your syllabus, timetable, assignment, or notes",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file:
    st.image(
        uploaded_file,
        caption="Uploaded material",
        use_container_width=True
    )

    question = st.chat_input(
        "Ask something about this material..."
    )

    if question:
        image_bytes = uploaded_file.getvalue()

        parts = [
            types.Part.from_bytes(
                data=image_bytes,
                mime_type=uploaded_file.type
            ),
            question
        ]

        with st.spinner("Analyzing your material..."):
            try:
                response = st.session_state.chat.send_message(parts)
                answer = response.text

                st.chat_message("user").write(question)
                st.chat_message("assistant").write(answer)

            except Exception as error:
                st.error(f"Something went wrong: {error}")