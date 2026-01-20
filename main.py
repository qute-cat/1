import streamlit as st
import time

# 1. 페이지 설정 및 커스텀 CSS
st.set_page_config(page_title="MBTI 커리어 마스터", page_icon="🎯", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stAlert { border-radius: 10px; }
    .mbti-card {
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. 16가지 유형 데이터 (샘플 데이터를 확장하여 구성)
mbti_db = {
    "INFJ": {
        "emoji": "🔮", "color": "#6B4E71", "title": "선의의 옹호자",
        "jobs": ["상담심리사", "작가", "환경 운동가"],
        "strength": "통찰력, 공감 능력, 강한 신념",
        "weakness": "완벽주의, 번아웃에 취약함, 비판에 민감",
        "confusing": "INFP (INFJ는 훨씬 계획적이고 구조적인 삶을 원합니다)",
        "best_mate": "ENTP, ENFP (아이디어를 현실로 바꿔줄 에너자이저)"
    },
    "ENTP": {
        "emoji": "🗣️", "color": "#3D5A80", "title": "뜨거운 논쟁을 즐기는 변론가",
        "jobs": ["변호사", "스타트업 창업가", "광고 디렉터"],
        "strength": "임기응변, 독창적 아이디어, 지적 호기심",
        "weakness": "뒷마무리 부족, 논쟁적인 태도, 반복 업무 혐오",
        "confusing": "ESTP (ENTP는 현실적인 이득보다 이론과 가능성에 집중합니다)",
        "best_mate": "INFJ, INTJ (번뜩이는 아이디어를 정리해 줄 전략가)"
    },
    "ISTJ": {
        "emoji": "📋", "color": "#4A4E69", "title": "청렴결백한 논리주의자",
        "jobs": ["회계사", "공무원", "법조인"],
        "strength": "철저한 준비성, 책임감, 정직함",
        "weakness": "변화에 대한 거부감, 고집이 강함, 융통성 부족",
        "confusing": "ISFJ (ISTJ는 감정보다 원칙과 논리를 우선시합니다)",
        "best_mate": "ESFP, ESTP (삶의 활력과 유연함을 불어넣어 줄 동료)"
    }
    # 나머지 13개 유형도 위와 같은 구조로 추가 가능합니다.
}

# 3. 메인 인터페이스
st.title("🎯 MBTI 직업 분석 리포트")
st.caption("성격 유형에 맞는 강점, 약점, 그리고 최고의 동료를 찾아보세요.")

selected_mbti = st.selectbox("본인의 MBTI를 선택하세요", ["유형 선택"] + sorted(list(mbti_db.keys())))

if selected_mbti != "유형 선택":
    data = mbti_db[selected_mbti]
    
    with st.spinner('성격 리포트를 생성 중...'):
        time.sleep(0.7)
    
    # 상단 메인 카드
    st.markdown(f"""
        <div class="mbti-card" style="background-color: {data['color']};">
            <h1 style="font-size: 80px; margin: 0;">{data['emoji']}</h1>
            <h2 style="margin: 0;">{selected_mbti}</h2>
            <p style="font-size: 1.2rem; opacity: 0.9;">{data['title']}</p>
        </div>
    """, unsafe_allow_html=True)

    # 섹션 1: 강점과 약점
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("✅ 강점")
        st.success(data['strength'])
    with col2:
        st.subheader("⚠️ 보완할 점")
        st.warning(data['weakness'])

    st.divider()

    # 섹션 2: 추천 직업 (이모지와 함께)
    st.subheader("💼 추천 커리어 매칭")
    cols = st.columns(3)
    for i, job in enumerate(data['jobs']):
        cols[i].info(f"**{job}**")

    # 섹션 3: 헷갈리는 유형 & 찰떡 동료
    st.write("###")
    c1, c2 = st.columns(2)
    
    with c1:
        with st.expander("🤔 헷갈리는 유형?", expanded=True):
            st.write(data['confusing'])
            
    with c2:
        with st.expander("🤝 찰떡궁합 동료", expanded=True):
            st.write(f"추천: **{data['best_mate']}**")

    # 마무리 효과
    st.balloons()

else:
    st.info("MBTI를 선택하면 맞춤형 분석 결과가 나타납니다.")
    # 초기 화면에 MBTI 4요소 지표 이미지 보여주기
    

st.sidebar.markdown("### 💡 활용 팁")
st.sidebar.write("1. 자신의 약점을 알고 보완책을 세워보세요.")
st.sidebar.write("2. 헷갈리는 유형과의 차이점을 통해 자기 이해를 높이세요.")
st.sidebar.write("3. 찰떡궁합 동료 유형과 협업할 때 시너지가 납니다.")
