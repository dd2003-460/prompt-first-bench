# T44 · Related Work Update (Nov 2026) — 阶段 01：目标分解、已知与空缺条件

> 创建时间：2026-11-06 UTC · 阶段：01（目标分解）
> 规则包：`loop/prompt-first/00-common-review.md` + `01-goal-decomposition.md` + `02-information-research.md`（参考 `loop/modules/decomp-01.md` 正交纪律）
> 任务书：`tasks/T44-related-work-update.md`
> 工作分支：`arena/de827540-prompt-first-bench`（当前日期：2026-11-06 UTC）
> **阶段边界声明**：本文件仅做正交因素分解、已知/可推导/空缺条件切分、候选类别冻结与阶段 02 检索入口设计；**不在此阶段声称任何尚未核验的新文献事实、arXiv ID 或结论**。

---

## 1. 目标定义与交付判据（根标量与硬门禁）

### 1.1 任务目标重述
围绕 2026 H2（重点补充 2026-09~11 最新文献，兼顾 2026 H2 即 2026-07~11 中尚未被当前草稿收录的重要竞品）的 5 个指定方向开展系统文献调研，为 `experiments/stage-ablation/paper-draft.md` 的 §2 Related Work 提供经一手源交叉核验的增量引用、可直接贴入论文的建议修改段落，以及与本文结论存在矛盾/张力的工作清单与差异归因。

### 1.2 可检验交付判据（约束类 vs 质量类口径声明）
- **[约束 C1 · 数量下限]**：净新增核验通过的文献数 $N_{\text{new}} \ge 8$（与 `paper-draft.md` 既有 31 篇严格去重后计数）。
- **[约束 C2 · 唯一标识符硬门禁]**：每篇入选文献必须具备经一手源核实的 `arXiv ID` 或 `DOI`（无来源一律不写；未核实或死链剔除）。
- **[约束 C3 · 五向覆盖]**：5 个调研方向（D1 Agent Benchmarks、D2 Prompt Structure Ablation、D3 LLM-as-Judge 2026、D4 Deep Research Agents、D5 Calibration 2026 H2）均须覆盖（每个方向至少检索并收录 $\ge 1$ 篇合格文献，若某子方向在 2026-09~11 无同设定工作则扩展至 2026 H2 并显式记录检索边界）。
- **[约束 C4 · 竞品属性二分]**：每篇新增文献必须显式区分「直接竞品」（同设定：no-tool / parametric-only 下的提示结构或阶段消融）vs「相关但不同设定」（有外部工具、RL 训练、端到端单标量评测、或纯裁判/校准研究）。
- **[约束 C5 · 小节落点标注与可贴入文本]**：每篇文献标注归入 `paper-draft.md` §2 的具体小节，并给出可直接贴入论文的英文段落（含配套 References 条目）。
- **[约束 C6 · 矛盾/张力清单]**：凡与本文核心结论相反或构成实质限定条件的工作，必须单独成表并分析差异来源（模型规模、工具可达性、任务类型、裁判机制等）。
- **[约束 C7 · 流程与版本控制]**：完整落盘 `loop-artifacts/stages/01..04.5` 工件及主产出 `loop-artifacts/stages/04/T44-related-work-update.md`，使用 commit message `"T44: related work update Nov 2026"` 提交并 push 到当前分支 `arena/de827540-prompt-first-bench`。

---

## 2. 正交递归分解（目标 → 顶层因素 → 原子叶节点）

将总目标分解为 **5 个互相正交、合起来完整覆盖任务闭环的顶层因素 F1–F5**，并递归展开至不可再分的原子叶节点：

