
import os
from datetime import date

import streamlit as st

# OpenAI API 사용
from openai import OpenAI


# -----------------------------
# 기본 설정
# -----------------------------
st.set_page_config(
    page_title="CHAD MODE",
    page_icon="⚫",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# -----------------------------
# 동기부여 명언
# -----------------------------
QUOTES = [
    {
        "text": "IT ALWAYS SEEMS IMPOSSIBLE UNTIL IT'S DONE.",
        "author": "Nelson Mandela",
        "meaning": "불가능해 보이는 일도 해내고 나면 달라진다."
    },
    {
        "text": "WELL DONE IS BETTER THAN WELL SAID.",
        "author": "Benjamin Franklin",
        "meaning": "말을 잘하는 것보다 행동으로 해내는 것이 낫다."
    },
    {
        "text": "THE SECRET OF GETTING AHEAD IS GETTING STARTED.",
        "author": "Mark Twain",
        "meaning": "앞서 나가는 비결은 일단 시작하는 것이다."
    },
    {
        "text": "YOU MISS 100% OF THE SHOTS YOU DON'T TAKE.",
        "author": "Wayne Gretzky",
        "meaning": "시도하지 않으면 성공할 가능성도 없다."
    },
    {
        "text": "ACTION IS THE FOUNDATIONAL KEY TO ALL SUCCESS.",
        "author": "Pablo Picasso",
        "meaning": "행동은 모든 성공의 기본이다."
    },
    {
        "text": "DISCIPLINE IS CHOOSING BETWEEN WHAT YOU WANT NOW AND WHAT YOU WANT MOST.",
        "author": "Abraham Lincoln에게 흔히 귀속되는 문구",
        "meaning": "절제란 지금 원하는 것과 진정으로 원하는 것 사이에서 선택하는 것이다."
    },
    {
        "text": "THE FUTURE DEPENDS ON WHAT YOU DO TODAY.",
        "author": "Mahatma Gandhi에게 흔히 귀속되는 문구",
        "meaning": "미래는 오늘 네가 무엇을 하느냐에 달려 있다."
    },
    {
        "text": "DO SOMETHING TODAY THAT YOUR FUTURE SELF WILL THANK YOU FOR.",
        "author": "널리 알려진 동기부여 문구",
        "meaning": "미래의 네가 고마워할 일을 오늘 해라."
    },
]


# 날짜에 따라 하루에 하나씩 표시
today_quote = QUOTES[date.today().toordinal() % len(QUOTES)]


# -----------------------------
# 검은색 배경 + 흰색 텍스트 디자인
# -----------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Black+Ops+One&family=Roboto:wght@400;500;700;900&display=swap');

    html, body, [class*="css"] {
        background-color: #000000;
        color: #FFFFFF;
        font-family: 'Roboto', sans-serif;
    }

    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }

    .block-container {
        max-width: 850px;
        padding-top: 3rem;
        padding-bottom: 5rem;
    }

    h1, h2, h3, p, label, span {
        color: #FFFFFF;
    }

    .brand {
        text-align: center;
        font-family: 'Black Ops One', cursive;
        font-size: clamp(2.5rem, 8vw, 5rem);
        letter-spacing: 5px;
        font-weight: 900;
        color: #FFFFFF;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        color: #999999;
        font-size: 0.9rem;
        letter-spacing: 4px;
        margin-top: 0.3rem;
        margin-bottom: 3rem;
    }

    .section-title {
        font-size: 1.1rem;
        font-weight: 900;
        letter-spacing: 2px;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
    }

    .motivation-box {
        border: 1px solid #444444;
        background: #080808;
        padding: 1.8rem;
        margin-top: 1rem;
        margin-bottom: 2rem;
        border-radius: 4px;
        white-space: pre-wrap;
        line-height: 2;
        font-size: 1.15rem;
        font-weight: 700;
    }

    .quote-label {
        color: #888888;
        text-align: center;
        font-size: 0.8rem;
        letter-spacing: 5px;
        margin-top: 4rem;
        margin-bottom: 1.5rem;
    }

    .quote-text {
        color: #FFFFFF;
        font-size: clamp(1.8rem, 5vw, 3.5rem);
        font-weight: 900;
        text-align: center;
        line-height: 1.25;
        letter-spacing: -1px;
        overflow-wrap: anywhere;
        margin-bottom: 1.5rem;
    }

    .quote-author {
        color: #888888;
        text-align: center;
        font-size: 0.9rem;
        letter-spacing: 2px;
    }

    .quote-meaning {
        color: #AAAAAA;
        text-align: center;
        font-size: 0.95rem;
        margin-top: 1rem;
        line-height: 1.8;
    }

    .footer {
        color: #555555;
        text-align: center;
        font-size: 0.75rem;
        letter-spacing: 2px;
        margin-top: 5rem;
    }

    div[data-testid="stTextArea"] textarea {
        background-color: #101010;
        color: #FFFFFF;
        border: 1px solid #444444;
        border-radius: 3px;
        font-size: 1rem;
    }

    div[data-testid="stTextArea"] textarea:focus {
        border: 1px solid #FFFFFF;
        box-shadow: none;
    }

    .stButton > button {
        width: 100%;
        background-color: #FFFFFF;
        color: #000000;
        border: 1px solid #FFFFFF;
        border-radius: 3px;
        height: 3.3rem;
        font-weight: 900;
        letter-spacing: 2px;
        transition: 0.2s;
    }

    .stButton > button:hover {
        background-color: #CCCCCC;
        color: #000000;
        border-color: #CCCCCC;
    }

    [data-testid="stAlert"] {
        background-color: #111111;
        color: #FFFFFF;
        border: 1px solid #444444;
    }

    #MainMenu, footer, header {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# 화면 상단
