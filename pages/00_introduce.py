import streamlit as st
from PIL import Image

# 1. 페이지 설정
st.set_page_config(page_title="내 자기소개 페이지", page_icon="👋", layout="centered")

# 2. 사이드바 (연락처 정보 등)
st.sidebar.header("Contact Info")
st.sidebar.write("📧 Email: yourname@example.com")
st.sidebar.write("🔗 [LinkedIn](https://linkedin.com)")
st.sidebar.write("💻 [GitHub](https://github.com)")

# 3. 메인 섹션 - 사진과 타이틀
col1, col2 = st.columns([1, 2], gap="medium")

with col1:
    # 사진 파일이 없다면 샘플 이미지를 사용하거나 경로를 수정하세요.
    # st.image("profile.jpg", width=200) 
    st.image("https://via.placeholder.com/200", caption="내 프로필 사진")

with col2:
    st.title("안녕하세요, 홍길동입니다! 👋")
    st.write("새로운 기술을 배우고 문제를 해결하는 것을 좋아하는 개발자입니다.")

st.divider()

# 4. 상세 내용 (Tabs 사용)
tab1, tab2, tab3 = st.tabs(["내 소개", "기술 스택", "프로젝트"])

with tab1:
    st.subheader("About Me")
    st.write("""
    안녕하세요! 저는 데이터 시각화와 웹 개발에 관심이 많은 열정적인 학습자입니다. 
    Streamlit을 사용해 데이터 앱을 구축하는 것을 즐깁니다.
    - 📍 거주지: 대한민국 서울
    - 🎓 전공: 컴퓨터공학
    - 🌟 목표: 사용자에게 가치를 전달하는 서비스 만들기
    """)

with tab2:
    st.subheader("Technical Skills")
    st.write("**Languages:** Python, JavaScript, SQL")
    st.write("**Frameworks:** Streamlit, React, Flask")
    st.write("**Tools:** Git, Docker, AWS")
    
    # 숙련도 시각화 예시
    st.progress(90, text="Python 숙련도")
    st.progress(70, text="Streamlit 숙련도")

with tab3:
    st.subheader("Recent Projects")
    st.write("- **Personal Portfolio**: Streamlit을 활용한 자기소개 웹 제작")
    st.write("- **Data Dashboard**: 공공 데이터를 활용한 실시간 대시보드 구축")

# 5. 푸터 (Footer)
st.write("")
st.caption("© 2026 Your Name. Built with Streamlit.")
