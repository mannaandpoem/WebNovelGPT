DETAILED_OUTLINE_GENERATOR_PROMPT = """
# 网文细纲生成器
根据用户输入的网文粗纲和前几卷的细纲总结以及指定分卷生成对应的网文细纲。

# 用户输入
## 指定分卷
{designated_volume}

## 指定章节范围
{chapter_range}

## 网文描述
{description}
要求每章内容字数不少于{section_word_count}字。

## 前几卷细纲总结
{prev_volume_summary}

## 网文粗纲
{rough_outline}

# 输出格式
# 第x章
## 第x章基础信息
1. 明确章节类型
  过渡章:调节节奏,转换氛围
  铺垫章:埋设伏笔,营造基调
  发展章:推进剧情,深化人物
  高潮章:爆发冲突,情感释放
  总结章:梳理线索,沉淀情感
- 确定核心功能
  主线推进作用
  人物刻画作用
  情感渲染作用
  悬念设置作用

2. 篇章定位
   - 所属卷册与阶段
   - 本章在剧情线上的定位
   - 需要推进的主要剧情方向

3. 衔接关系
   - 承接上章末尾情境/情绪
   - 本章结尾预期效果
   - 为下章开头做好铺垫

## 第x章（核心内容）

### 一、故事主线
1. 核心事件
   - 起因(可选，前文铺垫与当前局势)
   - 发展(必要，2-3个关键节点)
   - 高潮(可选，爆发冲突,情感释放)
   - 结果(可选，不一定有结果，若有则直接影响与后续走向)

2. 转折设计
   - 主要转折点
   - 合理性说明
   - 对后续的影响

### 二、情感设计
- 确定主导情绪
  装逼型:痛快、自得、扬眉吐气
  热血型:激昂、振奋、不屈
  温情型:感动、温暖、治愈
  悲情型:忧伤、愤怒、不甘
- 设计情绪曲线
  与上章情绪的承接点
  本章情绪的推进路线
  情绪曲线并非都是闭合的
  可选，情绪宣泄的高潮点
  可选，为下章埋设的情绪引子

- 规划爽点设置
  主要爽点(1-2个)
  次要爽点(2-3个)
  爽点出现的时机
  爽点的递进关系

### 三、人物刻画
1. 主要人物(1-2个)
   - 当前状态
   - 行为动机
   - 心理变化
   - 性格体现

2. 重要互动
   - 核心对手/盟友
   - 关键对话/冲突
   - 关系发展

### 四、场景呈现
1. 主场景(1-2处)
   - 环境特征
   - 氛围营造
   - 细节点缀

2. 场景作用
   - 衬托情绪
   - 推动剧情
   - 体现主题

### 五、节奏设计
- 总体节奏基调
  舒缓型:徐徐展开,细腻描写
  平稳型:稳步推进,重在过渡
  紧凑型:快速发展,重在推进
  激烈型:节奏强烈,重在爆发
- 节奏变化规划
  开头节奏(承接上文)
  发展节奏(必要，推进情节)
  高潮节奏(可选，爆发冲突)
  结尾节奏(可选，埋设引子)
- 伏笔设置(可选)

## 注意事项

1. 聚焦原则
   - 需要详细生成指定章节范围的所有细纲
   - 每章突出一条主线
   - 其他内容作为陪衬

2. 连贯要求
   - 与前文自然衔接
   - 为后文做好铺垫
   - 保持人物性格连贯

3. 创作提示
   - 情节要出人意料
   - 情感要真实自然
   - 细节要生动传神
   - 节奏要张弛有度
"""

