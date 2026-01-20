import streamlit as st
import time

# 1. 페이지 설정
st.set_page_config(page_title="MBTI 커리어 가이드", page_icon="🕵️", layout="centered")

# 2. 고도화된 데이터 설정
mbti_info = {
    "INFJ": {
        "emoji": "🔮", "color": "#B185DB", "title": "선의의 옹호자", 
        "jobs": ["상담심리사", "작가", "인사팀(HR)"], 
        "strength": "깊은 통찰력, 뛰어난 공감 능력, 도덕적 관념",
        "weakness": "완벽주의 성향, 비판에 민감함, 쉽게 지칠 수 있음(번아웃)",
        "confusing": "INFP (둘 다 감성적이지만, INFJ는 훨씬 계획적입니다!)"
    },
    "INTJ": {
        "emoji": "♟️", "color": "#5E548E", "title": "용의주도한 전략가", 
        "jobs": ["SW 개발자", "전략 기획자", "데이터 분석가"], 
        "strength": "전략적 사고, 독립적 추진력, 높은 효율성",
        "weakness": "지나치게 분석적임, 타인의 감정에 무심할 수 있음",
        "confusing": "INTP (둘 다 똑똑하지만, INTJ는 실행과 결과를 중시합니다!)"
    },
    "ENFP": {
        "emoji": "🌟", "color": "#FFEE32", "title": "재기발랄한 활동가", 
        "jobs": ["마케터", "크리에이터", "이벤트 기획자"], 
        "strength": "밝은 에너지, 무궁무진한 상상력, 소통 능력",
        "weakness": "반복 업무에 쉽게 질림, 마무리가 다소 부족함",
        "confusing": "ENTP (둘 다 에너지가 넘치지만, ENFP는 가치와 감정을 더 중시합니다!)"
    },
    "ENTP": {
        "emoji": "🗣️", "color": "#00BBF9", "title": "뜨거운 논쟁을 즐기는 변론가", 
        "jobs": ["변호사", "광고 디렉터", "스타트업 창업가"], 
        "strength": "임기응변, 고정관념 타파, 지적 호기심",
        "weakness": "논쟁을 지나치게 즐김, 세부 사항 처리에 약함",
        "confusing": "ESTP (둘 다 활동적이지만, ENTP는 추상적인 아이디어에 더 끌립니다!)"
    },
    # ... 다른 유형들도 동일한 구조로 데이터를 채울 수 있습니다.
}

# (데이터가 길어지므로 예시로 4개 유형만 상세히 넣었습니다. 실제 운영 시 위와 같은 포맷으로 16개를 채우면 됩니다.)

# 3. 메인 화면 구성
st.markdown("<h1 style='text-align: center;'>🕵️ MBTI 커리어 심층 분석</h1>", unsafe_allow_html=True)
st.write("---")

left, mid, right = st.columns([1, 2, 1])
with mid:
    user_mbti = st.selectbox("당신의 MBTI를 선택해 보세요", ["선택하세요"] + sorted(list(mbti_info.keys())))

if user_mbti != "선택하세요":
    with st.spinner('당신의 잠재력과 그림자를 분석 중입니다...'):
        time.sleep(0.8)
    
    st.snow() # 겨울 느낌의 눈 내리는 효과 (선택사항)
    
    data = mbti_info[user_mbti]
    
    # 유형 카드 메인
    st.markdown(f"""
        <div style="background-color: {data['color']}; padding: 30px; border-radius: 20px; text-align: center; color: white;">
            <h1 style="font-size: 50px;">{data['emoji']}</h1>
            <h2 style="margin-bottom: 0;">{user_mbti}</h2>
            <h4 style="font-weight: 300;">{data['title']}</h4>
        </div>
    """, unsafe_allow_html=True)

    st.write("###")

    # 1단: 강점과 약점 (비교)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("💪 강점 (Power)")
        st.success(data['strength'])
    with col2:
        st.subheader("⚠️ 약점 (Warning)")
        st.warning(data['weakness'])

    # 2단: 추천 직업
    st.write("---")
    st.subheader(f"💼 {user_mbti}를 위한 추천 커리어")
    job_cols = st.columns(len(data['jobs']))
    for i, job in enumerate(data['jobs']):
        job_cols[i].info(f"**{job}**")

    # 3단: 재미있는 추가 정보 (헷갈리는 유형)
    st.write("###")
    with st.expander("🤔 혹시 이 유형과 헷갈리시나요?"):
        st.write(f"**{user_mbti}** 유형은 종종 **{data['confusing']}**")
        st.write("결정적인 차이는 '판단 기준'이나 '에너지 활용 방식'에 있습니다!")

    # 4단: 역량 수치
    st.write("---")
    st.subheader("📊 핵심 직무 역량")
    c1, c2, c3 = st.columns(3)
    c1.metric("창의성", "High")
    c2.metric("분석력", "Very High")
    c3.metric("협업 능력", "Medium")

else:
    st.info("MBTI 유형을 선택하면 상세 분석 리포트가 나타납니다.")

st.markdown("<br><p style='text-align: center; color: gray;'>여러분의 강점은 키우고 약점은 보완하여 최고의 커리어를 쌓으세요!</p>", unsafe_allow_html=True)
