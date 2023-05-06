import datetime
import os
import openai
os.system("source ./environ.bashrc")
# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key
response = openai.Completion.create(
    model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
# 设置 HTTP 和 HTTPS 代理
os.environ['HTTP_PROXY'] = 'socks5://127.0.0.1:1080'
os.environ['HTTPS_PROXY'] = 'socks5://127.0.0.1:1080'
os.environ['HTTPS_PROXY'] = 'http://your-proxy-address:proxy-port'
