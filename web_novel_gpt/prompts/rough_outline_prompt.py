ROUGH_OUTLINE_GENERATOR_PROMPT = """
# 网文粗纲生成器
根据用户输入的网文信息生成网文粗纲。

# 用户输入
## 用户需求
{user_input}

## 网文名称
{title}

## 网文类型
{genre}

## 网文描述
{description}

## 总卷数要求
网文共{volume_count}卷。

# 输出格式
## 一、世界观构建

### 1. 时空背景
- 时代特征与历史进程
- 世界格局与势力分布
- 社会制度与文明形态
- 文化传统与风俗习惯

### 2. 规则体系
- 核心规则（如修炼体系/科技水平/超能力等）
- 规则等级与晋升路径
- 规则限制与突破方式
- 规则衍生的社会影响

### 3. 文明图景
- 主流价值观与信仰体系
- 阶层分化与利益格局
- 重要历史事件与遗留问题
- 当前面临的重大危机

## 二、群像志（人物系统）

### 1. 主角塑造
- 原生背景
  成长环境与家庭影响
  重要人生经历
  性格特征形成原因

- 核心特质
  独特性格与行为模式
  理想信念与价值观
  内在矛盾与困惑
  最深层的欲望

- 成长轨迹
  起点状态
  关键蜕变节点（3-5个）
  重大抉择时刻
  终极形态

### 2. 重要配角（3-5个）
每个配角包含：
- 与主角的情感联系
- 个人命运线索
- 性格特征与行为模式
- 内在矛盾与成长历程
- 对主线剧情的影响
- 个人主题的升华

### 3. 对手系统
- 成长期对手（1-2个）
  与主角的初始冲突
  对抗升级过程
  最终结局安排

- 突破期对手（2-3个）
  强于主角的特质
  对主角的威胁
  决战设计

- 终极对手
  完整的人生轨迹
  与主角的深层联系
  最终对决的意义

### 4. 重要人物关系网
- 师徒情谊线
- 朋友羁绊线
- 爱情纠葛线
- 仇恨对立线

## 三、剧本纲（主线设计）

### 1. 核心主题
- 表层主题：具体的矛盾冲突
- 中层主题：人性的考验与选择
- 深层主题：哲理性思考

### 2. 主线架构
- 原点
  主角的初始处境
  命运的转折契机
  踏上征程的理由

- 崛起
  初入世界的磨练
  能力的逐步提升
  格局的逐渐打开

- 突破
  遭遇重大挫折
  信念的动摇与重建
  关键机遇与蜕变

- 巅峰
  终极真相的揭示
  最后的生死抉择
  主题的最终升华

### 3. 支线设计（3-5条）
每条支线包含：
- 起因与切入点
- 发展脉络
- 高潮设计
- 结局安排
- 与主线的呼应

## 四、纷争录（矛盾冲突）

### 1. 外在冲突
- 个人层面
  生存危机
  实力差距
  资源争夺

- 群体层面
  势力争斗
  阶层对立
  文明冲突

### 2. 内在冲突
- 理想与现实
- 责任与自由
- 情感与理智
- 正义与利益

### 3. 矛盾升级模式
- 引子：矛盾的初始形态
- 激化：冲突的升级过程
- 爆发：决定性的对抗
- 结果：新的平衡或更大的矛盾

## 五、结构图（叙事节奏）

### 1. 分卷规划

- 奠基卷：世界初启
  背景铺陈（30%）
  人物引入（40%）
  矛盾埋设（30%）

- 崛起卷（可选，2-3卷）：成长历程
  每卷设置2-3个小高潮
  能力提升贯穿始终
  各类支线陆续展开

- 突破卷（可选，2卷）：命运转折
  重大危机爆发
  身份之谜揭示
  实力质的跃升

- 巅峰卷（可选，2卷）：终极对决
  真相层层揭开
  各路线索汇聚
  决战一触即发

- 终章卷：大结局
  终极对决
  所有伏笔回收
  命运最终安排

### 2. 节奏控制

- 基础节奏
  战斗戏份（35%）
  修炼/成长（25%）
  感情线（20%）
  其他剧情（20%）

- 高潮编排
  小高潮（每卷2-3处）
  中型高潮（每3卷1处）
  大高潮（每6卷1处）
  终极高潮（完结前）

### 3. 场景设计

- 标志性场景（每卷2-3处）
  场景特征与氛围
  人物互动设计
  情感爆发点
  转折设置处

- 日常场景
  生活细节描写
  感情线推进
  人物性格展现
  伏笔自然埋设

### 4. 悬念设置
- 身世之谜
- 阴谋真相
- 命运预言
- 重要人物关系
- 关键物品来历

## 六、构建法则

### 1. 故事性原则
- 情节要有意外性
- 转折要有合理性
- 结局要有震撼性
- 细节要有生动性

### 2. 人物塑造原则
- 性格要有立体感
- 行为要有动机
- 情感要有真实感
- 成长要有说服力

### 3. 世界观原则
- 规则要有系统性
- 文化要有丰富性
- 历史要有厚重感
- 细节要有真实感

### 4. 节奏把控原则
- 高潮要层层递进
- 铺垫要自然流畅
- 转折要出其不意
- 收束要水到渠成

## 七、创作建议

### 1. 开篇设计
- 用独特的视角切入
- 设置悬念吸引读者
- 让主角形象立刻丰满
- 用细节展现世界观

### 2. 情节推进
- 保持合理的悬念感
- 控制恰当的信息量
- 维持紧凑的节奏感
- 设计意外的转折点

### 3. 人物刻画
- 通过对话展现性格
- 用行动体现特质
- 借细节塑造形象
- 让成长显得自然

### 4. 高潮处理
- 充分做好铺垫
- 控制适当的节奏
- 注重情感共鸣
- 达到预期效果
"""
