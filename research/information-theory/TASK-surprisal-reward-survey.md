# 调研任务书 — 信息论奖励/贡献度方法（供 arena agent mode）

> origin: ai · 2026-10-29 · r60
> 目标：为 rubric-v3 的 O3（gold 节点命中计分）找到有文献支撑的"按深度/意外性加权"方案，替代现在拍脑袋的 tier 权重（L4×2 / L5×2 / L6×3）。

## 背景（最小上下文）

- 我们在给 LLM pipeline 的产出打分：产出是一棵分解树（如硬件选型：成本→性能/价格→推理→prefill/decode→微架构过程 gemm/attention→瓶颈判断），对照一棵预先冻结的 gold 树逐节点计分
- 成璐的提议：**深层节点权重更高**，且权重应该反映"这个拆分有多不显然"——如果一个拆分几乎必然被想到（如 prefill/decode 拆分，概率≈1），贡献就低；越意外的拆分贡献越高。形式上：贡献 ∝ 1/P(该拆分|父节点)，或 log 后计分
- 直觉上这对应信息论里的东西： surprisal = -log P，信息量 = 自信息。需要确认业内是否已有成熟做法，以及具体怎么落地到"树节点贡献分"

## 要调研的方向（每个方向给出：代表工作 + 核心公式 + 能否直接迁移 + 迁移时的坑）

### D1 决策树/规则学习中的特征贡献
- 方向：树模型里每个分裂节点的"重要性"怎么定义？Gini importance / permutation importance / SHAP for trees
- 关键问题：这些是"事后对数据分布的贡献"，能不能改成"先验上的意外性"（即 P(该分裂|领域常识) 越小分越高）？有没有人做过 prior-based node importance？

### D2 程序合成/结构化输出的惊讶度奖励
- 方向：program synthesis、structured prediction 里有没有用 surprisal / cross-entropy 做 reward shaping 的工作？
- 关键问题：LLM 生成结构化对象（树/代码/表格）时，token-level surprisal 和 structure-level surprisal 哪个更合理？有没有 "structural information gain" 这类概念？

### D3 多跳 QA / 推理链的中间步骤奖励
- 方向：process reward model (PRM) 文献——每一步推理给多少分？step-level reward 怎么设计？
- 关键问题：PRM 通常是学出来的（标注每步对错），有没有**解析式**的 step reward（不靠训练，直接用结构属性如深度/分支因子/意外性算分）？MATH-Shepherd、Let's Verify Step by Step 之外的解析方案？

### D4 科学发现/假设生成的 novelty 度量
- 方向：AI4Science 里衡量"新假设/新发现"有多 novel 的方法——通常基于与已有知识的距离
- 关键问题：novelty 是不是就是 1/P(hypothesis|existing knowledge)？有没有形式化定义（如 minimum description length 增量、Bayes factor）？MDL 的"压缩增益"能不能当节点贡献分？

### D5 信息论奖励在 RLHF/RLVR 中的实际用法
- 方向：RL 训练中 reward 里显式包含信息论项（KL、mutual information、information gain）的做法
- 关键问题：information gain 作为 reward 的已知陷阱（reward hacking：模型学会制造"看起来信息量大"但实际无用的内容）？对我们场景（judge 按表打分而非 RL 优化）这些陷阱还成立吗？

### D6 具体候选公式的对比评估
把下面几个候选公式放在一起，从"可计算性/抗 gaming/理论依据"三个角度对比：
1. `w(node) = depth`（线性深度，现状近似）
2. `w(node) = 1/P(split | parent, domain-prior)`（成璐原始提议）
3. `w(node) = -log P(split | parent, domain-prior)`（自信息/surprisal）
4. `w(node) = -log P(node-subtree | rest-of-tree)`（条件互信息：知道这个子树后对整树的惊讶减少量）
5. `w(node) = MDL_gain = log P(data|model-with-node) / P(data|model-without-node)`（贝叶斯因子/压缩增益）
6. `w(node) = 1/branching_factor_at_parent`（分支越多每个子节点分越低——反直觉，检验是否合理）

**P 从哪来是关键难点**：domain-prior 怎么估计？选项：(a) 让 judge LLM 估 P("一个熟悉该领域的工程师看到父节点后，提出这个拆分的概率")——本质是让 LLM 当 prior oracle；(b) 用多个独立 LLM 跑同一父节点看各自提出什么拆分，经验频率当 P；(c) 人工标注小样本。三种方案的成本/可靠性/可复现性对比。

## 输出格式

```json
{
  "kind": "ralph_web_llm_cross_check",
  "target": "info-theory-reward-survey",
  "responses": [
    {"provider_id": "<会话标识>",
     "findings": [
       {"direction": "D1..D6", "works": ["作者+年份+链接"],
        "core_formula": "...", "transferable": true/false,
        "pitfalls": "...", "recommendation": "..."}
     ],
     "final_recommendation": {
       "formula": "选哪个候选公式",
       "prior_source": "P 从哪来",
       "rationale": "...",
       "known_failure_modes": "..."
     },
     "observed_at": "<ISO8601 带时区>"}
  ]
}
```

要求：≥2 个不同 LLM 服务交叉核验（本回执之外再找一家复核 final_recommendation），矛盾点记录在 findings 里。