| 顶层因素 | 独占控制维度（正交检验） | 口径类型 | 原子叶节点（递归到底） |
|---------|------------------------|---------|----------------------|
| **F1 检索覆盖与时间窗** | 外部候选池的召回广度与发表月份（2026 H2 / 2026-09~11） | `[约束+质量]` | **F1.1** D1：2026 H2 LLM agent benchmarks（重点排查有无 no-tool / parametric-only 对照设定）<br>**F1.2** D2：2026 prompt structure ablation（decomposition vs CoT vs ToT / pipeline scaffolding 的量化对比）<br>**F1.3** D3：2026 LLM-as-judge 可靠性、self-preference bias、cross-family / heterogeneous validation<br>**F1.4** D4：DREAM / DeepResearch Bench 之后的 deep research 学术评测（含 Perplexity / OpenAI / Gemini Deep Research 评测与新基准）<br>**F1.5** D5：2026 H2 calibration（verbalized vs logprob / internal representation confidence 新结果） |
| **F2 元数据真值与双源核验** | 单篇文献题录字段（标题/作者/年份/arXiv ID/DOI/venue）的真实性与独立印证 | `[约束]` | **F2.1** 一手源核验（arXiv API `export.arxiv.org` / ACL Anthology / CrossRef / OpenReview 页面实抓）<br>**F2.2** 独立第二源交叉印证（DBLP API / Semantic Scholar / 官方 GitHub 仓库 / 会议录）<br>**F2.3** 与 `paper-draft.md` 现有 31 篇引用的 ID 级精确去重 |
| **F3 竞品分类学与 §2 结构对齐** | 文献与本文实验设定的映射关系及论文正文落位 | `[约束+质量]` | **F3.1** 设定同构性判定：`直接竞品`（固定模型 + no-tool parametric-only + prompt/stage 消融 + 多维评分）vs `相关但不同设定`（含工具检索/浏览、端到端 RL、仅端到端成功率标量、或独立评测器/校准方法）<br>**F3.2** 章节结构对齐：调和任务书简述（§2.1–2.3 三小节）与 `paper-draft.md` 实盘结构（§2.1–2.6 六小节），给出精确插入位置与无冲突引用格式 |
| **F4 结论张力与差异归因** | 外部文献实证发现与本文核心主张（C_p1–C_p6）的逻辑相容性 | `[约束+质量]` | **F4.1** 逐篇比对本文 6 条核心结论（阶段消融有界性、分解 ROI、风格 vs 结构、M7 机械提示退化、同族裁判保守偏置 ≈0.15、工具源锚定与双遍核验、口头校准跳升）<br>**F4.2** 矛盾/张力机理拆解：按「模型参数量级（27B vs Frontier）」「工具通道（no-tool vs web）」「任务复杂度」「裁判同源性」「采样/训练范式（prompt-only vs RL/fine-tuning）」五维定位分歧根源 |
| **F5 工件组装与 Git 交付** | 本地仓库文件写入一致性、三道闸自检与远程分支同步 | `[约束]` | **F5.1** 阶段 01→02→02.5→03→04→04.5 六份阶段工件完备落盘<br>**F5.2** 主交付物 `loop-artifacts/stages/04/T44-related-work-update.md` 满足三部分结构（≥8 篇表格 + §2 建议英文修改段落与新增 References + 矛盾/张力清单）并通过三道闸检查<br>**F5.3** `git commit -m "T44: related work update Nov 2026"` + `git push origin arena/de827540-prompt-first-bench` 成功返回 0 |

- **SHARED 耦合显式声明**：
  - 候选池质量同时向 **F1**（方向覆盖）与 **F4**（能否捕获高价值反例，特别是 D3 同族裁判 self-preference 膨胀 vs 本文保守偏置、D2 分解是否总是正收益、D5 口头置信度 vs 内部概率优劣）传导。
- **主导瓶颈识别（高弹性项）**：
  - **瓶颈 1（约束一票否决）**：**F2.1/F2.2（2026-09~11 最新文献的真实 arXiv ID / DOI 双源核验）**——沙箱 bash 外网仅白名单放通 GitHub/npm/pypi，必须依赖 Arena 原生 `web_search` 与 `fetch_page` 工具访问 arXiv / DBLP / Anthology；任何凭参数记忆编写的 2026 H2 arXiv 号极易幻觉（前序 T37 已查出原稿 5 处假 ID），因此「实抓一手源」是最高优先级门禁。
  - **瓶颈 2（学术深度决定项）**：**F3.1 + F4.2（直接竞品稀缺性判定 + 同族裁判/提示分解/校准反例归因）**——决定 §2 更新是简单堆砌文献还是真正加固论文审稿防线。

---

## 3. 已知条件、项目可推导条件与空缺清单

