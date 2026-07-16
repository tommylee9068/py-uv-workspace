
import streamlit as st

# 사용자 입력 관련 기능 소개
st.title('튜토리얼 2: 입력 위젯')

# 문자열을 입력받을 수 있는 텍스트 필드 생성
name = st.text_input('이름을 입력하세요.')  

# 숫자를 입력받는 위젯 - 최소/최대값 범위 지정
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120)

# 드롭다운 형태로 항목 선택
hobby = st.selectbox("취미를 선택하세요", ["독서", "운동", "게임", "요리"])

# 체크박스 - True/False 값 반환
agree = st.checkbox("개인정보 수집에 동의합니다")

# 입력값이 유효하고 동의했다면 결과 메세지 출력
if name and agree:
    st.success(f'{name}님, {age}세 / 취미 : {hobby}')
