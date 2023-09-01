# call-zoe-gpt-python-demo

调用左医大模型的示例, 包括流式调用

您可以访问 左手医生开放平台 https://ai.zuoshouyisheng.com/ 浏览接口文档、创建API密钥.

左医大模型提供的接口兼容 openai 格式, 所以您可以使用 openai 官方 client 调用左医大模型.

请注意左医大模型与openai有一些差异

1. 左医大模型的接口有前缀 "/gpt/v1/openai-compatible"

   如 https://openapi.zuoshouyisheng.com/gpt/v1/openai-compatible/v1/chat/completions

2. 左医大模型通过 http header 中的 "X-API-KEY" 鉴权
3. 左医大模型只支持少量 openai 接口