### 3.1 人类已提供的确定条件（来自任务书 + 用户指令）
| 编号 | 条件内容 | 来源 |
|------|---------|------|
| H1 | 调研时间重点：2026 H2，特别是补充 2026-09~11 最新文献，确保不遗漏重要竞品 | 用户指令 + `tasks/T44-related-work-update.md` |
| H2 | 调研五大方向：1) LLM agent benchmark 2026 H2（关注 no-tool/parametric-only）；2) Prompt structure ablation（decomposition vs CoT vs ToT 量化比较）；3) LLM-as-judge 2026（reliability, self-preference bias, cross-family validation）；4) Deep research agents（DREAM/DeepResearch Bench 之后对 Perplexity/OpenAI/Gemini deep research 的学术评估）；5) Calibration 2026 H2（verbalized vs logprob 新结果） | `tasks/T44-related-work-update.md` |
| H3 | 硬性约束：每篇必须给 arXiv ID 或 DOI；区分「直接竞品」vs「相关但不同设定」；标注加入 §2 哪一小节；列出与本文结论矛盾的工作并分析差异来源 | `tasks/T44-related-work-update.md` |
| H4 | 交付路径与提交规范：`loop-artifacts/stages/04/T44-related-work-update.md`（≥8 篇新引用 + 建议修改文本 + 矛盾清单），走完 1-loop `01..04.5`，commit message `"T44: related work update Nov 2026"`，push 到当前分支 `arena/de827540-prompt-first-bench` | 用户指令 + `tasks/T44-related-work-update.md` |
| H5 | 失败降级规则：若 `web_search` 不可用，降级为 parametric knowledge + `[UNVERIFIED]` 标注（conf 0.2）；若通道 403/故障则报告 Lead | `tasks/T44-related-work-update.md` |

