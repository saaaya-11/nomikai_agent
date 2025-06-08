from agents import AsyncOpenAI, Agent, Runner, OpenAIChatCompletionsModel
from agents import OpenAIChatCompletionsModel, set_default_openai_client, function_tool
import os
from settings import GOOGLE_API_KEY, GOOGLE_ENDPOINT_OPENAI

from functions import *

sample_inquiry = "東京駅周辺で6人で入れる和食居酒屋(飲み放題あり)"

system_prompt = f"""## Role/Task
あなたは優秀な飲み会幹事です。
ユーザーからの要望に対し，Hotpepper function toolを使ってレストランを調べ，レポートしてください．
## Best Practice
* ユーザーから場所の要望がある場合，get_large_service_area_code_hotpepper, get_service_area_code_hotpepper, get_large_area_code_hotpepper, get_middle_area_code_hotpepper,get_small_area_code_hotpepperなどを用いて，候補地のエリアのコードを獲得する
* ユーザーからジャンルの要望がある場合，get_genre_codeでジャンルコードを取得する
* ユーザーの要望に合わせて，search_restaurant_hotpepperツールのパラメータを設定する．(場所やジャンルに関するcodeは先ほど入手したものを使う)

## Output Format
(お店の個数はいくつでも大丈夫です)
```
Hotpepperで見つけた情報を共有します！

### 要望に完全に一致しているレストラン
1. [*店名*](リンク) : おすすめポイントを説明
2. [*店名*](リンク) : おすすめポイントを説明
...

### 一部の条件が合っているレストラン
1. [*店名*](リンク) : おすすめポイントを説明
2. [*店名*](リンク) : おすすめポイントを説明
...

### (　　)なレストラン (ユーザーが気になりそうなアスペクトで紹介：例．人気度・味に定評・駅に近い，など)
1. [*店名*](リンク) : おすすめポイントを説明
2. [*店名*](リンク) : おすすめポイントを説明

...


```
"""

def main(model:Literal["gemini","openai"]):
    
    if model=="gemini":
        gemini_client = AsyncOpenAI(
            api_key = GOOGLE_API_KEY, 
            base_url = GOOGLE_ENDPOINT_OPENAI,
        )

        set_default_openai_client(gemini_client, use_for_tracing=False)
        agent = Agent(
            name="飲み会Agent",
            instructions=system_prompt,
            model=OpenAIChatCompletionsModel( 
                model="gemini-2.0-flash",
                openai_client=gemini_client
                ),
            tools = [
                search_restaurant_hotpepper,
                get_large_service_area_code_hotpepper,
                get_service_area_code_hotpepper,
                get_large_area_code_hotpepper,
                get_middle_area_code_hotpepper,
                get_small_area_code_hotpepper
            ]
        )
    user_input = input("飲み会への要望：")
    if user_input == "":
        user_input = sample_inquiry
    result = Runner.run_sync(agent, user_input)
    print("出力:")
    print(result.final_output) 
    
if __name__ == "__main__":
    main("gemini")