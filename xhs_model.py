# 从 pydantic 库中导入 BaseModel（基础模型类）和 Field（字段自定义工具）
from pydantic import BaseModel, Field
# 从 Python 标准类型库中导入 List，用于声明一个列表类型
from typing import List

# 定义一个名为 XHS 的类，继承自 BaseModel
# 这使得该类拥有了自动验证数据、解析 JSON 以及生成数据结构说明（Schema）的能力
class XHS(BaseModel):
    # 定义“title”（标题）字段：
    # 1. 类型约束：必须是一个由字符串（str）组成的列表（List）
    # 2. description：给 AI 的提示词，告诉它这里需要生成“小红书的5个标题”
    # 3. min_items/max_items：硬性约束，规定列表长度必须精准等于 5，多一个或少一个都会报错
    title: List[str] = Field(description="小红书的5个标题", min_items=5, max_items=5)
    
    # 定义“content”（正文）字段：
    # 1. 类型约束：必须是一个字符串（str）
    # 2. description：给 AI 的提示词，明确这里存放的是“小红书的正文内容”
    content: str = Field(description="小红书的正文内容")