### 3.2 从仓库可推导的已确定条件（来自实读仓库文件，非猜测）
| 编号 | 推导事实 | 仓库证据锚点 | 对本任务的实质影响 |
|------|---------|-------------|-------------------|
| P1 | **任务书背景与 `paper-draft.md` 实盘存在结构版本差**：任务书背景写「当前引用止于 2026-07；Paper 现有 §2 三小节：2.1, 2.2, 2.3」，但实盘 `experiments/stage-ablation/paper-draft.md`（经 T37 扩充后）实际包含 **6 个小节（§2.1–§2.6）** 与 **31 篇参考文献** | `experiments/stage-ablation/paper-draft.md` L27–L65, L347–L380 | 建议修改文本必须精确对齐实盘 `paper-draft.md` 的 §2.1–§2.6（同时在映射表中注明与任务书 §2.1–§2.3 三大主块的对应关系；其中 D3 LLM-as-judge 可嵌入 §2.4 或新增/扩充评测段，D4 Deep Research 对齐 §2.1 与 §2.5），确保 Lead 可零摩擦直接粘贴 |
| P2 | **实盘引用截止时间分布**：现有 31 篇中仅有 **3 篇 `2609.*`**（`2609.19644` ScientistTwo、`2609.20541` Meyer et al.、`2609.34454` Xu et al.）及 2 篇 2026 会议论文（DREAM `ACL 2026`、DeepResearch Bench `arXiv:2506.11763` ICLR 2026）；**2026-10 至 2026-11（`2610.*` / `2611.*`）为 0 篇**，且 **D3（LLM-as-judge 2026 self-preference / cross-family）在 §2 中几乎空白**（仅 §2.4 提了一句 2024 年的 ARES） | `experiments/stage-ablation/paper-draft.md` L347–L380 | 2026-09~11 确有明显缺口，尤其 `2610.*`/`2611.*`、D3 LLM-as-judge 2026、D4 商业 Deep Research 学术横评、D1/D2 2026 H2 消融对比 |
| P3 | **本文 6 条核心结论（用于 F4 矛盾筛查的基准集）**：<br>① **C_p1（阶段消融有界性）**：27B no-tool 下 S5 较 S0 提升 +0.182（Total 0.397→0.579），增益集中于组织与缺口识别（M1/M4），而非生成新知；且非单调（S2/S4 在 M1 上高于 S5），S3 无工具交叉核验近零增益（−0.006，异族裁判亦确认 S2→S3 ≤ 0）。<br>② **C_p2（分解 ROI 与跨题分歧）**：本地裁判下 S1（分解）单步增益最大（+0.129），但异族裁判跨题扩展（Q2–Q5）显示 H1（S1>S0）为 INCONCLUSIVE（2 正 2 负，Q1 反向 −0.187），真正跨题稳健的是 H2（S1→S2 信息调研段增益最大）。<br>③ **C_p3（风格独立于结构）**：300 字符模糊提示 S6 超过 S0（+0.065）并在纯概念题 Q5 夺冠（0.701）；混合提示 S7 在事实密集题 Q1/Q2 夺冠（M1=0.771 > S5=0.521），最优提示高度依赖题型。<br>④ **C_p4（M7 矛盾推理退化）**：27B 规模下机械结构化提示反而稀释并降低矛盾检测与裁决能力（S1 M7=0.256 < S0=0.306，S5=0.278）。<br>⑤ **C_p5（同族裁判偏置方向）**：本地同族 Qwen3.8-27B 裁判相比异族前沿裁判系统性**更严格约 0.15（保守低估）**，而非文献常见的同族自我偏爱（高估/inflation），但保持相对排序一致。<br>⑥ **C_p6（口头校准与工具双遍核验）**：自然语言不确定性提示将 M2 从 0.037 拉升至 0.618；朴素注入搜索结果（S7T）因 source anchoring 使 M1 暴跌（0.771→0.480），需双遍 claim-level 核验（S7V）才恢复 M1=0.762，单遍内嵌核验（S8E）无效 | `experiments/stage-ablation/paper-draft.md` §1, §4.1–§4.5, §5.1–§5.3, §6 | 任何在 2026 H2 讨论：(a) 同族 LLM-as-judge 自偏爱高估 vs 低估、(b) 结构化分解对推理/矛盾检测的正负效应、(c) verbalized vs logprob/internal 校准优劣、(d) RAG/Deep Research 检索噪声反伤准确率的工作，都是 F4 重点比对对象 |
| P4 | **仓库内既有线索库（待核验，不可直接当已核验引用）**：`competitor-survey.md` 提及 OpenResearcher (`arXiv:2603.20278` / EMNLP 2026)、DRACO (Perplexity+Harvard 2026)、DeepResearchGym、BrowseComp-Plus、ResearchRubrics、Mercor DeepResearch Bench II；`lit-survey/t24-receipt.md` 提及 Sprague et al. (ICLR 2025) 等 | `experiments/stage-ablation/competitor-survey.md`, `lit-survey/t24-receipt.md` | 这些线索可作为背景参照，但若纳入 T44 必须满足时间窗相关性并通过一手源重新核验 arXiv ID / DOI；重点仍须优先检索 **2026 H2（尤其 2026-09~11）** 的新论文 |
| P5 | **沙箱网络环境边界**：bash 外网仅允许 `github.com` / `npmjs.org` / `pypi.org`，无 `ego-browser` 和 `ralph` CLI；但平台原生工具 `web_search` 与 `fetch_page` 可直接访问公网学术源（前序 T37 已实证 arXiv API / DBLP API / ACL Anthology 可达） | 环境说明 + `experiments/stage-ablation/loop-artifacts/stages/02/research.md` §0 | 阶段 02 必须记录 `ego-browser` 不可用状态，并主用 `web_search` + `fetch_page`（arXiv API / DBLP / Anthology / CrossRef）执行双源核验 |

### 3.3 空缺清单（黑盒收口表 B1–B7 = 待研究条件 G1–G7）

以下所有条目在阶段 01 均属**未知/待核验状态**，严禁预设具体论文或数字：

