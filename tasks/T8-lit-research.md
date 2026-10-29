# T8-lit 文献调研任务书（可解释性前沿 · 三方向）

**状态**: ready（2026-10-29 成璐指令：先调研前沿再说，再定 C3 执行细节）
**执行通道**: arena agent mode @ prompt-first-bench 仓 `research/interpretability` 分支
**目的**: C3 paired runs 方案已过对抗核验（r50 PASS-with-fixes），开跑前先把三个方向的成熟方法调研清楚——哪些是重复造轮子、哪些能直接用成熟方法替代。

## 背景（≤10 行，够用即可）

我们在做 **prompt 组件级消融实验**：一个七阶段 LLM pipeline（pfb）里，每个 prompt 段（如"候选集冻结声明""owner 标注""证据 URL 要求"）对最终输出质量指标 M8（核验真实性率）的因果贡献。当前方案 = 行为层 paired runs（删组件前后对比，独立 AI 裁决打分）+ 内部状态探针（最后一层 hidden-state 偏离度）。已锁定 top-k={candidate-freeze, owner-tag, evidence-url}，待跑确认性实验。

调研问题：**这套做法在学界有没有成熟对应物？我们的设计里哪些环节可以用成熟方法直接替代或加强？**

## 三个方向（各写一节，正交）

### 方向 1: Prompt ablation / sensitivity analysis 成熟方法
- LLM prompt 组件消融有没有标准方法论（类比 ML 里的 ablation study 规范）？
- 关键问题：删除 vs 替换（sham/placeholder control）、位置混淆控制、统计功效规划（多少 run 才有 power）、多重比较校正——这些在 prompt engineering 评估领域有没有既定实践？
- 找：arXiv 论文、LLM eval 框架（HELM/MT-Bench/LMSYS 类）的消融协议、prompt optimization 工具链（DSPy 等）的做法
- 交付：表格 [方法名 | 出处 URL | 核心做法 | 与我们 C3 方案的差异 | 可直接借用的点]，≥5 条来源

### 方向 2: LLM interpretability 用于 prompt 段归因
- probing classifier / activation patching / representation engineering / logits lens 用在"哪个 prompt 段导致输出行为差异"这个具体问题上，有没有先例？
- 关键问题：最后一层 hidden state 偏离度（我们 C1 的做法）作为归因证据，学界认为它有多可靠？中间层 vs 最后一层的结论会不会反转？双实例对照（同变体 ≥3 seed 比分布差）是不是标准做法？
- 找：activation patching 综述、probing 局限性讨论（spurious correlation / layer selection bias）、representation engineering 在 instruction following 上的应用
- 交付：表格 [方法 | 出处 URL | 因果强度 | 已知局限 | 对我们的适用性判断]，≥5 条来源

### 方向 3: LLM-as-judge 偏差与校准
- 我们用独立 AI 裁决 M8（核验真实性），方向 3 要查：judge 模型的系统性偏差有哪些（position bias / verbosity bias / self-preference / contamination），成熟校准协议是什么？
- 关键问题：①可变分母问题（被评对象产出条目数不同 → 难项退出分母）在 judge 评估里怎么处理的？②固定 rubric + 覆盖率指标（我们的 M8-truth/M8-cover 拆分）有没有先例？③双裁决 + 人工金标准校准、盲法呈现，最低配置是多少？④judge 评分噪声与真实效应量同量级时怎么办（我们的失败门禁）？
- 找：LLM-as-judge 综述/偏差论文（MT-Bench 作者后续工作、JudgeBench 类）、calibration 方法
- 交付：表格 [偏差类型 | 出处 URL | 影响机制 | 缓解方法 | 我们是否已覆盖]，≥5 条来源

## 约束
- 中文回答；每条结论标 conf(0-1)；给来源 URL（arXiv/GitHub/官方文档优先）；不确定的标"未验证"
- 不要泛泛综述，每条必须落到"对我们 C3 方案的具体含义"
- 最后加一节「**对照结论**」：逐条列出 ①我们方案里属于重复造轮子的环节 ②可以直接用成熟方法替代/加强的环节 ③我们比成熟做法多做的（别删）④成熟做法有而我们缺的（建议补）

## 交付
- 文件：`experiments/T8-lit/lit-survey-pipeline-prompts.md`（本仓 research/interpretability 分支）
- 结构：核心发现 ≤20 行（开头）+ 三方向表格 + 对照结论 + 附录（完整来源列表）
- 长度：正文 ≤150 行
- 落盘硬约束：文件不存在=任务未完成，Lead 不验收