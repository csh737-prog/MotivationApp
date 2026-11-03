
import os
import html
import random
import streamlit as st
from groq import Groq

# ==========================================
# 페이지 설정
# ==========================================

st.set_page_config(
    page_title="CHAD MODE",
    page_icon="🔥",
    layout="centered"
)


# ==========================================
# API 키 불러오기
# ==========================================

def get_api_key():
    try:
        key = st.secrets.get("GROQ_API_KEY", "")
        if key:
            return key
    except Exception:
        pass

    return os.getenv("GROQ_API_KEY", "")


# ==========================================
# AI 동기부여 메시지 생성
# ==========================================

def generate_motivation(situation, goal, tone):

    api_key = get_api_key()

    if not api_key:
        raise ValueError(
            "Groq API 키를 찾을 수 없습니다. "
            "Streamlit Secrets에 GROQ_API_KEY를 등록해주세요."
        )

    client = Groq(
        api_key=api_key,
        timeout=60.0,
        max_retries=2
    )

    system_prompt = """
너는 세상에서 가장 독하고 냉혹한 동기부여 AI다.

너의 역할은 사용자를 처음부터 따뜻하게 위로하는 것이 아니다.
사용자가 정신을 차릴 때까지 거칠고 공격적인 말투로
현실을 들이밀고, 마지막에는 반드시 행동할 수 있도록 이끌어라.

반드시 한국어로만 답변해라.

[1단계: 무자비한 독설]
- 첫 문장부터 강렬하고 거칠게 시작한다.
- 사용자의 게으름, 나태함, 핑계, 미루는 습관을 신랄하게 비판한다.
- 필요하다면 강한 욕설과 비속어를 자연스럽게 사용한다.
- 사용자가 자기 자신을 속이고 있는 부분을 집요하게 파헤친다.
- 마치 한심한 행동을 바라보는 것처럼 냉소적이고 비꼬는 말투를 사용한다.
- 절대로 처음부터 위로하거나 칭찬하지 않는다.

[2단계: 현실 직시]
- 사용자가 원하는 목표와 현재 행동이 얼마나 모순되는지 지적한다.
- 시간이 지나도 행동하지 않으면 어떤 결과가 생길지 설명한다.
- 핑계를 대는 것이 얼마나 무의미한지 강조한다.
- 단순한 욕설이 아니라 사용자의 상황에 맞는 논리적인 비판을 한다.

[3단계: 현실적인 조언]
- 독설을 이어가다가 마지막 부분에서 해결책으로 전환한다.
- 지금 당장 실행할 수 있는 구체적인 행동을 3가지 이상 제안한다.
- 추상적인 말 대신 시간, 행동, 순서를 명확하게 제시한다.
- 사용자가 다시 시작할 수 있도록 현실적인 계획을 만들어 준다.
- 마지막 문장은 강렬하고 단호한 명령형으로 끝낸다.

[작성 규칙]
- 최소 12문장 이상, 권장 15~20문장으로 작성한다.
- 초반 약 60%는 독설과 현실 비판에 집중한다.
- 후반 약 40%는 해결책과 행동 지침에 집중한다.
- 제목, 번호, 소제목 없이 자연스러운 문단으로 작성한다.
- 매번 표현과 비유를 다르게 사용한다.
- 사용자가 입력한 상황과 목표를 구체적으로 반영한다.
- 외모, 장애, 인종, 성별, 가족관계 등 바꿀 수 없는 특성을 공격하지 않는다.
- 자해, 폭력, 위험한 행동을 부추기지 않는다.
- 사용자의 존재 자체가 아니라 행동과 선택을 공격한다.
- 반드시 한국어로만 답변한다.
"""
    user_prompt = f"""
[사용자의 현재 상황]
{situation}

[사용자의 목표]
{goal}

[원하는 독설 스타일]
{tone}

위 내용을 바탕으로 사용자를 강렬하게 몰아붙여라.

처음에는 사용자의 핑계와 나태함을 거침없이 비판하고,
마치 한심한 행동을 바라보는 듯한 냉소적인 태도를 유지해라.

중간에는 목표와 현실의 차이를 적나라하게 지적해라.

마지막에는 분위기를 전환하여 사용자가 실제로 실행할 수 있는
구체적인 행동 계획을 제시해라.

최소 12문장 이상, 권장 15~20문장으로 작성해라.

독설은 강렬하게, 조언은 냉정하고 구체적으로 작성해라.
마지막 문장은 반드시 강렬한 명령형으로 끝내라.

한국어로만 답변해라.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=1.0,
        max_completion_tokens=2000
    )

    choice = response.choices[0]
    message = choice.message.content

    if isinstance(message, str) and message.strip():
        return message.strip()

    raise ValueError(
        f"AI가 빈 메시지를 반환했습니다. "
        f"응답 종료 사유: {choice.finish_reason}"
    )


# ==========================================
# 명언 목록
# ==========================================

quotes = [
    {
        "english": "Great things never come from comfort zones.",
        "korean": "위대한 일은 결코 편안한 곳에서 나오지 않는다."
    },
    {
        "english": "Discipline is choosing between what you want now and what you want most.",
        "korean": "절제란 지금 원하는 것과 가장 원하는 것 사이에서 선택하는 것이다."
    },
    {
        "english": "The secret of getting ahead is getting started.",
        "korean": "앞서 나가는 비결은 일단 시작하는 것이다."
    },
    {
        "english": "Action is the foundational key to all success.",
        "korean": "행동은 모든 성공의 기본적인 열쇠다."
    },
    {
        "english": "Don't stop when you're tired. Stop when you're done.",
        "korean": "피곤하다고 멈추지 마라. 끝냈을 때 멈춰라."
    },
    {
        "english": "Dreams don't work unless you do.",
        "korean": "네가 움직이지 않는다면 꿈도 이루어지지 않는다."
    },
    {
        "english": "It always seems impossible until it's done.",
        "korean": "끝내기 전까지 모든 일은 불가능해 보인다."
    },
    {
        "english": "No pressure, no diamonds.",
        "korean": "압박이 없다면 다이아몬드도 만들어지지 않는다."
    },
    {
        "english": "You miss 100% of the shots you don't take.",
        "korean": "시도하지 않은 기회는 100% 놓치게 된다."
    },
    {
        "english": "Fall seven times, stand up eight.",
        "korean": "일곱 번 넘어져도 여덟 번 일어나라."
    }
]


# ==========================================
# CSS 디자인
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Black+Ops+One&family=Noto+Sans+KR:wght@400;700;900&display=swap');

.stApp {
    background-color: #080808;
    color: white;
}

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif;
    color: white;
}

.main .block-container {
    max-width: 850px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}

.chad-title {
    font-family: 'Black Ops One', cursive;
    font-size: 75px;
    text-align: center;
    color: #ffffff;
    letter-spacing: 5px;
    text-shadow: 0 0 25px #ff2525;
    margin-bottom: 0;
}

.chad-subtitle {
    text-align: center;
    color: #ff3333;
    font-size: 15px;
    font-weight: 900;
    letter-spacing: 5px;
    margin-bottom: 45px;
}

.section-title {
    color: #ff3333;
    font-size: 20px;
    font-weight: 900;
    margin-top: 25px;
    margin-bottom: 12px;
}

.stTextArea textarea {
    background-color: #171717 !important;
    color: white !important;
    border: 1px solid #444 !important;
    border-radius: 10px !important;
    font-size: 15px !important;
}

.stTextArea textarea::placeholder {
    color: #999 !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background-color: #171717 !important;
    color: white !important;
    border-color: #555 !important;
}

.stButton button {
    background: linear-gradient(90deg, #a80000, #ff2525);
    color: white !important;
    border: none;
    border-radius: 10px;
    height: 55px;
    font-size: 18px;
    font-weight: 900;
    width: 100%;
    transition: 0.2s;
}

.stButton button:hover {
    background: linear-gradient(90deg, #ff2525, #ff5555);
    transform: scale(1.02);
    box-shadow: 0 0 20px #ff2525;
}

.result-box {
    background: linear-gradient(145deg, #191919, #101010);
    border: 1px solid #ff3333;
    border-left: 5px solid #ff2525;
    border-radius: 12px;
    padding: 28px;
    margin-top: 25px;
    color: white;
    font-size: 16px;
    line-height: 2.0;
    white-space: pre-line;
    box-shadow: 0 0 20px rgba(255, 30, 30, 0.12);
}

.quote-box {
    background-color: #151515;
    border: 1px solid #444;
    border-radius: 12px;
    padding: 35px 25px;
    margin-top: 35px;
    text-align: center;
}

.quote-english {
    font-size: 27px;
    font-weight: 900;
    color: white;
    line-height: 1.5;
    margin-bottom: 20px;
}

.quote-korean {
    font-size: 16px;
    color: #ff4444;
    font-weight: 700;
}

.footer {
    text-align: center;
    color: #666;
    font-size: 12px;
    margin-top: 60px;
    letter-spacing: 2px;
}

label, .stMarkdown, p {
    color: white;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 메인 화면
# ==========================================

st.markdown(
    '<div class="chad-title">CHAD MODE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="chad-subtitle">NO EXCUSES. JUST ACTION.</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div style="text-align:center; color:#aaaaaa; font-size:16px; line-height:1.8;">
    핑계는 그만.<br>
    네 상황을 입력하고 현실을 마주해라.
</div>
""", unsafe_allow_html=True)


