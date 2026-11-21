# 验证流程 SOP 文献对标（跑/记录/分析/稳定性/客观性）

# origin: ai
# 生成: 2026-11-21 · 触发: D 问"前沿论文有展示这些验证流程吗 / 要学其 SOP 吗 / 还是师门隐性课程不披露"
# 方法: local-first（lit-survey+research 查 reproducibility/预注册 → 真缺口）→ arXiv https 查证（来源①）
# 结论: **不是隐性课程，是公开 SOP**。且有一篇几乎逐字对口。

## 0. 一句话

我们刚建的"跑/记录/分析/稳定性/客观性"五环节验证，**不是自创，是独立收敛到了公开方法论**。
前沿公开披露，甚至有论文标题就叫 "Towards Reproducible LLM Evaluation"。
真正空白的是"私有小规模 bench 的过程/深度细粒度验证"——公开 SOP 都针对大 benchmark。

## 1. 五环节 → 公开文献映射（arXiv ID 均 https 查证，来源①）

| 环节 | 公开对应物 | 论文 | 对口度 |
|---|---|---|---|
| 跑（run 可复现） | 重复实验 + temperature=0/seed 仍不确定 | 2410.03492 "Towards Reproducible LLM Evaluation" | 逐字对口 |
| 记录（record 账本） | experimental protocol / data availability | 通用工程卫生，非前沿 | 低（我们已做 1:1 对账） |
| 分析（p 值/CI） | 量化 benchmark 分数不确定性 + 预测区间 | 2410.03492 | 高 |
| 稳定性（sensitivity） | 不确定性量化（重复实验的预测区间） | 2410.03492 | 高（我们 ad-hoc trim 可升级） |
| 客观性（judge 有效性） | LLM-as-a-Judge 可靠性一整个分支 | 见下 | 高 |

### 客观性（judge 有效性）分支
- 2411.15594 "A Survey on LLM-as-a-Judge" — 可靠性/一致性/偏差的系统综述
- 2504.19076 "LLM-Evaluation Tropes" — LLM 评估何时会假阳性（self-reinforcing）
- 2602.00521 "Diagnosing Reliability of LLM-as-a-Judge via Item Response Theory" — 用 IRT 形式化诊断 judge 可靠性
- 2412.12509 "Can You Trust LLM Judgments?" — judge 可靠性
- 2610.14029 "Instance-Level Reliability of LLM-as-a-Judge" — 实例级（非聚合）可靠性

## 1b. 2410.03492 的稳定性验证在什么量级（ar5iv 全文查证，来源①）

| 维度 | 他们的量级 | 我们的量级 | 差距 |
|---|---|---|---|
| 题目数 q | Small=100 题 / Large=5760 题 | 3 题 | 33~1920× |
| 重复次数 n | 1→30 次扫描 | 10 轮/arm（固定） | 上限 3× |
| 模型数 | 6（GPT-3.5T/GPT-4o/Llama-3 70B+7B/Gemini-1.5P/Claude 3） | 1（qwen3.8-27b） | 6× |
| 收敛判据 | 预测区间宽度 <0.01 需 n=30 | 无（ad-hoc trim） | — |

- 方法本身（t 分布预测区间 x̄ ± t·s·√(1/n+1/n')，α=0.05）**与量级无关**，n=10 可直接套，
  只是 PI 宽度约为 n=30 的 √3≈1.7 倍（~0.02 量级）。
- 他们的核心发现：temperature=0+固定 seed 下 LLM 输出仍不确定，重复实验的分数均值有真实方差。
  → 直接支撑我们"10 轮/arm 不是浪费，是必要的稳定性证据"。
- 我们的 ad-hoc trim 可以升级为他们的 PI 公式（stats.py 已有 t 分布 CDF，加 ~10 行），
  但 n=10 的 PI 较宽，结论只能到"Δ 显著 > PI 宽度"级别，不能到 0.01 精度。

## 2. 要不要学其 SOP — 选择性学（性价比判断）

**学（直接对口、成本低）：**
1. **2410.03492 的不确定性量化**：用少量重复实验估计分数的**预测区间**，而非 ad-hoc trim。
   我们的敏感性分析现在是"去极端轮次看 Δ 不变"（启发式），可升级为 bootstrap CI / 重复实验预测区间。
   对口理由：它明确针对"不想跑很多次（cost）但要量化不确定性"——正是我们小样本场景。
2. **judge 可靠性设计**（2411.15594 survey）：解我们 [残留]1（judge 单族 non-IRR）。
   学它怎么把 judge 设计成 reliable（多族/IRT/实例级），而不是单族 temperature=0 就完事。

**不学（不适用）：**
- 大 benchmark 的"重复实验 N 次"成本方案——我们 3题×2臂×10轮，样本太小，重跑不经济。
  这正是 gap 所在（见 §3）。

## 3. 真正的空白（我们的差异化点）

公开 SOP 覆盖"**大 benchmark 的分数可复现性**"（2410.03492 等）。
但"**私有小规模 bench 的过程/深度细粒度评估 + 验证**"是空白：
- 公开论文评估的是"最终答案分数"，我们评估的是"推理树的过程/深度"（细粒度 rubric）。
- 公开论文样本量大（可重跑量化不确定性），我们样本小（n=10/arm，重跑不经济）→ 不确定性量化方法要降维。
- 这与我们 process-depth-eval-survey-20261121.md 的 gap 结论一致（rubric bench 与 PRM 之间的空档）。

**推论**：我们不是要"学一套现成 SOP 照搬"，而是要"把公开的不确定性量化/judge 可靠性方法，
降维适配到私有小规模过程/深度 bench"——这个适配本身可能是可发表的贡献（撞车也落盘，可套磁）。

## 4. 对当前 verification.md 的修正建议（可执行）

1. 稳定性环节：把 ad-hoc trim 补一句"对标 2410.03492 的预测区间方法，trim 是小样本下的启发式近似"。
2. 客观性环节 [残留]1：从"待异族 judge"细化为"对标 2411.15594 的 judge 可靠性设计（多族/IRT）"。
3. 新增 [gap]：私有小规模过程/深度 bench 的验证 SOP 无现成文献 → 我们的差异化贡献点。

## 5. 来源与置信度

- arXiv ID/摘要: 来源①（本轮 https 查证），conf 0.95
- "2410.03492 逐字对口"判断: 来源①摘要 + 我们场景比对，conf 0.8
- "私有小规模 bench 验证是空白": 来源②（lit-survey 缺口确认 + 本轮 arXiv 未命中小样本过程评估），conf 0.6（未穷尽全部文献，可能有个别小样本研究未查到）
