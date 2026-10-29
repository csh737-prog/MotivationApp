
import streamlit as st
import random
import re
from datetime import date


# =====================================
# 기본 설정
# =====================================
st.set_page_config(
    page_title="CHAD MODE",
    page_icon="⚫",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# =====================================
# 명언 데이터
# =====================================
QUOTES = [
    {
        "text": "IT ALWAYS SEEMS IMPOSSIBLE UNTIL IT'S DONE.",
        "author": "NELSON MANDELA",
        "meaning": "불가능해 보이는 일도 해내고 나면 달라진다.",
    },
    {
        "text": "WELL DONE IS BETTER THAN WELL SAID.",
        "author": "BENJAMIN FRANKLIN",
        "meaning": "말을 잘하는 것보다 행동으로 해내는 것이 낫다.",
    },
    {
        "text": "THE SECRET OF GETTING AHEAD IS GETTING STARTED.",
        "author": "MARK TWAIN",
        "meaning": "앞서 나가는 비결은 일단 시작하는 것이다.",
    },
    {
        "text": "YOU MISS 100% OF THE SHOTS YOU DON'T TAKE.",
        "author": "WAYNE GRETZKY",
        "meaning": "시도하지 않으면 성공할 가능성도 없다.",
    },
    {
        "text": "ACTION IS THE FOUNDATIONAL KEY TO ALL SUCCESS.",
        "author": "PABLO PICASSO",
        "meaning": "행동은 모든 성공의 기본이다.",
    },
    {
        "text": "THE FUTURE DEPENDS ON WHAT YOU DO TODAY.",
        "author": "오늘의 행동을 강조하는 널리 알려진 문구",
        "meaning": "미래는 오늘 네가 무엇을 하느냐에 달려 있다.",
    },
    {
        "text": "DO SOMETHING TODAY THAT YOUR FUTURE SELF WILL THANK YOU FOR.",
        "author": "널리 알려진 동기부여 문구",
        "meaning": "미래의 네가 고마워할 일을 오늘 해라.",
    },
    {
        "text": "GREAT THINGS ARE DONE BY A SERIES OF SMALL THINGS BROUGHT TOGETHER.",
        "author": "VINCENT VAN GOGH",
        "meaning": "위대한 일은 작은 일들이 모여 이루어진다.",
    },
]


# =====================================
# CSS 디자인
# =====================================
st.markdown(
    """
    <style>
    @import url(
        'https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap'
    );

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
        padding-bottom: 4rem;
    }

    h1, h2, h3, p, label, span {
        color: #FFFFFF;
    }

    .brand {
        text-align: center;
        font-size: clamp(2.8rem, 9vw, 5.5rem);
        font-weight: 900;
        letter-spacing: 4px;
        line-height: 1.1;
        color: #FFFFFF;
        margin-bottom: 0.4rem;
    }

    .subtitle {
        text-align: center;
        font-size: 0.8rem;
        letter-spacing: 5px;
        color: #888888;
        margin-bottom: 3rem;
    }

    .section-title {
        font-size: 0.9rem;
        font-weight: 900;
        letter-spacing: 3px;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        color: #FFFFFF;
    }

    .description {
        color: #AAAAAA;
        text-align: center;
        line-height: 1.9;
        font-size: 0.95rem;
    }

    .motivation-box {
        background: #080808;
        border-left: 4px solid #FFFFFF;
        border-top: 1px solid #333333;
        border-right: 1px solid #333333;
        border-bottom: 1px solid #333333;
        padding: 1.5rem;
        margin-top: 1rem;
        margin-bottom: 1.5rem;
        border-radius: 3px;
        color: #FFFFFF;
        font-size: 1.12rem;
        font-weight: 700;
        line-height: 2;
        white-space: pre-line;
        overflow-wrap: anywhere;
    }

    .quote-label {
        color: #777777;
        text-align: center;
        font-size: 0.8rem;
        letter-spacing: 5px;
        margin-top: 4rem;
        margin-bottom: 1.5rem;
    }

    .quote-text {
        color: #FFFFFF;
        font-size: clamp(1.8rem, 5.5vw, 3.6rem);
        font-weight: 900;
        text-align: center;
        line-height: 1.3;
        letter-spacing: -1px;
        overflow-wrap: anywhere;
        margin-bottom: 1.5rem;
    }

    .quote-author {
        color: #888888;
        text-align: center;
        font-size: 0.8rem;
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
        letter-spacing: 3px;
        margin-top: 5rem;
        line-height: 2;
    }

    div[data-testid="stTextArea"] textarea,
    div[data-testid="stTextInput"] input {
        background-color: #101010;
        color: #FFFFFF;
        border: 1px solid #444444;
        border-radius: 3px;
    }

    div[data-testid="stTextArea"] textarea:focus,
    div[data-testid="stTextInput"] input:focus {
        border: 1px solid #FFFFFF;
        box-shadow: none;
    }

    .stButton > button,
    .stFormSubmitButton > button {
        width: 100%;
        background-color: #FFFFFF;
        color: #000000;
        border: 1px solid #FFFFFF;
        border-radius: 3px;
        height: 3.2rem;
        font-weight: 900;
        letter-spacing: 2px;
        transition: 0.2s;
    }

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
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


# =====================================
# 상황 분석 및 메시지 생성
# =====================================
def generate_message(situation, goal):
    """
    입력된 상황의 키워드를 분석해
    상황별 문장과 행동 지침을 조합한다.
    외부 API를 사용하지 않는다.
    """

    text = situation.lower()
    goal = goal.strip()

    # 상황별 분석 규칙
    if any(word in text for word in [
        "시험", "공부", "성적", "내신", "수능",
        "숙제", "과제", "수행평가", "시험공부"
    ]):
        problem = "시험과 공부는 걱정만 한다고 해결되지 않는다."
        action = "지금 가장 중요한 범위 하나를 정하고 10분만 집중해라."

    elif any(word in text for word in [
        "휴대폰", "핸드폰", "유튜브", "게임",
        "틱톡", "인스타", "쇼츠", "sns", "스마트폰"
    ]):
        problem = "네 집중력을 빼앗는 것은 화면 속 자극이다."
        action = "휴대폰을 손이 닿지 않는 곳에 두고 해야 할 일부터 시작해라."

    elif any(word in text for word in [
        "귀찮", "미루", "하기 싫", "의욕",
        "게으르", "무기력", "시작을 못", "하기싫"
    ]):
        problem = "시작할 기분이 생기기만 기다리면 시간은 계속 사라진다."
        action = "완벽하게 하려 하지 말고 딱 5분만 시작해라."

    elif any(word in text for word in [
        "실패", "망했", "포기", "실수",
        "좌절", "떨어졌", "못했"
    ]):
        problem = "한 번의 실패가 네 전체 능력을 결정하지는 않는다."
        action = "실패한 원인 하나를 찾아 다음 시도에서 바꿔라."

    elif any(word in text for word in [
        "불안", "걱정", "두렵", "무서",
        "긴장", "초조"
    ]):
        problem = "걱정은 미래를 바꾸지 않지만 준비는 가능성을 바꾼다."
        action = "지금 통제할 수 있는 일 하나를 골라 실행해라."

    elif any(word in text for word in [
        "운동", "다이어트", "체력", "헬스",
        "달리기", "근육"
    ]):
        problem = "결과는 한 번의 결심보다 꾸준히 반복하는 행동에서 나온다."
        action = "오늘 할 수 있는 현실적인 운동 계획 하나를 실행해라."

    elif any(word in text for word in [
        "친구", "인간관계", "연애", "짝사랑",
        "갈등", "사람들", "왕따"
    ]):
        problem = "다른 사람의 반응을 전부 통제할 수는 없다."
        action = "네가 통제할 수 있는 말과 행동부터 정리해라."

    elif any(word in text for word in [
        "진로", "꿈", "목표", "미래", "진학",
        "직업", "대학"
    ]):
        problem = "미래는 고민만으로 선명해지지 않는다. 직접 경험해야 한다."
        action = "관심 분야를 조사하거나 작은 프로젝트 하나를 시작해라."

    else:
        problem = "상황이 저절로 바뀌기를 기다리면 지금과 같은 결과가 반복된다."
        action = "지금 당장 할 수 있는 가장 작은 행동 하나를 실행해라."

    # 목표에 따른 문장
    if goal:
        goal_line = f"네 목표는 '{goal}'이다. 말이 아니라 행동으로 가까워져라."
    else:
        goal_line = "원하는 결과가 있다면 오늘의 행동부터 바꿔라."

    # 상황을 직접 반영하는 문장
    short_situation = re.sub(r"\s+", " ", situation.strip())
    if len(short_situation) > 65:
        short_situation = short_situation[:65] + "..."

    opening_options = [
        f"네 상황은 이거다: {short_situation}",
        f"현실을 보자. 지금 네 상황은 '{short_situation}'이다.",
        f"좋아. 네가 처한 상황은 '{short_situation}'이다.",
    ]

    closing_options = [
        "핑계는 내려놓고, 지금 바로 움직여라.",
        "생각은 여기까지. 이제 행동으로 증명해라.",
        "완벽한 순간은 없다. 지금 시작해라.",
        "오늘의 너를 바꾸는 건 오늘의 행동뿐이다.",
    ]

    # 약 4줄의 메시지
    message_lines = [
        random.choice(opening_options),
        problem,
        goal_line,
        action,
    ]

    # 마지막 문장은 강렬한 행동 촉구
    message_lines.append(random.choice(closing_options))

    return "\n\n".join(message_lines)


# =====================================
# 페이지 상단
# =====================================
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
    <div class="description">
        네 상황을 솔직하게 입력해라.<br>
        현실을 직시하고, 지금 할 수 있는 행동을 찾아라.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")


# =====================================
# 입력창
# =====================================
st.markdown(
    '<div class="section-title">01 / YOUR SITUATION</div>',
    unsafe_allow_html=True,
)

with st.form("situation_form"):
    situation = st.text_area(
        "지금 네 상황은?",
        placeholder=(
            "예: 내일 시험인데 공부를 거의 안 했다. "
            "휴대폰만 보면서 계속 미루고 있다."
        ),
        height=160,
        max_chars=1000,
    )

    goal = st.text_input(
        "이루고 싶은 목표 (선택)",
        placeholder="예: 수학 시험에서 90점 받기",
        max_chars=150,
    )

    submitted = st.form_submit_button(
        "ANALYZE MY SITUATION"
    )


# =====================================
# 결과 표시
# =====================================
if submitted:
    if not situation.strip():
        st.warning("먼저 네 상황부터 입력해라.")
    else:
        st.session_state["motivation_message"] = generate_message(
            situation,
            goal,
        )

if "motivation_message" in st.session_state:
    st.markdown("---")

    st.markdown(
        '<div class="section-title">02 / YOUR REALITY CHECK</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="quote-label">READ IT. OWN IT. DO IT.</div>',
        unsafe_allow_html=True,
    )

    # 사용자 입력이 HTML로 해석되지 않도록 안전하게 표시
    st.text(st.session_state["motivation_message"])

    st.markdown(
        """
        <div style="
            color:#888888;
            text-align:center;
            font-size:0.85rem;
            letter-spacing:2px;
            margin-top:1rem;
        ">
            NO MORE EXCUSES.
        </div>
        """,
        unsafe_allow_html=True,
    )


# =====================================
# 오늘의 명언
# =====================================
today_quote = QUOTES[date.today().toordinal() % len(QUOTES)]

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


# =====================================
# 하단
# =====================================
st.markdown(
    """
    <div class="footer">
        DISCIPLINE OVER MOTIVATION<br>
        CHAD MODE · BUILT FOR ACTION
    </div>
    """,
    unsafe_allow_html=True,
)
