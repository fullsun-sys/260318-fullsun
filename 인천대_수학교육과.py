import streamlit as st

# 사이드바 메뉴
menu = st.sidebar.selectbox("메뉴 선택", ["자기소개서", "목차"])

if menu == "자기소개서":
    st.set_page_config(page_title="자기소개서", page_icon="📄")

    st.title("📄 자기소개서")

    # 구분선
    st.divider()

    # 기본 정보 섹션
    st.subheader("✍️ 기본 정보")

    col1, col2 = st.columns(2)
    with col1:
        st.text_input("이름", placeholder="이름을 입력하세요")
    with col2:
        st.text_input("생년월일", placeholder="YYYY-MM-DD")

    col1, col2 = st.columns(2)
    with col1:
        st.text_input("전화번호", placeholder="010-XXXX-XXXX")
    with col2:
        st.text_input("이메일", placeholder="example@email.com")

    st.text_input("주소", placeholder="주소를 입력하세요", key="address")

    # 자기소개 섹션
    st.divider()
    st.subheader("🎯 자기소개")
    st.text_area(
        "자신에 대해 소개해주세요",
        placeholder="자신의 성격, 가치관, 삶의 목표 등을 작성하세요",
        height=150,
        key="intro"
    )

    # 경력/학력 섹션
    st.divider()
    st.subheader("🎓 경력 및 학력")

    st.write("**학력**")
    st.text_area(
        "학력을 입력하세요",
        placeholder="입학년도 ~ 졸업년도 | 학교명 | 전공 (각 항목마다 엔터로 구분)",
        height=100,
        key="education"
    )

    st.write("**경력**")
    st.text_area(
        "경력을 입력하세요",
        placeholder="입사년도 ~ 퇴사년도 | 회사명 | 직급/직무 (각 항목마다 엔터로 구분)",
        height=100,
        key="career"
    )

    # 경험 및 성과 섹션
    st.divider()
    st.subheader("⭐ 경험 및 성과")

    num_experiences = st.number_input(
        "경험/성과 항목 개수를 선택하세요",
        min_value=1,
        max_value=5,
        value=1
    )

    for i in range(num_experiences):
        with st.expander(f"경험/성과 항목 {i+1}"):
            st.text_input(f"제목 {i+1}", placeholder="제목을 입력하세요", key=f"exp_title_{i}")
            st.text_area(
                f"설명 {i+1}",
                placeholder="상세 내용을 입력하세요",
                height=100,
                key=f"exp_desc_{i}"
            )
            st.text_input(f"기간 {i+1}", placeholder="YYYY.MM ~ YYYY.MM", key=f"exp_period_{i}")

    # 기술/역량 섹션
    st.divider()
    st.subheader("💻 기술 및 역량")
    st.text_area(
        "보유한 기술 및 역량을 입력하세요",
        placeholder="기술스택, 언어능력, 자격증 등 (각 항목마다 쉼표(,)로 구분)",
        height=100,
        key="skills"
    )

    # 마지막 메시지
    st.divider()
    st.info("작성 내용을 정리하고 검토한 후 제출하세요.")

elif menu == "목차":
    st.title("중학교 수학 수업 목차")

    st.markdown("""
    ## 1단원: 실수와 그 연산
    - 제곱근과 실수
    - 근호를 포함한 식의 계산

    ## 2단원: 식의 계산
    - 다항식의 곱셈
    - 다항식의 인수분해

    ## 3단원: 이차방정식
    - 이차방정식과 그 풀이
    - 이차방정식의 활용
    """)

    # 여기에 추가적인 목차 항목이나 기능을 넣을 수 있습니다.
