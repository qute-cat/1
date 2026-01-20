import streamlit as st
import time

# 1. 페이지 설정
st.set_page_config(page_title="MBTI 커리어 탐색기", page_icon="🧪", layout="centered")

# 2. 데이터베이스 (16개 전 유형)
mbti_db = {
    "ISTJ": {"emoji": "📋", "color": "#4A4E69", "title": "청렴결백한 논리주의자", "jobs": ["회계사", "공무원", "법조인"], "strength": "철저함, 정직함", "weakness": "변화 거부, 융통성 부족", "confusing": "ISFJ (ISTJ는 감정보다 원칙을 우선시합니다)", "best_mate": "ESFP, ESTP"},
    "ISFJ": {"emoji": "🛡️", "color": "#94D2BD", "title": "용감한 수호자", "jobs": ["간호사", "초등교사", "사서"], "strength": "인내심, 헌신적", "weakness": "과도한 자기희생, 변화 두려움", "confusing": "ISTJ (ISFJ는 사람의 감정과 필요를 먼저 읽습니다)", "best_mate": "ESFP, ESTP"},
    "INFJ": {"emoji": "🔮", "color": "#6B4E71", "title": "선의의 옹호자", "jobs": ["심리상담사", "작가", "인사팀"], "strength": "통찰력, 공감 능력", "weakness": "완벽주의, 번아웃 취약", "confusing": "INFP (INFJ는 계획적이고 구조적인 삶을 원함)", "best_mate": "ENTP, ENFP"},
    "INTJ": {"emoji": "♟️", "color": "#5E548E", "title": "용의주도한 전략가", "jobs": ["전략 기획자", "데이터 과학자", "교수"], "strength": "논리적 사고, 독립성", "weakness": "오만함, 타인 감정에 무심함", "confusing": "INTP (INTJ는 실행과 결과를 중시합니다)", "best_mate": "ENFP, ENTP"},
    "ISTP": {"emoji": "🛠️", "color": "#E9D8A6", "title": "만능 재주꾼", "jobs": ["엔지니어", "파일럿", "정비사"], "strength": "적응력, 분석력", "weakness": "위험 감수, 감정 표현 서투름", "confusing": "ISFP (ISTP는 기술적 작동 원리에 집중합니다)", "best_mate": "ESFJ, ESTJ"},
    "ISFP": {"emoji": "🎨", "color": "#F4A261", "title": "호기심 많은 예술가", "jobs": ["디자이너", "사진작가", "수의사"], "strength": "미적 감각, 온화함", "weakness": "우유부단함, 미래 계획 부족", "confusing": "INFP (ISFP는 현실의 감각에 더 충실합니다)", "best_mate": "ESFJ, ESTJ"},
    "INFP": {"emoji": "🦋", "color": "#FFB703", "title": "열정적인 중재자", "jobs": ["작가", "예술가", "에디터"], "strength": "창의성, 공감 능력", "weakness": "현실감 부족, 비판에 상처받음", "confusing": "INFJ (INFP는 계획보다 영감을 따릅니다)", "best_mate": "ENFJ, ENTJ"},
    "INTP": {"emoji": "💡", "color": "#48CAE4", "title": "논리적인 사색가", "jobs": ["프로그래머", "물리학자", "경제학자"], "strength": "지적 호기심, 분석력", "weakness": "관습 무시, 실행력 부족", "confusing": "INTJ (INTP는 결론보다 질문을 즐깁니다)", "best_mate": "ENTJ, ENFJ"},
    "ESTP": {"emoji": "🏃", "color": "#E76F51", "title": "모험을 즐기는 사업가", "jobs": ["영업사원", "소방관", "펀드매니저"], "strength": "대담함, 현실 감각", "weakness": "충동적 성향, 규칙 무시", "confusing": "ENTP (ESTP는 이론보다 행동을 즐깁니다)", "best_mate": "ISFJ, ISTJ"},
    "ESFP": {"emoji": "🎤", "color": "#F15BB5", "title": "자유로운 영혼의 연예인", "jobs": ["배우", "이벤트 플래너", "승무원"], "strength": "사교성, 낙천적", "weakness": "집중력 부족, 계획성 없음", "confusing": "ENFP (ESFP는 눈앞의 현실에 집중합니다)", "best_mate": "ISFJ, ISTJ"},
    "ENFP": {"emoji": "🌟", "color": "#FFEE32", "title": "재기발랄한 활동가", "jobs": ["마케터", "홍보 전문가", "상담가"], "strength": "열정, 친화력", "weakness": "반복 업무 취약, 감정 기복", "confusing": "ESFP (ENFP는 깊은 의미와 가능성을 찾습니다)", "best_mate": "INTJ, INFJ"},
    "ENTP": {"emoji": "🗣️", "color": "#00BBF9", "title": "뜨거운 논쟁을 즐기는 변론가", "jobs": ["변호사", "발명가", "기획자"], "strength": "두뇌 회전, 임기응변", "weakness": "마무리 부족, 타인 기분 간과", "confusing": "ENTJ (ENTP는 조직 관리보다 아이디어를 즐김)", "best_mate": "INFJ, INTJ"},
    "ESTJ": {"emoji": "📋", "color": "#264653", "title": "엄격한 관리자", "jobs": ["경영자", "경찰관", "PM"], "strength": "조직 관리력, 질서", "weakness": "독단적 성향, 공감 부족", "confusing": "ENTJ (ESTJ는 검증된 매뉴얼을 중시합니다)", "best_mate": "ISFP, ISTP"},
    "ESFJ": {"emoji": "🤝", "color": "#FFCAD4", "title": "사교적인 외교관", "jobs": ["호텔리어", "초등교사", "비서"], "strength": "협동심, 봉사 정신", "weakness": "타인 시선 의식, 변화 소극적", "confusing": "ENFJ (ESFJ는 공동체의 전통을 중시합니다)", "best_mate": "ISFP, ISTP"},
    "ENFJ": {"emoji": "📢", "color": "#FB5607", "title": "정의로운 사회운동가", "jobs": ["교사", "정치 리더", "코치"], "strength": "리더십, 이타심", "weakness": "과도한 감정 몰입, 비판 예민", "confusing": "ESFJ (ENFJ는 사회적 비전을 꿈꿉니다)", "best_mate": "INFP, INTP"},
    "ENTJ": {"emoji": "👑", "color": "#8338EC", "title": "대담한 통솔자", "jobs": ["CEO", "전략 컨설턴트", "투자자"], "strength": "결단력, 효율성", "weakness": "지배적 태도, 감정 무시", "confusing": "ESTJ (ENTJ는 혁신적인 시스템을 선호합니다)", "best_mate": "INTP, INFP"}
}

