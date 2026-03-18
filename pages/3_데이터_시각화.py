import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import plotly.express as px
import plotly.graph_objects as go

# 한글 폰트 설정 (matplotlib용)
font_path = '/workspaces/260318-fullsun/fonts/static/NotoSansKR-Regular.ttf'
font_manager.fontManager.addfont(font_path)
plt.rcParams['font.family'] = 'Noto Sans KR'
plt.rcParams['axes.unicode_minus'] = False

st.title("데이터 시각화 페이지")

st.markdown("중학교 수학 수업 관련 데이터를 다양한 라이브러리를 사용하여 시각화합니다.")

# 샘플 데이터 생성: 학생들의 수학 점수
data = {
    '학생': ['김철수', '이영희', '박민수', '정수진', '홍길동', '강감찬', '유관순', '안중근'],
    '점수': [85, 92, 78, 88, 95, 82, 90, 87],
    '단원': ['정수', '분수', '소수', '방정식', '기하학', '확률', '통계', '함수']
}
df = pd.DataFrame(data)

st.header("1. 데이터 표 (Pandas)")
st.dataframe(df)

st.header("2. 막대 그래프 (Matplotlib)")
fig, ax = plt.subplots()
ax.bar(df['학생'], df['점수'], color='skyblue')
ax.set_title('학생별 수학 점수')
ax.set_xlabel('학생')
ax.set_ylabel('점수')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

st.header("3. 선 그래프 (Plotly)")
# 점수를 정렬해서 선 그래프로
sorted_df = df.sort_values('점수')
fig_line = px.line(sorted_df, x='학생', y='점수', title='학생별 수학 점수 (정렬됨)', markers=True)
fig_line.update_layout(xaxis_title='학생', yaxis_title='점수', font_family='Noto Sans KR')
st.plotly_chart(fig_line)

st.header("4. 산점도 (Plotly)")
# 단원별로 색상 구분
fig_scatter = px.scatter(df, x='학생', y='점수', color='단원', title='학생별 점수와 단원')
fig_scatter.update_layout(xaxis_title='학생', yaxis_title='점수', font_family='Noto Sans KR')
st.plotly_chart(fig_scatter)

st.header("5. 파이 차트 (Matplotlib)")
# 단원별 평균 점수 계산
unit_scores = df.groupby('단원')['점수'].mean()
fig_pie, ax_pie = plt.subplots()
ax_pie.pie(unit_scores, labels=unit_scores.index, autopct='%1.1f%%', startangle=90)
ax_pie.set_title('단원별 평균 점수 비율')
ax_pie.axis('equal')
st.pyplot(fig_pie)

st.header("6. 히스토그램 (Plotly)")
fig_hist = px.histogram(df, x='점수', title='점수 분포', nbins=5)
fig_hist.update_layout(xaxis_title='점수', yaxis_title='빈도', font_family='Noto Sans KR')
st.plotly_chart(fig_hist)

st.markdown("이 페이지는 샘플 데이터를 사용하여 다양한 시각화를 보여줍니다. 실제 데이터를 업로드하거나 수정하여 사용하세요.")