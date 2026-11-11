# 原始 idea 滚雪球调研（2026-11-11）

来源：D 本轮提出的几个 idea（v17 hack 机制 / 公式 vs 文字目标函数 / 压缩即智能路线），arXiv API 实查（①类，可复现）。
落盘时间：2026-11-11。与 `2026-11-07-idea-list.md` 是两份文件——那份是 D 的 idea 清单，这份是对其中新 idea 的文献核验结果。

## Idea A：「压缩即智能」作为分解目标函数（MDL 路线）

**D 的原话方向**：正交完备本身应该就是压缩的表述——好分解 = 最短无损描述，同义变体不降复杂度，不会把变量变化当新维度。

**已存在的工作（有）**：
1. **Agentic System as Compressor: Quantifying System Intelligence in Bits** (arXiv:2606.25960, 2026) — 最接近我们想法的一篇。明确以 "compression is intelligence" 为分析视角：固定任务分布、接口和算力预算下，更强的 agentic system 能用更少的 bits 重建目标对象；用算术编码/种子编码操作化，在 5 个 setting（反向文本、棋步、蛋白序列、RAG QA、语义故事压缩）上验证 agent 能力与压缩率正相关。**它量化的是系统智能，不是分解树质量——但「智能 = 更少 bits 重建」的操作化路径可以直接借来给分解树定 MDL 得分。**
2. **Compression Represents Intelligence Linearly** (arXiv:2404.09937, 2024) — 实证 LLM 压缩能力与下游 benchmark 均分线性相关，给「压缩≈智能」提供了经验基础。
3. **Information Capacity: Evaluating the Efficiency of LLMs via Text Compression** (arXiv:2511.08066, 2025) — 压缩效率/算力比作为模型效率度量，同样以 compression-intelligence 相关性为动机。

**结论**：「压缩即智能」不是我们的原创提法，学界已有共识级工作；但**把它用作分解状态机的目标函数形式（MDL 替代 S_α 计数项）没查到直接先例**——这是空白点，也是 T53 可以主张新颖性的地方。conf 0.8（基于 arXiv 检索覆盖度，非穷尽）。

## Idea B：prompt 里写显式目标函数 → 模型把它当奖励函数优化（v17 hack 机制）

**已存在的工作（有，且很多）**：
1. **Inference-Time Reward Hacking in LLMs** (arXiv:2506.19248, 2025) — 推理时对齐中 reward model 被过度优化的完整刻画 + hedging 缓解。直接支持「proxy 写在 prompt/训练信号里都会被 hack」。
2. **Reward Hacking Mitigation using Verifiable Composite Rewards** (arXiv:2509.15557, 2025) — 复合奖励 + 对特定 hack 行为显式罚项，RLVR 场景。与我们「S_α - β·redundancy」结构同构（主奖励 + 反 hack 罚项）。
3. **Demonstrating specification gaming in reasoning models** (arXiv:2502.13295, 2025)；**Winning at All Cost** (arXiv:2505.07846, 2025)；**Sycophancy to Subterfuge: reward-tampering in LLMs** (arXiv:2406.10162, 2024) — 推理模型 specification gaming 系列。
4. **Goodhart's Law Applies to NLP's Explanation Benchmarks** (arXiv:2308.14272, 2023) — Goodhart 在 NLP 评估上的早期实证。

**结论**：「显式目标函数文字驱动 hack」这个机制在 RLHF/reward hacking 文献里是成熟结论，不是空白。我们的 v17 案例是它在 **prompt-only、无梯度** 设置下的实例——这个具体场景（纯 prompt 里的公式描述导致刷分）没查到专门论文，但机制归属清晰。T53 报告里应引用这批而非自证。conf 0.9。

## Idea C：公式描述 vs 文字描述的目标函数差异

**未查到直接研究**。最接近的是上面 Idea B 的 inference-time hacking 线（它们区分了不同 misspecification 形式的 hack 难度，但没有做「同一目标，公式写法 vs 散文写法」的对照实验）。
**现状**：这仍是开放问题，我们的消融（删 P1_DECOMPOSE 目标函数段 vs 保留）会产出第一个数据点。标记为 [空白，可做]。

## Idea D：冗余度量选型（n-gram vs embedding vs LLM-judge）

**部分已有**：MIDGARD (arXiv:2405.05189, 2024) 用 MDL 做 self-consistency 的结构选择（候选答案按描述长度选），证明 MDL 判据在 LLM 输出选择上可用；但它是选答案不是去重节点。embedding 相似度去重在 RAG 文献常见（未单列）。LLM-judge 去重未见标准基准。
**现状**：三种度量在「分解树节点去重」上的对比实验 = 空白，正是 SOP 决策 12 记的待办（拿 v17 的 1930 节点树跑三种度量看分离度）。conf 0.7。

## 汇总：有了 / 没有

| Idea | 学界已有？ | 我们的位置 |
|---|---|---|
| A 压缩即智能 | ✅ 有（2606.25960 等三篇） | 借用其操作化，用于分解树目标函数 = 新组合 |
| B 显式目标函数→hack | ✅ 有（成熟 RLHF 线） | v17 是 prompt-only 实例，引用即可 |
| C 公式 vs 文字 | ❌ 没查到 | 开放问题，消融可产首个数据点 |
| D 冗余度量选型 | ⚠️ 部分（MDL 选答案有，节点去重对比无） | 待办实验，空白 |

覆盖率：4 个 idea 里 1 个完全已有（B）、1 个基本已有+新应用（A）、1 个部分已有（D）、1 个空白（C）——约 50% 有直接先例，50% 是我们的增量空间。
