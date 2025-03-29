import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import json

try:
    creds_json = st.secrets["GOOGLE_CREDENTIALS"]
    creds_dict = json.loads(creds_json)

    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ])
    client = gspread.authorize(creds)
except Exception as e:
    st.error(f"Google Credentials 로드 실패: {e}")
    st.stop()

try:
    notice_sheet = client.open('공지사항').sheet1
    eval_sheet = client.open('수행평가').sheet1

    notice_data = notice_sheet.get_all_records()
    eval_data = eval_sheet.get_all_records()

    st.title("🐀 공지사항")
    st.caption("Google Sheets에서 가져온 정보")
    notice_df = pd.DataFrame(notice_data)
    st.write(notice_df)

    st.title("🐀 수행평가")
    st.caption("Google Sheets에서 가져온 정보")
    eval_df = pd.DataFrame(eval_data)
    st.write(eval_df)
except Exception as e:
    st.error(f"Google Sheets 연결 오류: {e}")

st.title("✏️ 공지사항 등록")
content = st.text_input("내용(공지)")
date1 = st.text_input("일시(공지)")

if st.button("공지사항 등록"):
    try:
        notice_sheet.append_row([content, date1])  # 구글 시트에 데이터 추가
        st.success("등록 완료!")
    except Exception as e:
        st.error(f"등록 실패: {e}")

st.title("✏️ 수행평가 등록")
subject = st.text_input("과목(수행)")
content_a = st.text_area("내용(수행)")
date2 = st.text_input("일시(수행)")

if st.button("수행평가 등록"):
    try:
        eval_sheet.append_row([subject, content_a, date2])  # 구글 시트에 데이터 추가
        st.success("등록 완료!")
    except Exception as e:
        st.error(f"등록 실패: {e}")
