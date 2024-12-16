import streamlit as st

st.title("간단한 계산기")

num1 = st.number_input("정수1를 입력해 주세요:", step=1.0, format="%.0f")
num2 = st.number_input("정수2를 입력해 주세요:", step=1.0, format="%.0f")

op = st.selectbox("연산자를 선택해 주세요.", ["+", "-", "*", "/"])

if st.button("계산하기"):
    try:
        if op == '+':
            result = num1 + num2
            st.success(f"{num1} + {num2} = {result}")
        elif op == '-':
            result = num1 - num2
            st.success(f"{num1} - {num2} = {result}")
        elif op == '*':
            result = num1 * num2
            st.success(f"{num1} * {num2} = {result}")
        elif op == '/':
            if num2 == 0:
                st.error("0으로 나눌 수 없습니다.")
            else:
                result = num1 / num2
                st.success(f"{num1} / {num2} = {result}")
    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")
