# Arena 任务卡 · idea53 收敛定位的投稿策略审查（2026-11-25 第二轮） &gt; 与上轮分工：上轮审 novelty（报告见 arena-review-report-r
Arena 任务卡 · idea53 收敛定位的投稿策略审查（2026-11-25 第二轮）

> 与上轮分工：上轮审 novelty（报告见 arena-review-report-raw-20261125.md）；本轮只做投稿策略，不重审 novelty，不写稿。

> SOP：`tasks/00-ops/sop-arena-review-light.md`

[任务]

对一个收敛后的研究定位做**投稿策略判断**。角色：熟悉 ML/systems workshop 与顶会 D&B 轨道的资深审稿人 + 投稿顾问。必须联网核实 CFP/费用/截稿日期，禁止凭记忆给数字。

[背景]（已收敛定位，以此为准，不要重审旧叙事）

一项已完成的 toy-model 工作，定位为**前置工作（可计算、可测量的评分基础）**，不是完整方法、不 solve 任何对齐问题：

核心量：在分解树上，深层节点相对浅层判断的**增量信息** \(H(D|S)\)；闭式可算（硬件 spec + workload prior，无需跑实验/无需训练）。

已验证（toy）：4 平台 × 40,000 workload；flip 43–56%；deep-only MI 0.71–0.77 bits；flat-rate 负控制使增量**精确=0**；24 排列不变；预注册时间戳早于数据。

结构只是**最简单示例**：树/GPU 示例/数学示例都是 toy model，明确写"可推广到更复杂结构（新数据贝叶斯更新 + 假设约束下的最小描述长度结构）"，但**本稿不实现推广**。

与已知工作的切割：ID3 信息增益、roofline、PID 是教科书工具（不 claim）；Specification Self-Correction（2507.18742, SCALR@COLM 2025）做 test-time 自然语言 spec 改写，无 IG/无树/无量化/不训练——本工作的区别是"有量化结构 + 精确零负控制"，且本工作**不碰** hack→spec 修订这一步，只是其前置的评分基础。

主动收窄：不声称 solve reward hacking/Goodhart；不声称首次/无人做过；不声称认识论等价；不声称 H(D|S) 可跨轮比较。

[必答问题]

**Q1 workshop 可发性**：以这个收敛定位（前置工作 + toy + 闭式 + 负控制 + 预注册），投 ML/systems 方向的 workshop 够不够？给出**最匹配的 3 个具体 workshop**（名称 + 所属顶会 + 2027 截稿窗口 + 是否接受 analysis/measurement/short paper + 版面格式页数）。明确说明这类"测量协议/分析型、无 code 无实验"的稿子在 workshop 的竞争力。

**Q2 顶会中稿概率最大化路径**：在"概率最大的顶会中稿"目标下，给出排序后的 2–3 条路径（例如 workshop paper → 主会 D&B/E&D、或 analysis note 直接投某轨道），每条给：venue 全名、类别、截稿日期（2026H2–2027 窗口）、接受率（若有官方数字给来源）、对该定位的适配理由、被拒的主要风险。**注意区分"workshop 录用"与"顶会主会录用"，分别给概率估计（主观须标 conf）。**

**Q3 费用/免费**：上述每条路径的**注册费与版面费**——是否免费？区分：workshop 是否通常随主会注册、学生/作者注册费量级、是否有 waiver、arXiv 是否 0 元。给出可核验来源（CFP/官网 URL）。若 2027 费用未公布，明确说"未公布"，禁止编造数字。

**Q4 加固建议**：在不动结论的前提下，为提高 workshop 命中率，投入产出比最高的 1–2 个补充动作是什么（例如加一张结构图、补一个公开数据 spot-check、加 comparison table）？按"必做/可选"分级。

[约束]

中文。每条结论标 conf(0–1)。每个 workshop/顶会/费用必须给可核验来源 URL；截稿日期和费用**必须联网核实**，拿不到就写"未公布/未验证"，禁止编造。

时间盒 30 分钟；超时交已有 + 缺口清单。

回答 ≤ 70 行，结构化（Q1–Q4 分节）。不复述背景。

不要写稿、不要改仓库、不要重审 novelty。

[交付]

把完整策略报告作为回复正文发出（无需写文件、无需动仓库）。

Thought for 1 minute and 51 seconds

Let me understand the task. This is a research submission strategy review task. The user wants me to:

Q1: Workshop publishability - give 3 specific most-matching workshops (name + top conference + 2027 deadline window + whether they accept analysis/measurement/short papers + format/pages)
Q2: Path to maximize main-conference acceptance probability - 2-3 ranked paths with venue full name, category, deadlines (2026H2-2027), acceptance rates (with sources), fit reasons, rejection risks. Distinguish workshop vs main conference acceptance, give probability estimates (subjective, mark conf).
Q3: Fees - registration/publication fees for each path, whether free, student rates, waivers, arXiv costs. Must verify online with URLs. If 2027 fees not published, say "not published".
Q4: 1-2 highest ROI reinforcement actions to improve workshop hit rate, graded "must do/optional".

Constraints:

Chinese, conf(0-1) on each conclusion, verifiable source URLs, must verify deadlines and fees online, no fabrication
Time box 30 minutes
Answer ≤ 70 lines, structured Q1-Q4
Don't write the paper, don't modify repo, don't re-review novelty
Deliver report as reply text (no file needed)

I need to search the web for:

ML/systems workshop CFPs for 2027 (NeurIPS 2026/2027 workshops, ICML 2027, ICLR 2027 workshops)
Since today is 2026-11-25, relevant deadlines: ICLR 2027 workshops (deadlines ~Dec 2026-Jan 2027), ICML 2027 workshops (~Feb-Apr 2027), NeurIPS 2027 workshops (~May-June 2027). Also MLSys 2027, EuroSys/SOSP D&B tracks, ASPLOS 2027, etc.
Main conference D&B (Datasets & Benchmarks) tracks: NeurIPS D&B track, ICLR doesn't have one... Actually NeurIPS has Datasets and Benchmarks track. ICML has... ICLR has "Tiny Papers"? No that was discontinued. ICML 2025 had position paper track? Let me search.
E&D = Evaluation and Data? Maybe "Evaluation & Data" track? Hmm, the task mentions "主会 D&B/E&D" - NeurIPS Datasets & Benchmarks track, and maybe "Evaluation and Data" - actually there's "Evaluation in AI" workshops. Or ICML's "Evaluation" track? Let me think - AAAI has an "AI Alignment" track. Actually the mention "workshop paper → 主会 D&B/E&D" likely refers to NeurIPS Datasets & Benchmarks (D&B) and possibly "Evaluation and Development"? Hmm.

Actually "E&D" might refer to ICLR's... no. Could be "Empirical Deep Learning"? Hmm. Or "Evaluation & Data" track at ... Actually ICML 2025 introduced "Position Paper Track"? ICML 2025 had a "Position Papers" track. Hmm, but the task says D&B/E&D. NeurIPS has Datasets & Benchmarks. "E&D" - maybe "Evaluation & Data" track? Actually there might be an "Evaluation and Data (E&D)" track somewhere - possibly at ICML 2026? Or it could refer to the new "Datasets & Benchmarks" at other venues like ICLR... Actually ICLR 2026 doesn't have one.

Hmm, wait - maybe "E&D" = "Evidence & Data"? Or "Experiments & Data"? Let me just search online. Also relevant: workshops like "Mechanistic Interpretability Workshop", "Science of LLM Workshop", "AI Safety", "SafeAI", "Helm" etc. For systems: MLSys, "ML for Systems", "SysML", "ISCA/MICRO workshops", "Hardware for ML". The work is about hardware spec + workload prior scoring deep nodes in a decomposition tree — sounds like hardware-allocation/decomposition analysis with information gain. Actually the topic: "在分解树上，深层节点相对浅层判断的增量信息 H(D|S)" — incremental information of deep nodes over shallow judgments on a decomposition tree; closed-form computable from hardware spec + workload prior; 4 platforms × 40,000 workloads; flip rate 43-56%; MI0.71-0.77 bits; flat-rate negative control gives exactly 0; 24 permutation invariance; preregistered timestamps.

This sounds like analysis of roofline-style / hardware spec scoring for some alignment/decomposition thing? It mentions reward hacking, Goodhart, spec self-correction (SCALR@COLM 2025). So it's an AI-safety-flavored measurement protocol: a scoring basis for decomposition trees, quantifying how much incremental info deep nodes provide over shallow judgments. Cross-cut with ID3 info gain, roofline, PID.

Target venues: ML/systems workshops, NeurIPS D&B track, maybe "Evaluation" tracks. Also relevant: "SoLaR" (Socially Responsible Language Modelling), "ME-FoMo" workshop, "Building Trust", "Re-Align", "HINT", "ViGIL", "SIREN" (Safety-benchmarks?), "SafeAI", "AISafety", "Do-Not-Answer"... For analysis/measurement type: "Insights from Negative Results in NLP", "Repl4NLP", "BlackboxNLP" (analysis), "COGSCI"... Also "MLSys" workshops: "ML for Systems", "SysML" is now a conference (MLSys). MLSys conference 2027 deadline ~Sept 2026 (passed?) - MLSys 2027 deadline might be around Sept 2026, which is past. Hmm.

Also "Evaluation and Data (E&D)" — wait, maybe this refers to ICML 2026's new track? Or "Evaluations and Data"? Hmm, actually I wonder if this is "NeurIPS D&B" and "ICLR Blogpost track"? No.

Let me search the web for actual facts. I need:

NeurIPS 2026/2027 Datasets & Benchmarks track deadlines & fees
ICML 2027 deadlines & any evaluation/data track
ICLR 2027 (happening April 2027, deadline was Sept 2026 - passed) — for ICLR 2027, the paper deadline was likely Sept 2026, already past. Workshops at ICLR 2027 have deadlines around Jan2027.
Workshop options:
NeurIPS 2026 workshops (deadline ~June 2026, passed; the conference is Dec 2026 — actually NeurIPS 2026 is happening around Dec 6-12, 2026? Its workshops deadlines passed).
ICLR 2027 workshops: deadlines ~Nov 2026 - Jan 2027 — OPEN NOW.
ICML 2027 workshops: deadlines ~Feb-Mar 2027.
MLSys 2027: deadline was ~Sept 2026? Actually MLSys 2026 deadline was Sept 2025. MLSys 2027 likely Sept 2026 (passed). Hmm.
EuroSys 2027, ASPLOS 2027 (deadlines passed?), ATC/OSDI...
AAAI 2027 workshops (AAAI 2027 conference Jan 2027? AAAI 2027 would be Feb 2027; workshop deadlines ~Oct 2026).

Given the timing (Nov 2026), the actionable windows are:

ICLR 2027 workshops (deadlines Dec 2026–Jan 2027) ✓
ICML 2027 workshops (deadlines ~Mar2027) ✓
NeurIPS 2027 workshops (deadlines ~May 2027) ✓
Main conference: ICML 2027 (deadline ~Jan 2027), NeurIPS 2027 D&B (deadline ~May 2027), ICLR 2028 (deadline ~Sept 2027), MLSys 2027 (deadline ~Sept 2026 — passed?), maybe MLSys 2028.
Also AAAI 2028 / AAAI 2027 (deadline ~Aug 2026 passed).
ACL/EMNLP: ACL 2027 (deadline ~Jan/Feb 2027?) — resource & evaluation tracks? EMNLP 2027 later. There's also "Language Resources and Evaluation" — LREC.

