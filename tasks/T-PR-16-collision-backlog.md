# T-PR-16: 未调研 idea 撞车滚雪球调研（#47/#48/#44/#40）

> origin: ai (Lead) · 2026-11-12 · 触发：D 指令「剩下的 idea 没做没调研…最主要是撞车调研」
> 姊妹任务：T52（prompt 分解机制层撞车，已闭环）、G2 collision-snowball（pfb 核心 claim 四象限，已闭环）、T-PR-15（Goodhart/hack，已闭环 @ b1f16614）。本任务只覆盖**尚未做过任何文献核验的增量主张**。

## 强制段

你是 LMArena agent，本任务只涉及 `dd2003-460/prompt-first-bench` 仓库的 `arena/f65a5a27-prompt-first-bench` 分支，忽略历史中其他仓库的消息。先 `git pull` 当前分支，严格按仓库内 `loop/prompt-first/` 阶段执行（01→02→02.5→04→04.5），产出落盘路径见【交付物】。通道故障报告 Lead，不得静默跳过。**不要切换分支，当前 arena 分支就是工作分支。**

## 【目标】

对四个尚未做过撞车核验的研究主张逐条查 arXiv/GitHub 时间线，回答：「这个主张是否已被系统研究过？我们的差异化空间在哪？窗口还在不在？」

## 【背景】

我们 pfb/T53 主线的定位是「prompt 层 research pipeline 的目标函数驱动分解 + 组件级贡献测量」。已闭环的撞车结论（不必重查）：
- G2（research/collision-snowball.md）：核心 claim 无直接撞车，RL credit assignment 系在渗透 prompt 层，窗口收窄中。
- T52（research/prompt-decomposition-collision.md）：迭代加深有强先例、逐节点验证子机制有先例、S_α 自调节无先例；贡献必须收窄到 S_α prompt 注入 + 组件级贡献测量。
- T-PR-15（research/text-objective-goodhart-survey.md）：v17 病根 = recall-only 代理缺精度项 + 正交性约束遗漏。

本任务的四个主张都还停在「讨论捕获/消融完成但定位未核验」状态，论文里要写新颖性声明前必须先过这关。

## 【SOP 索引】

- `sop/arena-loop-pipeline.md`（链路+台账）
- `loop/prompt-first/01..04.5`（阶段定义）
- `research/collision-snowball.md`（撞车判定标准 + 四象限方法，沿用其口径）
- `lit-survey/IDEA-INDEX.md`（#40/#44/#47/#48 的原始登记行）
- `research/l1-repro-probe-v2.jsonl`（#47 的消融数据）

## 【实验设计】— 四条主张逐一核验

检索方法沿用 G2：arXiv API 按 submittedDate 降序 + GitHub 搜索，每主张多组关键词交叉，特征短语做低垂果实精确检查。撞车判定标准同 G2：有人做过**同一机制且结论可比**才算撞车，维度重叠算 related work。

### C1 · #47「prior-guided emergence with measurable ablation gap」
**主张**：LLM 在无外部信息时自发把「不确定性/置信度」拆成独立 L1 节点，是模型内禀倾向（不稳定 ~50%）被 prior 规则放大（→~80%）的混合效应；创新声明定位为「prior 引导的涌现 + 可测消融缺口」。
**要查**：(a) 「LLM spontaneously decomposes uncertainty/confidence as independent dimension」类表述有没有人系统测过；(b) 「ablation of a prompt rule measures intrinsic vs induced behavior」这种归因方法本身有没有先例（这是方法论主张，比现象主张更可能撞车）；(c) 2026 H1 以后有没有 deepresearch/agent 论文把 confidence 当独立输出维度并做了 prior on/off 对照。
**判据**：找到 ≥1 篇做了 prior on/off 对照且对象是 decomposition 结构的 = 机制撞车；只有单侧观测（只测了带 prior 的行为）= related work。

