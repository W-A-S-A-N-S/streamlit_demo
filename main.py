# hello_streamlit.py
import streamlit as st

# 보색 계산 함수
def get_complementary_color(hex_color):
    # # 제거하고 RGB 값 추출
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    
    # 보색 계산 (255에서 빼기)
    comp_r = 255 - r
    comp_g = 255 - g
    comp_b = 255 - b
    
    # 다시 헥스 코드로 변환
    return f"#{comp_r:02x}{comp_g:02x}{comp_b:02x}"

# 색상 선택기
color = st.color_picker("배경색을 선택하세요", "#434D52")

# 선택된 색의 보색 계산
complementary_color = get_complementary_color(color)

# 색상 선택기를 보색 배경 박스로 표시
st.markdown(f"""
<div style="
    border: 3px solid #333; 
    border-radius: 10px; 
    padding: 15px; 
    background-color: {complementary_color}; 
    margin: 10px 0;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    text-align: center;
">
<p style="margin: 0; color: black; font-weight: bold;">선택기 배경색 (보색): {complementary_color}</p>
</div>
""", unsafe_allow_html=True)

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
    st.balloons()

st.write(f"현재 배경색: {color}")
st.write(f"보색: {complementary_color}")

options = ["North", "East", "South", "West"]
selection = st.pills("Directions", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")

# 사이드바에 통계 추가
st.sidebar.divider()
st.sidebar.subheader("📊 통계")

col1, col2 = st.sidebar.columns(2)
with col1:
    st.metric("총 프롬프트", "127")
with col2:
    st.metric("총 사용자", "23")

st.sidebar.metric("오늘 등록", "5", delta="2")

#실행방법
#streamlit run main.py