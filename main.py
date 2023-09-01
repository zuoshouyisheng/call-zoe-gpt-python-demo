import asyncio
import json

import openai

from openai import util

util.api_key_to_header = lambda api, key: {"X-API-KEY": f"{key}"}

import importlib

importlib.reload(openai)

openai.api_base = "https://openapi.zuoshouyisheng.com/gpt/v1/openai-compatible/v1"
openai.api_key = "ZOE-xxxxxx-1d8b97"


async def try_chat_completion_stream():
    r = await openai.ChatCompletion.acreate(
        model="zoe-gpt",
        messages=[
            {"role": "system", "content": "你是一名全科医生"},
            {"role": "user", "content": "肚子疼应该挂什么科室"},
        ],
        stream=True,
    )

    # 流式返回时, r 是一个 async_generator 对象, 可以使用 async for 进行迭代
    async for item in r:
        print(item.choices[0].delta.content, end='')

    print("\n[生成结束]")


async def try_chat_completion():
    r = await openai.ChatCompletion.acreate(
        model="zoe-gpt",
        messages=[
            {"role": "system", "content": "你是一名全科医生"},
            {"role": "user", "content": "肚子疼应该挂什么科室"},
        ],
        stream=False,
    )

    print("生成结果: ", json.dumps(r.to_dict(), ensure_ascii=False))


if __name__ == '__main__':
    asyncio.run(try_chat_completion_stream())
    # asyncio.run(try_chat_completion())
