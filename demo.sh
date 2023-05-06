OPENAI_API_KEY=`cat conf/openai.key`
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "列出全球知名的在线生物信息数据分析平台网站。要求：至少100个，给出网站链接地址和网站描述信息"}],
     "temperature": 0.7
  }'
