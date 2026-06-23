from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

import streamlit as st

PASSWORD = "hansung"
pwd = st.text_input("비밀번호", type="password")

if pwd != PASSWORD:
    st.stop()
st.title("인공지능 시인")


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])
chain = prompt | llm | StrOutputParser()

content = st.text_input("시의 주제를 입력하세요")
if st.button("시 작성 요청하기"):
    if content:
        with st.spinner("시를 작성하는 중입니다..."):
            response = chain.invoke({"input": content + "에 대한 시를 써줘."})
            st.text_area("작성된 시", value=response, height=300)
    else:
        st.warning("주제를 입력해주세요.")

# content = "코딩"
# response = chain.invoke({"input": content + "에 대한 시를 써줘."})
# print(response)