# -----------------------------
st.markdown(
    '<div class="brand">CHAD MODE</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">NO EXCUSES. JUST ACTION.</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <p style="text-align:center; color:#AAAAAA; line-height:1.9;">
        네 상황을 입력해라.<br>
        변명은 분석하고, 행동은 시작한다.
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")


# -----------------------------
# 사용자 상황 입력
# -----------------------------
st.markdown(
    '<div class="section-title">01 / YOUR SITUATION</div>',
    unsafe_allow_html=True,
)

with st.form("motivation_form"):
    situation = st.text_area(
        "지금 네 상황을 솔직하게 적어라.",
        placeholder=(
            "예시: 내일 시험인데 공부를 하나도 안 했다. "
            "계속 휴대폰만 보고 있고, 시작해야 한다는 건 알지만 "
            "귀찮아서 미루고 있다."
        ),
        height=170,
        max_chars=2000,
    )

    goal = st.text_input(
        "네가 이루고 싶은 목표 (선택)",
        placeholder="예: 수학 시험에서 90점 이상 받기",
        max_chars=200,
    )

    submitted = st.form_submit_button("ANALYZE MY SITUATION")


# -----------------------------
# AI 동기부여 메시지 생성
# -----------------------------
def make_fallback_message(user_situation, user_goal):
    """API 키가 없을 때 사용하는 기본 메시지."""

    goal_text = (
        f"네 목표는 '{user_goal}'이다."
        if user_goal.strip()
        else "네가 원하는 결과가 있다면 행동으로 증명해야 한다."
    )

    return (
        f"네 상황은 '{user_situation[:100]}'이다.\n\n"
        f"{goal_text}\n\n"
        "기분이 좋아질 때까지 기다리지 마라. "
        "지금 당장 할 수 있는 가장 작은 행동부터 시작해라.\n\n"
        "완벽한 계획보다 실제로 실행한 10분이 더 가치 있다."
    )


def generate_motivation(user_situation, user_goal):
    """OpenAI API로 상황에 맞는 메시지를 생성한다."""

    api_key = os.getenv("OPENAI_API_KEY")

    # Streamlit Cloud의 Secrets에서도 API 키를 읽는다.
    if not api_key:
        try:
            api_key = st.secrets.get("OPENAI_API_KEY", "")
        except Exception:
            api_key = ""

    if not api_key:
        return None

    client = OpenAI(api_key=api_key)

    prompt = f"""
너는 CHAD MODE라는 동기부여 앱의 냉정하고 강렬한 코치다.

사용자의 상황을 분석하고 한국어로 동기부여 메시지를 작성해라.

[사용자 상황]
{user_situation}

[사용자 목표]
{user_goal if user_goal.strip() else "구체적인 목표를 입력하지 않음"}

[작성 규칙]
1. 총 4줄 정도로 작성한다.
2. 사용자의 상황을 실제로 반영한다. 누구에게나 통하는 뻔한 말만 하지 마라.
3. 기가채드 밈처럼 단호하고 자신감 있으며 직설적인 말투를 사용한다.
4. 핑계와 현실적인 장애물을 구분하고, 지금 할 수 있는 행동을 제시한다.
5. 마지막 문장은 즉시 행동하게 만드는 짧고 강렬한 문장으로 끝낸다.
6. 사용자를 모욕하거나 비하하지 마라. 자해, 위험한 행동, 수면이나 식사를 극단적으로 줄이는 행동을 권하지 마라.
7. 서론, 제목, 번호, 해설 없이 메시지만 출력한다.
8. 줄바꿈을 활용해 약 4줄로 작성한다.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
    )

    return response.output_text.strip()


if submitted:
    if not situation.strip():
        st.warning("먼저 네 상황부터 입력해라.")
    else:
        with st.spinner("상황 분석 중... 변명은 잠시 내려놔라."):
            try:
                ai_message = generate_motivation(
                    situation,
                    goal,
                )

                if ai_message:
                    st.session_state["motivation_message"] = ai_message
                    st.session_state["message_mode"] = "AI"
                else:
                    st.session_state["motivation_message"] = (
                        make_fallback_message(situation, goal)
                    )
                    st.session_state["message_mode"] = "BASIC"

            
            except Exception as e:
                st.error("AI 요청에 실패했어.")
                st.write("오류 종류:", type(e).__name__)
                st.code(str(e))
            
                st.session_state["motivation_message"] = (
                    make_fallback_message(situation, goal)
                )
                st.session_state["message_mode"] = "BASIC"


# -----------------------------
# 결과 표시
# -----------------------------
if "motivation_message" in st.session_state:
    st.markdown("---")

    st.markdown(
        '<div class="section-title">02 / YOUR REALITY CHECK</div>',
        unsafe_allow_html=True,
    )

    mode = st.session_state.get("message_mode", "BASIC")

    if mode == "AI":
        st.caption("AI PERSONALIZED COACHING")
    else:
        st.caption("BASIC COACHING · AI API 연결 시 맞춤 분석 가능")

    message = st.session_state["motivation_message"]

    st.markdown(
        f'<div class="motivation-box">{message}</div>',
        unsafe_allow_html=True,
    )

    st.button(
        "READ IT AGAIN. THEN TAKE ACTION.",
        on_click=lambda: st.toast("이제 행동으로 증명할 차례다."),
    )


# -----------------------------
# 오늘의 명언
# -----------------------------
st.markdown("---")

st.markdown(
    '<div class="quote-label">03 / QUOTE OF THE DAY</div>',
    unsafe_allow_html=True,
)

st.markdown(
    f'<div class="quote-text">“{today_quote["text"]}”</div>',
    unsafe_allow_html=True,
)

st.markdown(
    f'<div class="quote-author">{today_quote["author"]}</div>',
    unsafe_allow_html=True,
)

st.markdown(
    f'<div class="quote-meaning">{today_quote["meaning"]}</div>',
    unsafe_allow_html=True,
)


# -----------------------------
# 하단 문구
# -----------------------------
st.markdown(
    """
    <div class="footer">
        DISCIPLINE OVER MOTIVATION<br><br>
        CHAD MODE · BUILT FOR ACTION
    </div>
    """,
    unsafe_allow_html=True,
)
