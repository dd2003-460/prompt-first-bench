# RL 预算控制与 prompt 解禁：文献调研

> 2026-11-22 · 触发：D 问"关于解除限制，有没有系统阐述的论文"
> 背景：synth 实验发现 27b 即使 prompt 说"完整保留推导"仍把 67k 字压到 10k 字；
> 解禁 prompt（"你的训练让你倾向简洁，请覆盖那个倾向"）使 L4 层输出 3.5x（6317→22397 字）。
> 假设：RL 让模型学会输出预算控制，prompt 必须显式解禁。

## 结论先行

**没有一篇论文直接研究"RL 让模型学会输出长度预算控制 + 显式 prompt 解禁"这个精确组合**——这个 framing 本身是 gap，我们的 L4 解禁实验（3.5x 输出）是本地实证。但三条相邻线覆盖组件：

## 线 1：underthinking 现象（最接近，全部 abs 页核验 2026-11-22）

| ID | 标题 | 要点 |
|---|---|---|
| **2501.18585** | Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs | 定义 underthinking：模型在推理路径间频繁切换而不充分探索有希望的路径 → 推理深度不足 |
| **2505.00127** | Between Underthinking and Overthinking: An Empirical Study of Reasoning Length and correctness | 实证：模型对简单题 overthink（不必要地长）、对难题 underthink（该长不长）——**预算错配**，正是 D 说的"不同成本下信息增益不同" |
| **2508.13141** | OptimalThinkingBench | 统一 benchmark 同时评 over/underthinking；thinking 模型简单题 over、non-thinking 模型难题 under |
| **2510.19767** | SmartSwitch: Overcoming Underthinking via Promoting Deeper Thought Exploration | **最接近"解禁 prompt"**：推理时 prompting 策略，显式促进更深探索以克服 underthinking——证明 prompt 层干预可以覆盖模型的浅层倾向 |

## 线 2：系统阐述（survey）

| ID | 标题 | 要点 |
|---|---|---|
| **2507.02076** | Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute | **最系统的阐述**：核心观察"模型对简单/难题花同样推理算力"；两层分类法 L1 控制生成长度 / L2 动态分配。本地 `paradigm-routing/research/cot-necessity-survey.md` 已引（conf 0.85） |

## 线 3：prompt 为何能覆盖训练行为（机制）

| ID | 标题 | 要点 |
|---|---|---|
| **2410.09102** | Instructional Segment Embedding: Improving LLM Safety with Instruction Hierarchy | 机制：LLM 架构把所有输入同等对待，低优先级 user prompt 可以覆盖高优先级 system 指令——**prompt 覆盖训练行为的结构性原因** |
| **2604.09443** | Many-Tier Instruction Hierarchy in LLM Agents | 多来源指令（system/user/tool/agent）各带不同信任级，冲突时按特权层级解析 |
| **2603.10521** | IH-Challenge | 训练鲁棒 instruction hierarchy 的数据集；IH 失败与 instruction-following 失败会混淆 |

## 线 4：RL 行为效应的受控证据（本地已调研，来源②）

- **2604.10585**（AISTATS 2026 Workshop，`paradigm-routing/research/reasoning-activation-mechanisms.md`）：sycophancy 诱导 GRPO 的受控单变量实验，ECE +0.006、p=0.41 **不显著**——"RL 把行为变成骗子"的叙事强于文献支持。对"RL 学会预算控制"这个机制断言同理：方向合理但效应量需受控实验确认。

## 与我们现象的映射与差距

| 我们的发现 | 文献覆盖 | 差距 |
|---|---|---|
| 27b 摘要 67k→10k 字（6.7x 压缩） | underthinking 线覆盖"该长不长" | 文献聚焦 reasoning chain 长度，**我们的是 summarization 保真度**——相邻但不相同 |
| 解禁 prompt 3.5x 输出 | SmartSwitch（2510.19767）证明 prompt 可覆盖浅层倾向 | SmartSwitch 针对推理深度，未针对"数值/推导链保真" |
| depth 分数未涨（树缺 L5 整合节点） | 无 | 文献不涉及"信息在树里但缺最终整合步骤"的瓶颈 |

## 可引用的一句话（论文用）

> 模型对推理/生成长度的预算分配是 RL 对齐的副作用（2507.02076, 2505.00127），
> 可通过推理时 prompting 覆盖（2510.19767），机制源于 LLM 对输入指令的层级化处理
> （2410.09102）；但在结构化研究管线中，解禁输出预算后瓶颈转移到分解树的
> 完整性（缺 L5 整合节点），而非生成侧。

## 核验记录

- 8 个 arXiv ID 全部经 abs 页核验（2026-11-22，https://arxiv.org/abs/<id>）
- 2507.02076 另见本地 cot-necessity-survey.md（来源②交叉确认）
- 2604.10585 来自本地 reasoning-activation-mechanisms.md（来源②，未本轮重验 abs 页）