# 3. 테스트 문항 설정
questions = [
    {"q": "새로운 사람들을 만나는 모임에서...", "a": "에너지를 얻는다 (E)", "b": "혼자만의 시간이 필요하다 (I)", "type": "EI"},
    {"q": "나는 업무를 할 때 주로...", "a": "전체적인 숲과 가능성을 본다 (N)", "b": "현재의 구체적인 사실에 집중한다 (S)", "type": "SN"},
    {"q": "결정을 내릴 때 나는...", "a": "논리와 객관적인 분석이 우선이다 (T)", "b": "사람들의 감정과 조화를 고려한다 (F)", "type": "TF"},
    {"q": "여행 계획을 세울 때...", "a": "시간 단위로 꼼꼼하게 계획한다 (J)", "b": "상황에 따라 유연하게 움직인다 (P)", "type": "JP"},
    # 문항을 더 늘리면 정확도가 올라갑니다 (여기선 예시로 4개만 상세히 구현)
]

# 4. 세션 상태 초기화
if 'mbti_scores' not in st.session_state:
    st.session_state.mbti_scores = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'result_mbti' not in st.session_state:
    st.session_state.result_mbti = None

# 5. 메인 함수
def main():
    st.title("🧪 MBTI 정밀 커리어 매칭")
    
    # 사이드바: 바로 조회하기 기능
    st.sidebar.title("🔍 유형 바로 조회")
    quick_find = st.sidebar.selectbox("MBTI를 이미 알고 계신가요?", ["선택"] + sorted(list(mbti_db.keys())))
    if quick_find != "선택":
        st.session_state.result_mbti = quick_find

    # 메인 컨텐츠 영역
    if st.session_state.result_mbti is None:
        show_test()
    else:
        show_result(st.session_state.result_mbti)
        if st.button("다시 테스트하기"):
            st.session_state.step = 0
            st.session_state.result_mbti = None
            st.session_state.mbti_scores = {k: 0 for k in st.session_state.mbti_scores}
            st.rerun()

def show_test():
    progress = (st.session_state.step) / len(questions)
    st.progress(progress)
    
    if st.session_state.step < len(questions):
        item = questions[st.session_state.step]
        st.subheader(f"Q{st.session_state.step + 1}. {item['q']}")
        
        col1, col2 = st.columns(2)
        if col1.button(item['a']):
            type_char = item['a'][-2] # (E), (N) 등에서 알파벳 추출
            st.session_state.mbti_scores[type_char] += 1
            st.session_state.step += 1
            st.rerun()
            
        if col2.button(item['b']):
            type_char = item['b'][-2]
            st.session_state.mbti_scores[type_char] += 1
            st.session_state.step += 1
            st.rerun()
    else:
        # 결과 계산
        s = st.session_state.mbti_scores
        res = ""
        res += "E" if s['E'] >= s['I'] else "I"
        res += "N" if s['N'] >= s['S'] else "S"
        res += "T" if s['T'] >= s['F'] else "F"
        res += "J" if s['J'] >= s['P'] else "P"
        st.session_state.result_mbti = res
        st.rerun()

def show_result(mbti):
    data = mbti_db[mbti]
    st.balloons()
    
    # 헤더 카드
    st.markdown(f"""
        <div style="background-color: {data['color']}; padding: 40px; border-radius: 20px; text-align: center; color: white;">
            <h1 style="font-size: 70px; margin:0;">{data['emoji']}</h1>
            <h2 style="margin:0;">당신의 유형은 {mbti}</h2>
            <p style="font-size: 1.3rem; opacity: 0.9;">{data['title']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("###")
    
    # 상세 리포트
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("💪 강점")
        st.success(data['strength'])
    with c2:
        st.subheader("⚠️ 보완할 점")
        st.warning(data['weakness'])
        
    st.divider()
    
    st.subheader(f"💼 {mbti}에게 추천하는 직업")
    cols = st.columns(3)
    for i, job in enumerate(data['jobs']):
        cols[i].info(f"**{job}**")
        
    st.write("###")
    
    # 헷갈리는 유형 및 동료
    col_a, col_b = st.columns(2)
    with col_a:
        with st.expander("🤔 이 유형과 헷갈리시나요?", expanded=True):
            st.write(data['confusing'])
    with col_b:
        with st.expander("🤝 환상의 팀워크 동료", expanded=True):
            st.write(f"추천: **{data['best_mate']}**")

if __name__ == "__main__":
    main()
