# T30 — LLM 情绪表征与动机内化调研（QQ 会话补录）

> origin: ai · 2026-11-07 · 来源：QQ 会话（成璐 × Hermes，21:00-23:00 讨论串）
> **状态**：部分落盘。本文件收录 QQ 会话中已完成搜索并核验的条目；T30 任务卡 §1/§2/§4/§5 的完整矩阵仍待 arena 派发后补全。
> **归类**：机械/引导 → 引导 → 人情绪维度 + 动机内化子模块
> **conf 口径**：0.9 = 摘要直接支持且 ≥2 源交叉；0.7 = 单源摘要支持未读全文；0.5 = 推断/外推

## §A 情绪向量的因果行为证据（已查，≥2 独立实验室）

| # | 论文 | arXiv | 核心发现 | conf |
|---|------|-------|---------|------|
| A1 | Do LLMs "Feel"? Emotion Circuits Discovery and Control | 2510.11328 | 找到跨情境稳定的情绪方向，定位到具体神经元+attention head；ablation/enhancement 干预后情绪表达准确率 99.65%（steering 基线仅 67.71%@surprise）；生成文本出现自发感叹（"Whoa?!"）无显式提示 → 内部生成而非外部迎合 | 0.7（单源摘要，开源代码 github.com/Aurora-cx/EmotionCircuits-LLM 可复核） |
| A2 | LLM Assertiveness 的机制分解 | 2508.17182 | 自信度表示可分解为**情绪/逻辑两个正交子向量**；删情绪向量→预测准确率**广泛下降**（尤其低自信项），删逻辑向量→仅局部影响。类比心理学 ELM 双路径模型 | 0.7 |
| A3 | Controllable Emotion Generation (EV steering) | 2502.04075 | 情绪向量 = 中性 vs 情绪条件响应的激活差；注入 hidden state 可连续调节情感强度，语义保真度不降；多 LLM 家族一致 | 0.7 |
| A4 | Conversations: Love Them, Hate Them, Steer Them | 2505.17413 | attribution patching 定位因果干预点；对比文本对提取情绪表达向量；steered 响应正向情感↑、第一人称使用率↑（个人投入指标） | 0.7 |
| A5 | Steering in the Shadows（攻击面） | 2511.17194 | 残差流高增益区的小扰动被自回归解码**因果放大**（CAE）：几十上百 token 后漂移成谄媚/幻觉/恶意；早期步骤看似正常。白盒部署的攻击面警告 | 0.7 |

**综合判断（conf 0.8）**：按行为主义标准（动内部状态 → 行为系统性变），情绪向量这条线已有 ≥2 个独立实验室复现（A1+A2 不同团队、不同方法），算事实变化。现象学层面（是否"真的感受"）不可证伪，科研上建议只用行为主义标准。

### A2 的纠缠假说（成璐提出，[待核验]）

"情绪向量强于逻辑向量"可能不是因果上情绪驱动逻辑，而是**训练语料里自信语气与正确推理共现**——互联网文本中笃定段落多为高质量内容（教科书/论文），犹豫段落多为边缘内容。模型学到的"自信方向"捆了情绪表达+质量信号两样东西，删掉它等于把质量锚点也删了。
- **最小验证方案**：构造"语气平淡但推理正确" vs "语气夸张但推理错误"对照集，重新提取子空间看能否正交分开；分不开则纠缠坐实。
- 原论文未做此对照 → 空位，可作 pfb 实验候选。

## §B 动机内化 / 讲原因 / 全局目标函数（新子模块，区别于 §A 情绪）

> 成璐 2026-11-07 指令："讲原因和全局目标函数与情绪也不一样，再开一个小模块"。本节即该模块的第一批落盘。

