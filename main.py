
import os
import random
import streamlit as st
import streamlit.components.v1 as components
from google import genai

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="CHAD MODE",
    page_icon="🔥",
    layout="centered"
)

# -----------------------------
# API 키 가져오기
# -----------------------------
def get_api_key():
    try:
        key = st.secrets.get("GEMINI_API_KEY", "")
        if key:
            return key
    except Exception:
        pass

    return os.getenv("GEMINI_API_KEY", "")


# -----------------------------
# 명언 데이터
# -----------------------------
QUOTES = [
    ("Discipline beats motivation.", "규율은 동기부여를 이긴다."),
    ("No excuses. Just results.", "변명은 그만. 결과로 증명하라."),
    ("Become the person you promised yourself to be.", "스스로 약속한 사람이 되어라."),
    ("Your future is created by what you do today.", "너의 미래는 오늘의 행동으로 만들어진다."),
    ("The pain of discipline is less than the pain of regret.", "규율의 고통은 후회의 고통보다 작다."),
    ("Dream big. Start small. Act now.", "크게 꿈꾸고, 작게 시작하고, 지금 행동하라."),
    ("Winners are not born. They are built.", "승자는 태어나는 것이 아니라 만들어진다."),
    ("Stop waiting. Start becoming.", "기다리지 말고, 변화를 시작하라."),
    ("You vs. You. Every single day.", "매일의 경쟁 상대는 오직 어제의 너다."),
    ("Great things never come from comfort zones.", "위대한 일은 결코 안락한 곳에서 나오지 않는다.")
]

