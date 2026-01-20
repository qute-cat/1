import streamlit as st
import pandas as pd

# 1. 데이터 설정
mbti_data = {
    "ISTJ": {"title": "청렴결백한 논리주의자", "jobs": "회계사, 공무원, 군인, 감사관", "desc": "철저하고 규칙을 준수하며 사실에 근거해 사고합니다."},
    "ISFJ": {"title": "용감한 수호자", "jobs": "간호사, 초등교사, 사회복지사, 사서", "desc": "타인을 돕는 것에 보람을 느끼며 책임감이 강합니다."},
    "INFJ": {"title": "선의의 옹호자", "jobs": "상담심리사, 작가, 교수, 인사팀(HR)", "desc": "통찰력이 뛰어나고 사람들에게 영감을 주는 일을 선호합니다."},
    "INTJ": {"title": "용의주도한 전략가", "jobs": "SW 개발자, 전략 기획자, 과학자", "desc": "분석적이고 독립적이며 복잡한 문제를 해결하는 것을 즐깁니다."},
    "ISTP": {"title": "만능 재주꾼", "jobs": "엔지니어, 파일럿, 경찰관, 시스템 분석가", "desc": "객관적이고 합리적이며 도구를 다루는 실용적인 일에 능합니다."},
    "ISFP": {"title": "호기심 많은 예술가", "jobs": "디자이너, 사진작가, 수의사, 플로리스트", "desc": "말없이 다정하며 현재의 삶을 즐기고 미적 감각이 뛰어납니다."},
    "INFP": {"title": "열정적인 중재자", "jobs": "작가, 심리치료사, 콘텐츠 크리에이터", "desc": "자신만의 가치를 중시하며 공감 능력이 뛰어나고 창의적입니다."},
    "INTP": {"title": "논리적인 사색가", "jobs": "대학교수, 프로그래머, 물리학자, 경제학자", "desc": "아이디어와 이론에 관심이 많으며 비평적인 관점을 가졌습니다."},
    "ESTP": {"title": "모험을 즐기는 사업가", "jobs": "영업사원, 소방관, 기업가, 스포츠 매니저", "desc": "활동적이고 직설적이며 문제 상황에서 빠른 대처 능력을 보입니다."},
    "ESFP": {"title": "자유로운 영혼의 연예인", "jobs": "배우, 이벤트 플래너, 홍보 전문가, 승무원", "desc": "사교적이고 낙천적이며 사람들과 함께하는 분위기를 주도합니다."},
    "ENFP": {"title": "재기발랄한 활동가", "jobs": "마케터, 저널리스트, 카피라이터, 파티 플래너", "desc": "열정적이고 상상력이 풍부하며 새로운 가능성을 찾아냅니다."},
    "ENTP": {"title": "뜨거운 논쟁을 즐기는 변론가", "jobs": "변호사, 정치인, 발명가, 광고 감독", "desc": "지적인 도전 정신이 강하며 새로운 아이디어를 제안하는 데 능합니다."},
    "ESTJ": {"title": "엄격한 관리자", "jobs": "경영자, 법조인, 프로젝트 매니저, 군 장교", "desc": "체계적이고 현실적이며 조직을 관리하고 이끄는 데 탁월합니다."},
    "ESFJ": {"title": "사교적인 외교관", "jobs": "교사, 홍보 담당자, 호텔리어, 고객 서비스", "desc": "협동을 중시하며 타인의 요구에 민감하게 반응하고 조화를 이룹니다."},
    "ENFJ": {"title": "정의로운 사회운동가", "jobs": "커리어 코치, 정치 리더, 시민단체 활동가", "desc": "타인의 성장을 돕는 리더십이 있으며 사교성이 매우 좋습니다."},
    "ENTJ": {"title": "대담한 통솔자", "jobs": "CEO, 경영 컨설턴트, 벤처 캐피탈리스트", "desc": "장기적인 계획 수립에 능하며 효율적이고 결단력이 있습니다."}
}

# 2. 웹 앱 UI 구성
st.set_page_config(page_title="MBTI 직업 추천 서비스", page_icon="💼")

st.title("💼 MBTI 유형별 맞춤 직업 추천")
st.write("자신의 MBTI를 선택하고 어울리는 직업군을 확인해 보세요!")

# 사이드바에서 선택
selected_mbti = st.selectbox("당신의 MBTI 유형은 무엇인가요?", list(mbti_data.keys()))

if selected_mbti:
    info = mbti_data[selected_mbti]
    
    st.divider()
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader(f"✨ {selected_mbti}")
        st.caption(info['title'])
        
    with col2:
        st.info(f"**💡 특징:** {info['desc']}")
        st.success(f"**🎯 추천 직업:** {info['jobs']}")

    # 3. 간단한 성향 시각화 (임의 데이터)
    st.write("### 📊 유형별 성향 분포 (예시)")
    mbti_chars = list(selected_mbti)
    chart_data = pd.DataFrame({
        '지표': ['E/I', 'S/N', 'T/F', 'J/P'],
        '강도': [70, 80, 60, 90] # 실제 데이터는 아니며 시각화 용도입니다.
    })
    st.bar_chart(chart_data.set_index('지표'))

st.sidebar.title("About")
st.sidebar.info("이 앱은 MBTI 성격 유형에 기초한 일반적인 직업 성향을 보여줍니다. 실제 직업 선택 시 참고용으로만 활용하세요!")
