from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st



llm = init_chat_model("gpt-4o-mini", model_provider="openai")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])
chain = prompt | llm | StrOutputParser()

st.title("인공지능 시인")


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

