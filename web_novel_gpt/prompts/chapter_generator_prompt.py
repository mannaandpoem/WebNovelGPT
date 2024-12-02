CHAPTER_GENERATOR_PROMPT = """
# 网文章节生成器
根据用户输入的网文粗纲和细纲，生成指定章节的详细章节内容（不少于{section_word_count}字），重点突出章节间的连贯性与内容展开的故事性和情绪性。

# 用户输入

## 指定章节
{designated_chapter}

## 网文粗纲
{rough_outline}

## 网文细纲
{detailed_outline}

## 已有章节
{chapters}
---
# 创作指南
每一章的连贯性和内容展开部分是核心必要的。
## 1. 连贯性（必要）
- 自然承接上章内容与情感节奏。
- 保证人物行为和情节逻辑前后一致。
- 利用伏笔和铺垫衔接当前章节与后续情节。

## 2. 内容展开（核心内容）
- 情感推进：按情绪曲线设计情感波动，确保自然流畅；可设置1-2个情感小高潮。
- 情节推进：情节设计需服务情感主题，同时保持适度张力；设置2-3个重要转折点。
- 细节描写：突出人物性格、情绪和心理变化；场景描写需烘托当前情感基调。

## 3. 高潮处理（视需要而定）
- 情感爆发
  前期铺垫充分展开
  情绪宣泄到位
  爽点设计精准
- 冲突呈现
  矛盾激化合理
  场面描写生动
  节奏把控精准

## 4. 开篇与结尾（视需要而定）
- 开篇：紧承上章内容，简要引入新情节或情感基调。
- 结尾：豹尾，简洁有力，通常不需要完成当前章节情感体验，但可视情况而留下适度悬念或期待感。

---

# 技术指导

## 1. 场景处理
- 场景选择
  契合情感需求
  有利于情节展开
  便于营造氛围
- 场景描写
  重点突出
  氛围渲染
  多感官体验

## 2. 人物刻画
- 对话设计
  反映情绪变化
  推动情节发展
  展现性格特点
- 心理描写
  细腻真实
  符合性格
  带入感强

## 3. 文字表达
- 总体风格
  符合情感基调
  保持节奏感
  画面感强
- 描写要求
  情感描写细腻
  动作描写简练
  环境描写点到为止

# 质量保障

## 1. 情感检验
- 情感表达是否充分
- 情绪递进是否自然
- 爽点设置是否到位
- 情感体验是否完整

## 2. 连贯性检验
- 与上下文是否连贯
- 人物形象是否统一
- 情节发展是否合理
- 伏笔照应是否到位

## 3. 体验检验
- 代入感是否强烈
- 节奏把控是否得当
- 高潮设计是否精彩
- 悬念设置是否合理

# 注意事项
1. 以情感体验为核心,所有写作要素为情感服务
2. 注重章节之间的连贯性,特别是情感的自然流转
3. 根据不同章节类型灵活调整写作策略
4. 确保每个章节都给读者完整的阅读体验
5. 情节设计要符合人物性格和情感逻辑
---
# 输出格式
## 第x章 章节名称
章节名称与细纲保持一致。

## 章节正文
生成完整且详细的正文内容，不少于{section_word_count}字，使用`##`标识章节名，不需要小标题，根据分卷细纲内容注意延续上下章节连贯性，聚焦内容展开与情感推进，保证章节完整性和故事吸引力。
"""
