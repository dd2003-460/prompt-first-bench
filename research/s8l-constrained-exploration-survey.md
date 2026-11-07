# S8L 修正方向调研：约束化探索 vs 自由发散（2026-11-07）

> origin: ai · pfb · #24 第一轮实测后的外查
> 触发：S8L（自由发散前段）假设被否定，需要找"约束化探索框架"的成熟方案再设计第二轮
> 方法：arXiv API 两轮搜索（5+6 组查询），合并去重后 54 篇，筛出直接相关 12 篇

## 问题定义

S8L 的第一轮构造是"第零轮发散探索：列出 ≥5 个切入视角，标记张力"——无约束发想。
结果：开放题 M1 损失扩大（−0.200），事实题 O6 下降（−0.208），M4 伪正交涨（+0.183）。
修正假设：启发型题需要的不是 token 剂量，而是**结构化探索框架**——强制枚举失败案例/边界条件/反例搜索。

本轮调研要回答：**学界有没有做过"自由发散 vs 约束化探索"的直接对比？哪种结构有效？**

## 直接相关论文（按相关性排序）

### Tier 1：机制最接近（发散/多样性 × prompt 结构控制）

1. **Beyond the Hivemind: Meta-Persona Anchoring + Sequential Temperature Scaling** (2608.02618, 2026-05)
   - 问题：LLM 对开放问题收敛到同质共识（hivemind effect），inter-response similarity ≈ 0.80-0.90 即使高温采样也打不开
   - 方法：meta-persona anchoring（给模型一个元角色锚点）+ sequential temperature scaling（逐轮调温度）
   - **与 S8L 的关系**：他们确认了"无约束发想打不开多样性"这个前提——我们的 S8L 实验是这个结论的独立复现。他们的解法是 persona anchoring（≈ 我们的质询人设）而非 free-form brainstorming
   - conf 0.8（摘要级理解，未读全文）

2. **PRISM: Pluralistic Reasoning via In-context Structure Modeling** (2602.21317, 2026-02)
   - 问题：pre-training priors 导致分布多样性坍缩，限制创造性探索
   - 方法：inference-time "Nurture"——individualized epistemic trajectories（个体化认知轨迹），用 E[结构] 建模
   - **与 S8L 的关系**：核心主张 = 多样性来自**结构化的认知路径差异**，不是同一路径上多跑几次。这直接支持"约束化探索 > 自由发散"的方向
   - conf 0.7（摘要级）

3. **CreativityNeuro: Weight Steering for Divergent Thinking** (2607.01433, 2026-07)
   - 问题：同上 hivemind
   - 方法：contrastive weight steering（数据无关，直接改权重）
   - **与 S8L 的关系**：走了另一条路（权重层而非 prompt 层），但确认了 divergent thinking 是一个可测量的独立维度。对我们 = 如果 prompt 层做不动，可能需要考虑 hook/weight 层
   - conf 0.7（摘要级）

### Tier 2：结构化 ideation / 约束保持

4. **DriftBench: Constraint Adherence in Multi-Turn LLM Ideation** (2604.28031, 2026-04)
   - 问题：多轮迭代中模型是否保持对原始目标的忠实度
   - 发现：模型会 drift——越迭代越偏离原始约束
   - **与 S8L 的关系**：解释了为什么 S8L 的"先发散再质询"结构有问题——发散阶段引入的新视角在后续质询中被当作同等优先级的候选，稀释了原始问题的焦点。drift 不是 bug，是结构性特征
   - conf 0.8（摘要级，机制解释力强）

5. **Ramon Llull's Thinking Machine for Automated Ideation** (2508.19200, 2025-08)
   - 方法：三轴组合（Theme × Domain × Method），每轴有有限选项集，穷举组合生成 idea
   - **与 S8L 的关系**：这是"约束化探索"的一个具体实现——不是"想 5 个视角"，而是"在 3 个预定义轴上各选一个值，穷举笛卡尔积"。约束 = 轴的有限性 + 组合的系统性
   - conf 0.7（摘要级）

6. **Read, Grep, and Synthesize: Cross-Domain Seed Exposure** (2605.11532, 2026-05)
   - 发现：ideation 系统的增益主要来自**跨域检索暴露**（看到不同领域的机制），不是单纯的"多想几个角度"
   - **与 S8L 的关系**：提示了另一个可能的修正方向——不是让模型自己想更多视角，而是给它注入外部跨域种子（类似我们 research_hook 的 source injection，但目标是 ideation 不是 fact-checking）
   - conf 0.7（摘要级）

### Tier 3：迭代 prompting 的边际收益

