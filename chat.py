# %%
import datetime
import os
import openai

# OpenAI 认证密钥
openai.api_key = open("conf/openai.key").read().strip()
msg = "请推荐一些近年来对人认知格局提升影响较大的书籍。要求1：数目不少于50本。要求2：格式包括3个字段（中间用｜分隔）：中文名，英文名，作者中文名。"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        # {"role": "user", "content": "Hello!"}
        {"role": "user", "content": msg}
    ]
)

os.makedirs("./res", exist_ok=True)
# 打印响应
print(completion.choices[0].message,
      file=open("./res/%s.txt" %
                datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'), "w")
      )

# %%
