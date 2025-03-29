import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# 구글시트 연결 세팅
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'credentials.json', scope)  # credentials.json 파일을 프로젝트 폴더에 두세요.
client = gspread.authorize(creds)

# 구글시트에서 데이터 가져오기
notice_sheet = client.open('공지사항').sheet1
eval_sheet = client.open('수행평가').sheet1

# Google Sheets 데이터 가져오기
notice_data = notice_sheet.get_all_records()
eval_data = eval_sheet.get_all_records()

# 공지사항 표시
st.title("🐀공지사항")
notice_df = pd.DataFrame(notice_data)
st.write(notice_df)

# 수행평가 표시
st.title("🐀수행평가")
eval_df = pd.DataFrame(eval_data)
st.write(eval_df)

# 공지사항 등록
st.title("✏️공지사항 등록")
content = st.text_input("내용(공지)")
date1 = st.text_input("일시(공지)")

if st.button("공지사항 등록"):
    notice_sheet.append_row([content, date1])  # 구글 시트에 데이터 추가
    st.success("등록 완료!")

# 수행평가 등록
st.title("✏️수행평가 등록")
subject = st.text_input("과목(수행)")
content_a = st.text_area("내용(수행)")
date2 = st.text_input("일시(수행)")

if st.button("수행평가 등록"):
    eval_sheet.append_row([subject, content_a, date2])  # 구글 시트에 데이터 추가
    st.success("등록 완료!")
