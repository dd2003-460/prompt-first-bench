# Revision Log — think-mechanism-paper (T4a, 按 arena review 报告修订)

> origin: ai · 2026-11-26 · 依据：`arena-review-report-raw-20261126.md`（判决"需修改后投" conf 0.7）
> 执行：Lead 直接执行（T4a r1/r2 subagent 均死于 27b 输出上限，0 编辑落盘；任务书为机械修改单，降级 Lead 执行）
> 编译：xelatex 两遍 0 error，10 页（红线 8-15 内），红线词 grep 0 命中，8 条引用全闭合

| M | 状态 | 改了哪里 | 改前 → 改后（各 ≤2 句） | 对应 arena 报告 |
|---|------|---------|------------------------|----------------|
| M1 | done | Def 1（§Core Formalization）+ Abstract + Intro contributions + Conclusion + §Facets 引导句 | Def 1 原来只有 `$\Dmap\circ\Cmap=\mathrm{id}$` 一条 → 加 (i) tolerance 带内 ≈id + (ii) 非平凡性条款（压缩表示尺寸严格小于输入减 slack）+ remark（排除 C=D=id 平凡解；Kolmogorov 形式 K(C(x))<K(x)−ε 注明 uncomputable 仅作直觉）；全文 =id → ≈id 统一（Abstract/Intro/§Facets/Conclusion，仅 remark 反例行保留 =id）；Limitations 新增"非平凡性条款是操作性定义，非认知主张" | Q2(a) top-3 #1：D∘C=id 在 C=D=id 时平凡满足；tolerance 下实为 ≈id 与定义漂移 |
| M2 | done | §Two Structural Observations（原 Two Derivations）整节 | 节标题 "Two Derivations" → "Two Structural Observations"，引导句声明"heuristic arguments, not theorems"；Obs 1 标题去掉 "why ... are equivalent" 改 "share a series structure"；Obs 2 标题 "order cannot be reversed" → "order should not be reversed" + 新增最小反例（双 regime：线性 x∈[0,1] + 饱和 x>1，先精化=跨 kink 平滑插值在 kink 附近全错，先选域=分段精确）；自指有限性段：Gödel 表述修正（需要算术表达力，表达力不足的系外在作用域外，不声称任何不完备定理推论）+ 收敛声明降级为经验观察非定理；"This explains an empirical observation" → "This is consistent with an empirical observation" | Q2(c) top-3 #2：Gödel 适用条件误述 + 无收敛条件；Q2(d)：两阶段无反例/无测度/无定理陈述 |
| M3 | done | §Facets facet 3 + facet 4 | facet 3 "Progress is gradient descent on this landscape" → "Progress, as a metaphor, resembles gradient descent on this landscape"；facet 4 "it explains why a model that misses its leading term fails" → "it offers a reading of why ..." | Q3c 两处越界表述（因果语气/隐喻作事实） |
| M4 | done | Related Work "Compression as understanding" 段 + thebibliography | 原段只引 Newman 2005 → 加 Chaitin 2006（math/0506552，"Understanding is compression!" 口号原始出处）+ Queloz & Beckmann 2026（arXiv:2609.04962，作者实查 API 确认 Matthieu Queloz + Pierre Beckmann，2026-09-04）+ 切割句（Chaitin 是一向压缩-解释观，无 round-trip 恒等结构；我们做的是把压缩-解压往返本身作为理解的操作性定义）；参考文献表 +2 条 | Q1：Chaitin 2006 窗口外必引 |
| M5 | done | Related Work 4 段 | "Our difference:" ×4 同构句式 → 四种不同句式（In contrast, we... / Whereas those analyses... / Here we identify... / Our T5 template differs in target and remedy:）；7/7 表前引导句未加（caption 已有 internal consistency 声明，按任务书"已有就不重复"） | Q5b：LLM 套壳观感 |
| M6 | done | §Core Formalization "Losslessness" 段 | 原"unique plus reproducible" → 操作性定义（tolerance 带内回到同一现象 + 同输入两次压缩输出差异在 τ 内），显式声明 "we use 'lossless' in an operational sense, distinct from information-theoretic invertibility"，并注明 D 是函数时可复现性继承自确定性、实质内容是 tolerance-bounded uniqueness | Q2(b)：D 是函数则可复现自动成立，条款零增量；与信息论 lossless 术语冲突 |
| M7 | done | §Protocol 末新增 subsection "A Minimal Pilot (preliminary)" + Limitations "Template effectiveness untested" 段同步 | 新增：5 prompt × 2 条件分数表（A 3/5 vs B 5/5，照抄 pilot/results.md）+ 解读（B−A 只在 P1/P5，因这两个 prompt 未点名目标结构；P2-P4 baseline 已满分；明确写"测量的是模板对 prompt 未诱导维度的补齐效果，不是普遍增益"+ 截断窗口位置成分声明）+ 局限性（n=1/cell、单模型、无统计检验、机械 checklist 非质量分、raw+rubric 随论文发布可独立复审）；Limitations 原"untested"段改为"pilot 只查机械 injectability，下游性能仍 untested"；number-trace 已同步（pilot 数字行，来源 pilot/runs.json） | top-3 #3：worked example + 最小 pilot |

## 红线自查（改完全文 grep）

- 红线词 first to/in/work, unprecedented, no one has, the only, nobody：**0 命中**
- 7/7 的 internal consistency 限定词：**8 处**（Abstract/Intro/contributions/表 caption/"All seven"段/Honesty of the test/Limitations/Conclusion，原 4 处 + 修订中同步措辞新增）
- 现有 6 条引用未动；新增 2 条均为任务书已验证条目（Chaitin math/0506552；Queloz & Beckmann 2609.04962，作者名 Lead 实查 arXiv API 修正）
- 编译 0 error，10 页（8-15 内），无 undefined citation
