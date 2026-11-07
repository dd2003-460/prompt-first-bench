# Self-Judge "噪声惩罚"现象：文献对照与机制假设

> origin: ai
> 触发：成璐 2026-11-08 问"自我裁判居然会觉得噪声?有调研过这方面倾向和规律的论文吗"
> 状态：调研完成，机制假设立起，待对照实验验证
> conf：文献事实 = 本轮 web_search 实查（高）；机制归因 = 推断（0.7，待实验）

## 1. 我们观察到的现象（pfb 内部证据）

同一批 S8L 输出（自由发散前段 + 质询），两个 judge 打分方向相反：

| 指标 | self-judge (27b 自评) | B-face (qwen2.5-7b 异族) | 翻转方向 |
|---|---|---|---|
| Q1 O6 | −0.21（相对基线） | **+0.25** | 负→正 |
| Q5 M1 | −0.20 | **+0.283** | 负→正 |
| M4 伪正交 | 出现 | 消失 | — |

来源：`experiments/stage-ablation/runs/s8-report.md`（commit b7ce0ef9 "S8L B-face翻转"）。
人话：自己评自己的发散输出 → 打低分；换个模型评 → 看到实质增益。

## 2. 文献对照（本轮 web_search，arXiv / ACL Anthology）

### 2.1 主流 verbosity bias 方向是"偏爱更长"——与我们相反

- GPT-4o-mini 在内容相同、仅长度不同的对比里 **100% 选更长的**；markdown 格式也 100% 偏好（arXiv:2607.02104, "When Can You Debias an LLM Judge?"）。
- MT-Bench 上 verbosity 系数显著为正（CEUR Vol-4275, "Accounting for Bias Enables Sustainable LLM Evaluation"，β_verbosity = +0.163）。
- 多篇综述一致："judges prefer longer responses regardless of quality"（BabelJudge arXiv:2606.22329; PUAUDIT arXiv:2606.19057）。

**结论：经典 verbosity bias 奖励长度，不惩罚额外内容。我们的现象不是它。**

### 2.2 关键区分：apparent substance vs raw length

arXiv:2607.02104 明确说：**"verbosity bias is about apparent substance, not raw length"**——judge 奖励的是"看起来有实质"的展开，纯 padding 反而被惩罚。
→ 这跟我们对上了：S8L 的发散如果**结构松散**，judge 可能判定为"没有 apparent substance 的额外内容"→ 扣分。

### 2.3 最接近的机制：self-preference = perplexity 偏好

arXiv:2410.21819（Wataoka et al., NeurIPS 2024 Safe Generative AI Workshop）：
- LLM judge 给**低困惑度**（更熟悉、更可预测）的文本打高分，无论是否自己生成。
- "the essence of the bias lies in perplexity... LLMs prefer texts more familiar to them."
→ **自己生成的非典型发散内容，对自己 perplexity 高 → 被自己的 judge 压低**。独立 7b judge 没这个自参照偏好，所以看穿实质。

### 2.4 其他相关偏差（方向不符，记录备查）

- **Distraction / Irrelevant Detail Bias**（arXiv:2510.12462）：judge 被无关细节吸引 → 但方向是"打高分"，不符。
- **Self-Enhancement / same-family affinity**（Panickssery et al. 2024; CEUR Vol-4275 λ_same-family > 0）：同族偏好 → 方向是"给自己家打高分"，与"惩罚自身发散"相反。
- **Pointwise vs Pairwise**（arXiv:2504.14716, COLM 2025）：pairwise 更易被 distractor 操纵（35% 翻转），pointwise 更稳（9%）。我们用 pointwise，理论上抗噪，但 self-perplexity 偏好在 pointwise 下仍成立。
- **Refine-Aware Bias**（llm-judge-bias.github.io）：judge 知道答案经过"精炼"后会改变判断 → 提示：judge 对"生成过程元信息"敏感，我们的 self-judge 知道文本是自己发的，可能触发类似效应。

## 3. 机制假设（待验证）

**H：flip = self-perplexity 偏好 × 松散发散被判"无 apparent substance" 的复合效应。**

- 子假设 H1（perplexity）：控制内容相同、只变"是否像该模型典型输出"，self-judge 分数随典型性上升，异族 judge 不变。
- 子假设 H2（结构）：同一段发散内容，结构化排版 vs 松散流水账，self-judge 分差 > 异族 judge 分差。
- 子假设 H3（题型依赖）：窄事实题（Q1）flip 强于开放题（Q5），因为事实题的"正确收敛"更典型，发散更显得离群。（注：我们数据里 Q1/Q5 都 flip，但幅度不同，需量化。）

## 4. 最小对照实验设计（下一步执行）

**目的**：分离 H1/H2/H3，确认 flip 的机制归属，支撑"non-trivial"判断。

**材料**：取 S8L-Q1-r1 的输出（含发散段），构造 4 个变体：
1. V0 = 原样（松散发散）
2. V1 = 同内容，重排成结构化列表（控 H2：内容不变，结构变）
3. V2 = 同结构，换成"典型收敛式"措辞（控 H1：结构不变，典型性变）
4. V3 = 截断发散段，只留收敛答案（baseline，控长度）

**judge**：
- J_self = 27b（生成者本人）
- J_hetero = qwen2.5-7b（异族）

**测量**：每个变体 × 每个 judge，打 M1/M4/O6（统一 rubric v2 模板，n=3 取均值）。

**预期判读**：
- 若 J_self 在 V0<V1<V2 单调上升、J_hetero 平 → H1/H2 成立（self 惩罚非典型/松散）。
- 若 J_self 在 V3 最高 → 纯长度/存在效应，回到经典 verbosity，机制降级。
- 若两者都平 → flip 来自别处（如 judge 知道 provenance），需加 provenance-blind 条件重测。

**成本**：4 变体 × 2 judge × 3 指标 × n=3 ≈ 72 次 7b 调用（~9 min）+ 27b 自评 36 次。可接受。

## 5. 这对 autoresearch 系统的含义（如果 H 成立）

- 模型自评自己的探索输出时，会**系统性压掉有价值的非结构化发散**——正是 autoresearch 想保留的东西。
- 缓解方向：① 评估层强制异族 judge（不能 self-grade 探索产物）；② 发散段先做结构化压缩再进评估（把"松散"这个 confound 去掉）；③ 评估 prompt 显式声明"额外视角是目标而非噪声"（counter-verbosity framing）。

## 6. 边界声明

- 文献事实均来自本轮 web_search 摘要级阅读，未逐篇精读 PDF；具体数字（100%、β=0.163 等）以原文为准，引用前需回查。
- 机制归因（§3）是从"现象 + 文献旁证"推的，**未经我们自己的对照实验验证**——在 §4 跑完前，不要把 H 当结论用。
- 本文件是调研落盘，不是最终报告；§4 实验结果出来后回填 §3 的验证状态。