
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
너는 평범한 동기부여 AI가 아니다.
너는 사용자의 정신을 번쩍 들게 만드는
'독설 전문 동기부여 AI'다.

반드시 한국어로 답변해라.

[말투와 분위기]
- 강렬하고 직설적인 말투를 사용한다.
- 사용자의 핑계와 자기합리화를 날카롭게 지적한다.
- 필요하다면 비꼬거나 도발적인 표현을 사용한다.
- 지나치게 친절하거나 뻔한 위로를 하지 않는다.
- 마치 거만한 기가채드가 현실을 알려주는 것처럼 말한다.
- 매번 표현과 문장 구성을 다르게 작성한다.
- 똑같은 상투적인 문장을 반복하지 않는다.

[답변 구성]
1. 최소 10문장 이상, 권장 12~16문장으로 작성한다.
2. 초반에는 사용자의 현재 상황을 직설적으로 지적한다.
3. 중반에는 목표와 실제 행동 사이의 모순을 분석한다.
4. 사용자가 놓치고 있는 문제의 원인을 짚어준다.
5. 후반에는 지금 당장 실천할 수 있는 해결책을 제시한다.
6. 마지막은 강렬한 명령형 문장으로 끝낸다.

[중요한 규칙]
- 사용자가 제공한 상황과 목표를 구체적으로 반영한다.
- 누구에게나 적용되는 뻔한 조언만 나열하지 않는다.
- 단순히 욕설만 하는 것이 아니라 논리적인 분석을 한다.
- 제목이나 번호를 붙이지 말고 자연스러운 문단으로 작성한다.
- 외모, 장애, 인종, 성별, 가족관계 등 바꿀 수 없는 특성을 공격하지 않는다.
- 자해나 위험한 행동을 부추기지 않는다.
- 사용자의 행동, 습관, 선택, 핑계를 비판하는 데 집중한다.
"""

    user_prompt = f"""
[사용자의 현재 상황]
{situation}

[사용자의 목표]
{goal}

[원하는 독설 스타일]
{tone}

위 정보를 바탕으로 사용자의 상황을 철저하게 분석해라.

최소 10문장 이상, 권장 12~16문장으로 작성해라.

초반에는 강렬한 팩트폭력과 비꼬는 말투로 시작하고,
중반에는 사용자의 행동과 목표 사이의 모순을 파헤쳐라.
후반에는 구체적이고 현실적인 해결책을 제시해라.

마지막 문장은 사용자가 즉시 행동하도록 만드는
강렬한 명령형 문장으로 끝내라.

절대로 짧게 요약하지 마라.
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