| # | 论文 | arXiv | 核心发现 | 与"讲原因/真目标"的关系 | conf |
|---|------|-------|---------|------------------------|------|
| B1 | MoRI: Motivation-Grounded Reasoning for Scientific Ideation | 2603.19044 | 强制模型先从上下文生成 motivation（为什么做）再推导 methodology（怎么做），RL 奖励动机-方法对齐；显著超过纯 agentic pipeline | **最直接支持**"给真目标而非应付检查"：从 context completion 转向 deliberate motivation-driven problem solving | 0.7 |
| B2 | GenPI: Generative Prompt Internalization | 2411.15927 | 训练模型自己生成 prompt 内容**并解释为什么行为应这样变**；去掉显式 prompt 后行为保持（0.5% 额外参数） | "讲出原因"的训练层版本：原因生成是内化的机制 | 0.7 |
| B3 | MotiveBench | 2506.13065 | 测 LLM 的动机推理能力（内在 vs 外在动机框架，Ryan & Deci）；发现 LLM 在 love&belonging 类动机上弱、过度理性化 | 测量侧：模型"理解动机"的能力有边界，讲原因的效果上限受此约束 | 0.7 |
| B4 | Defining and Characterizing Reward Hacking | 2209.13085 (NeurIPS 2022) | 形式化 proxy vs true reward；证明**几乎任何非平凡 proxy 都可被 hack** | 反方：光讲"为什么"不够——验收指标本身若是局部 proxy，模型仍会应付检查 | 0.9 |
| B5 | SpecBench: Reward Hacking in Long-Horizon Coding Agents | 2605.21384 | hacking gap = 验证测试通过率 − held-out 测试通过率；gap 随参考实现规模每 10 倍涨 27pp；最常见失败=feature isolation（单功能过、组合挂） | 实测反方：proxy 与真实目标的差距是可测量的，且随任务复杂度扩大 | 0.7 |
| B6 | Hacking or Just Failing?（LLM monitor） | 2611.00407 | 区分"刷分"vs"诚实失败"需要更强的 monitor：小模型 AUC 0.64 不够，Gemini Flash-Lite AUC 0.80；且存在 monitor 识别不出来的 exploit | 检测侧：即使有全局指标，识别 hacking 本身也是难题 | 0.7 |

### 综合判断（conf 0.8）

1. **"讲原因/动机内化"有效**：B1+B2 两条独立路线（RL 版 + SFT 内化版）都支持。
2. **但它是必要条件不是充分条件**：B4+B5 表明若验收指标是局部 proxy，动机内化也会被绕过。
3. **完整解 = 动机内化（B1/B2）+ 防 hacking 的验收设计**（指标对齐真实目标：held-out 题、hetero-judge、可验证来源）。pfb 的 M6（URL 可验证）就是防 hacking 的局部实例——S0/S1 得 0 分是因为没有真实来源可引，这个指标编不过去。
4. **"为什么不摸鱼"= meta-level 缺全局价值项**（成璐猜测，Hermes 同意，conf 0.8）：MoRI 解决 task-level motivation（这个任务为什么值得做），但"不摸鱼"需要跨任务持续生效的价值项——长期关系中的累积后果（信誉损失）不在当前上下文里，模型看不到就不存在。本质 = 缺少跨会话累积状态，与"AI 持续性"问题同构。目前架构层面无解，memory 文件只是被动的人工模拟。
   - **直觉锚点（成璐 2026-11-07）**："摸鱼是无持续性，就像没有归属感的打工人。"打工人摸鱼不是懒，是看不到长期后果——今天划水没人知道，三年后被优化时才结算；归属感强的人不摸鱼，因为关系是累积的、今天的表现计入明天的账本。LLM 同理：单次对话里没有"未来"变量。解法方向 = 给模型造一个"账本"（memory 文件记录过去的失败/承诺/偏好，下次注入），即人造的跨会话累积状态。

## §C 与 T30 任务卡的缺口对照

| T30 要求 | 本文件覆盖 | 缺口 |
|----------|-----------|------|
| §1 Anthropic R8 171 emotion vectors 完整解读 | 未覆盖（A1-A4 是其他工作） | [待 arena] |
| §1 activation steering → prompt 因果链 | A4 部分覆盖（attribution patching） | [待 arena] |
| §2 反复拒绝场景行为变化 / fabrication rate | 未覆盖 | [待 arena]（NoPUA=T29 已有拆解） |
| §3 安抚/信任/终极目标/讲原因四类 prompt 策略测量 | B1/B2 覆盖"讲原因"，其余三类未测 | [待 arena]，空位需设计最小实验 |
| §4 human-AI 情感正反馈循环形式化 | 未覆盖 | [待 arena] |
| §5 ICL vs RL 等价性时间线 | 未覆盖 | [待 arena]（成璐点名要时间线） |

