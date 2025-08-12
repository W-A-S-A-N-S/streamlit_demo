# hello_streamlit.py
import streamlit as st

# 제목 추가
st.title("🎉 내 첫 번째 Streamlit 앱!")

# 텍스트 추가
st.write("안녕하세요! Streamlit으로 만든 웹 애플리케이션입니다.")

# 버튼 추가
if st.button("클릭해보세요!"):
    st.success("버튼이 클릭되었습니다! 🎊")
    st.balloons()

color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)

options = ["North", "East", "South", "West"]
selection = st.pills("Directions", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")
#실행방법
#streamlit run main.py