For "measurement protocol/analysis, no code no experiments" (well, it has a toy-model validation with 40k workloads but "无需跑实验/无需训练" — closed-form; the toy validation is simulation-like). Actually it says "已完成的 toy-model 工作" with validated results on 4 platforms × 40,000 workloads — so there IS some computation, but it's closed-form computable. "无 code 无实验" — hmm, Q1 says "这类'测量协议/分析型、无 code 无实验'的稿子" — measurement-protocol/analysis type papers without code or experiments. OK so the pitch is analysis/measurement paper.

Relevant workshops that accept analysis/measurement/short papers:

NeurIPS 2026 "Insights from Negative Results" — no, passed.
ICLR 2027 "Science of LLMs"? Hmm.
"ME-FoMo" (Model Evaluation for Foundation Models) at ICLR/ICML — very fitting! ME-FoMo @ ICLR 2024/2025... there was ME-FoMo at ICLR 2024? Actually "ME-FoMo: Model Evaluation for Foundation Models" workshop at ICLR 2024. And ICML 2025 had "ME-FoMo"? Let me search.
"Re-Bench" / "Benchmarks" workshops: "Benchmarking AI" at NeurIPS 2025? There's "1st Workshop on Benchmarks"?
"Building Trust Workshop"?
"Helm"?
SysML side: "ML for Systems @ NeurIPS" (MLSys-related workshop "ML for Systems" at NeurIPS 2025?), "SysML" conference. Also "ISCA 2027" D&B? No, ISCA has "SRC". ASPLOS has "DARTS"? Hmm.
"Hardware for ML" / "Efficient Systems for Foundation Models" — NeurIPS 2025 had "Efficient Systems for Foundation Models" workshop? Hmm.
"AI4Sys / Sys4AI".
"Evaluation of Agentic Systems"?
"SafeAI @ AAAI/ICLR" — fits AI safety angle.
"AISafety workshop" (IJCAI).
"SIREN: Safety-benchmarks"? Hmm.
"NeurIPS 2026 Workshop on Responsible AI"?
"ICLR 2027 Workshop on Reliable ML from Theory to Practice"?

Also main-conference paths:

NeurIPS Datasets & Benchmarks track — accepts measurement/protocol papers with code+data typically required. Deadline ~May 2027 (for NeurIPS 2027). Acceptance rate ~25-30%.
ICML 2027 Position Paper track? ICML 2025 had position papers track. ICML 2026 might have "Position Paper Track" too. Hmm.
ICLR 2027 — deadline passed (Sept 2026).
ACL 2027 Resource & Evaluation track — deadline likely Feb 2027 (ARR). ACL has a "Resources and Evaluation" theme track! EMNLP 2026 deadline... passed (May 2026). ACL 2027 via ARR cycles: ARR October 2026 cycle (commitment to ACL 2027?) Hmm, actually ARR Oct 2026 → ACL 2027 commitment. ARR deadlines: Oct 2026 cycle deadline ~Oct 2026 (passed or imminent?), Dec 2026 cycle → ACL 2027? Let me think: ACL 2025 used ARR Feb 2025 cycle... ACL 2026 (San Diego?) used ARR Oct 2025 cycle. So ACL 2027 would use ARR Oct 2026 (deadline ~Oct 2026, passed) or maybe also Dec 2026? Hmm. Actually EMNLP 2026 used ARR May/June 2026. Let me search.
AAAI 2028 (deadline ~Aug 2027) — too late? In window2026H2-2027: AAAI 2027 deadline was Aug 2026 (passed).
COLM 2027 — deadline ~March 2027. COLM has "D&B"-ish? COLM 2025 had a "Datasets & Benchmarks" track? Hmm, not sure.
"MLSys 2027" — deadline likely September 2026 (passed). Actually MLSys 2026 deadlines: abstract Sept 2025. So MLSys 2027 ~Sept 2026 passed. MLSys 2028 would be Sept 2027 (in window? just at edge).

Hmm wait, the task says "截稿日期（2026H2–2027 窗口）" — deadlines in the 2026H2–2027 window. So anything with deadline July 2026 – Dec 2027. That includes ICLR 2027 (Sept 2026 — passed but in window), ICML 2027 (Jan 2027), NeurIPS 2027 (May 2027), plus workshops.

And "E&D" — maybe this is "Evaluation & Development"? Hmm. Or maybe the user means "NeurIPS D&B / ICML E&D"? Hmm, hold on — maybe "E&D" refers to the new ICML track "Evaluation and Data"? Or "Empirics & Data"? Let me just search. Actually I wonder if it's "ICLR 2027 Datasets & Benchmarks"? No... Hmm, maybe it's "Evaluation & Data (E&D) track" at ECML PKDD? Or "EVAL"? Hmm. Or maybe the user means "AISTATS/CoLM E&D"?

Hmm, actually there IS a thing: "ICML 2025 Workshop on Evaluation"? And "EvalLM"? Hmm.

Wait — could "E&D" be "Evidence & Demonstration"? Or in the context of alignment: "Eliciting Deliberation"? Hmm. Or "Experiments & Data"? Hmm. Or maybe it's "Evaluation and Data (E&D) track at EMNLP 2027"? Hmm, EMNLP has "Theme: Language Resources and Evaluation (LREC)"...

Actually! I remember now: NeurIPS 2025 had a new track called "Evaluation and Data (E&D)"? Hmm, no. Hmm, wait — NeurIPS 2025 Datasets and Benchmarks Track... and there's also "ICLR 2026 Evaluation"... Hmm.

Hmm, could it be "E&E"? Or maybe it's a typo for "D&B/ERE"? The previous report might mention it. The task card says "workshop paper → 主会 D&B/E&D". Maybe in their SOP or the previous round report (arena-review-report-raw-20261125.md) there's context. The task says don't re-review novelty and answer ≤70 lines, but I could peek at the previous report and the SOP file for context about what "E&D" means. The task says don't modify the repo — reading is fine. Let me check the workspace for those files.

Actually, wait — "E&D" might be "Emerging Directions"? Hmm. Or "ICML 2026 Evaluation & Data track"? Hmm. Hmm, let me think about CoLM (Conference on Language Modeling) — COLM 2025 had tracks? Hmm. Or "Evaluation and Development"...

OH WAIT. I think I remember: ICLR 2025 introduced "Position Paper Track"? No... ICML 2025 introduced a "Position Paper Track"? Hmm. And there's "EVAL @ ..."...

Actually — maybe it's "Evidence & Data"? Hmm no. Let me look: in the ML systems world there's "Experimental & Demonstration"? Hmm. Or maybe the D&B is NeurIPS Datasets & Benchmarks, and E&D is "Evaluations & Data" at... Hmm.

Hmm, maybe it's "ICML 2027 Evaluation and Data (E&D) Track"? I really should search. Or check the repo files first — the previous report likely defines these. Let me start by looking at the workspace.

Plan:

Read the SOP file and previous report (skim) to understand context (allowed — just don't re-review novelty).
Web searches (parallel batches):
ICLR 2027 workshops CFP relevant to evaluation/measurement/safety/systems
ICML 2027 deadlines
NeurIPS 2027 Datasets & Benchmarks track deadline + acceptance rate
Workshop fees: ICLR 2027 registration fees, ICML 2027 fees, NeurIPS 2026 fees (as proxy), workshop-only registration policies
Specific workshops: ME-FoMo, "Science of LLMs", "SafeAI", "Insights from Negative Results", "ML for Systems", "Efficient Systems for Foundation Models", "Benchmarking", "Repl4NLP", "BlackboxNLP" (analysis), "RepL4NLP", "Idea"...
Verify deadlines and fees with fetch_page on official CFP pages.
Compose ≤70 lines Chinese report with conf markers and URLs.

Time box 30 min — be efficient. Let me start.

First, look at workspace files for context (quick), then searches.

Actually the deliverable is reply text only, no files. Let me be careful: "回答 ≤ 70 行" — the reply must be ≤ 70 lines. That's tight but doable.

Let me check the workspace first.

Ran commands
2

Thought for 1 minute

The workspace is empty — no SOP file, no previous report. So I work from the task card alone. "E&D" remains ambiguous — likely "Evaluation & Data" or similar track. Let me search the web to figure out what D&B/E&D tracks exist. Given the context "主会 D&B/E&D" — NeurIPS Datasets & Benchmarks (D&B) is clear. "E&D" might be a track at another main conference. Let me search.

Actually — I recall now! ICLR has no D&B track, but ICML 2026 might have introduced something. OR — "E&D" could be "Evaluation & Development"? Hmm. Wait, maybe it's "Evaluations and Data (E&D)" track at AAAI? Hmm, no.

Hmm — maybe it's not a track name but the user's shorthand: "D&B/E&D" = "Datasets & Benchmarks / Evaluation & Data" tracks generally. There IS a "Workshop on Evaluation (Eval)"... Hmm.

Actually! I think I've got it: NeurIPS 2025 had a new "Evaluation and Data (E&D)"? Hmm no. Let me think about "EVAL"...

Hmm, what about "ICML 2025: Evaluation of AI systems"? Hmm. Or maybe "E&D" = "Empirical & Data"? Hmm.

Hmm, wait — maybe it's about the alignment conference scene: "Eliciting & Detecting"? Hmm. Or "Evidence & Data" track at... Hmm.

OR — the user might mean "主会 D&B"（NeurIPS Datasets & Benchmarks）和 "E&D"（Evaluation & Diagnostics?） Hmm.

Actually there's another possibility: "E&E" at ... no. What about "D&E"... Hmm. What about "MLSys D&B"? Hmm.

Let me just search for it. Possibly it's the "ICLR 2026 Workshop on Evaluation"? Or the user could mean "EMNLP Findings"? Hmm.

Actually, maybe "E&D" is "Evaluation & Data" track of CoLM 2025/2026! Hmm — CoLM (Conference on Language Modeling) 2025 had tracks like "D&B"? Hmm.

OR — "EvalSys"? Hmm.

One more guess: "E&D" = "Experiments & Demonstrations"? Hmm.

You know what — there's a well-known one: "EVAL" workshop... Hmm.

Hmm, what about "NeurIPS 2026 Evaluations and Data (E&D) track"? Hmm, hold on. Actually I do recall NeurIPS 2025 introduced a new track called "Datasets & Benchmarks" (since 2021) and also... hmm.

Let me think about what a "资深审稿人 + 投稿顾问" for "ML/systems workshop 与顶会 D&B/E&D 轨道" would mean. D&B = Datasets & Benchmarks. E&D = ... "Evaluation & Diagnostics"? "Empirical & Data"? "Evaluation and Data"?

OH WAIT. I remember now! ICML 2025 had a track called "Position Paper Track"... no. Hmm, but AISTATS? no.

Actually — "E&D" could be "Emerging & Disruptive Ideas (EDI)"! YES! That's it! ICRA has "Emerging & Disruptive Ideas" track... hmm, but that's robotics. Hmm.

Hmm, what about "ECIR"? no.

Hmm — "Evaluation & Data (E&D)"... Let me just do web searches; if it turns out ambiguous, I'll interpret "E&D" generically as evaluation/data-oriented main-conference tracks (e.g., NeurIPS D&B, ICML position/evaluation tracks, COLM D&B, ACL Resources & Evaluation). Actually since the workspace is empty and this is "第二轮", the previous report isn't accessible. The task says "上轮审 novelty（报告见 arena-review-report-raw-20261125.md）" but that file doesn't exist in the workspace. Fine — I proceed from the task card.

Let me now do parallel web searches for the key facts. Batch 1:

NeurIPS 2027 Datasets and Benchmarks track deadline
ICML 2027 paper submission deadline
ICLR 2027 workshops deadline CFP (evaluation/measurement)
ML systems workshop 2027 CFP ("ML for Systems", "SysML", MLSys 2027 deadline)

Then batch 2 for specific workshops + fees.

Given today is 2026-11-25:

ICLR 2027: conference ~April/May 2027 (probably San Juan? or wherever). Paper deadline was ~Sept 2026 (passed). Workshop deadlines ~Dec 2026-Jan 2027 (OPEN — great target).
ICML 2027: conference ~July 2027. Deadline ~late Jan 2027 (OPEN-ish — within window).
NeurIPS 2027: deadline ~May 2027 (open). D&B track same deadline. Acceptance rates: D&B ~25-30%.
NeurIPS 2026: conference Dec 6-12, 2026 (next week or so!). Its workshops deadlines passed.
MLSys 2027: deadline ~Sept 2026 (likely passed). Abstract deadlines... Actually MLSys 2026 was May 2026 in San Jose? Hmm, MLSys 2025 was May 2025. Deadline for MLSys 2025 was Sept 2024. So MLSys 2027 deadline ~Sept 2026 (passed). MLSys 2028 deadline ~Sept 2027 (within "2027 window"?).
EuroSys 2027: two deadlines (May 2026 & Nov 2026?). EuroSys has rolling: fall deadline ~Nov 2026 for EuroSys 2027. Hmm — EuroSys 2027 would be April 2027. EuroSys uses two submission cycles: ~May and ~October. October 2026 cycle might have just passed (Oct 2026). Hmm.
ASPLOS 2027: rolling quarterly? ASPLOS 2026 deadlines passed. ASPLOS 2027 (spring 2027 conference?) — ASPLOS moved to multiple cycles (three deadlines per year: ~Jun, ~Oct, ~Feb?). ASPLOS 2027 might have a Feb 2027 cycle! Hmm, ASPLOS 2025 had deadlines Jun/Oct/Feb for spring2025 conf... Actually ASPLOS 2025 was March 2025, with deadlines in 2024 (Jun/Oct). Hmm.

For systems-flavored analysis papers: "MLSys" (main conf), "EuroSys/SOSP D&B"? SOSP 2027 (fall 2027, deadline ~Apr/May 2027). OSDI 2027 (deadline ~Dec 2026!). OSDI '27 would be July 2027, deadline typically ~December 2026 (OSDI '25 deadline was Dec 2024). Actually OSDI '26 deadline Dec 2025. So OSDI '27 deadline ~Dec 2026 — RIGHT NOW in window! But a toy-model measurement paper with no implementation is a poor fit for OSDI.