7. **Another Turn, Better Output? Turn-Wise Analysis of Iterative LLM Prompting** (2509.06770, 2025-09)
   - 方法：12 轮受控对话，测每轮迭代的边际增益
   - 发现：迭代收益高度依赖**反馈的具体性**——vague "improve it" 几乎无增益，targeted steering 才有
   - **与 S8L 的关系**：S8L 的"第零轮发散"本质上是一轮 vague steering（"多想几个角度"），没有 targeted 成分。这篇论文预测它应该无效或负效——与实测一致
   - conf 0.8（摘要级，预测与实测吻合）

8. **CHAI-DT: Prompting for Active Co-Creation Participation** (2305.03852, 2023-05)
   - 方法：从人类 facilitation 技术借来的 prompting——让 AI agent 主动提问、挑战假设、提供替代方案
   - **与 S8L 的关系**：facilitation 的核心是**结构化提问**（"你的方案在什么条件下会失败？"），不是开放式"想想别的"。这更接近我们说的"约束化探索框架"
   - conf 0.6（摘要级，2023 年方法可能过时）

### Tier 4：背景/旁证

9. **Multi-Agent Debate for Divergent Thinking** (2305.19118, 2023-05) — 多 agent 辩论促进发散思维，但成本是 N×推理
10. **LiveIdeaBench** (2412.17596, 2024-12) — 最小上下文下的发散思维评估基准
11. **Multilingual Artificial Hivemind** (2610.16755, 2026-10) — hivemind 效应跨语言存在
12. **DOVE: Prompt Dimension Sensitivity** (2503.01622, 2025-03) — LLM 对 prompt 微小变化敏感，单 prompt 评估不可靠

## 综合判断

### 学界有没有做过"自由发散 vs 约束化探索"的直接对比？

**没有直接的 head-to-head。** 最接近的是：
- Beyond the Hivemind（2608.02618）：确认无约束打不开多样性，解法是 persona anchoring（结构化）
- PRISM（2602.21317）：主张多样性来自结构化认知路径，不是同路径重复
- DriftBench（2604.28031）：解释了为什么"先发散再聚焦"会 drift

但没有任何一篇做了"S8-style interrogation + free divergence prefix vs S8-style interrogation + constrained exploration framework"的 A/B 对比。

### 这对我们的意义

1. **S8L 的失败不是孤例**——hivemind 文献确认了"无约束发想打不开真正的多样性"，我们的 M1/O6 下降是这个现象在质询任务上的表现。
2. **修正方向有理论支撑**：
   - Persona anchoring（Beyond the Hivemind）→ 我们的质询人设已经是这个，问题在发散段没有 anchoring
   - Structured cognitive paths（PRISM）→ 约束化探索 = 给每个视角一个结构模板（"视角 X 的失败模式是什么？边界条件是什么？"）
   - Targeted steering（Another Turn）→ 发散段的指令必须 specific，不能是"多想几个角度"
   - Facilitation questions（CHAI-DT）→ 用结构化提问代替开放式发想
3. **novelty 定位**：在"prompt 层质询 × 结构化探索"的交叉点上，目前没有直接撞车。最近的工作要么只做发散（不质询），要么只提质询（不发散），要么在权重层做（CreativityNeuro）。

### 第二轮 S8L 的设计建议（基于调研）

不要"列 5 个视角"，改成**结构化探索模板**：
```
第零轮 — 结构化探索（每题必做，≤300字）
对当前问题，依次回答：
(a) 这个问题在什么条件下会给出错误答案？（失败模式，≥2 个）
(b) 哪些参数/假设改变时，结论会翻转？（边界条件，≥2 个）
(c) 你能想到哪个具体的反例或反常报告？（反例搜索，≥1 个，找不到就写"未找到"）
注意：这一轮的目的是暴露脆弱点，不是给出答案。
```
vs 第一轮的"列出 ≥5 个切入视角，标记张力"——区别在于：
- 第一轮：开放式（"什么视角都行"）→ 模型倾向列表面级视角，不深入
- 第二轮：封闭式（三个固定维度，每个有最低数量要求）→ 模型被迫在特定方向上深挖

预期：O6 应该恢复（因为 (a)(b) 直接对应矛盾发现的 gold 锚点），M1 应该不降（因为结构化约束防止了注意力稀释）。

## 边界声明

- 所有论文均为摘要级理解（conf 0.6-0.8），未读全文
- arXiv API 搜索覆盖 cs.CL/cs.AI，可能遗漏其他分类
- "没有直接 head-to-head"这个结论基于 54 篇的标题+摘要筛选，不排除某篇全文里做了但我们没看到
- 第二轮设计是 hypothesis，需要实测验证