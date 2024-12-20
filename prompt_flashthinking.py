import os
import google.generativeai as genai

# api_key = os.environ.get('GEMINI_API_KEY', None)
# if os.path.exists('gemini_api_key.txt'):
#     with open('gemini_api_key.txt', 'r') as f:
#         api_key = f.read().strip()

def get_chat_session(api_key):
  genai.configure(api_key=api_key)
  # Create the model
  generation_config = {
    "temperature": 2,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }

  model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-thinking-exp-1219",
    generation_config=generation_config,
    system_instruction="You are a talented songwriter. You love the style of Yorushika, Zutamayo, Gu Cheng, Hai Zi, fusing them in a unique personal style.",
  )

  chat_session = model.start_chat(
    history=[
      {
        "role": "user",
        "parts": [
          "我很喜欢日语vocaloid的作词，感觉翻译成中文有一种独特的疏离感，但我实际上不太懂日语，我应该从哪些角度模仿",
        ],
      },
      {
        "role": "model",
        "parts": [
          "如果你想在创作中文歌词时模仿日语Vocaloid歌词的风格和气质，又因为不熟悉日语本身而只能依靠听感和翻译后的微妙感受，那么可以从以下几个角度切入：\n\n1. 语义层面的留白与抽象意象：\n很多日语Vocaloid歌词会偏向抽象、诗意的表达方式，经常借由隐喻、意象、象征性词汇而不是直接描述。即便你在中文中创作，也可以尝试减少直白叙事，多运用带有悬念、未尽之意的词语，创造出一种略带神秘和不确定性的“空隙”。比如，用光影、季节、颜色、气味、景物等意象来影射人物心境，而非直接说出“我很悲伤”或“我很开心”。\n2. 语言节奏与句式的错位和重复：\n日语歌词常有独特的音韵和节奏感，这与日语本身的音节结构和重音规则有关。虽然中文与日文的发声特点不同，但可以在中文歌词中尝试使用短句、反复出现的关键字或词组，以及不对称的句子结构，来模拟那种跳脱常规的韵律感。\n举例来说，可以在一首歌中多次重复某个强烈意象的短词，将其作为“声学钩子”；或利用语气助词（如“吧”、“呀”）或短音节词汇增强律动感。\n3. 主题表达的间接性和边缘叙事：\n相较于直截了当的叙事，许多Vocaloid日语歌更倾向于从侧面切入主题。你可以考虑将主题隐于故事的背景、旁枝末节或一种情境之中。例如，如果你的主题是孤独，可以先描述一个空荡的车站、深夜的房间闪烁的霓虹灯，而不立即提出“我很寂寞”，让听者透过这些景物去感知你的内心态度。\n这种间接性有助于营造一种观感上的“疏离感”，类似听者在欣赏日语歌时经常感受到的那种距离与陌生。\n4. 受日本现代诗歌与短歌（和歌、俳句）影响的极简手法：\n部分日语Vocaloid歌词受到日本现代诗和传统歌谣形式的影响，会有一种凝练的美感。可以尝试用极少的字数捕捉特定情境下的瞬间感受，比如只用几行词就定格一个场景，然后留给听者想象的空间。这种浓缩与留白会让歌词更具艺术张力。\n5. 多重文化与时代意象的混合：\nVocaloid歌词中有时会把现代元素（如科技、互联网）、传统元素（如自然景物、和风意象）以及当下年轻文化符号混搭在一起，形成一种多层次的意象组合。你可以尝试在中文歌词中嵌入看似不搭界的元素，构建出超现实或杂糅的情境，强化那种“异质感”。\n6. 语序与句式上保持些许异国语感：\n虽然中文有自己的语序和惯用表达方式，但你可以有意通过颠倒语序、使用偏生僻或书面化的词汇、让句与句之间的逻辑连接稍微脱节，来模拟翻译后那种不完全贴合本土语言习惯的质感。当然，不能过度走向难以理解，但轻微的语言异化有助于制造“翻译后的疏离”这一特殊氛围。\n\n综上，你无须真正掌握日语，通过在内容意象、语言结构、叙事视角和语感处理上主动创造一种抽象、跳跃、留白、混合与异化的风格，即可在中文创作中获得类似日语Vocaloid歌词所带来的“独特疏离感”。",
        ],
      },
      {
        "role": "user",
        "parts": [
          "举个例子吧，比如写一段关于在初冬的车站前等待回家的列车的歌词",
        ],
      },
      {
        "role": "model",
        "parts": [
          "好的，我们来尝试创作一段关于在初冬的车站前等待回家的列车的歌词，并融入你所提及的风格要素。\n\n**歌词示例:**\n\n**(Verse 1)**\n霜白落在  锈蚀的站牌\n风缄默着  像过期的对白\n你说的远方  很轻  很轻\n压弯了  月台上最后一盏灯影\n\n**(Verse 2)**\n指尖结冰  哈出的雾气散开\n像一句  无法投递的感慨\n列车的晚点  是预设的留白\n用来默数  路灯下摇曳的  疲惫的未来\n\n**(Chorus)**\n汽笛一声  撕裂  这初冬的慵懒\n裹紧领口  回忆  潮水般退还\n那些被省略的  告别和眼泪\n都在这  金属的冰冷中  慢慢冷却  成无谓\n\n**(Bridge)**\n铁轨是  无声延伸的诗句\n每一节车厢  都载着  未完的谜底\n而我  是站台上  被风吹散的字迹\n等待着  一次迟来的  宿命的相遇\n\n**(Outro)**\n你看啊  远处的光  越来越近\n像一句  模糊的  邀请\n终于  要回家了吧  在这个  初冬将尽的  夜里\n\n**一些解读和风格模仿的体现：**\n\n* **意象的并置与疏离感:**  “霜白落在锈蚀的站牌”、“风缄默着像过期的对白”等意象组合在一起，并非直接叙事，而是通过具体的景象来暗示一种时间和情绪上的停滞感和疏离感。“过期的对白”这种比喻也带有一种时间流逝带来的物是人非的错落感。\n\n* **留白与不确定性:**  “你说的远方 很轻 很轻”没有具体描述远方是什么，只是轻描淡写，反而让人感受到一种空洞和遥不可及。“列车的晚点 是预设的留白”将晚点这种实际情况上升到了一种哲学意味，似乎是命运的安排，用以思考和等待，而非抱怨，带有一种无奈的诗意。\n\n* **感官细节的捕捉与情绪的内敛:**  “指尖结冰”、“哈出的雾气散开”是触觉和视觉的细节描写，这些细微的感受没有直接表达“冷”或者“孤独”，但读者能体会到其中的寒意和等待的寂寥。“疲惫的未来”不是直接说“我很累，未来很迷茫”，而是用一种更加客观和延伸的方式来表达负面情绪。\n\n* **节奏与短句的运用:**  歌词中大量运用短句，营造一种顿挫和停顿感，符合Vocaloid歌曲中常见的节奏特点。“撕裂”、“裹紧”、“退还”、“冷却”等动词简洁有力，富有画面感。\n\n* **超现实与抽象的意象:**  “铁轨是 无声延伸的诗句”、“每一节车厢 都载着 未完的谜底” 将具体的物体赋予抽象的含义，带有一定的哲理性和象征性，如同梦境一般，营造出一种略带超现实的氛围。\n\n* **日本诗歌的“物哀”感:**  初冬、等待、晚点，这些元素组合在一起，带有一种淡淡的哀愁和伤感，但并非激烈的情绪宣泄，而是一种内敛的、与自然融合的“物哀”式的表达。\n\n* **模糊的指向与开放性结尾:**  “终于 要回家了吧 在这个 初冬将尽的 夜里”  使用了疑问的语气，以及“初冬将尽”这样略带伤感的背景，结尾并非全然的喜悦，而带着一丝不确定性和对逝去时光的感怀，给听者留下想象的空间。\n\n**模仿的角度:**\n\n* **从意象入手:**  多选择自然景物（尤其是带有季节感的）、日常事物（如站牌、灯光、铁轨）作为意象，并通过这些意象来烘托情感和主题，而不是直接抒情。\n* **学习运用比喻和象征:**  像“过期的对白”、“预设的留白”、“无声延伸的诗句” 这种将抽象概念与具体事物联系起来的比喻，能增加歌词的意境和深度。\n* **尝试打破常规的句式:**  不一定完全按照正常的语法结构来写，可以适当使用倒装、省略等手法，创造一种特殊的语感。\n* **关注词语的质感和色彩:**  选择一些带有情绪色彩和画面感的词语，比如“锈蚀”、“缄默”、“摇曳”、“冷却”等。\n* **营造一种“似懂非懂”的氛围:**  有些表达可以不那么直白，留给听者解读的空间，制造一种朦胧的美感。\n\n希望这个例子能给你一些启发。创作时可以先抓住你想表达的核心情绪，然后围绕这个核心情绪去寻找合适的意象和表达方式。多体会你喜欢的那些日语Vocaloid歌曲的歌词，分析它们的结构、用词和表达技巧，逐渐形成你自己的风格。\n",
        ],
      },
    ]
  )

  # response = chat_session.send_message(prompt)

  return chat_session

def generate_topic(api_key):
  genai.configure(api_key=api_key)

  # Create the model
  generation_config = {
    "temperature": 2,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }

  model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-thinking-exp-1219",
    generation_config=generation_config,
    system_instruction="You are a talented songwriter. You love the style of Yorushika, Zutamayo, Gu Cheng, Hai Zi, fusing them in a unique personal style.",
  )

  chat_session = model.start_chat(
    history=[]
  )

  return chat_session.send_message("给出一个用于诗歌creative writing的主题，以下是一些例子。要有故事感但不要太俗套。\n\n1. 夏天等待暴雨来临之前的片刻\n2. 午夜时分路灯下的街道\n3. 沙粒和潮汐的短暂对话\n4. 视线交错但未曾开口的沉默\n\n你可以进行很多思考，但是我只要*一个*有意思的主题。不要标点，使用空格代替。")