Realistically the best fits for "measurement protocol/analysis" are:

NeurIPS 2026/2027 workshops like "Insights from Negative Results" (NeurIPS 2025 had it), "ME-FoMo", "Benchmarking...", "Science of LLMs", "SafeAI".
ICLR 2027 workshops (deadlines Dec 2026–Jan 2027).
ICML 2027 workshops.
SysML-ish workshops: "ML for Systems and Systems for ML" (NeurIPS 2025 workshop "ML for Systems"), "SysML" (now MLSys conf), "ISCA/MICRO workshops", "HPCA workshops". Also "MLSys workshop on Efficient Systems for Foundation Models" (NeurIPS 2024?).

Also very fitting: "Workshop on the Economics of Large Language Models"? Hmm. And "SoLaR", "ME-FoMo" (Model Evaluation For Foundation Models) — at ICLR 2024 (and it was at ICML 2025? hmm). There's also "EvalAI / EvalRS"? Hmm. And "Reliable ML from Theory to Practice (R2-FM?)"...And for the safety angle: "Specification Self-Correction, SCALR@COLM 2025" — the author knows COLM. COLM 2027 deadline ~March 2027. COLM has... hmm, COLM 2025 had "D&B" track? Hmm.

Also "SafeAI workshop @ AAAI 2027" (AAAI 2027 is Jan 2027 in Singapore? AAAI 2027 — hmm, AAAI 2026 was Jan 2026 in Singapore; AAAI 2027 would be ~Jan/Feb 2027 in ... deadline for AAAI 2027 papers was ~Aug 2026, passed). SafeAI workshop deadlines ~Oct/Nov 2026.

OK let me search now. I'll batch multiple web_search calls in parallel.

工作区为空（无 SOP/上轮报告文件），我将基于任务卡直接执行联网核实。先并行检索关键 venue 事实。

Searched the web

Thought for 1 minute

Good progress. Key facts so far:

NeurIPS 2027: deadline ~May 20-21, 2027 (not yet official as of Oct 30, 2026; CFP typically published March/April). IMPORTANT: NeurIPS has renamed its D&B track! Per NeurIPS newsletter April 2026: "The NeurIPS Evaluation and Datasets (previously Datasets and Benchmarks) track" — so E&D = "Evaluation and Datasets" track at NeurIPS! That resolves "D&B/E&D" — the track was renamed from Datasets & Benchmarks (D&B) to Evaluation and Datasets (ED/E&D) at NeurIPS 2026. Great — this is exactly the "主会 D&B/E&D" reference: NeurIPS Datasets & Benchmarks → now Evaluation and Datasets track. So Q2's "主会 D&B/E&D" = NeurIPS's Evaluation and Datasets track (2027 edition).

ICML 2027: official CFP is out (blog.icml.cc Nov 24, 2026 — yesterday!). Conference in Rio de Janeiro, July 31–Aug 6, 2027. Submission deadline January 22, 2027, abstract deadline January 14, 2027 (blog says Jan 14 abstract; opencurious estimated Jan 16 — use the official blog: "abstract submission deadline eight days earlier on January 14, 2027"). New policies: two-stage reviewing (first-stage rejection), reciprocal reviewer requirement, co-author limit 2 papers for non-reviewers. Also mentions "papers for position tracks (PPT)" at NeurIPS; ICML 2026 had position papers track too. ICML 2027 CFP "features a number of changes" — need to check if ICML 2027 has a position paper track or D&B-like track. Let me fetch the ICML 2027 CFP.

ICLR 2027: main deadline passed (Sept 25, 2026). ICLR 2027 in San Francisco, Apr 26-30, 2027. Workshop deadlines would be ~Dec 2026–Jan 2027. Need workshop CFP info.

ME-FoMo search wasn't great. Need targeted searches for workshops.

Also for NeurIPS 2026 (Dec 6-12, 2026 — happening now/next week in Europe? Actually NeurIPS 2026 is Dec 6-12, 2026): its workshops are Dec 2026 — deadlines passed. But "NeurIPS 2026 workshop" papers could still be presented — not useful for submission now.

Workshop targets with deadlines in Dec 2026–2027:

ICLR 2027 workshops (conference Apr 26-30, 2027; workshop day likely Apr 26 or 30; deadlines typically Dec 2026–Feb 2027)
ICML 2027 workshops (conference Jul 31-Aug 6, 2027; workshop deadlines ~Mar-Apr 2027)
NeurIPS 2027 workshops (deadlines ~May-Jun 2027)
MLSys 2027 (deadline ~Sept 2026 — probably passed; verify)
COLM 2027 (deadline ~Mar 2027)
AAAI 2027 workshops — AAAI 2027 conference is Jan 2027 (Singapore?) — deadlines passed mostly.

Also relevant: "Evaluation and Datasets" track renaming means the 2027 call will likely be under that name.

Now specific workshops to verify (analysis/measurement friendly, ML/systems or eval/safety):

ME-FoMo (Model Evaluation for Foundation Models) — was at ICLR 2024... ICML 2025? Need current.
"Insights from Negative Results in NLP" (Insights-NLP) — EMNLP-affiliated. Hmm.
"Science of LLMs" (SoLLM?) — ICML 2025 workshop.
"SafeAI" workshop — AAAI/ICLR affiliated.
"ML for Systems" / "Systems for ML" — NeurIPS workshop "ML for Systems" / "SysML workshop"...
"Benchmarking in the Age of Foundation Models"?
"Evaluation of Agentic Systems"?
"Reliable and Robust Foundation Models"?
"Helm"?
"Data Problems for Foundation Models"?
"Building Trust in LM Workshop"?
"AlignEval"?

Also systems conferences with D&B flavor: MLSys (has a "MLSys artifacts"?), EuroSys (has "artifacts evaluation"), ASPLOS (has "DARTS"?). Actually systems venues: workshops like "ISCA 2027: Workshop on ML for Computing Architecture", "HPCA", "MICRO". Also "SysML" has become MLSys conference. MLSys 2027: check deadline.

Let me also check:

NeurIPS 2026 "Evaluation and Datasets" track CFP page (for format/fees/acceptance rate) → gives info relevant to NeurIPS 2027 ED track.
NeurIPS E&D acceptance rates: D&B track 2025 acceptance rate ~28%? Need source.
ICML 2027 CFP details (tracks).
ICLR 2027 workshops list (there's usually a workshop page with all CFPs).

Fees:

NeurIPS 2026 registration fees (main conf + workshops). NeurIPS 2026 in Europe (Madrid? "Europe TBD"). NeurIPS 2025 was San Diego: in-person registration ~$1150 non-student? Actually NeurIPS 2025 fees: ~$750 early? Hmm, must verify online. NeurIPS 2024: $750? Hmm no — NeurIPS 2024 Vancouver: regular $1050? I must not rely on memory. Search.
ICML 2026 fees (Rio 2027 not published). ICML 2025 Vancouver: ~$850? verify.
ICLR 2027 fees: ICLR 2026 (Rio?) hmm, ICLR 2026 was in Rio? No — ICLR 2026 was San Juan, Puerto Rico? Hmm. ICLR 2025 Singapore. ICLR 2027 San Francisco. Registration fees need verification.
Workshop-only registration: many conferences offer workshop-only day passes at lower cost. NeurIPS offers workshop-only registration? Usually yes ~$100-250? verify.
Student rates, waivers: NeurIPS has volunteer/DEI travel awards; ICML has registration waivers? Verify what's on official pages.
arXiv: free to submit (no fee). arXiv moderation fees? No — arXiv is free for authors (submission is free; they ask for optional endorsement...). Yes, arXiv submission is free. OpenReview free. So "arXiv 是否 0 元" — yes, $0.

Acceptance rates:

NeurIPS D&B 2025: need source. NeurIPS 2025 D&B ~ 32%? Must verify. If not found, say 未验证.
Workshop acceptance rates: typically 25-50%, not officially published — mark conf.
ICML 2026 overall ~22%? verify.

Now, workshop specifics. Let me search for ICLR 2027 workshops list + a few specific ones. Also MLSys 2027 deadline. And COLM 2027.

Also the "E&D" mystery is likely solved: NeurIPS renamed D&B → "Evaluation and Datasets" (E&D? or "ED"). The newsletter says "Evaluation and Datasets (ED)"... Actually it says "Responsible AI (RAI) fields for Evaluations and Datasets (ED) track" and "Call for Papers for Evaluation and Datasets". So the track is now "Evaluation and Datasets" — abbreviated ED or E&D. Great. So in Q2, "主会 D&B/E&D" = NeurIPS Evaluation and Datasets track (formerly Datasets & Benchmarks). I should note this renaming in the report.

Hmm wait, but the task says "顶会 D&B/E&D 轨道" as a plural concept across conferences — maybe NeurIPS ED track + others. I'll interpret as: NeurIPS Evaluation & Datasets (former D&B) track as the primary main-conference target, plus possibly similar tracks elsewhere (e.g., COLM D&B?). Let me quickly check if COLM has D&B track... COLM 2025 had... hmm not sure. Skip if time-boxed.

Next batch of searches:

NeurIPS "Evaluation and Datasets" track CFP 2026 (page detail: format, page limits, acceptance rate)
ICLR 2027 workshops list / call for workshop proposals (deadlines)
MLSys 2027 deadline CFP
NeurIPS 2026 registration fees

Then:
5. Specific workshops: "ME-FoMo2027" or eval workshops at ICLR 2027; "SafeAI 2027"; "Insights from negative results 2027"; "ML for systems workshop 2027"
6. ICML 2026/2027 registration fees
7. NeurIPS 2025 Datasets & Benchmarks acceptance rate
8. COLM 2027 deadline

Let me batch4 at a time.

关键发现：NeurIPS 已将 D&B 轨道更名为 Evaluation and Datasets (E&D/ED) —— 这正是"D&B/E&D"所指。继续核实 E&D 轨道细节、workshop 窗口与费用。

Searched the web

Thought for 20 seconds

Great progress. Key facts gathered:

NeurIPS 2026: Sydney main + Atlanta + Paris satellites, Dec 6-12, 2026. Fees (Paris official site): workshops-only €180-300 (student/academic/industry, standard); full €480-950. Sydney/Atlanta: workshops-only $200-600 depending on site/affiliation. Virtual-only $50-275. NeurIPS 2027 fees: not published.

NeurIPS E&D track: renamed from Datasets & Benchmarks to "Evaluation and Datasets" (per NeurIPS blog April 2026). For NeurIPS 2026: abstracts May 4, 2026, full papers May 6, 2026. For NeurIPS 2027: expected ~mid-May 2027 (not yet official). Format: 9 content pages NeurIPS style (from D&B 2024 CFP). Need to check the 2026 ED CFP page for details + acceptance rate. Let me fetch https://neurips.cc/Conferences/2026/CallForDatasetsBenchmarks or the ED call page.

ICLR 2027: San Francisco, Apr 26-30, workshops Apr 29-30. Main deadline passed. Workshop paper deadlines: typically announced per-workshop, usually Dec 2026-Feb 2027. Need to find ICLR 2027 workshop list. There's usually https://iclr.cc/Conferences/2027/CallForWorkshops or a "Workshops" page. Workshop proposals for ICLR 2027 were probably due ~Sept-Oct 2026, and accepted workshops announced ~Nov 2026. Let me check the ICLR 2027 workshops page.

MLSys 2027: deadline Oct 30, 2026 — PASSED (26 days ago). Conference June 21-25, 2027, Bellevue. So not a path. (Could mention as closed.)

ICML 2027: Rio, July 31-Aug 6, 2027. Abstract Jan 14,2027, paper Jan 22, 2027 (official blog). Two-stage review, reciprocal reviewer, co-author caps. Need ICML 2027 CFP for tracks (is there a position paper track? evaluation track?). Let me fetch the ICML 2027 CFP page (icml.cc). Also ICML registration fees (2026 for reference; 2027 not published).

Still needed:

ICLR 2027 workshop list +2-3 specific relevant workshop CFPs with deadlines/formats (e.g., eval/benchmark/safety/systems workshops). Let me fetch iclr.cc/Conferences/2027/... workshop page.
NeurIPS 2026 E&D track CFP details (acceptance rate, format, whether analysis/protocol papers without datasets welcome).
NeurIPS D&B/ED acceptance rates (2024/2025).
ICML 2027 CFP details + ICML fees (2026) + ICML workshop info.
arXiv fees (free) — well known, but cite arxiv.org help page. Actually arXiv submission is free; there are no author fees. I can cite https://info.arxiv.org/help/submit/index.html or the "cost" FAQ. Quick search maybe not needed; but the task demands verifiable sources for fees... "arXiv 是否 0 元" — I should give a source. arXiv help page says submission is free. I know https://info.arxiv.org/help/faq/index.html has "Is there a cost?" Hmm. Let me do a quick search for "arXiv submission free of charge" to get a citable URL.
Workshop acceptance rates — typically not published; mark conf low.

Also maybe AAAI 2027 SafeAI workshop or similar. And COLM 2027 deadline (~March 2027) for completeness? COLM 2025 was Oct 2025 in Montreal; COLM 2026? Hmm, COLM 2026 deadline ~March 2026, conference Oct 2026? COLM 2027 deadline likely ~March 2027. COLM doesn't have D&B track AFAIK. Skip COLM or mention briefly.

Let me now fetch:

https://iclr.cc/Conferences/2027/CallForWorkshops or search "ICLR 2027 workshops accepted list"
https://neurips.cc/Conferences/2026/CallForDatasetsBenchmarks (2026 ED track CFP)
NeurIPS D&B 2025 acceptance rate search
ICML 2026 registration fee search

Batch these.

Searched the web

Thought for 30 seconds

Excellent findings:

NeurIPS ED track (Evaluations & Datasets): Renamed from D&B at NeurIPS 2026. Expanded scope: "evaluation as a scientific object of study" — "Works whose primary contribution is the analysis, critique, redesign, or stress-testing of evaluation practices or methodologies are fully in scope." This is HUGE for this paper — a measurement-protocol/analysis paper is now explicitly in scope for the ED track. CFP URL: https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets; blog: https://blog.neurips.cc/2026/03/23/introducing-the-evaluations-datasets-track-at-neurips-2026/. Also note main track has "Negative Results" contribution type now! And "Concept & Feasibility" contribution type. Interesting — NeurIPS 2026 main track contribution types: General, Theory, Use-Inspired, Concept & Feasibility, Negative Results. For NeurIPS 2027 these may persist.

Also the example in the newsletter: "Fairness Through Awareness (Dwork et al., 2011)... main contribution is about the definition of a new fairness metric... Evaluations & Datasets Track is most appropriate" — a new metric/scoring definition fits the ED track!

NeurIPS 2025 D&B: main track 24.52% acceptance (5290/21575). D&B acceptance rate ~25% (per Mannheim news "CORE Rank A*, Acceptance rate 25%"). Good enough with conf caveat.

ICML 2026 fees: student conference-only $200 early/$245 late; academic $450/$500; full (tutorials+conf+workshops) student $425/$540, academic $900/$1030; virtual $50-200. Source: piedpiperg.github.io (unofficial). Hmm — need better source. Let me check ICML 2026 official registration page... icml.cc/virtual/2026/registration? Hmm. Might not be accessible. I'll cite it as unofficial/indicative and mark 2027 未公布. Actually let me quickly fetch the ICML 2027 blog post to confirm the CFP details and check whether ICML 2027 has an evaluation/dataset track or position papers track.

ICLR 2027 workshops: workshops Apr 29-30, 2027. Workshop CFP deadlines — need specific workshops. ICLR workshop proposals were due ~Sept 2026; accepted workshop list usually posted ~Oct/Nov. Let me search for specific ICLR 2027 workshops in eval/safety/systems space:

"ICLR 2027 workshop evaluation"
"ICLR 2027 workshop benchmarks"
"ICLR 2027 workshop AI safety"
"ICLR 2027 workshop systems/MLSys"

Also candidates beyond ICLR:

ICML 2027 workshops (~Mar-Apr 2027 deadlines)
NeurIPS 2027 workshops (~May-Jun 2027)
AAAI 2027 workshops passed (AAAI-27 conference Jan 2027 Singapore?).
COLM 2027: deadline ~Mar 2027; has "D&B"? Hmm, COLM 2025 had... actually COLM 2024/2025: tracks? COLM 2025 had a "Datasets & Benchmarks" track? Hmm, not sure. Let me check quickly.

For "ML/systems workshop" specifically:

MLSys 2027 workshops (MLSys conf Jun 21-25, 2027 — workshop deadlines ~Feb-Mar 2027?). MLSys has workshops (e.g., "ML for Systems", "SysML workshop"?).- "MLSys Workshop on Efficient Systems for Foundation Models"?
ISCA 2027 / MICRO / HPCA workshops: e.g., "AWLCA", "CBSys"... Probably too hardware-arch focused.
"Workshop on ML for Computer Architecture and Systems (MLArchSys)"? Hmm.
ASPLOS 2027 workshops? ASPLOS 2027: hmm.
"SoK" style: systems conferences accept "SoK" papers (S&P Oakland SoK; USENIX; EuroSys?). Actually for measurement/analysis in systems: IEEE S&P SoK track (Security & Privacy) — but this is not security. USENIX ATC/OSDI — no. Hmm.

Wait — actually, what is this paper about? Hardware spec + workload prior, decomposition tree, deep vs shallow judgments, incremental information H(D|S), flat-rate negative control... 4 platforms × 40,000 workloads. Cross-cuts roofline (hardware performance modeling!) and ID3 info gain and PID (partial information decomposition). And alignment framing (reward hacking, Goodhart, spec revision). So it's like: a scoring/measurement protocol for how much incremental information "deep" nodes of a decomposition (e.g., hardware-level specs in a roofline-style decomposition of a compute platform) provide over shallow judgments, in the context of evaluating/aligning... something. "workload prior" — hardware spec + workload prior gives closed-form computation. "flip 43–56%" — judgment flips when adding deep info. So it measures value-of-information for hierarchical evaluation of platforms/agents?

Whatever the exact domain, the venues remain: ML evaluation workshops, ML systems workshops, safety/alignment workshops, and NeurIPS ED track.

Time check: I have enough for the big picture. Now I need 3 specific workshops with 2027 deadlines. Let me search for ICLR 2027 workshops that fit. Also check "Science of LLM workshop 2027", "ME-FoMo 2027", "SafeAI 2027", "benchmark workshop ICLR 2027".

Let me do a batch:

search "ICLR 2027 workshop" benchmarks evaluation measurement2. search ICLR 2027 workshop safety alignment "workshop"
search "MLSys 2027 workshop" call for papers
fetch https://blog.icml.cc/2026/11/24/new-peer-review-policies-for-icml-2027/ (already have gist from search; maybe fetch the CFP link for tracks/position papers)

Actually, more targeted: there's typically a page listing accepted ICLR 2027 workshops. Try fetching https://iclr.cc/Conferences/2027/AcceptedWorkshops or search. Let me search.

E&D 轨道扩scope（"evaluation as a scientific object of study"）对本定位非常有利。现在锁定具体 workshop 窗口与 ICLR 2027 workshop 列表。

Searched the web

Thought for 1 minute and 18 seconds

Excellent! Found three highly relevant ICLR 2027 workshops:

SciEval: The 1st Workshop on the Science of Evaluation @ ICLR 2027 (science-of-eval.github.io) — PERFECT fit: "studying evaluation as a scientific object in its own right", meta-evaluation: validity, robustness, reproducibility, psychometrics/preregistration explicitly invited ("clinical-trial methodology has a mature treatment of power, preregistration, and multiplicity... explicitly invite submissions from these other measurement communities"). Submission deadline Feb 1, 2027, notification Feb 19, 2027. Workshop Apr 29-30, 2027, San Francisco, hybrid. OpenReview double-blind. Non-archival presumably. Page limits TBA ("Formatting instructions, page limits... will be posted"). Work already published at ICLR/ICML/NeurIPS discouraged.

Science and Society of Modern AI @ ICLR 2027 (science-society-ai.github.io) — "Testing the claims about AI that society already relies on". Submission deadline Jan 30, 2027 AoE. Two non-archival tracks: Full papers up to 8 pages; Tiny papers up to 3 pages ("a simple unpublished idea with its evaluation, or a self-contained theoretical result"). Topics include "Measurement: the evaluations that decisions rest on — validity and resolution of benchmarks". Great fit for analysis/short paper. Call opens Dec 7, 2026.

Verifiable Agent Safety @ ICLR 2027 (verifiableagentsafety.github.io) — specs/guarantees/evaluation with guarantees; "specification gaming, guarantee coverage". Two tracks: regular 5–9 pages, short papers 2–4 pages ("modest self-contained results, replications, counterexamples, early-stage work"). Abstract Jan 25, 2027; paper Feb 1, 2027; notification Feb 26. Non-archival, double-blind. Topics include "Learning and evaluation with guarantees: verification feedback... specification gaming" and "Communication, evidence, and oversight... assumptions placed on observations, semantic interpretations, and judgments" — fits the alignment/spec angle (given the SCALR/spec-self-correction cut). Dates "proposed and subject to confirmation".

These three are all ICLR 2027 workshops with deadlines Jan 25–Feb 1, 2027. But maybe also find one systems-flavored workshop for diversity (ML/systems direction). The task says "ML/systems 方向的 workshop" — the 3 most matching. SciEval is evaluation-science (ML), Science&Society is measurement/claims, Verifiable Agent Safety is safety/specs. A systems-flavored one would be e.g. "ML for Systems" workshop at NeurIPS/ICLR, or MLSys workshops. Let me do one more search for a systems-flavored workshop (e.g., "MLSys 2027 workshop", "ICLR 2027 workshop systems efficiency" or "NeurIPS 2026 workshop ML for systems"), to have alternatives. Also the flat-rate negative control / hardware spec angle fits "MLSys" workshops like "Efficient Systems for Foundation Models" or "ML for Systems (ML4Sys)".

Also still need:

ICML 2027 CFP: does it have position/eval track? (blog says "number of changes... sister conferences NeurIPS 2026 and ICLR 2027"). Fetch the ICML 2027 CFP briefly. Also ICML 2027 deadlines: abstract Jan 14, paper Jan 22, 2027 (from official blog; myhuiban says submission 2027-01-14 which is the abstract). Notification May 3, 2027? (myhuiban) — blog didn't say. Fine.
Fees: ICLR 2027 registration fees — not yet known? "Registration opens December 23, 2026". So ICLR 2027 fees未公布/registration not open. ICLR 2026 (Rio) fees for reference? Quick search maybe. ICML 2027 fees: 未公布. NeurIPS 2027 fees: 未公布; NeurIPS 2026 known (Paris €130-300 workshops-only; Sydney/Atlanta workshops $200-600).
NeurIPS ED track 2027 deadline: estimated mid-May 2027 (CFP usually March/April). Mark as 未正式公布, estimate.
NeurIPS D&B/ED acceptance rate: ~25% (Mannheim says "Acceptance rate 25%" for D&B; main track 24.52% in 2025 per official blog). For ED2026 — probably similar; say ~25% conf 0.6 with sources.
arXiv cost: free. Need source URL: https://info.arxiv.org/help/submit/index.html or arxiv.org/help/faq. Let me quickly verify with a search or fetch.
Workshop fees: ICLR workshops typically require conference/workshop registration. ICLR 2025 (Singapore) workshop-only registration? ICLR registration fees vary. Since ICLR 2027 registration opens Dec 23, 2026, fees未公布. For reference give ICLR 2026 numbers? Let me search quickly "ICLR 2026 registration fee". Actually, time budget — I've used maybe 15 min. Let me do one more round of searches: (1) ICLR 2026 registration fee for reference; (2) arXiv submission cost free; (3) ICML 2027 CFP tracks (position papers?); (4) maybe ML4Sys/NeurIPS "ML for Systems" workshop 2026/2027 as a systems-flavored alternative.

Also for Q4 (加固建议): the paper has preregistration timestamp, negative control, permutation invariance. Highest ROI: (1) 一张结构图 (decomposition tree + H(D|S) 定义 + 负控制示意) — must; (2) comparison table vs ID3/roofline/PID/SCALR — must; (3) public data spot-check (e.g., published GPU spec pages) — optional; (4) make code/data public or at least artifact appendix for ED track (ED track requires Croissant metadata for datasets — but this is an evaluation-protocol paper, maybe code release helps); (5) tiny paper version for Science&Society (3p) as low-cost second shot.

Also should distinguish "workshop 录用概率" vs "主会录用概率" with conf.

Probability estimates (subjective):

Workshop (SciEval/Science&Society/VAS short): 40-60% conf 0.5-0.6 — analysis/protocol papers are the exact topic at SciEval; short tracks are friendlier. Risks: no empirical LLM results; toy structure; "no code no experiments" — SciEval explicitly wants methodology + psychometrics transfer, preregistration is a plus.
NeurIPS 2027 ED track (main conference): 15-25% conf 0.4-0.5 — ED explicitly welcomes "analysis, critique, redesign, stress-testing of evaluation practices" and "new metric definition" (Fairness Through Awareness example). But toy-only validation + no released artifact may hurt; ED requires Croissant/RAI metadata only for dataset submissions (this paper wouldn't submit a dataset... though the workload set could be packaged).
ICML 2027 main track: <10% conf 0.5 — two-stage review with first-stage rejection makes risky/incremental-position papers die fast; toy paper at ICML main is a stretch. ICML 2027 might have position papers track (ICML 2026 had "position papers" call per the di9 blog: "2026 site also ran calls for position papers"). Hmm, the ICML 2026 call had a position paper track? Actually I believe ICML 2025 had a "position paper track"? Hmm, not sure. The di9.ir blog says ICML 2026 had calls for position papers. If ICML 2027 has a position track, that could fit "measurement protocol advocacy" — but our paper is not a position paper per se; it's an analysis/technical paper. Keep ICML main as low-probability path or skip.

Path ranking for "概率最大的顶会中稿":

ICLR 2027 workshop (SciEval, Feb 1 2027) → 扩展后投 NeurIPS 2027 ED track (May 2027): workshop first (non-archival, no prior-publication bar for ED? Note: ED track likely allows papers that appeared as workshop non-archival — NeurIPS allows non-archival workshop papers. Also SciEval is non-archival.) This staged path maximizes combined probability.
直接投 NeurIPS 2027 ED track (May 2027): best main-conference fit after rename; risk: toy-only, no artifact.
Science & Society of Modern AI tiny paper (Jan 30, 2027) 或 Verifiable Agent Safety short (Feb 1) as low-cost parallel shots — these are workshop though. For "顶会中稿" paths maybe: ICML 2027 (Jan 22) main track — low prob, high effort; or NeurIPS 2027 Position Paper Track? Hmm — actually NeurIPS Position Paper Track (PPT) could fit a "measurement protocol/analysis note" framing, but our work is results-bearing, not a position. ED fits better.

Wait, but the Q2 asks: "在'概率最大的顶会中稿'目标下，给出排序后的 2–3 条路径（例如 workshop paper → 主会 D&B/E&D、或 analysis note 直接投某轨道）"。So paths can be staged. Distinguish workshop acceptance vs main-conference acceptance probabilities. Good.

Path A: ICLR'27 workshop (SciEval; fallback Science&Society tiny / VAS short) → 扩展投 NeurIPS'27 ED track. Workshop P≈50-60% (conf 0.55); NeurIPS ED P≈15-25% (conf 0.45).
Path B: 直接投 NeurIPS 2027 ED track (May 2027, CFP ~Mar-Apr 2027). P≈15-20% (conf 0.4). Preemptive risk: none; but no workshop feedback; also can still submit workshop versions later? Actually non-archival workshops allow later publication.
Path C: ICML 2027 main (Jan 22, 2027) — P≈5-10% (conf 0.55); high cost (reciprocal reviewing obligation: authors must serve as reviewers!); two-stage desk-filter risk. Alternatively AAAI 2028 (Aug 2027 deadline, in-window? AAAI 2028 deadline ~Aug 2027 — yes within 2027). Hmm, or COLM 2027 (~Mar 2027) — COLM is LLM-focused; our paper is hardware/workload + alignment-scoring — partial fit. I'll keep C as ICML 2027 main (noting risk) or maybe "NeurIPS 2027 Position Paper Track + ED" dual. Keep it simple: 3 paths = A (workshop→ED), B (direct ED), C (ICML 2027 main, 或 COLM 2027). Hmm.

Actually for path C, maybe more sensible: "SciEval→扩展→NeurIPS 2027 ED" and "直接 NeurIPS 2027 ED" and "ICML 2027 主会" — with C noted as low-probability/高成本. Also mention MLSys 2027 已于 2026-10-30 截稿（错过），MLSys 2028 (Oct 2027) 作为 systems轨道备份。

Q1: 3 most matching workshops:

SciEval @ ICLR 2027 — deadline Feb 1, 2027; non-archival; page limits TBA (conf 0.8 that it'll be ~4-9 pages typical); accepts analysis/meta-evaluation/measurement — explicitly psychometrics/preregistration; double-blind OpenReview.
Science and Society of Modern AI @ ICLR 2027 — deadline Jan 30, 2027; full 8p + tiny 3p non-archival; "Measurement: the evaluations that decisions rest on" topic; tiny paper fits "unpublished idea with its evaluation".
Verifiable Agent Safety @ ICLR 2027 — regular 5-9p + short 2-4p; deadline Feb 1, 2027 (abstract Jan 25); non-archival; fits spec-gaming/evaluation-with-guarantees framing.

All three: ICLR 2027 workshops day Apr 29-30 2027, SF. Acceptance of analysis/measurement/short: yes for all three (each explicitly). Workshop competitiveness for "measurement protocol/analysis, no code no experiments": high at SciEval (it IS the topic; psychometrics/preregistration invited); medium-high at Science&Society (measurement problems listed; tiny track welcomes self-contained theory); medium at VAS (wants formal results/verified monitors — our closed-form + exact-zero negative control reads as "formalizable"; risk: reviewers want agent-runtime verification). Note "无 code无实验" is slightly generous — there IS a toy validation (40k workloads) — position it as "closed-form + simulation-free validation".

Hmm wait — "无 code 无实验" — the task card itself frames it that way ("这类'测量协议/分析型、无 code 无实验'的稿子"), though the background says toy validation exists. I'll phrase as "分析/协议型、以闭式推导+toy 验证为主、无训练无真实系统实验".

Q3 fees per path:

ICLR 2027 workshops: 注册费未公布 (registration opens Dec 23, 2026 per scifig.ai citing iclr.cc). ICLR 2026 reference? Let me search quickly for ICLR 2026 registration fee to give量级. ICLR2025 Singapore: student ~$300? Hmm — must verify. Search.
Workshops随主会注册: ICLR workshop-only registration — ICLR usually sells workshop-only tickets? I believe ICLR offers "workshop only" registration. Need source... risky. I'll say:通常需注册（workshop-only 或全会），ICLR 2027 费用未公布，registration opens 2026-12-23 (source). Historical量级: ICLR 2026 student ~$xxx — only if verified.
NeurIPS 2027: fees 未公布; NeurIPS 2026 workshops-only: €130-300 (Paris, official neurips-europe.cc) / $200-600 (Sydney/Atlanta per qrsntu — unofficial). Better cite neurips-europe.cc official numbers. ED track registration: 作者需至少一人注册主会 (NeurIPS policy) — conf 0.7; source: NeurIPS registration FAQ. Hmm, "at least one author must register" is standard. I'll state it with conf.
版面费 (page charges/publication fees): NeurIPS/ICLR/ICML 无版面费 (proceedings free, OpenReview/PMLR) conf 0.85; workshops 无版面费 (non-archival, OpenReview) conf 0.8; arXiv $0 (source: arxiv.org help).
Waivers: NeurIPS has DEI/volunteer programs & student rates; ICML 2026 student rates; "registration waiver" — NeurIPS offers "registration support"? Hmm, verify quickly? Time-boxed — mark 未验证 for waivers, or search "NeurIPS registration support waiver". One quick search.

Let me now do final verification batch (4 searches):

"ICLR 2026 registration fee" (reference scale)
"arXiv submission free of charge authors" (cost = 0)
"ICML 2027 call for papers" tracks position (fetch blog/icml.cc CFP)
"NeurIPS registration support waiver student travel award" (waivers)

Then maybe one quick check on a systems workshop alternative (NeurIPS 2026 "ML for Systems" workshop or ICLR 2027 systems workshop) — if time permits, include as "备选" in Q1 briefly. Actually Q1 wants exactly 3; I can add one line "备选: ...". Let me include a systems-flavored 4th as backup only if verified quickly.

Actually — one of the searches should also confirm whether SciEval is archival or not and page limits. The site says "Formatting instructions, page limits, and the submission link will be posted here when the call opens" → 未公布. Science&Society: full 8p/tiny 3p confirmed. VAS: 5-9p/2-4p confirmed ("dates proposed and subject to confirmation").

OK final batch now.

三个高度匹配的 ICLR 2027 workshop 已锁定（SciEval / Science & Society / Verifiable Agent Safety）。最后一轮核实费用与备用事实。

Searched the web

Thought for 2 minutes and 30 seconds

HUGE finding: ICML 2027 main track has contribution types including "Datasets, Evaluations, and Benchmarks" and "Position Papers" — all within the MAIN TRACK of ICML 2027! (https://icml.cc/Conferences/2027/ContributionTypes). So there IS an "E&D" style track at ICML 2027 — "Datasets, Evaluations and Benchmarks (DEB)" contribution type within the main track. This changes the path analysis:

ICML 2027 "Datasets, Evaluations and Benchmarks" contribution type (main track) — deadline Jan 22, 2027 (abstract Jan 14). This is a main-conference submission option with evaluation-science fit. Risk: two-stage review (first-stage rejection by AC flag) — toy work might get flagged; reciprocal reviewing requirement (one co-author must be eligible reciprocal reviewer and complete reviews — burden); co-author quotas.
NeurIPS 2027 ED track (separate track) — deadline ~May 2027 (estimate).
ICLR 2027 workshops (Jan 30/Feb 1, 2027).

Also NeurIPS 2026 contribution types (General, Theory, Use-Inspired, Concept and Feasibility, Negative Results) — interesting: "Negative Results" and "Concept and Feasibility" types exist at NeurIPS 2026 main track too. For NeurIPS 2027 these may continue.

Now — "主会 D&B/E&D" in the task card = NeurIPS ED track (formerly D&B). And ICML 2027's "Datasets, Evaluations and Benchmarks" contribution type is another main-track target. Great.

Fees summary now solid:

ICLR: no publication fee ($0, OpenReview) [scispace + generally]. ICLR 2027 registration opens Dec 23, 2026; fees未公布. ICLR 2026 financial assistance page gives student registration valued ~$425 (Tier 3 registration "valued at 425 USD (for students) or more") — that's a nice official-ish reference point from iclr.cc! [iclr.cc/Conferences/2026/FinancialAssistance]. ICLR also offers financial assistance (registration waivers + hotel) — official page. Workshop-only passes "available at reduced rates" per unofficial wiki (conf 0.5).
NeurIPS 2026: Paris official (neurips-europe.cc): workshops-only €130 student/€170 academic/€250 industry early; standard €180/€220/€300. Full: €380-950. Sydney/Atlanta workshops-only $200-600 (qrsntu, unofficial). Virtual-only $50-275. NeurIPS financial assistance: complimentary registration + hotel (workwander blog; official NeurIPS financial assistance exists). EurIPS (NeurIPS-endorsed Europe conf) registration waiver program for students presenting (eurips.cc/registration-waiver) — that's for EurIPS though. Actually "EurIPS" is the Paris satellite? The waiver page says "students presenting a NeurIPS paper at EurIPS" — EurIPS = the European NeurIPS-endorsed conference (Paris satellite is "NeurIPS 2026 in Paris Satellite"). Hmm, "EurIPS" might be the successor name for the European satellite. Whatever — cite it as waiver program example.
NeurIPS 2027 fees: 未公布 (2026 pricing was released ~July 2026).
ICML 2027 fees: 未公布. ICML 2026 reference: student conf-only $200 early/$245 late; tutorials+conf+workshops $425/$540 (source: unofficial piedpiperg.github.io — hmm, that's a personal page. conf 0.6. Maybe better to just say ICML 2026 student ~$200-425 with unofficial source and mark accordingly).
版面费: none for NeurIPS/ICML/ICLR (proceedings; ICLR $0 confirmed by scispace; PMLR/NeurIPS no APC — conf 0.85). Workshops non-archival → no fees.
arXiv: $0 confirmed (info.arxiv.org/about: "There are no fees or costs for article submission") [1] (https://info.arxiv.org/about/index.html).

Acceptance rates:

NeurIPS 2025 main track: 24.52% (5,290/21,575) official blog 1. D&B track ~25% (Mannheim news citing CORE) — conf 0.6.
NeurIPS 2026 ED track rate: not yet published (2026 decisions ~Sep 2026? For NeurIPS 2026, notifications were ~Sep 2026; acceptance stats maybe available. Skip — mark 未验证/未公布.)
ICML 2026 overall ~22-23%? Not verified. ICML 2027: unknown + two-stage. Mark 未验证.
ICLR 2026: 5,357/19,525 = 27% (reviewpaper.ai; actually it said "ICLR 2026 accepted 5,357 of 19,525 submissions (27%)") — decent.
Workshops: typically 30-60% for non-archival; 未公布 per-workshop.

Now, the deadlines for the 3 workshops:

SciEval @ ICLR 2027 (science-of-eval.github.io): submission 2027-02-01, notification 2027-02-19; OpenReview double-blind; non-archival (hmm — is SciEval non-archival? The site says "Work already published at major ML venues is discouraged" — implies it's archival-ish or at least they care. It doesn't explicitly say non-archival. Page limits TBA. I'll state: 双盲 OpenReview；页数/格式未公布 (conf 0.9); "已发表于 ICLR/ICML/NeurIPS 的工作不鼓励投稿".)
Science and Society of Modern AI @ ICLR 2027 (science-society-ai.github.io): CFP opens Dec 7, 2026; deadline 2027-01-30 AoE; full ≤8p, tiny ≤3p (excl. refs); non-archival (stated "two non-archival tracks").
Verifiable Agent Safety @ ICLR 2027 (verifiableagentsafety.github.io): abstract 2027-01-25, paper 2027-02-01; regular 5–9p, short 2–4p; non-archival, double-blind; dates "proposed/subject to confirmation" (conf 0.7).

ICLR 2027 workshop day: Apr 29–30, 2027, SF (iclr.cc).

Also for Q1 "是否接受 analysis/measurement/short paper": all three yes:

SciEval: explicitly meta-evaluation/measurement science + psychometrics/preregistration tradition — the single best match (this paper = measurement protocol with preregistration!).
Science&Society: "Measurement: the evaluations that decisions rest on" problems; tiny papers welcome "unpublished idea with its evaluation, or self-contained theoretical result" — fits closed-form analysis.
VAS: short papers for "modest self-contained results... early-stage work"; topics on evaluation with guarantees + spec gaming — fits the alignment-adjacent positioning (SCALR cut).

Competitiveness assessment of "测量协议/分析型、无训练无真实实验" workshop papers:

SciEval: 高 (this is precisely their CFP; preregistration + negative control + exact-zero control would stand out methodologically). conf 0.7.
Science&Society: 中高 (claims-testing + measurement framing; toy model as "what claims can a scoring basis support"). conf 0.6.
VAS: 中 (they emphasize formal results/verified monitors; our closed-form + exact-zero control can be framed as formalizable; but risk "not about agents runtime"). conf 0.5.

One concern: ICLR workshop deadlines "tentative" for SciEval ("Tentative, following the ICLR 2027 workshop timeline") and VAS ("Dates are proposed and subject to confirmation"). Must flag. ICLR usually centralizes workshop deadlines (common deadline ~Feb 2027?). Historically ICLR had a common workshop paper deadline in early Feb. So Feb 1, 2027 aligns.

Now Q2 paths (概率最大排序):

路径1（推荐）：ICLR'27 workshop（SciEval 2027-02-01；备选 Science&Society 2027-01-30 tiny）→ 扩展后投 NeurIPS 2027 E&D/ED 轨道（~2027-05，CFP 未出）

Workshop 录用概率 ≈ 50–65% (conf 0.55); 主会 E&D≈ 15–25% (conf 0.45)（改名后 analysis-of-evaluation 明确 in scope，"新指标定义"例子（Fairness Through Awareness）直接类比 H(D|S) 评分）。
适配：SciEval CFP 明文邀 psychometrics/preregistration/multiplicity 转移研究 — 本工作的预注册+负控制正中靶心；workshop non-archival（SciEval 未明说，Science&Society/VAS 明确 non-archival）→ 不占用 NeurIPS 新颖性。
风险：toy 结构被批 trivial（"就是 ID3/PI"）；E&D需要 artifact（Croissant/RAI 元数据要求只针对 dataset submission — 若打包 workload集则需遵守）；NeurIPS 2027 CFP 未出，轨道细则可能变。

路径 2：直接投 ICML 2027 主会 "Datasets, Evaluations and Benchmarks" contribution type（abstract 2027-01-14 / full 2027-01-22）

主会录用概率 ≈ 8–15% (conf 0.5)。
适配：ICML 2027 首次把 Datasets/Evaluations/Benchmarks 作为主轨 contribution type（blog2026-11-24, icml.cc/Conferences/2027/ContributionTypes）；与 NeurIPS E&D 同构。
风险：两阶段评审（AC 可 first-stage reject）对 toy-only 极不友好；reciprocal reviewing 义务（须有合格审稿 co-author 并完成评审）；时间紧（~7 周）；ICML 2026接收率未验证。
也可与路径1并行（workshop 非存档不冲突）。

路径 3：NeurIPS 2027 主会（E&D 轨道 或 main "Negative Results/Concept & Feasibility" contribution type；~2027-05截稿）直接投

概率 ≈ 12–20% (conf 0.4)（若走 E&D）；风险：距离远、结果陈旧化；无 workshop反馈先行。
或者 MLSys 2028（2027-10 截稿，超窗口末端）作为 systems 轨道备份 — mention briefly.

Hmm, Q2 wants "排序后的 2–3 条路径…每条给：venue 全名、类别、截稿日期、接受率、适配理由、被拒风险。区分 workshop 录用与顶会主会录用，分别给概率。" So I'll do 3 paths: (A) ICLR'27 workshop→NeurIPS'27 E&D; (B) ICML'27 主会 DEB type (可与 A 并行); (C) NeurIPS'27 E&D 直投（含 Position/负结果 alternative）. Actually A and C both involve NeurIPS E&D... A is staged (workshop first then ED), C is direct ED. B is ICML main. That's a reasonable set. Alternatively C = "SciEval→扩展→ICML'27 DEB (Jan)?" no, order is wrong (ICML deadline Jan 22 before SciEval Feb 1).

Hmm wait — actually maybe order paths differently. "概率最大的顶会中稿" — the target is 顶会中稿 (main conference acceptance) probability maximized. Path A stages workshop first → feedback → improved ED submission in May. Path B: ICML main-track DEB type directly (Jan). Path C: NeurIPS ED direct (May). The combined P(main conf accept) is highest for A (feedback + polished + ED scope fit), then C, then B (two-stage review risk).

Let me also mention alternative workshops in Q1 as backup? The task asks for exactly 3 — I'll give 3 + a one-line "备选" mention. Keep within 70 lines!

Q4 加固建议 (不动结论):

必做 1: 一张"结构图+负控制对照图"（分解树示意、H(D|S) 计算路径、flat-rate 精确零的图解）— SciEval/评审最容易在这点上给分；成本低。
必做 2: comparison table（vs ID3 信息增益 / roofline / PID / SCALR：坐标、输入、输出、是否闭式、是否负控制、是否预注册）— 直接回应"这就是 ID3"质疑。
可选: 公开数据 spot-check（用 2–3 个公开 GPU spec（如 NVIDIA H100/MI300 spec 页）+ 公开 workload trace做一个外部可复算的小验证）或 artifact 附录（脚本+40k workload 生成器）→ 对 NeurIPS E&D 收益大（artifact/RAI 元数据要求）。
可选: 3 页 tiny paper 版投 Science&Society（与主投稿不冲突，练手+曝光）。

Actually, "1–2 个补充动作" — pick top 2: (1) comparison table + 结构图 (these could be one "figure+table package"); (2) public-spec spot-check. Grade 必做/可选.

Now let me also double-check the SciEval non-archival status and page limits... The fetch earlier didn't show "non-archival" for SciEval. I'll write "非存档性未明示/页数未公布（CFP 开放后发布）" — hmm, the SciEval page says "Work already published at major machine learning venues (ICLR, ICML, NeurIPS) is discouraged" which suggests it might be archival or at least they don't want republished work. Important for path A (workshop→ED): if SciEval is archival, a published workshop paper might conflict with NeurIPS ED novelty. But NeurIPS allows arXiv'd and workshop versions typically (NeurIPS dual-submission policy allows non-archival workshop papers; archival workshop proceedings might be an issue). Since SciEval's archival status is unclear, I should note the safer combo: Science&Society (明确 non-archival) 或 VAS (明确 non-archival) for the staged path if archivality matters; SciEval 页数/存档性待 CFP 正式发布确认 (deadline Feb 1). Hmm — but SciEval is the best topical match. I'll note the caveat: "若 SciEval 为存档则改投其前先挂 arXiv/或选明确非存档的 Science&Society 做首站". Actually simpler: recommend Science&Society or VAS as the staged first stop (non-archival confirmed), and SciEval as the best topical match with archival status TBD. Hmm, but Q1 asks "最匹配的 3 个" — SciEval is #1 by topic. In Q2 path A, I can say workshop首站选 SciEval（需确认非存档；若存档则用 Science&Society 非存档 tiny/full打头）。

Let me also quickly verify the NeurIPS 2027 ED track: since the 2027 CFP is not out, deadline estimate "约 2027 年 5 月上中旬（2026 为 5/4 abstract、5/6 full；2025 为 5/11、5/15）", conf 0.7. Note "未正式公布".

Also NeurIPS 2026 acceptance for ED track — the "beri.net" page said topics include "Evaluation and datasets". No rate. Fine.

ICLR2027 registration fee: "Registration opens December 23, 2026" (scifig.ai citing iclr.cc Dates) → 2027 费用未公布。Reference: ICLR 2026 student registration valued $425+ (official financial assistance page) — good.

Workshop随主会注册: NeurIPS 明确有 workshops-only 票种（官方巴黎站价目）→ workshop通常可单独注册,不必全会注册 (conf 0.85 for NeurIPS). ICLR workshop-only passes "available at reduced rates" (unofficial, conf 0.5). ICML 2026 had "Tutorials + Conference + Workshops" tier vs conf-only (unofficial source) → workshops 通常并入全会票或单独加购 (conf 0.6).

版面费 (page charges): 无 (NeurIPS/ICML/PMLR/OpenReview 无 APC; ICLR $0 per scispace) conf 0.85.

Waivers: NeurIPS Financial Assistance (免费注册+酒店, official program ~千人规模 per workwander blog; official link neurips.cc Financial Assistance... I have eurips.cc/registration-waiver (学生注册费豁免) and ICLR 2026 Financial Assistance (iclr.cc/Conferences/2026/FinancialAssistance: 注册+酒店预付或报销). Good enough with URLs.

arXiv: 0 元 (info.arxiv.org/about/index.html).

Now line budget: ≤70 lines. Structure: Q1 (3 workshops, compact), Q2 (3 paths), Q3 (fee table-ish), Q4 (2 items), plus 缺口清单 (time-box mentions gaps). Let me draft tightly.

Format per line — use compact bullets. Count lines carefully. Chinese. Each conclusion with conf(0-1). URLs required per venue/fee.

Draft:

idea53 投稿策略报告（2026-11-25，第二轮·仅投稿策略）
Q1 workshop 可发性（够，且有三个强匹配位）

定位评估：可发 conf 0.85。"闭式可算+精确零负控制+预注册+24排列不变"正是 evaluation-science/methodology 稿的标准卖点；短板是 toy 结构与无真实系统实验（写成"协议+概念验证"即可）。

SciEval: The 1st Workshop on the Science of Evaluation @ ICLR 2027（会期 4/29–30，SF）|截稿 2027-02-01（通知 02-19）| 双盲 OpenReview；接受 analysis/meta-evaluation/measurement；页数与存档性未公布 |匹配度最高：CFP 明文邀 psychometrics/预注册/多重比较传统迁移研究——本稿预注册+负控制正中靶心（conf 0.85）| 来源: https://science-of-eval.github.io/
Science and Society of Modern AI @ ICLR 2027 | 截稿 2027-01-30 AoE（12/07 开 CFP）| 非存档；full ≤8 页 / tiny ≤3 页（不含参考文献）| 主题含"Measurement: the evaluations that decisions rest on"；tiny 收"未发表想法+其评估/自足理论结果"，与"前置评分基础"定位吻合（conf 0.8）| 来源: https://science-society-ai.github.io/
Verifiable Agent Safety @ ICLR 2027 | 摘要 2027-01-25 / 全文 2027-02-01（日期标注"proposed, subject to confirmation"）| 非存档双盲；regular 5–9 页 / short 2–4 页 |适配 spec-gaming、"evaluation with guarantees"、判断的证据与监督假设；short收"小型自足结果/早期工作"（conf 0.7，偏 systems/safety 视角做第三选择）| 来源: https://verifiableagentsafety.github.io/
竞争力判断：analysis/measurement 型、无训练无真实实验的稿在 SciEval 属"主场作"（conf 0.7）；在另两个属合格 short（conf 0.55–0.65）。主要被拒理由只会是"结构过于 toy"，而非"类型不符"。
Q2 顶会中稿概率最大化路径（workshop 录用 ≠ 主会录用，分列）

路径1（推荐）ICLR'27 workshop（SciEval 2/1；若其存档则改用 Science&Society 非存档打头）→ 按反馈扩展 → NeurIPS 2027 Evaluations & Datasets（E&D，原 D&B）轨道直投。| E&D 截稿未正式公布，按 2026（5/4 摘要+5/6 全文）估 2027-05 中旬（conf 0.7）| workshop 录用 50–65%（conf 0.55）；NeurIPS E&D 录用 15–25%（conf 0.45）。| 适配：E&D 更名后明文欢迎"analysis/critique/redesign/stress-testing of evaluation practices"，且官方示例把"新评价指标定义"（Fairness Through Awareness）归入 E&D——H(D|S) 评分协议同类（blog.neurips.cc/2026/03/23/...）。| 风险：toy 被批 trivial；E&D 对 dataset 提交要求 Croissant+RAI 元数据（若打包 workload 集需遵守）；2027 CFP 未出细则可变。| 接收率参考：NeurIPS 2025 主轨 24.5%（官方），D&B≈25%（第三方）。来源: blog.neurips.cc/2025/09/30/... ；neurips.cc/Conferences/2026/CallForEvaluationsDatasets
路径2（可与1并行）ICML 2027 主轨 contribution type "Datasets, Evaluations and Benchmarks" | 摘要 2027-01-14 / 全文 2027-01-22（官方 blog 2026-11-24；Rio 7/31–8/6）| 主会录用 8–15%（conf 0.5）。| 适配：ICML 2027 首设该 contribution type（另有 Position Papers/Negative Results 类型），评审按类型对齐（icml.cc/Conferences/2027/ContributionTypes）。| 风险：两阶段评审（AC 可一阶段拒稿）对 toy-only 最不友好；reciprocal reviewing 义务（需合格 co-author 承担评审）；时间仅 ~7 周。| ICML 2026 总体接收率未验证。
路径3 NeurIPS 2027 E&D 直投（不先去 workshop；或 main轨 Negative Results/Concept & Feasibility 类型）| ~2027-05（未公布）| 录用 12–20%（conf 0.4）| 适配同路径1；风险：无 workshop 反馈打磨、5 个月空窗、与路径1二选一（勿重复投）。
备注：MLSys 2027 已于 2026-10-30 截稿（mlsys.org/Conferences/2027/Dates）；systems 轨备份只能等 MLSys 2028（~2027-10）。

Q3 费用/免费（区分版面费与注册费）
版面费/APC：NeurIPS、ICML、ICLR 均无版面费；ICLR 出版 $0（scispace；OpenReview 免费开放）。conf 0.85- arXiv：0 元，"There are no fees or costs for article submission"（info.arxiv.org/about/index.html）。conf 0.95
Workshop 注册：通常需注册但可单独买 workshop 票，不必全会注册。NeurIPS 2026 巴黎站官方价：workshops-only 学生 €130 早/€180 普、学术 €170/€220、工业 €250/€300；全会+workshops 学生 €380–480（neurips-europe.cc）。Sydney/Atlanta workshops-only $200–600（第三方 qrsntu.org）。conf 0.8
ICLR 2027：注册 2026-12-23 开放，费用未公布（iclr.cc/Conferences/2027/Dates 转引）。参考量级：ICLR 2026 学生注册价值 ~$425+（官方 FinancialAssistance 页）；workshop-only 减免票"通常有"（非官方，conf 0.5）。
ICML 2027：费用未公布。参考 ICML 2026（非官方）：学生 conference-only $200 早/$245 晚、含 workshops全票 $425/$540（piedpiperg.github.io，conf 0.55）。
NeurIPS 2027：费用未公布（2026 价7 月才出）。
Waiver：有。NeurIPS Financial Assistance（免费注册+酒店，学生作者优先）；ICLR Financial Assistance（注册+酒店预付/报销，iclr.cc/Conferences/2026/FinancialAssistance）；EurIPS 学生注册费豁免（eurips.cc/registration-waiver）。conf 0.8
结论：全部路径仅注册/差旅花钱；投稿与发表 0 元，arXiv 0 元，学生 workshop-only 注册量级 €130–300/$200 上下，且有 waiver 渠道。
Q4 加固建议（不动结论）
必做①：一张"分解树+增量信息+负控制"三合一结构图（H(D|S) 计算路径、flat-rate→精确 0 的图解）。审稿第一印象分全在此；1天工作量，workshop 命中提升最直接（conf 0.75）。
必做②：comparison table：vs ID3 信息增益 / roofline / PID / SCALR（输入、输出、闭式性、负控制、预注册、是否涉 spec 修订 6 列），把"就是 ID3"质疑前置封死。半天（conf 0.7）。
可选③：公开数据 spot-check（2–3 张公开 GPU spec 页 + 公开 workload trace复算一个点）或 artifact 附录（脚本+workload 生成器）——对 NeurIPS E&D 与 reproducibility 评审加分（conf 0.6）。
缺口清单（30 分钟盒内未尽项）
SciEval 页数/存档性、ICLR 2027 统一 workshop 截稿政策待 CFP 正式发布（现为 tentative）；2) NeurIPS 2027 E&D 与 ICML/NeurIPS 2027 注册费未公布；3) ICML 2026/2027、NeurIPS 2026 E&D 轨接收率未取得官方数字；4) NeurIPS 2026 E&D 是否要求非数据类论文附 Croissant 需细读 2027 CFP。

Line count: let me count. Header + sections... roughly 45-50 lines. Good, under 70.

Wait — one correction: earlier search said ICLR 2026 was in Rio (Apr 23-27, 2026, Riocentro). Yes "ICLR 2026 in Rio is closed" — consistent. ICLR 2027 SF Moscone Apr 26-30. Good.

Also double-check the SciEval "pre-registration" invite: the CFP section "Beyond machine learning: Psychometrics... clinical-trial methodology has a mature treatment of power, preregistration, and multiplicity. We explicitly invite submissions from these other measurement communities" — yes! Perfect citation for Q4/fit.

Also note: SciEval deadline "Feb 1, 2027" marked "Tentative, following the ICLR 2027 workshop timeline" — flag tentative (conf 0.75 on date).

One more check on "Science and Society" dates: "Call for papers opens: December 7, 2026; Submission deadline: January 30, 2027 (AoE); author notification Feb 22" — good.

VAS: "Abstract Registration: January 25, 2027; Paper: February 1, 2027; Notification: Feb 26, 2027; Workshop Apr 29 or 30" + "Dates are proposed and subject to confirmation" — flag.

Now probabilities: be careful to label subjective estimates with conf. Workshop rates typically30-60%; for a well-matched short paper at a first-edition workshop,50-65% is reasonable; SciEval first edition — could be competitive (eval science is hot). Keep.

Also Q2 must give "接受率（若有官方数字给来源）": NeurIPS 2025 main 24.52% official blog URL: https://blog.neurips.cc/2025/09/30/reflections-on-the-2025-review-process-from-the-program-committee-chairs/ (the search result id 1 URL). D&B ~25% third-party (uni-mannheim). ICLR 2026 27% (reviewpaper.ai — third party). Workshops: 未公布.

For Q2 I should distinguish "workshop 录用概率" vs "顶会主会录用概率" — done in path 1 (50-65% vs 15-25%). For paths 2/3 they're main-conference-only; state those directly.

URLs to include (keep compact):

https://science-of-eval.github.io/
https://science-society-ai.github.io/
https://verifiableagentsafety.github.io/
https://blog.neurips.cc/2026/03/23/introducing-the-evaluations-datasets-track-at-neurips-2026/ (from X post: blog.neurips.cc/2026/03/23/int... — full slug presumably "introducing-the-evaluations-datasets-track-at-neurips-2026"). I only saw truncated "int…". Risky to fabricate slug. Safer: cite https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets (full URL seen in newsletter result) + https://blog.neurips.cc/2026/04/22/neurips-newsletter-april-2026/ (seen fully). Use those two fully-verified URLs. Also blog.neurips.cc/2025/09/30/reflections... — the search result gave URL "https://blog.neurips.cc/2025/09/30/reflections-on-the-2025-review-process-from-the-program-committee-chairs/" — full, good.
https://blog.icml.cc/2026/11/24/new-peer-review-policies-for-icml-2027/ (fetched, full) + https://icml.cc/Conferences/2027/ContributionTypes (from blog text) + https://icml.cc/Conferences/2027/CallForPapers (from blog).
https://mlsys.org/Conferences/2027/Dates
https://neurips-europe.cc/ (fees)
https://iclr.cc/Conferences/2026/FinancialAssistance
https://info.arxiv.org/about/index.html
https://eurips.cc/registration-waiver/

OK. Also "E&D"命名: 报告里说明 E&D=NeurIPS Evaluations & Datasets（2026 起由 D&B 更名）——这解释任务卡的"D&B/E&D"。加一行在 Q2 或开头。

Line budget fine. Write final answer directly as reply body (no file). Keep ≤70 lines. Let me finalize wording compactly.

One nuance for Q1 version: "版面格式页数" asked for each workshop. SciEval: 未公布（CFP 开放后公布）; Science&Society: full ≤8p/tiny ≤3p excl refs, non-archival; VAS: 5–9p/2–4p excl refs+appendix, non-archival. Also all use OpenReview double-blind (SciEval & VAS confirmed; Science&Society "Submissions go through OpenReview" — double-blind not explicitly stated; say OpenReview、双盲待确认? It says "two non-archival tracks" and submission via OpenReview; review type unstated. Keep "OpenReview（双盲未明示）".

Also Q1 asks "2027 截稿窗口" — done.

Final answer below. Keep Chinese, tight. I'll aim ~55 lines.

核实完毕（30 分钟盒内）。关键背景修正：任务卡所称 D&B/E&D 即 NeurIPS "Evaluations & Datasets (ED)" 轨道——2026 年由 Datasets & Benchmarks 更名，且扩 scope 明文欢迎"evaluation 作为科学对象的分析/批评/重构"，对本定位是重大利好。完整策略报告如下：

idea53 投稿策略报告（2026-11-25 · 仅投稿策略，不涉 novelty 重审）
Q1 workshop 可发性：够，且有 3 个强匹配位

总体判断：以"闭式 + 精确零负控制 + 预注册 + 排列不变"的测量协议定位，workshop 可发性充分，短板仅是 toy 结构与无真实系统实验（应写成"协议 + 概念验证"）；conf 0.85。

SciEval: 1st Workshop on the Science of Evaluation @ ICLR 2027（4/29–30，旧金山）| 截稿 2027-02-01（通知 02-19，官方标 tentative）| 双盲 OpenReview；analysis/meta-evaluation/measurement 全收；页数与存档性未公布（CFP 开放后发布）| 匹配度第一：CFP 明文邀请 psychometrics/临床试验方法（power/preregistration/multiplicity）向 ML 的迁移研究——本稿预注册+负控制正中靶心；conf 0.85 | science-of-eval.github.io
Science and Society of Modern AI @ ICLR 2027 | 截稿 2027-01-30 AoE（12/07 开 CFP）| 非存档；full ≤8 页 / tiny ≤3 页（不含参考文献），OpenReview | 主题含"Measurement: the evaluations that decisions rest on"（benchmark 的 validity/resolution）；tiny 轨收"未发表想法 + 其评估 / 自足理论结果"，与"前置评分基础"定位严丝合缝；conf 0.8 | science-society-ai.github.io
Verifiable Agent Safety @ ICLR 2027 | 摘要 2027-01-25 / 全文 2027-02-01（官方注明日期 proposed, subject to confirmation）| 非存档双盲；regular 5–9 页 / short 2–4 页（不含参考文献与附录）| 适配 spec-gaming、"evaluation with guarantees"、判断/监督的证据假设（与 SCALR 切割叙事配套）；short 轨收"小型自足结果/早期工作"；conf 0.7 | verifiableagentsafety.github.io
竞争力：此类"测量协议/分析型、无训练无真实实验"稿件在 SciEval 是主场题材（conf 0.7），在另两个是合格 short（conf 0.55–0.65）；唯一系统性风险是"结构过于 toy"，而非稿件类型不符。备选（systems 味）：MLSys 2027 workshop 系列，但主会征稿已于 2026-10-30 截止（mlsys.org）。
Q2 顶会中稿概率最大化路径（workshop 录用与主会录用分列；概率为主观估计）

路径 1（推荐）：ICLR'27 workshop → 扩展 → NeurIPS 2027 Evaluations & Datasets 轨道（E&D，原 D&B）

首站 SciEval（2/1）；若其最终为存档版，改用明确非存档的 Science&Society（1/30）打头，避免占用 NeurIPS 新颖性。E&D 截稿未正式公布，按 2026（摘要 5/4 + 全文 5/6）估 2027-05 中旬；conf 0.7。
workshop 录用 50–65%（conf 0.55）；NeurIPS E&D 主会录用 15–25%（conf 0.45）。
适配：E&D 更名后官方明文欢迎"对评估实践的 analysis/critique/redesign/stress-testing"，且官方示例将"新评价指标定义"（Fairness Through Awareness）归入 E&D——H(D|S) 评分协议同类；ED CFP、2026-04 newsletter。
风险：toy 被批 trivial（用 Q4 的对比表前置封堵）；若打包 workload 数据集需满足 Croissant+RAI 元数据要求；2027 CFP 未出。接收率参考：NeurIPS 2025 主轨 24.5%（官方 blog），D&B≈25%（第三方，conf 0.6）。
路径 2（可与 1 并行）：ICML 2027 主轨 contribution type "Datasets, Evaluations and Benchmarks"
摘要 2027-01-14 / 全文 2027-01-22（官方 blog 2026-11-24；里约 7/31–8/6）。主会录用 8–15%（conf 0.5）。
适配：ICML 2027 首设该贡献类型（另有 Position Papers、Negative Results 类型），评审按类型对齐；官方 CFP、ContributionTypes。
风险：两阶段评审（AC 可一阶段拒稿）对 toy-only 最不友好；reciprocal reviewing 义务（须有合格 co-author 承担评审）；仅 ~7 周备稿。ICML 2026 接收率未验证。
路径 3：NeurIPS 2027 E&D 直投（跳过 workshop）| 截稿估 2027-05（未公布）| 录用 12–20%（conf 0.4）| 适配同路径 1；风险：无 workshop 反馈先行、成果空窗 5 个月、与路径 1 二选一。
Q3 费用/免费（版面费与注册费分开）
版面费/APC：全部为 0。NeurIPS/ICML 无版面费；ICLR 出版 $0、OpenReview 免费开放（conf 0.85）。
arXiv：0 元，官方明示 "no fees or costs for article submission"（info.arxiv.org/about）；conf 0.95。
Workshop 注册：通常须注册但可单独买 workshop 票。NeurIPS 2026 巴黎站官方价：workshops-only 学生 €130（早）/€180（标准）、学术 €170/€220、工业 €250/€300，全会+workshops 学生 €380–480（neurips-europe.cc）；conf 0.85。悉尼/亚特兰大 workshops-only $200–600（第三方 qrsntu.org，conf 0.6）。
ICLR 2027：注册 2026-12-23 开放，费用未公布。参考量级：ICLR 2026 学生注册价值 ~$425 起（官方 Financial Assistance）；workshop-only 减免票"通常有"（非官方，conf 0.5）。
ICML 2027 / NeurIPS 2027：费用未公布（ICML 2026 非官方参考：学生 conference-only $200–245、含 workshops 全票 $425–540，conf 0.55）。
Waiver：有。NeurIPS Financial Assistance（免费注册+酒店，学生作者优先）；ICLR Financial Assistance（注册+酒店预付/报销，同上官方页）；EurIPS 学生注册费豁免（eurips.cc/registration-waiver）；conf 0.8。
结论：三条路径投稿与发表全程 0 元、arXiv 0 元；仅注册/差旅花钱，学生 workshop-only 量级约 €130–300，且有 waiver 渠道。
Q4 加固建议（不动结论）
必做①："分解树 + 增量信息 + 负控制"三合一结构图（H(D|S) 计算路径、flat-rate→精确 0 的图解）。审稿第一印象分集中于此，约 1 天，对 workshop 命中提升最直接；conf 0.75。
必做②：comparison table：vs ID3 信息增益 / roofline / PID / SCALR（输入、输出、闭式性、负控制、预注册、是否涉 spec 修订六列），把"这不就是 ID3"的必然质疑前置封死；半天；conf 0.7。
可选③：公开数据 spot-check（2–3 张公开 GPU spec + 公开 workload trace 复算一点）或 artifact 附录（脚本 + workload 生成器），对 E&D 评审加分；conf 0.6。
缺口清单（超时即以现状交付）

① SciEval 页数/存档性与 ICLR 2027 统一 workshop 政策未定（现为 tentative）；② NeurIPS 2027 E&D CFP 与 ICML/NeurIPS 2027 注册费未公布；③ ICML 2026/2027 与 NeurIPS 2026 E&D 轨接收率无官方数字；④ E&D 对非数据类论文的具体 artifact 要求需待 2027 CFP 细读。

9m 51s | just now
20:38
此任务成功了吗？
Esc
是
否
继续工作
Workspace

All files that are created or uploaded in this session will be saved here

Connectors