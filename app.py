import streamlit as st
import pandas as pd

# -------------- 페이지 설정 --------------
# Streamlit 페이지의 기본 설정을 합니다
# layout="wide"는 페이지를 전체 화면 너비로 설정합니다
st.set_page_config(page_title="테이블 데이터 수정 예제", layout="wide")

# -------------- 제목 섹션 --------------
st.title("테이블 데이터 수정 예제")

# -------------- 상단 컨트롤 섹션 --------------
# columns()를 사용하여 화면을 여러 열로 나눕니다
# [5, 0.1, 1]은 각 열의 상대적 너비를 나타냅니다
col1, col2, col3 = st.columns([5, 0.1, 1])

with col1:
    # toggle()은 켜고 끌 수 있는 스위치를 만듭니다
    # 반환값은 True/False입니다
    edit_mode = st.toggle("편집 모드")

# 편집 모드일 때만 저장 버튼을 표시합니다
save_button = False
if edit_mode:
    with col3:
        # button()은 클릭할 수 있는 버튼을 만듭니다
        # type="primary"는 버튼을 강조 표시합니다
        save_button = st.button(
            "저장하기",
            type="primary",
            use_container_width=True,  # 버튼을 열 너비에 맞춥니다
        )

# -------------- 데이터 로드 섹션 --------------
# CSV 파일 읽기를 시도합니다
try:
    df = pd.read_csv("research_projects.csv")
except FileNotFoundError:
    # 파일이 없으면 에러 메시지를 표시하고 앱을 중단합니다
    st.error(
        "research_projects.csv 파일이 없습니다. generate_data.py를 먼저 실행해주세요."
    )
    st.stop()

# -------------- 상태 관리 섹션 --------------
# session_state는 페이지가 다시 로드되어도 데이터를 유지합니다
# 웹 앱의 '상태'를 관리하는 중요한 기능입니다
if "df" not in st.session_state:
    st.session_state.df = df.copy()

# -------------- 메인 화면 섹션 --------------
# 편집 모드일 때 경고 메시지를 표시합니다
if edit_mode:
    st.warning("주의: 변경사항을 저장하지 않으면 수정한 내용이 사라집니다!")

# 편집 모드에 따라 다른 형태의 테이블을 표시합니다
if edit_mode:
    # data_editor는 수정 가능한 테이블을 만듭니다
    # pandas DataFrame을 입력으로 받아 수정된 DataFrame을 반환합니다
    edited_df = st.data_editor(
        st.session_state.df,
        num_rows="dynamic",  # 행 추가/삭제 가능
        use_container_width=True,  # 전체 너비 사용
        height=600,  # 테이블 높이 설정
        hide_index=False,  # 행 번호 표시
    )

    # 테이블 데이터가 변경되었는지 확인합니다
    if not edited_df.equals(st.session_state.df):
        st.session_state.df = edited_df.copy()

    # 저장 버튼이 클릭되면 CSV 파일로 저장합니다
    if save_button:
        edited_df.to_csv("research_projects.csv", index=False)
        # toast()는 화면 상단에 잠시 나타났다 사라지는 알림을 표시합니다
        st.toast("저장되었습니다! 🎉")

else:
    # 편집 모드가 아닐 때는 읽기 전용 테이블을 표시합니다
    st.dataframe(
        st.session_state.df,
        use_container_width=True,
        height=600,
        hide_index=False,  # 행 번호 표시
    )