# -----------------------------
# Gemini AI 동기부여 생성
# -----------------------------
def generate_motivation(situation, goal, tone):

    api_key = get_api_key()

    if not api_key:
        raise ValueError(
            "Gemini API 키를 찾을 수 없어. "
            "Streamlit Secrets에 GEMINI_API_KEY를 등록해 줘."
        )

    client = genai.Client(api_key=api_key)

    prompt = f"""
너는 CHAD MODE라는 동기부여 서비스의 AI다.

사용자의 상황을 분석하고 강렬하고 직설적인 동기부여 메시지를 작성해라.

[사용자의 현재 상황]
{situation}

[사용자의 목표]
{goal}

[원하는 말투]
{tone}

작성 규칙:
1. 반드시 한국어로 작성한다.
2. 정확히 4줄로 작성한다.
3. 각 줄은 짧고 강렬하게 작성한다.
4. 뻔한 위로나 상투적인 표현은 피한다.
5. 사용자가 처한 상황과 목표를 구체적으로 반영한다.
6. 때로는 냉정하고 직설적으로 현실을 지적한다.
7. 무조건적인 비난이나 모욕은 하지 않는다.
8. 매번 새로운 표현과 비유를 사용한다.
9. 제목이나 번호 없이 메시지 4줄만 출력한다.
10. 마지막 줄은 행동을 촉구하는 강렬한 문장으로 끝낸다.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "temperature": 1.0,
            "max_output_tokens": 300,
        },
    )

    message = (response.text or "").strip()

    if not message:
        raise ValueError("AI가 빈 메시지를 반환했어.")

    return message


# -----------------------------
# CSS 디자인
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Black+Ops+One&family=Noto+Sans+KR:wght@400;500;700;900&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at top, #252525 0%, #111111 45%, #050505 100%);
    color: white;
}

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif;
    color: white;
}

.block-container {
    max-width: 850px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}

.main-title {
    font-family: 'Black Ops One', cursive;
    font-size: clamp(3.5rem, 10vw, 6rem);
    color: #ffffff;
    text-align: center;
    letter-spacing: 5px;
    text-shadow: 0 0 25px rgba(255, 40, 40, 0.35);
    margin-bottom: 0;
}

.subtitle {
    text-align: center;
    color: #ff3333;
    font-size: 14px;
    font-weight: 900;
    letter-spacing: 5px;
    margin-bottom: 35px;
}

.section-title {
    color: #ff3b3b;
    font-size: 20px;
    font-weight: 900;
    margin-top: 25px;
    margin-bottom: 12px;
}

div[data-testid="stTextArea"] textarea,
div[data-testid="stTextInput"] input {
    background-color: #181818 !important;
    color: white !important;
    border: 1px solid #444 !important;
    border-radius: 12px !important;
    caret-color: white !important;
}

div[data-testid="stTextArea"] textarea::placeholder,
div[data-testid="stTextInput"] input::placeholder {
    color: #999 !important;
}

div[data-testid="stTextArea"] textarea:focus,
div[data-testid="stTextInput"] input:focus {
    border: 1px solid #ff3333 !important;
    box-shadow: 0 0 8px rgba(255, 50, 50, 0.3) !important;
}

div[data-testid="stSelectbox"] div[data-baseweb="select"] {
    background-color: #181818 !important;
    color: white !important;
}

div[data-testid="stSelectbox"] div {
    color: white !important;
}

.stButton > button {
    width: 100%;
    height: 55px;
    background: linear-gradient(90deg, #b50000, #ff2929);
    color: white !important;
    border: none;
    border-radius: 12px;
    font-size: 18px;
    font-weight: 900;
    letter-spacing: 2px;
    transition: 0.2s;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #ff2929, #ff5555);
    box-shadow: 0 0 20px rgba(255, 40, 40, 0.5);
    transform: scale(1.01);
    color: white !important;
}

.result-box {
    background: linear-gradient(145deg, #191919, #101010);
    border: 1px solid #5a1717;
    border-left: 5px solid #ff2929;
    border-radius: 15px;
    padding: 28px;
    margin-top: 25px;
    box-shadow: 0 0 25px rgba(255, 0, 0, 0.08);
}

.result-label {
    color: #ff3b3b;
    font-weight: 900;
    font-size: 13px;
    letter-spacing: 3px;
    margin-bottom: 18px;
}

.result-text {
    color: white;
    font-size: 19px;
    font-weight: 700;
    line-height: 2;
    white-space: pre-line;
}

.quote-box {
    text-align: center;
    padding: 40px 20px;
    margin-top: 35px;
    background: #171717;
    border-radius: 18px;
    border: 1px solid #333;
}

.quote-label {
    color: #ff3333;
    font-size: 13px;
    font-weight: 900;
    letter-spacing: 4px;
    margin-bottom: 25px;
}

.quote-en {
    color: white;
    font-size: clamp(23px, 5vw, 35px);
    font-weight: 900;
    line-height: 1.5;
    margin-bottom: 18px;
}

.quote-ko {
    color: #aaaaaa;
    font-size: 16px;
    line-height: 1.7;
}

.footer {
    text-align: center;
    color: #666;
    font-size: 12px;
    margin-top: 50px;
    letter-spacing: 2px;
}

.stAlert {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# 메인 화면
# -----------------------------
st.markdown(
    '<div class="main-title">CHAD MODE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">NO EXCUSES. JUST ACTION.</div>',
    unsafe_allow_html=True
)

st.markdown(
    "### 🔥 지금의 너를 분석해 보자.",
)

st.markdown(
    '<div class="section-title">01. YOUR SITUATION</div>',
    unsafe_allow_html=True
)

situation = st.text_area(
    "현재 상황",
    placeholder="예: 시험이 얼마 남지 않았는데 공부를 시작하지 못했어. 계속 핸드폰만 보고 있어.",
    height=130,
    label_visibility="collapsed"
)

st.markdown(
    '<div class="section-title">02. YOUR GOAL</div>',
    unsafe_allow_html=True
)

goal = st.text_input(
    "목표",
    placeholder="예: 이번 시험에서 평균 90점 이상 받기",
    label_visibility="collapsed"
)

st.markdown(
    '<div class="section-title">03. YOUR CHAD STYLE</div>',
    unsafe_allow_html=True
)

tone = st.selectbox(
    "말투 선택",
    [
        "냉정하고 직설적인 스타일",
        "강렬하고 자신감 넘치는 스타일",
        "현실을 뼈아프게 지적하는 스타일",
        "차분하지만 묵직한 스타일",
        "거침없이 도전하게 만드는 스타일"
    ],
    label_visibility="collapsed"
)

st.write("")

# -----------------------------
# 실행 버튼
# -----------------------------
if st.button("🔥 ACTIVATE CHAD MODE"):

    if not situation.strip():
        st.warning("먼저 현재 상황을 입력해 줘!")

    elif not goal.strip():
        st.warning("이루고 싶은 목표도 입력해 줘!")

    else:
        with st.spinner("CHAD MODE가 너의 상황을 분석하는 중..."):

            try:
                motivation = generate_motivation(
                    situation,
                    goal,
                    tone
                )

                st.session_state["motivation"] = motivation

                st.session_state["quote"] = random.choice(QUOTES)

            except Exception as e:
                st.error(
                    "메시지를 생성하지 못했어. API 키나 사용량 제한을 확인해 줘."
                )
                st.caption(f"오류 내용: {e}")


# -----------------------------
# 결과 출력
# -----------------------------
if "motivation" in st.session_state:

    st.markdown(
        f"""
        <div class="result-box">
            <div class="result-label">YOUR CHAD MESSAGE</div>
            <div class="result-text">
                {st.session_state["motivation"]}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    quote_en, quote_ko = st.session_state["quote"]

    st.markdown(
        f"""
        <div class="quote-box">
            <div class="quote-label">DAILY MOTIVATION</div>
            <div class="quote-en">“{quote_en}”</div>
            <div class="quote-ko">{quote_ko}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# 하단 문구
# -----------------------------
st.markdown(
    '<div class="footer">BUILT DIFFERENT. STAY DISCIPLINED.</div>',
    unsafe_allow_html=True
)
