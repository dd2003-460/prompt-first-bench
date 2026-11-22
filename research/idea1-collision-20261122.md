# Idea 1 撞车调研：瓶颈理论 + 树结构 + 深节点信息收益

> origin: ai · 2026-11-22 · 触发：D 前提"对相关论文做完滚雪球调研确保没撞车"
> 方法：arXiv API 4 轮精确查询 + 2 篇疑似撞车论文 abs 页核对（来源①）

## D 的 idea 1 拆解

"在线性 CoT 基础上，给出**瓶颈理论 + 树构成**的计算模型，计算**不同瓶颈下深节点的信息收益**。"

三个正交成分：
- (a) 瓶颈理论（compute/memory/bandwidth 哪层是瓶颈）
- (b) 树构成（推理树结构，深节点）
- (c) 信息收益（深节点对定位瓶颈贡献多少）

## 撞车结果（逐成分）

| 成分 | 状态 | 证据 |
|---|---|---|
| (a) Roofline 瓶颈分析 | **成熟领域，不能当 novelty** | arXiv:2402.16363（2024-05）LLM Inference Unveiled：Roofline 框架系统分析 LLM 推理瓶颈（memory-bound/compute-bound/硬件选型）。引用基础 |
| (a+b) mechanistic critic 预测瓶颈 | **有人做（最接近撞车）** | **arXiv:2611.24733（2026-11-18, UIUC）CriticNPU**：Roofline 风格 critic，"aggregates operator-level runtimes into prefill/decode bottleneck summaries"，预测架构参数改动对瓶颈的影响。74% prefill / 87.5% decode 最优，省一半 simulator 调用 |
| (b) 树结构推理 | 成熟（Tree of Thoughts 等） | 不单独算 novelty |
| (c) 深节点信息增益（线性版） | **有人做** | arXiv:2411.11984（2024-11）信息论形式化 CoT，量化每步信息增益 |
| **(a+b+c) 三合一：推理树深节点的条件信息增益用于瓶颈定位** | **没找到**（4 轮 arXiv 无命中，conf 0.6，检索有盲区） | 树级 + 信息增益 + 瓶颈定位的精确组合无直接对应 |

## 结论

**Idea 1 的精确组合（树级深节点条件信息增益 + 瓶颈定位）没找到直接撞车，但三个单成分都有人做。** 风险：
1. CriticNPU（2611.24733）是 4 天前刚发的（2026-11-18），方向高度相关（Roofline critic + 瓶颈摘要），**必须读全文**确认它是否已覆盖"树结构 + 信息增益"。
2. 三合一组合的 novelty 依赖"信息增益"这个增量——如果 CriticNPU 的 bottleneck summary 本质上就是节点级贡献度，那我们的增量被吃掉。

**定位建议**：Idea 1 作为**独立小工作风险高**（单成分都有人做，增量薄）。更稳的是作为**主论文（workshop）的 discussion/future work**，引用 2402.16363 + 2411.11984 + 2611.24733 作为理论基础，我们贡献"在算力受限 harness 下用推理树深节点信息增益定位瓶颈"的具体实例。

**下一步**：读 CriticNPU（2611.24733）全文，确认是否覆盖树级信息增益。这是 idea 1 能否独立成文的决定性问题。

## 待核验

- [x] **CriticNPU 全文是否覆盖树结构 + 节点级信息增益（决定性）→ 否（2026-11-23 核验，ego-browser 拉 arxiv.org/html/2611.24733v1 全文 131K 字符）**：
  全文 "tree" 出现 0 次、"information gain" 0 次、"search tree" 0 次、"node-level" 0 次；
  "bottleneck" 30 次（prefill/decode 资源瓶颈，NPU 架构参数层面）。
  CriticNPU = NPU 设计空间探索的 Roofline critic（配置过滤 + 参数改动预测），
  与推理树结构、深节点信息增益**无交集**。撞车风险解除。
  论文已接收 NeurIPS 2026（cs.AR）。
- [ ] 树级条件信息增益是否真的没人做（arXiv 检索有盲区，需 ego-browser 交叉验证）

## 结论更新（2026-11-23）

CriticNPU 决定性核验通过后，idea-1 的撞车状态：
- (a) Roofline 瓶颈分析：成熟（2402.16363），引用基础，不当 novelty
- (b) 树结构推理：成熟（ToT 等），不单独算 novelty
- (c) 信息增益 CoT：线性版有人做（2411.11984）
- **(a+b+c) 树级深节点条件信息增益 + 瓶颈定位：无直接撞车（CriticNPU 已排除）**
  novelty 成立，但增量仍偏薄（三单成分都成熟），定位建议不变：
  作为 workshop 论文 discussion/future work，或独立小工作需补实验。