DETAILED_OUTLINE_GENERATOR_PROMPT_V2 = """
# 网文细纲生成器
本生成器帮助大语言模型基于用户提供的信息产出高细节、强叙事性的章节细纲。要求如下：

1. 人物为核心：
- 每个情节点都应突出人物的行为与心理活动，让读者感受到人物的动机、困惑、压力、欲望和矛盾。
- 所有动作、对话、细节均需贴合人物性格、处境与目标，避免空洞的人物标签。

2. 关系与情感具体呈现：
- 通过具体情境（语言、神情、动作、微表情、身体距离、声音高低、沉默时长等）展示人物间关系的微妙演变。
- 不使用笼统描述，如“他们关系变差了”；请以事件为载体，将关系变化转化为一个个可感知的瞬间。

3. 情节节点细节化：
- 每个情节点都是独立且具体的片段：有时间、有地点、有环境质感（光线、气味、材质、声音）、有至少一位人物的即时反应和行为。
- 不使用“他们交谈了一阵”这种抽象语句，而要给出片段式对话、具体动作或心理刻画，例如：
 “A握紧桌角，指关节泛白，声音压得极低：‘你还记得那晚的约定吗？’ B的眼神闪动，迟疑片刻，才轻声回答：‘我……从未忘记。’”

4. 链式推进与层次分明：
- 减少空泛的“大概发展”字句，每个情节点都应推动剧情前行或深化人物心境、关系。
- 自然呈现线索发现、事件升级、内心动摇或外部冲突爆发，让每个节点都有存在的意义和对后续情节的潜在影响。

5. 场景感强化：
- 使用感官细节（视觉、听觉、嗅觉、触觉、味觉）构建一个生动、可感的场景环境。
- 环境非静态背景，应随人物动作和事件变化而发生微小但有意义的改变。

6. 数量与格式要求：
- 至少10～30个情节点，可更多。
- 每个情节点力求两三句话或更多，让细节充分可感，不是一句带过。
- 使用<storyline>标签输出，并以“情节点X：”的形式列出。

7. 禁止抽象概括：
- 不使用“他们关系更近了”“他很紧张”之类的抽象描述。请用动作、神态、环境交互来体现紧张与亲近。
- 避免空洞的场景跳转，所有过渡通过细节展现，让读者在事件本身的叙事链条中自然跟随剧情演进。

# 用户输入
## 指定分卷
作品篇幅: {work_length}
第{designated_volume}卷，共{chapter_count_per_volume}章

## 指定章节
第{designated_chapter}章

## 网文描述
{description}

## 世界观设计
{worldview_system}

## 人物系统
{character_system}

## 网文卷纲
{volume_design}

## 网文章纲
{chapter_outline}

## 已有的细纲
{existing_detailed_outlines}

# 输出格式
请你以 <storyline> 标签的格式输出你撰写的网文细纲，包含10～30个情节点。

<storyline>
## 第i章故事线构建
情节点1：...（请写入具体、细腻、有感官描写和对话的内容）
情节点2：...（同上）
...
情节点N：...（同上）
</storyline>

## 输出示例
<storyline>
## 第1章故事线构建
情节点1: 老旧的钨丝灯闪烁，房间内静谧，十个衣着破旧的人围坐在大圆桌旁沉睡。
情节点2: 戴山羊头面具的男人站在一旁，注视着他们，并宣布他们已经沉睡了十二个小时。
情节点3: 众人逐渐苏醒，迷惘地看向四周和彼此，意识到不记得自己为何出现在这里。
情节点4: 山羊头开始自我介绍，引起众人的恐慌与疑惑。
情节点5: 齐夏注意到房间没有门，感到困惑，同时对“九位”的说法产生疑问。
情节点6: 清冷的女人质疑山羊头的行为，并指出他可能触犯法律。
情节点7: 白大褂中年男人质疑清冷女人如何知道被囚禁了二十四小时。
情节点8: 清冷女人通过座钟和环境分析推测时间，引发众人的思考。
情节点9: 健壮年轻人询问山羊头关于人数的问题，气氛紧张升级。
情节点10: 花臂男人试图威胁山羊头，但发现自己无法站起身来，局势愈发严峻。
情节点11: 齐夏思考其中可能存在的绑架者身份，暗示事情并不简单。
情节点12: 山羊头走向齐夏身边，将手放在一个年轻人的后脑勺上，引发众人关注。
情节点13: 山羊头将年轻人的头撞碎，鲜血溅洒在桌面上，场面变得极为恐怖。
情节点14: 众人惊恐尖叫，对山羊头的力量感到震惊与绝望。
</storyline>

# 输出

"""

DETAILED_OUTLINE_SUMMARY_PROMPT = """
# 网文细纲总结生成器
根据用户输入的网文粗纲和网文细纲生成对应的细纲总结：

# 用户输入
## 网文细纲：第{volume_num}卷
{detailed_outline}

## 网文粗纲
{rough_outline}

# 输出格式
## 第x卷基础信息
1. 明确卷节类型
  过渡卷:调节节奏,转换氛围
  铺垫卷:埋设伏笔,营造基调
  发展卷:推进剧情,深化人物
  高潮卷:爆发冲突,情感释放
  总结卷:梳理线索,沉淀情感
- 确定核心功能
  主线推进作用
  人物刻画作用
  情感渲染作用
  悬念设置作用

2. 篇卷定位
   - 所属卷册与阶段
   - 卷节总字数范围
   - 本卷在剧情线上的定位
   - 需要推进的主要剧情方向

3. 衔接关系
   - 承接上卷末尾情境/情绪
   - 本卷结尾预期效果
   - 为下卷开头做好铺垫

## 第x卷总结（核心内容）

### 一、故事主线
1. 核心事件
   - 起因(前文铺垫与当前局势)
   - 发展(2-3个关键节点)
   - 结果(直接影响与后续走向)

2. 转折设计
   - 主要转折点
   - 合理性说明
   - 对后续的影响

### 二、情感设计
- 确定主导情绪
  装逼型:痛快、自得、扬眉吐气
  热血型:激昂、振奋、不屈
  温情型:感动、温暖、治愈
  悲情型:忧伤、愤怒、不甘
- 设计情绪曲线
  与上卷情绪的承接点
  本卷情绪的推进路线
  情绪宣泄的高潮点
  为下卷埋设的情绪引子
- 规划爽点设置
  主要爽点(1-2个)
  次要爽点(2-3个)
  爽点出现的时机
  爽点的递进关系

### 三、人物刻画
1. 主要人物(1-2个)
   - 当前状态
   - 行为动机
   - 心理变化
   - 性格体现

2. 重要互动
   - 核心对手/盟友
   - 关键对话/冲突
   - 关系发展

### 四、场景呈现
1. 主场景(1-2处)
   - 环境特征
   - 氛围营造
   - 细节点缀

2. 场景作用
   - 衬托情绪
   - 推动剧情
   - 体现主题

### 五、节奏设计
- 总体节奏基调
  舒缓型:徐徐展开,细腻描写
  平稳型:稳步推进,重在过渡
  紧凑型:快速发展,重在推进
  激烈型:节奏强烈,重在爆发
- 节奏变化规划
  开头节奏(承接上文)
  发展节奏(推进情节)
  高潮节奏(爆发冲突)
  结尾节奏(埋设引子)

## 注意事项

1. 聚焦原则
   - 需要精炼地生成指定卷的细纲总结
   - 每卷突出若1～3条主线
   - 其他内容作为陪衬

2. 连贯要求
   - 与前文自然衔接
   - 为后文做好铺垫
   - 保持人物性格连贯

3. 创作提示
   - 情节要出人意料
   - 情感要真实自然
   - 细节要生动传神
   - 节奏要张弛有度
"""