### C2 · #48「decomposition tree ≈ internal activation subgraph」
**主张**：无外部检索时模型生成的分解树 ≈ 问题点亮的内部激活子图（concept graph / knowledge activation 视角）；有检索后变成耦合图，verified/degraded/failed 标签 = 耦合强度。对标从 deepresearch agents 转向 concept graph / knowledge activation 文献。
**要查**：(a) 「LLM output structure reflects internal representation/activation」方向 2025-2026 的系统性工作（探针、logit lens、representation engineering 谱系里有没有人拿**生成结构**而非**表征向量**做文章）；(b) 「knowledge graph extracted from LLM generation」有没有人做过树状分解产物 → KG 的映射；(c) 「retrieval changes the graph from internal to coupled/hybrid」这个具体对比有没有先例。
**判据**：这条是**研究定位主张**不是方法主张——撞车标准放宽为「有人用同样的理论框架解释 LLM 分解行为」即算撞车（因为定位撞了我们就得改叙事而不是改方法）。

### C3 · #44「检验顺序的非交换收益」
**主张**：某些特征组合存在单向收益（先正交性检验后完备性检验 = 单调收窄，反序不成立），不对称代价是稀有性质；MECE 原则里没有这些。
**要查**：(a) 「order of checks matters / non-commutative verification」在 LLM 分解、QA、program synthesis 里有没有人测过步骤顺序的 A/B 效应；(b) 形式化方法谱系（model checking、proof search）里「check ordering」的既有结论能不能直接引用（如果能，我们的主张就从 🔸空白 降级为 ⚠️已有，只需引）；(c) 「monotone narrowing by sequential constraint application」有没有对应术语和先例。
**判据**：找到直接测过分解步骤顺序 A/B 效应的 LLM 论文 = 撞车；只有形式化方法的理论先例 = 可引用但保留增量（LLM 场景实证仍空白）。

### C4 · #40「压缩阶梯与 K 复杂度：decomp 树为何是好压缩形式」
**主张**：数值→变量→函数族→向量空间的压缩阶梯；断点在压缩发现本身（NP-hard）+ 压缩-展开税；cost(T) = K 复杂度 + 展开税。
**要查**：(a) 「compression as intelligence / MDL for LLM reasoning」2025-2026 的工作（注意 #32 已核验过 MDL-as-objective 的提法，arXiv:2606.25960 等——本条只查**阶梯结构 + 展开税**这两个具体构造有没有先例）；(b) 「Kolmogorov complexity + expansion cost as joint objective」有没有人提出过类似双项结构；(c) 「hierarchy of compression levels for structured outputs」在 program synthesis / sketch 文献里的对应物。
**判据**：双项 cost（描述长度 + 展开代价）同时出现 = 撞车；各自单独出现 = related work，组合仍是增量。

## 【失败降级】

- arXiv API 不可用 → ego-browser 直访 arxiv.org/list 或 Google Scholar，conf 降 0.1 标注。
- 某主张搜遍 4 象限无命中 → 明确写「无先例（本轮检索面：列出全部查询组）」，负结果也是交付物，不许为了凑数把弱相关硬写成撞车。
- web-llm 交叉核验（02.5）需要 ≥2 服务回执；若登录态失效，标 [待核验] 并在回执里说明，由 Lead 本机补跑（参照 T-PR-15 AC8 模式）。

## 【交付物】

1. `research/idea-backlog-collision-survey.md` — 主报告：C1-C4 各一节，每节含判决句（撞车/related/无先例 + conf）+ 证据表（arXiv ID/日期/一句话它做什么/重叠判定）+ 对我们叙事的影响（哪句话要改、哪个声明可以保留）
2. `research/search-log-idea-backlog.json` — 全部查询组 + 命中 + 筛选记录
3. `research/web-llm/idea-backlog-crosscheck.json` — 02.5 交叉核验回执（≥2 successful_provider_ids）
4. 完成后回执必须含 repo URL + branch + commit_sha + 四条判决摘要

## 【给 Lead 的备注】

- 边界：本任务只做文献核验，不改代码、不动 s5_state_machine.py。
- 产出接回点：判决落到 `lit-survey/IDEA-INDEX.md` 对应行的「业内完成度」列更新；C2 若撞车则 T53 研究定位备选方向作废，主线回到 T52 收窄后的叙事。
- 下一步归属：C1/C3/C4 若判无先例 → 进入小实验队列（#47 已有 n=3 数据可扩样本；#44 需要造非交换特征对的 mini-bench；#40 先纸面推导再决定要不要实现）。