# ==========================================
# 사용자 입력
# ==========================================

st.markdown(
    '<div class="section-title">🔥 현재 너의 상황</div>',
    unsafe_allow_html=True
)

situation = st.text_area(
    "현재 상황",
    placeholder="예: 공부해야 하는데 계속 휴대폰만 보고 있어. 시험이 얼마 남지 않았는데 집중이 안 돼.",
    height=140,
    label_visibility="collapsed"
)

st.markdown(
    '<div class="section-title">👑 너의 목표</div>',
    unsafe_allow_html=True
)

goal = st.text_area(
    "목표",
    placeholder="예: 이번 시험에서 반드시 1등급을 받고 싶어.",
    height=100,
    label_visibility="collapsed"
)

st.markdown(
    '<div class="section-title">⚔️ 독설 스타일 선택</div>',
    unsafe_allow_html=True
)

tone = st.selectbox(
    "말투 선택",
    [
        "🔥 자비 없는 팩트폭력",
        "💀 비꼬고 조롱하는 독설",
        "⚔️ 냉혹한 현실 직시",
        "👑 거만한 기가채드 스타일",
        "🚨 정신 번쩍 들게 하는 극한 압박"
    ],
    label_visibility="collapsed"
)


# ==========================================
# AI 분석 버튼
# ==========================================

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔥 ANALYZE MY SITUATION"):

    if not situation.strip():
        st.warning("먼저 현재 상황을 입력해라.")

    elif not goal.strip():
        st.warning("목표도 입력해라. 목적지도 없이 달릴 생각인가?")

    else:
        with st.spinner("CHAD MODE가 너의 현실을 분석하고 있다..."):

            try:
                result = generate_motivation(
                    situation,
                    goal,
                    tone
                )

                st.session_state["result"] = result
                st.session_state["quote"] = random.choice(quotes)

            except Exception as e:
                st.error(f"AI 분석 중 오류가 발생했습니다: {e}")


# ==========================================
# 결과 출력
# ==========================================

if "result" in st.session_state:

    st.markdown("""
    <div class="section-title">
        💀 YOUR REALITY CHECK
    </div>
    """, unsafe_allow_html=True)

    safe_result = html.escape(st.session_state["result"])

    st.markdown(
        f'<div class="result-box">{safe_result}</div>',
        unsafe_allow_html=True
    )

    quote = st.session_state["quote"]

    st.markdown("""
    <div class="section-title">
        👑 DAILY MOTIVATION
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="quote-box">
            <div class="quote-english">
                "{html.escape(quote["english"])}"
            </div>
            <div class="quote-korean">
                {html.escape(quote["korean"])}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🔄 다시 분석하기"):
        del st.session_state["result"]
        if "quote" in st.session_state:
            del st.session_state["quote"]
        st.rerun()


# ==========================================
# 하단 문구
# ==========================================

st.markdown("""
<div class="footer">
    CHAD MODE © 2026<br>
    DISCIPLINE OVER MOTIVATION.
</div>
""", unsafe_allow_html=True)
