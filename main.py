# hello_streamlit.py
import streamlit as st

# 색상 선택기를 테두리가 있는 박스 안에 배치
st.markdown("""
<div style="
    border: 3px solid #333; 
    border-radius: 10px; 
    padding: 20px; 
    background-color: white; 
    margin: 10px 0;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
">
""", unsafe_allow_html=True)

color = st.color_picker("배경색을 선택하세요", "#00f900")

st.markdown("</div>", unsafe_allow_html=True)

# 선택한 색으로 배경색 동적 변경
st.markdown(f"""
<style>
.stApp {{
    background-color: {color};
}}
</style>
""", unsafe_allow_html=True)

# 제목 추가
st.title("🎉 내 첫 번째 Streamlit 앱!")

# 텍스트 추가
st.write("안녕하세요! Streamlit으로 만든 웹 애플리케이션입니다.")

# 버튼 추가
if st.button("클릭해보세요!"):
    st.success("버튼이 클릭되었습니다! 🎊")
    st.balloons()

st.write(f"현재 배경색: {color}")

options = ["North", "East", "South", "West"]
selection = st.pills("Directions", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")

#실행방법
#streamlit run main.py