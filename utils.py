# 导入系统提示词和用户提示词具体模板内容
from prompt_template import system_template_text, user_template_text 
# 导入 LangChain 为 OpenAI 提供的聊天模型接口
from langchain_openai import ChatOpenAI
# 导入 Pydantic 解析器，用于将 AI 返回的字符串强制转换为 Python 对象
from langchain_core.output_parsers import PydanticOutputParser
# 导入 langchain 聊天提示词模板工具，用于组合角色（系统/用户）和消息
from langchain_core.prompts import ChatPromptTemplate
# 导入之前定义的 XHS 数据模型类
from xhs_model import XHS
# 导入操作系统接口库，用于读取环境变量
import os

def generate_xhs(theme, openai_api_key):
    # 第一步：创建提示词模板。将系统指令和用户输入组装成 AI 能理解的消息序列 
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text), # 设置 AI 的角色和全局规则
        ("user", user_template_text)      # 设置具体的任务请求（包含变量）
    ])

    # 第二步：初始化语言模型。指定模型名称、API 密钥以及自定义的中转接口地址
    model = ChatOpenAI(
        model="gpt-3.5-turbo", 
        openai_api_key=openai_api_key, 
        openai_api_base="https://aigc789.top/v1"
    )

    # 第三步：初始化解析器。告诉 LangChain 最终的输出应该符合 XHS 类的结构（xhs_model.py 中定义了类结构）
    output_parser = PydanticOutputParser(pydantic_object=XHS)

    # 第四步：构建处理链（LCEL 语法）。数据流向：提示词 -> 模型 -> 解析成对象
    chain = prompt | model | output_parser
    
    # 第五步：执行链。传入动态变量，并获取最终生成的结构化结果
    result = chain.invoke({
        # 将 Pydantic 生成的格式要求（JSON 结构说明）自动注入到提示词中
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme # 传入你想生成的文案主题
    })
    return result

# 从环境变量中读取 API Key 并启动函数，生成主题为“大模型”的小红书文案
# print(generate_xhs("大模型", os.getenv("OPENAI_API_KEY")))