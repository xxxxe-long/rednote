import streamlit as st
from utils import generate_xhs
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_title="小红书爆款文案生成器", page_icon="📕")
st.header("爆款小红书AI写作助手")

with st.sidebar:
    st.header("🔑 密钥配置")
    openai_api_key = st.text_input("请输入OpenAI API密钥：", type="password")
    st.info("💡 提示：密钥仅用于当前运行，不会被保存。")
    st.divider()
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")

theme = st.text_input("请输入小红书文案主题：", placeholder="例如：夏日护肤秘籍")
submission = st.button("🚀 Start")

if submission and not openai_api_key:
    st.info("请在侧边栏输入OpenAI API密钥！")
    st.stop()
if submission and not theme:
    st.info("请输入生成主题！")
    st.stop()
if submission:
    with st.spinner("🤖 正在撰写文案，请稍候..."):
        result = generate_xhs(theme, openai_api_key)
    st.balloons()
    st.success("✨ 小红书爆款文案已就绪！")
    st.divider()
    left, right = st.columns(2)
    with left:
        st.subheader("💡文案标题：")
        st.markdown(f"##### 小红书标题1")
        st.write(result.title[0])
        st.markdown(f"##### 小红书标题2")
        st.write(result.title[1])
        st.markdown(f"##### 小红书标题3")
        st.write(result.title[2])
        st.markdown(f"##### 小红书标题4")
        st.write(result.title[3])
        st.markdown(f"##### 小红书标题5")
        st.write(result.title[4])

    with right:
        st.subheader("📝文案正文（支持复制）")
        st.write(result.content)