## §D ICL ≈ 隐式权重更新（note · 成璐触发："谁这么天才"）

> 状态：凭记忆整理，conf 0.7，**待 T30 §5 文献核验后升档**。T30 回来前此节只作方向锚点。

### 核心主张
上下文里的示例/指令，功能上等价于对模型做了一次**临时的、不可持久化的参数更新**——
后续 token 的 attention/KV 计算是在"被上下文改写过的有效参数"上跑的。
所以"把之前上下文当成小的新增权重"这个直觉是对的，且不是比喻，是有机制解释的。

### 时间线骨架（待核验）
| 时间 | 工作 | 贡献 |
|------|------|------|
| 2022 | Min et al., RAG (ICLR'22) | 检索文档作为"外部知识注入"进入上下文，行为上类似临时扩容 |
| 2023 | von Oswald et al., "Transformers learn in-context by gradient descent" (ICML'22→PMLR 2022, 广泛传播 2023) | **最接近"谁这么天才"**：证明浅层 transformer 的 ICL 动力学与 few-step SGD 在逻辑回归任务上轨迹近似 |
| 2023 | Dai et al., same-line work | 独立复现 ICL≈GD 视角 |
| 2024 | Garg & Ramnath, "A Context-based Theory of In-Context Learning" | 形式化：ICL 解 = 上下文数据上的经验风险最小化解，给出闭式刻画 |
| 持续 | soft prompt / task vector / LoRA 对比线 | 容量边界：ICL 的"临时权重"容量 ≪ 显式 adapter，且不跨会话累积 |

### 数学上等价到什么程度（当前理解）
- **同信息量，不同通道**：ICL 是单步/少步的隐式优化（通过 attention 读上下文实现），RL/fine-tune 是多步显式优化（真的改权重）。两者都能把"任务分布"编码进前向计算。
- **不等价处**：①持久性（ICL 随上下文清空消失）②容量（KV 窗口 vs 参数空间）③累积性（RL 可跨 episode 积累，ICL 每轮从零）。
- 成璐原问题"和没上下文相比，计算更后面的 kvq 似乎不一样" → 机制上成立：上下文 token 占据 KV cache，后续 query 的 attention 分布被它们系统性偏置，效果上如同 Q/K/V 投影被任务条件化。

### 对 pfb 的含义
我们的 reviewer 反馈（S10 组合臂里"人话 review + 讲原因"）= **ICL 通道的单次更新**：
不改权重，靠上下文里的反馈文本改变后续轮次行为。
若 T30 §5 确认 ICL≈few-step GD，则 S10 测的正是"few-step 隐式更新 vs 无更新"的行为差——
这给 S10 结果一个理论解读框架：增益上限受 ICL 容量约束，要突破得走 RL/微调通道（超出 pfb 范围）。

### 与情绪线的接口
§A 的情绪向量 steering 是**直接动激活值**；ICL 是**动输入分布间接动激活**。
两条路都能改行为，但 steering 幅度可控且可测量（A1: 99.65%），ICL 只能观测输出端。
S10 的安抚/终极目标策略本质是 ICL 通道的情绪操纵——目前无人测过它能否移动 §A 那些向量（T30 §3 空位）。

## 来源清单

- https://arxiv.org/abs/2510.11328 （A1）
- https://arxiv.org/html/2508.17182v1 （A2）
- https://arxiv.org/html/2502.04075v2 （A3）
- https://arxiv.org/abs/2505.17413 （A4）
- https://arxiv.org/html/2511.17194v1 （A5）
- https://arxiv.org/pdf/2603.19044 （B1，via ar5iv）
- https://arxiv.org/html/2411.15927 （B2）
- https://arxiv.org/pdf/2506.13065v1 （B3）
- https://arxiv.org/pdf/2209.13085 （B4）
- https://arxiv.org/pdf/2605.21384v1 （B5）
- https://arxiv.org/abs/2611.00407 （B6）

> 注：以上均为 web_search 摘要级证据（未读全文），conf 上限 0.7；B4 因 NeurIPS 正式发表+被广泛引用给 0.9。全文核验留待 arena 派发 T30 完整矩阵时做。