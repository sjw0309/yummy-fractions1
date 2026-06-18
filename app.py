import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 1. 페이지 기본 설정 및 디자인 (CSS)
st.set_page_config(page_title="맛있는 분수 여행", page_icon="🍕", layout="centered")

st.markdown("""
    <style>
    .main-title { font-size: 32px; font-weight: bold; color: #E63946; text-align: center; margin-bottom: 5px; }
    .sub-title { font-size: 18px; color: #4A4A4A; text-align: center; margin-bottom: 25px; }
    .section-box { background-color: #F8F9FA; padding: 20px; border-radius: 10px; border-left: 5px solid #E63946; margin-bottom: 20px; }
    .quiz-box { background-color: #FFF3CD; padding: 20px; border-radius: 10px; border: 1px solid #FFEBAA; margin-top: 20px; }
    .fraction-text { font-size: 24px; font-weight: bold; color: #1D3557; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# 앱 타이틀 및 소개 
st.markdown("<div class='main-title'>🍕 초콜릿과 피자로 나누는 맛있는 분수 여행 🍫</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>슬라이더를 움직이고 칸을 채우며 분수를 직관적으로 배워봐요!</div>", unsafe_allow_html=True)

# 사이드바: 모드 선택 (피자 vs 초콜릿) 
st.sidebar.header("🎨 학습 모드 선택")
mode = st.sidebar.radio("원하는 구체물을 선택하세요:", ["🍕 피자 (원형)", "🍫 초콜릿 (직사각형)"])

# ---------------------------------------------------------
# [활동 1 & 2 & 3] 개념 학습 영역
# ---------------------------------------------------------
st.markdown(f"### 📍 탐구 활동: {mode} 조각내고 색칠하기")

if "🍕 피자" in mode:
    st.markdown("<div class='section-box'><b>[활동 1 & 2]</b> 피자를 똑같이 나누고, 원하는 조각만큼 선택해보세요.</div>", unsafe_allow_html=True) # [cite: 13, 17]
    
    # 입력 컨트롤: 등분할(분모)과 선택 조각 수(분자) [cite: 14, 17]
    col1, col2 = st.columns(2)
    with col1:
        total_slices = st.slider("피자를 몇 조각으로 똑같이 나눌까요? (분모)", min_value=2, max_value=12, value=4, step=1) # [cite: 14]
    with col2:
        selected_slices = st.slider("그 중 몇 조각을 먹을까요? (분자)", min_value=0, max_value=total_slices, value=3, step=1) # 

    # Matplotlib를 이용한 피자(원형 연속량) 시각화 [cite: 36]
    fig, ax = plt.subplots(figsize=(5, 5))
    
    # 기본 피자 테두리 및 배경색
    wedges, texts = ax.pie(
        [1]*total_slices, 
        colors=['#FFFFFF']*total_slices, 
        wedgeprops=dict(edgecolor='#D3D3D3', linewidth=2, antialiased=True),
        startangle=90
    )
    
    # 선택된 조각 색칠하기 
    for i in range(selected_slices):
        wedges[i].set_facecolor('#FFB703') # 맛있는 피자 치즈 색상
        wedges[i].set_edgecolor('#E63946')
        wedges[i].set_linewidth(2.5)

    ax.set_aspect('equal')
    plt.title(f"전체를 똑같이 {total_slices}로 나눈 것 중의 {selected_slices}", fontsize=12, pad=10)
    st.pyplot(fig)

else:
    st.markdown("<div class='section-box'><b>[활동 3]</b> 직사각형 모양의 초콜릿도 똑같은 원리로 분수를 표현할 수 있어요!</div>", unsafe_allow_html=True) # [cite: 21, 24]
    
    col1, col2 = st.columns(2)
    with col1:
        total_slices = st.slider("초콜릿을 몇 칸으로 똑같이 나눌까요? (분모)", min_value=2, max_value=12, value=6, step=1) # [cite: 22]
    with col2:
        selected_slices = st.slider("그 중 몇 칸을 색칠할까요? (분자)", min_value=0, max_value=total_slices, value=2, step=1) # [cite: 22]

    # Matplotlib를 이용한 초콜릿(직사각형 연속량) 시각화 [cite: 21, 24]
    fig, ax = plt.subplots(figsize=(6, 2))
    
    # 초콜릿 칸 그리기 [cite: 22]
    for i in range(total_slices):
        facecolor = '#8B4513' if i < selected_slices else '#FFFFFF' # 초콜릿 갈색
        edgecolor = '#4A2711' if i < selected_slices else '#D3D3D3'
        linewidth = 2.5 if i < selected_slices else 1.5
        
        rect = plt.Rectangle((i, 0), 1, 1, facecolor=facecolor, edgecolor=edgecolor, linewidth=linewidth)
        ax.add_patch(rect)
        
    ax.set_xlim(0, total_slices)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.title(f"전체를 똑같이 {total_slices}로 나눈 것 중의 {selected_slices}", fontsize=12, pad=10)
    st.pyplot(fig)

# ---------------------------------------------------------
# 개념 형식화 출력 (일상 언어 -> 수학 기호) [cite: 4]
# ---------------------------------------------------------
st.markdown("---")
st.markdown("### 🧮 수학 기호로 약속하기") # 

if total_slices > 0:
    # 일상적 표현과 수학적 표현 매핑 [cite: 4]
    st.markdown(f"<div class='fraction-text'>💬 말로 표현하면: \"{total_slices}개 중의 {selected_slices}개\"</div>", unsafe_allow_html=True) # [cite: 18]
    
    # LaTeX를 활용한 정밀한 분수 표현 수식 렌더링
    st.write("")
    st.markdown("<p style='text-align:center; font-size:16px; color:#666;'>수학 기호로는 아래와 같이 써요!</p>", unsafe_allow_html=True)
    st.markdown(f"$$ \\frac{{{selected_slices}}}{{{total_slices}}} $$")
    st.markdown(f"<p style='text-align:center; font-size:20px; font-weight:bold; color:#E63946;'>읽기: {total_slices}분의 {selected_slices}</p>", unsafe_allow_html=True) # [cite: 18]

    # 분모와 분자 개념 설명 (비유법 적용) [cite: 19, 20]
    with st.expander("💡 '분모'와 '분자'의 이름이 헷갈리나요?"):
        st.markdown(f"""
        * **밑에 있는 수 ({total_slices}) = 분모(分母):** 전체 조각 수를 뜻해요. 엄마(**母**)가 아들을 업고 있는 것처럼 아래에 있어요! [cite: 19, 20]
        * **위에 있는 수 ({selected_slices}) = 분자(分子):** 내가 선택한 부분의 조각 수를 뜻해요. 엄마 위에 업혀 있는 아들(**子**) 수랍니다! [cite: 19, 20]
        """)

# ---------------------------------------------------------
# [정리하기] 형성평가 간이 퀴즈 기능 
# ---------------------------------------------------------
st.markdown("---")
st.markdown("### ✍️ 오늘 배운 내용 도전! 미니 퀴즈") # 

st.markdown("<div class='quiz-box'><b>문제:</b> 영희는 초콜릿 1판을 똑같이 <b>8칸</b>으로 나눈 뒤, 그 중 <b>5칸</b>을 먹었습니다. 영희가 먹은 초콜릿은 전체의 얼마일까요?</div>", unsafe_allow_html=True)

# 학생 인터랙션을 위한 라디오 버튼 퀴즈
quiz_answer = st.radio(
    "정답을 고르세요:",
    ["1) 8분의 8", "2) 5분의 8", "3) 8분의 5", "4) 3분의 5"],
    index=None,
    placeholder="여기를 눌러 정답을 골라보세요."
)

if quiz_answer:
    if "3) 8분의 5" in quiz_answer:
        st.success("🎉 정답입니다! 전체 8칸(분모) 중 5칸(분자)이므로 5/8 (8분의 5)가 됩니다! 아주 훌륭해요! 👍")
    else:
        st.error("❌ 다시 한 번 생각해볼까요? 전체 조각 수가 '분모(아래)', 먹은 조각 수가 '분자(위)'로 가야 해요!")

# 하단 푸터 (수업 정보) [cite: 1]
st.markdown("<br><br><p style='text-align:center; color:#A0A0A0; font-size:12px;'>현대수학의 융합적 이해 기말과제 | 음악교육과 신정우</p>", unsafe_allow_html=True)
