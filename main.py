import streamlit as st
import time

# 1. 페이지 설정
st.set_page_config(page_title="나의 인생 직업 찾기", page_icon="🚀", layout="centered")

# 2. 데이터 및 테마 설정
mbti_info = {
    "ISTJ": {"emoji": "🧐", "color": "#A6A6A6", "title": "청렴결백한 논리주의자", "jobs": ["회계사", "공무원", "데이터 분석가"], "strength": "책임감, 정확성"},
    "ISFJ": {"emoji": "🛡️", "color": "#94D2BD", "title": "용감한 수호자", "jobs": ["간호사", "초등교사", "상담가"], "strength": "인내심, 헌신"},
    "INFJ": {"emoji": "🔮", "color": "#B185DB", "title": "선의의 옹호자", "jobs": ["상담심리사", "작가", "예술가"], "strength": "통찰력, 공감"},
    "INTJ": {"emoji": "♟️", "color": "#5E548E", "title": "용의주도한 전략가", "jobs": ["SW 개발자", "전략 기획자", "교수"], "strength": "논리, 독립성"},
    "ISTP": {"emoji": "🛠️", "color": "#E9D8A6", "title": "만능 재주꾼", "jobs": ["엔지니어", "파일럿", "정비사"], "strength": "적응력, 손재주"},
    "ISFP": {"emoji": "🎨", "color": "#F4A261", "title": "호기심 많은 예술가", "jobs": ["디자이너", "작곡가", "사진작가"], "strength": "겸손, 예술적 감각"},
    "INFP": {"emoji": "🦋", "color": "#FFB703", "title": "열정적인 중재자", "jobs": ["작가", "심리치료사", "에디터"], "strength": "이상주의, 창의성"},
    "INTP": {"emoji": "💡", "color": "#48CAE4", "title": "논리적인 사색가", "jobs": ["물리학자", "프로그래머", "철학자"], "strength": "지적 호기심, 분석"},
    "ESTP": {"emoji": "🏃", "color": "#E76F51", "title": "모험을 즐기는 사업가", "jobs": ["기업가", "소방관", "마케터"], "strength": "활동성, 대담함"},
    "ESFP": {"emoji": "🎤", "color": "#F15BB5", "title": "자유로운 영혼의 연예인", "jobs": ["배우", "승무원", "파티 플래너"], "strength": "사교성, 에너지"},
    "ENFP": {"emoji": "🌟", "color": "#FFEE32", "title": "재기발랄한 활동가", "jobs": ["홍보 전문가", "카피라이터", "크리에이터"], "strength": "열정, 상상력"},
    "ENTP": {"emoji": "🗣️", "color": "#00BBF9", "title": "뜨거운 논쟁을 즐기는 변론가", "jobs": ["변호사", "발명가", "광고 디렉터"], "strength": "임기응변, 독창성"},
    "ESTJ": {"emoji": "📋", "color": "#264653", "title": "엄격한 관리자", "jobs": ["프로젝트 매니저", "법조인", "군 장교"], "strength": "조직 관리, 현실감"},
    "ESFJ": {"emoji": "🤝", "color": "#FFCAD4", "title": "사교적인 외교관", "jobs": ["호텔리어", "비서", "사회복지사"], "strength": "협동심, 봉사 정신"},
    "ENFJ": {"emoji": "📢", "color": "#FB5607", "title": "정의로운 사회운동가", "jobs": ["교사", "정치인", "코치"], "strength": "카리스마, 이타심"},
    "ENTJ": {"emoji": "👑", "color": "#8338EC", "title": "대담한 통솔자", "jobs": ["CEO", "경영 컨설턴트", "투자자"], "strength": "결단력, 추진력"}
}

# 3. 메인 화면 구성
st.markdown("<h1 style='text-align: center;'>✨ 인생 직업 MBTI 탐색기 ✨</h1>", unsafe_allow_html=True)
st.write("---")

# 사용자 입력부 (가운데 정렬 느낌을 위해 컬럼 활용)
left, mid, right = st.columns([1, 2, 1])
with mid:
    user_mbti = st.selectbox("당신의 MBTI는 무엇인가요?", ["선택하세요"] + list(mbti_info.keys()))

if user_mbti != "선택하세요":
    # 재미 요소: 로딩 바 추가
    with st.spinner('당신의 성향을 분석 중입니다...'):
        time.sleep(1)
    
    st.balloons() # 축하 풍선 효과!
    
    data = mbti_info[user_mbti]
    
    # 유형 카드 스타일 출력
    st.markdown(f"""
        <div style="background-color: {data['color']}; padding: 30px; border-radius: 20px; text-align: center; color: white;">
            <h1 style="font-size: 60px;">{data['emoji']}</h1>
            <h2 style="margin-bottom: 0;">{user_mbti}</h2>
            <h4 style="font-weight: 300;">{data['title']}</h4>
        </div>
    """, unsafe_allow_html=True)

    st.write("###") # 간격 띄우기

    # 상세 정보 2단 구성
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💪 핵심 강점")
        st.info(data['strength'])

    with col2:
        st.subheader("💼 추천 커리어")
        for job in data['jobs']:
            st.success(f"• {job}")

    # 재미 요소: 능력치 그래프 (랜덤인 듯 정교한 시각화)
    st.write("---")
    st.subheader(f"📊 {user_mbti} 유형 직무 역량 지표")
    
    # 예시 능력치 (유형에 따라 다르게 표현 가능)
    cols = st.columns(4)
    labels = ["창의성", "논리력", "친화력", "실행력"]
    import random
    for i, col in enumerate(cols):
        val = random.randint(70, 100)
        col.metric(labels[i], f"{val}%")
        col.progress(val / 100)

else:
    st.info("좌측 메뉴에서 MBTI를 선택해 주세요!")

# 하단 푸터
st.markdown("<br><br><p style='text-align: center; color: gray;'>© 2024 MBTI Career Finder | 재미로 보는 가이드입니다.</p>", unsafe_allow_html=True)