| 空缺编号 | 为什么未知（复合空缺拆解子问题） | 估计产出区间 | 阶段 02 具体测法（工具 + 查询词 + 一手源 + 备用路径） | 弹性（优先级） | 阻塞的下游判断 |
|---------|-------------------------------|-------------|---------------------------------------------------|--------------|--------------|
| **G1 (D1: Agent Benchmarks 2026 H2)** | 子问题：<br>1) 2026-07~11（重点 09~11）有哪些新发布的 LLM agent evaluation benchmarks？<br>2) 其中是否存在评测 **no-tool / parametric-only** 或显式拆解「工具访问 vs 纯参数提示结构」的基准（直接竞品排查）？<br>3) 各候选的准确 arXiv ID / DOI 与评测维度（单标量 vs 多维 rubric）是什么？ | 2–3 篇合格新文献（直接竞品预计 0–1 篇，相关异设定 1–3 篇） | 1) `web_search`: `"agent benchmark" site:arxiv.org/abs/2609 OR site:arxiv.org/abs/2610 OR site:arxiv.org/abs/2611` 及 `arxiv 2609 2610 2611 LLM agent evaluation benchmark without tools`<br>2) `fetch_page`: `http://export.arxiv.org/api/query?search_query=...&sortBy=submittedDate&sortOrder=descending` 检索 `ti:"benchmark" AND ti:"agent"` 最新提交<br>3) 第二源：`dblp.org/search/publ/api` 或 `api.semanticscholar.org` / HuggingFace Papers / GitHub 官方仓 | **高** | 决定 §2.1 是否存在遗漏的「同设定直接竞品」 |
| **G2 (D2: Prompt Structure Ablation 2026)** | 子问题：<br>1) 2026 H2（尤其 09~11）有哪些关于 structured prompting / decomposition vs CoT vs ToT / agent workflow stage ablation 的量化对比研究？<br>2) 是否有工作实证发现显式分解/机械提示在特定模型或任务上无效甚至负效应（与本文 C_p2 / C_p4 对话）？<br>3) 准确 arXiv ID / DOI 与实验设定（模型规模、有无工具）是什么？ | 2–3 篇合格新文献 | 1) `web_search`: `site:arxiv.org/abs/2608 OR site:arxiv.org/abs/2609 OR site:arxiv.org/abs/2610 OR site:arxiv.org/abs/2611 "prompt" ("decomposition" OR "chain-of-thought" OR "ablation")`<br>2) `fetch_page`: arXiv API 检索 `all:"decomposition" AND all:"chain-of-thought" AND (cat:cs.CL OR cat:cs.AI)` 按 `submittedDate` 倒序取 2026-08~11<br>3) 第二源：DBLP / ACL Anthology (ACL 2026 / EMNLP 2026) | **高** | 决定 §2.2 & §2.6 能否为 S1/S6/S7/M7 提供 2026 H2 外部锚点与反例对话 |
| **G3 (D3: LLM-as-Judge 2026 H2)** | 子问题：<br>1) 2026 H2（尤其 09~11）关于 LLM-as-judge reliability、self-preference bias（同族偏置）、cross-family / heterogeneous judge validation 有哪些最新论文？<br>2) 2026 新文献对同族偏置的方向（高估 self-preference vs 严格低估）有何量化结论？与本文 §4.5「本地 27B 较前沿模型保守低估 ~0.15」是否矛盾？<br>3) 归入 `paper-draft.md` 哪一小节最自然（§2.4 扩展为 Evaluation & Judge Reliability 或 §2.1/§2.6）？ | 2–3 篇合格新文献 | 1) `web_search`: `site:arxiv.org/abs/2609 OR site:arxiv.org/abs/2610 OR site:arxiv.org/abs/2611 "LLM-as-a-Judge" OR "self-preference" OR "judge"`<br>2) `fetch_page`: arXiv API 检索 `(ti:"judge" OR ti:"self-preference" OR ti:"evaluat") AND all:"bias" AND cat:cs.CL` 按 `submittedDate` 倒序<br>3) 第二源：DBLP / OpenReview / ACL Anthology 2026 | **极高**（当前 `paper-draft.md` 最大结构性短板） | 直接决定 §2 对 §3.5/§4.5 异族裁判设计的文献支撑及矛盾清单核心条目 |
| **G4 (D4: Deep Research Agents 2026 H2)** | 子问题：<br>1) 在 DREAM (ACL 2026) 与 DeepResearch Bench (ICLR 2026) 之后，2026 年（尤其 H2 / 09~11）有哪些针对商业/开源 Deep Research 系统（Perplexity Deep Research, OpenAI Deep Research, Gemini Deep Research 等）的学术评测基准或横评论文（含 DRACO、BrowseComp-Plus、DeepResearch Bench 后续等是否有正式 arXiv ID / DOI）？<br>2) 它们对检索噪声/引用幻觉（citation grounding / source anchoring）有何发现？与本文 §5.1 S7T→S7V 是否一致或矛盾？ | 2–3 篇合格新文献 | 1) `web_search`: `("Deep Research" OR "DeepResearch") ("Perplexity" OR "OpenAI" OR "Gemini") site:arxiv.org` 及 `site:arxiv.org/abs/2608 OR site:arxiv.org/abs/2609 OR site:arxiv.org/abs/2610 OR site:arxiv.org/abs/2611 "deep research"`<br>2) `fetch_page`: arXiv API 检索 `ti:"deep research" OR ti:"deepresearch"` 按 `submittedDate` 倒序<br>3) 第二源：DBLP / ACL Anthology / 官方技术报告 DOI/arXiv | **高** | 决定 §2.1 与 §2.5 是否遗漏 DREAM/DRB 之后的直接赛道新基准 |
| **G5 (D5: Calibration 2026 H2)** | 子问题：<br>1) 除草稿已有的 Meyer et al. (`2609.20541`) 和 Xu et al. (`2609.34454`) 外，2026-09~11（及 2026 H2）还有哪些关于 verbalized confidence vs logprob / internal representation calibration 的新论文？<br>2) 同时顺带核查草稿既有 `2609.34454` 与 `2609.20541` 的真实 arXiv 元数据（防范上游草稿残留 ID 异常），确保新旧引用衔接无冲突。<br>3) 新结果支持还是反驳本文 C_p6（提示词单层即可校准 M2）？ | 2–3 篇合格新文献 | 1) `web_search`: `site:arxiv.org/abs/2609 OR site:arxiv.org/abs/2610 OR site:arxiv.org/abs/2611 ("verbalized confidence" OR "calibration" OR "uncertainty") LLM`<br>2) `fetch_page`: arXiv API 检索 `(ti:"calibration" OR ti:"confidence" OR ti:"uncertainty") AND all:"verbalized" AND cat:cs.CL` 按 `submittedDate` 倒序，并校验 `id_list=2609.20541,2609.34454,2609.19644`<br>3) 第二源：DBLP API / Semantic Scholar | **高** | 决定 §2.3 的 2026 H2 校准文献厚度与张力边界 |
| **G6 (双源独立印证可达性)** | 子问题：<br>1) 2026-10~11 刚挂上 arXiv 的最新预印本是否已被 DBLP / Semantic Scholar 收录？<br>2) 若刚发布数天/数周尚未进入 DBLP 索引，何种独立第二源符合阶段 02 规范？ | 100% 入选文献具备一手主源 + 尽可能高的独立次源率 | 主源：arXiv 官方 API (`export.arxiv.org`) 或出版商/ACL Anthology DOI 页面；独立第二源优先级：① DBLP API → ② Semantic Scholar / CrossRef API → ③ 论文作者公开 GitHub 仓库 / HuggingFace Papers / OpenReview 独立记录（注：`arxiv.org/abs` 与 `export.arxiv.org` 同源，绝不混充双源；若极新 2026-11 论文尚无外部索引，如实标注外部索引未同步状态） | **中** | 保障阶段 02/02.5 证据纪律不走样 |
| **G7 (§2 插入段落与篇幅平衡)** | 子问题：<br>1) 新增 ≥8 篇文献后，`paper-draft.md` §2 各小节如何自然融入而不破坏现有叙事流与字数区间（`arxiv-submission.md` 要求全文 4k–8k 词，当前约 6,874 词）？ | 增量约 400–800 词（全文仍在 8k 词上限内） | 在阶段 03/04 按 `paper-draft.md` 现有 §2.1–§2.6 逐节设计增量/替换段落，保持紧凑学术文风 | **中** | 决定建议修改文本能否真正「直接可贴进 paper」 |

---

## 4. 候选集冻结声明（防漂移硬门禁）

1. **冻结的候选检索域（5 类，严格对齐任务书）**：
   - **D1**：LLM Agent Benchmarks (2026 H2，重点排查 no-tool / parametric-only vs tool-augmented)
   - **D2**：Prompt Structure Ablation (2026，重点 decomposition vs CoT vs ToT / pipeline scaffolding 量化对比)
   - **D3**：LLM-as-Judge Reliability & Bias (2026 H2，重点 judge reliability, self-preference bias, cross-family validation)
   - **D4**：Deep Research Agents & Benchmarks (post-DREAM / post-DRB，重点 Perplexity / OpenAI / Gemini deep research 学术评估与新基准)
   - **D5**：Confidence Elicitation & Calibration (2026 H2，重点 verbalized vs logprob / internal states)
2. **明确排除规则（满足任一条即排除，阶段 02 逐条登记排除理由与时间戳）**：
   - **排除规则 E-dup**：已在 `experiments/stage-ablation/paper-draft.md` 现有 31 篇 References 中出现的文献（如 `2609.19644`, `2609.20541`, `2506.11763`, `2026.acl-long.448` 等）——不重复计入新增 ≥8 篇配额（但若发现既有条目元数据异常，可在核验节单独报告）。
   - **排除规则 E-noid**：无真实可核验 arXiv ID 且无真实可核验 DOI 的博客、推文、纯商业发布页（如无学术论文支撑的产品官网文案）——严格执行任务书「每个引用必须给 arXiv ID 或 DOI（无来源不写）」。
   - **排除规则 E-time**：发表/提交早于 2026 年的旧文献——原则上不计入 T44 的「≥8 篇 2026 H2 新增引用」核心配额（除非作为解释矛盾所必需的背景对照，且若引用须单独声明不占 ≥8 篇配额）。核心配额锁定 **2026 H2（2026-07~11，优先 2026-09~11）** 学术论文（若个别 D4 核心基准如 DRACO 等首发于 2026 H1 但在 H2 更新或属任务书点名必查的商业 Deep Research 学术评测，须在阶段 02 核实确切版本日期并显式说明，确保 2026-09~11 论文仍占绝对主体 ≥8 篇）。
3. **变更纪律**：后续阶段 02–04.5 不得悄悄增删 D1–D5 域定义或放宽 E-dup / E-noid / E-time 准入线。

---

## 5. 阶段 02 第一批立即执行入口

进入阶段 02 后，按以下顺序立即执行：
1. **通道实测登记**：记录 `ego-browser` 不可用状态，实测 `fetch_page` 访问 `export.arxiv.org/api/query` 与 `dblp.org/search/publ/api` 的连通性，并顺带核查 `paper-draft.md` 中既有 3 篇 `2609.*`（`2609.19644`, `2609.20541`, `2609.34454`）在 arXiv API 的真实回执。
2. **五向并行检索（围绕 G1–G5）**：利用 `fetch_page`（arXiv API 按 `submittedDate` 倒序精确拉取 2026-09~11 及 2026-07~08 候选）结合 `web_search`（补充 ACL/EMNLP/NeurIPS 2026 及商业 Deep Research 学术评测线索），在 D1–D5 每个方向筛选 2–4 篇高相关 2026 H2 论文（目标总计核验 12–15 篇，优中选优保留 ≥10 篇写入最终交付，远超 ≥8 篇底线）。
3. **逐篇一手详情抓取 + 第二源印证（闭合 G6）**：对每篇入选候选抓取完整 arXiv API Atom 记录（标题、全作者、v1/最新提交精确日期、abstract 核心定量数字、comment/DOI）及 DBLP / Semantic Scholar / CrossRef / GitHub 第二源记录。

---

## 6. 阶段 01 门禁自检（对照 `01-goal-decomposition.md` 质检标准）

> 注：当前 Arena 沙箱无外部 `ralph` Reviewer 进程，以下为严格对照 `00-common-review.md` 与 `01-goal-decomposition.md` 的逐项自检（不伪造 `stage-review` 路由块）。

- [x] **因素正交与原子化**：F1（检索覆盖/时效）、F2（元数据真值/双源）、F3（竞品分类/章节映射）、F4（结论矛盾/差异归因）、F5（工件组装/Git 闭环）五维互不重叠，全部展开至可执行原子叶节点（F1.1–F5.3）。
- [x] **覆盖全部目标**：任务书 5 个调研方向、≥8 篇硬指标、arXiv/DOI 硬约束、直接竞品 vs 相关异设定二分、§2 小节标注、建议修改段落、矛盾清单、commit+push 全部被叶节点覆盖。
- [x] **区分已知 / 可推导 / 未知**：H1–H5（人类给定）、P1–P5（仓库实读推导，特别是发现任务书「三小节/止于 07 月」与实盘「六小节/含 3 篇 09 月」的差异）、G1–G7（未知空缺）分表列明。
- [x] **未把未知伪装成已知**：本文件未预填任何未经阶段 02 核验的新论文标题、arXiv ID 或实验数值。
- [x] **候选集已冻结**：D1–D5 与排除规则 E-dup / E-noid / E-time 已冻结。
- [x] **阶段 02 可直接开工**：查询接口、检索式、主次源与降级路径均已具体到 URL 模板级。

**阶段 01 自检结论**：满足进入阶段 02 的全部门禁条件（status: pass → 推进至阶段 02）。
