# R121 外部文献核验回执

**核验日期**：2026-11-01（Asia/Shanghai）
**核验工具**：`fetch_page` 直读 arXiv abs 页 + arXiv HTML 全文（v1）+ 两个 bench 的 GitHub 仓库页（含 NEWS / commit 列表 / tags）
**核验对象**：AUDIT-report §4(a)「与 ResearcherBench / RACE 差异表」（L136–L148）中的 8 条事实性声明 + 版本漂移

**执行说明（分支处置）**：本次未 `git checkout main`（Arena 分支锁：只允许在 `arena/4a614e63-prompt-first-bench` 上作业）。取件用等价的路径读取：`git show origin/main:bench/rubric-v3/TASK-r121-paper-compare.md`、`git show origin/main:bench/rubric-v3/AUDIT-report.md`（本地 AUDIT-report 与 origin/main 逐字一致，`git diff` 为空），产物提交到 arena 工作分支。

**与仓库内既有同名文件的关系**：`origin/main` 上已有一版 `receipts/r121-paper-compare-verification.md`（commit `150f04d`），其自述「未直读 arXiv 原文，全部 verdict 基于 survey JSON」。本回执是**原文直读的替代版**，verdict 以 arXiv/官方仓库原文为准。两版差异集中在 **B3**（survey 版判 partial 的理由是「survey 无证据」；原文版判「双人」**refuted**，实证为三专家/任务）与 **C**（survey 版全 unverifiable；原文版已可判定 arXiv 无 v2，但仓库实现有重大漂移）。

---

## A. ResearcherBench（arXiv 2507.16280，GAIR-NLP / SJTU）

| # | 声明（AUDIT §4(a) 原文） | verdict | 原文证据（引用句 + 定位） |
|---|---|---|---|
| A1 | 「逐 claim grounding + 专家 insight criteria（重要性 1-3）」 | **confirmed** | ① 专家逐题提炼：§4.1.1 Criteria Construction「**human experts must participate in designing these criteria** to ensure they accurately reflect the standards and expectations of frontier scientific inquiry」；「Annotators also assigned weights to every rubric item based on their relative importance and impact on overall answer quality」。② 权重确为 1–3 三档：Appendix C.1.2 Weight Assignment Guidelines「**Assign weights from 1-3** based on the importance of each rubric item… Higher weights (**3**)… Medium weights (**2**)… Lower weights (**1**)」。③ claim 级 grounding：§4.2.1 Claim Extraction「We employ an extract model to extract **all factual claims** within DARS-generated reports… we save it as a **URL-claim-context triplet**」，§4.2 Score Computation「Faithfulness score… the proportion of **cited claims** that are actually supported by their referenced sources」 |
| A2 | 「judge-human F1 事后报告」 | **confirmed** | §5.4 Judge Model Selection and Meta Evaluation + Table 3：对 5 个候选 judge（DeepSeek R1 / Gemini 2.5 Flash / GPT-4.1 / o3 / o3-mini）给出 Unweighted 与 Weighted 的 Acc./Prec./Rec./F1。「we selected **o3-mini** for rubric assessment due to its optimal balance of consistency (**F1-score: 0.80 and precision: 0.85**) and cost-effectiveness ($0.13 per evaluation)」。性质为 meta-evaluation（「a validation sample of **10 responses** from different questions and different DARS systems」），**用于事后选型，不是开评前置门禁** → 「事后」定性成立 |
| A3 | 「极高标注成本（2,500+ rubrics ≈ 2,800+ 人时）」 | **refuted（归属错误，数字属 ResearchRubrics）** | **正确归属 = ResearchRubrics（arXiv 2511.07685，Sharma et al.，16 位作者，主体 Scale AI）**，三处原文互相印证：<br>① **Abstract**：「a standardized benchmark for DR built with **over 2,800+ hours of human labor** that pairs realistic, domain-diverse prompts with **2,500+ expert-written, fine-grained rubrics**」。<br>② **§1 Introduction（精确值）**：「in total, we provide **2,593 rubric criteria** that check factual grounding, coherence of reasoning, completeness, relevance, and clarity」——「2,500+」即 2,593 的取整。<br>③ **§3 Overview**：「ResearchRubrics consists of **101 single-turn prompts**, each paired with…」；**§2 Table 1** 给出「Average # Rubrics per task」：ResearchRubrics **26**、ResearcherBench **14**、DeepResearch Bench **25**。<br>**反证 ResearcherBench 不可能是该数字的出处**：其 v1 全文（11 个 HTML chunk 全读）无任何人时或 rubric 总量数字；dataset 为 65 题（Appendix A.1「Our dataset size of **65 questions**」），按 ResearchRubrics Table 1 记录的**平均 14 条/题**估算总量约 **910 条**，与 2,593 差约 2.8 倍；其 Appendix A.1 Limitations 仅列 Domain Specificity / Dataset Scale / Black-box Commercial Systems 三项，**无标注成本项** → AUDIT 把 ResearchRubrics 的成本数字挂到 ResearcherBench 名下是张冠李戴 |
| A4 | 「适用域 = 开放研究问答」 | **partially_confirmed** | Abstract：「**65 research questions** expertly selected from real-world scientific scenarios… spanning **35 different AI subjects** and categorized into **three types: technical details, literature review, and open consulting**」；Appendix A.1 Domain Specificity：「Our benchmark focuses **exclusively on AI-related research questions**, which may limit the generalizability… to other scientific domains」。→ 领域被限定在 **AI 学科**、且含技术细节/文献综述两类**非开放型**任务，「开放研究问答」表述**过宽**；Appendix A.1 给出题量分布「12 technical details, 20 literature review, 33 open consulting」 |

---

## B. RACE / FACT（DeepResearch Bench，arXiv 2506.11763，USTC）

| # | 声明（AUDIT §4(a) 原文） | verdict | 原文证据（引用句 + 定位） |
|---|---|---|---|
| B1 | 「动态 task-specific criteria（claim-source 对）」 | **confirmed** | ① 动态 criteria：§3.1 RACE「RACE offers a more adaptive and robust evaluation by first **dynamically generating task-specific weights and criteria**」；「for each dimension *d*, the Judge LLM generates a set of **K_d tailored criteria {c_d,k}** and their corresponding weights」；且做了 Static Criteria 消融（Table 2「Static Criteria 68.33 vs RACE(Full) 71.33」）。② claim-source 对：§3.2 FACT「**Statement-URL Pair Extraction and Deduplication**. We employ a Judge LLM to extract discrete statements from reports… with their corresponding cited source URLs. Then… identify cases where multiple statements associated with the same URL describe exactly the same fact. In such cases, **only one representative Statement-URL pair is retained**」。→ 术语上原文用「statement-URL pair」而非「claim-source pair」，语义等价；AUDIT 表述成立 |
| B2 | 「reference-relative 打分」 | **confirmed** | §3.1 Reference-Based Scoring：「RACE adopts a **reference-based scoring strategy**. For each task *t*, a high-quality report **R_ref** is selected as a reference」；Eq.(3)「**S_final(R_tgt) = S_int(R_tgt) / ( S_int(R_tgt) + S_int(R_ref) )**」。§4.2.1 亦自述「these scores are highly linearly correlated with human evaluations, **mapped to a different reference frame**」 |
| B3 | 「双人评分 / 人工一致性报告」 | **partially_confirmed（「双人」部分 refuted；「一致性报告」部分 confirmed）** | **refuted 的一半**：§4.3 Human Consistency「For each task, **three domain-expert annotators** score these reports」；Appendix A Human evaluation throughput「we limited human evaluation to **three experts per task**, covering 50 tasks across four agents (totaling 600 reports)」；§4.3.1「we recruit **70+ annotators** with Master's degrees」。→ 是**三专家/任务**（标注员池 70+），不是「双人」。且 RACE 的自动判分侧只有**单一 judge LLM**（Gemini-2.5-Pro，§4.1 Implementation Details），也不构成「双 judge」。<br>**confirmed 的一半**：人工一致性报告确实存在，§4.3.2 给出四指标 —— Table 2「RACE(Full): **PAR 71.33 / OPC 99.54 / FAP 60.24 / FAS 59.12 / Overall 72.56**」，并单列「**Human Inter-Agreement 68.44**」作对照 |
| B4 | 「跨题可比性弱（criteria 每题不同）」 | **partially_confirmed** | ① 机制成立：criteria 与维度权重**逐题动态生成**（§3.1，见 B1 证据）。② 但**原文未自认该局限**：Appendix A Limitations 只列三项 —— Benchmark scale / Domain coverage bias / Human evaluation throughput，**无「跨题可比性」条**。③ **原文反而主张相反**：§4.2.1「individual models maintain **relatively stable performance across different topic tasks**, demonstrating the **robustness** of our RACE evaluation framework」。④ 仅有间接支撑：§4.2.1「we should focus on the **rankings and proportional differences** between the scores rather than the **absolute score values**」——即绝对分不可直接横比，但这是「参考系不同」而非「跨题不可比」。→ AUDIT 表内已标注「这是我们的推断」，定性诚实；但若作为「对方自认的代价」引用则失据 |

---

## C. 版本漂移

**结论：截至 2026-11-01（快照日 2026-10-30 之后 2 天），三篇 arXiv 均无 v2；两个 GitHub 仓库在快照日之后也无新提交。但「论文 v1 ↔ 当前官方实现」之间存在显著漂移，且漂移主体发生在快照之前。**

### C.1 arXiv 版本历史（abs 页 Submission history 直读）

| arXiv | 标题 | Submission history | 判定 |
|---|---|---|---|
| 2507.16280 | ResearcherBench | **仅 [v1]** Tue, 22 Jul 2025 06:51:26 UTC | 无 v2；正文引用应标 `v1` |
| 2506.11763 | DeepResearch Bench | **仅 [v1]** Fri, 13 Jun 2025 13:17:32 UTC | 无 v2；正文引用应标 `v1` |
| 2511.07685 | ResearchRubrics | **仅 [v1]** Mon, 10 Nov 2025 23:07:14 UTC | 无 v2（A3 数字的出处） |

### C.2 GitHub 仓库（官方 repo）

| 仓库 | 最新 commit | 快照后（>2026-10-30）有变更？ | 关键变更点 |
|---|---|---|---|
| `GAIR-NLP/ResearcherBench` | `0b6a114`「Update README.md」**2026-07-21**（25 commits / 0 tags） | **否** | NEWS：[2026-07-09] 被 **COLM 2026** 接收；[2026-01-04] 增评 Claude Research / Doubao Deep Research / Mita Deep Research。仓库标题已改为「…on **Open-ended AI Research Tasks**」，与论文标题「…on the **Frontiers of Scientific Inquiry**」不同（标题级漂移，非统计口径漂移） |
| `Ayanami0730/deep_research_bench` | `f2735b5`「docs: announce GPT-5.6 Luna cleaning model」**2026-09-29**（47 commits / 0 tags） | **否** | 见下三条，均早于快照 |

**DRB 的三处实质漂移（按时间）：**

1. **[2026-02-06] 继任 bench 发布**：DeepResearch Bench **II**（arXiv **2601.08536**），首页 https://agentresearchlab.org/benchmarks/deepresearch-bench-ii/ 。README 明言「DRB II, as a follow-up to DRB, has a **different evaluation focus** from DRB; DRB will continue to be maintained」；DRB II 用「**9,430 fine-grained binary rubrics**」。
2. **[2026-05-11] 官方 judge 更换**：因 Gemini-2.5-Pro 将于 2026-06-17 下线，RACE 评测器由 **Gemini-2.5-Pro → GPT-5.5**，FACT 由 Gemini-2.5-Flash → **GPT-5.4-mini**；同时公布候选评测器与人类判断的对齐度（人类 inter-annotator 基线 **68.78%**）：GPT-5.5 Overall **71.82**（PAR 73.00 / OPC 89.70 / FAP 65.35 / FAS 59.23）、Gemini-3.1-Pro 70.58、Claude-Opus-4-7 70.11。旧代码保留在 `Gemini-2.5` 分支。
3. **[2026-09-22] 清洗模型更换**：RACE 流水线的文章清理模型 GPT-5.5 → **GPT-5.6 Luna**（judge 仍为 GPT-5.5 / FACT 仍为 GPT-5.4-mini）。

### C.3 对本项目的影响（需登记）

- **AUDIT §4(a) 若以「RACE = Gemini-2.5-Pro 判分」为前提描述对方方法，自 2026-05-11 起已过时**。但注意：AUDIT 表内 8 条声明本身（B1–B4）都是**结构性特征**（动态 criteria / reference-relative / 人工一致性报告 / 每题的 criteria），**不随 judge 换代而失效** —— 换代只影响绝对分数，不改机制。
- **风险点**：若后续要与 DRB 做**分数级**对比（而非结构对比），必须声明用的是哪一版 evaluator（legacy Gemini-2.5-Pro vs 现行 GPT-5.5），两个 leaderboard 不可混比 —— 官方 README 明确「Results are displayed on **two separate leaderboards** so the rankings remain directly comparable within each evaluator」。

---

## 总结

- **confirmed 4 条**：A1、A2、B1、B2
- **partially_confirmed 3 条**：A4（适用域过宽）、B3（「双人」应为三专家；一致性报告部分成立）、B4（机制成立，但原文未自认且主张相反）
- **refuted 1 条**：A3（2,500+ rubrics ≈ 2,800+ 人时 → 归属 **ResearchRubrics / arXiv 2511.07685**，不属 ResearcherBench）
- **unverifiable 0 条**
- **版本漂移**：arXiv 三篇均无 v2（可判定，非 unverifiable）；GitHub 两仓快照后无新提交；但 DRB 实现层有 3 处实质漂移（DRB II 发布 / judge 换代 / 清洗模型换代）

### 建议修改 diff（交 Lead 裁定，本回执不直接改冻结件）

**1｜A3 —— 成本数字迁移（refuted，最高优先级）**

```diff
  | 已知代价 | 同源偏置未闭环 + p̃ 估计不稳定（本审计实证） | 极高标注成本（2,500+ rubrics ≈ 2,800+ 人时） | 跨题可比性弱（criteria 每题不同） |
+ | 已知代价 | 同源偏置未闭环 + p̃ 估计不稳定（本审计实证） | 专家逐题人工设计 rubric（65 题 / 35 个 AI 子域；无公开人时数据） | 跨题可比性弱〔**本项目推断**；原文未自认，见 B4〕 |
```

并在表下方（或 §9 引用处）补一行出处更正：

```diff
+ 注：此前表中「2,500+ rubrics ≈ 2,800+ 人时」错误归属 ResearcherBench。该数字属
+ ResearchRubrics（Sharma et al., arXiv 2511.07685）：「over 2,800+ hours of human labor…
+ with 2,500+ expert-written, fine-grained rubrics」（Abstract）。R121 原文核验（2026-11-01）确认。
```

**2｜A4 —— 适用域收窄（partial）**

```diff
- | 适用域 | 长程研究任务（有可构建 gold 树的域；单域验证，S1 未到期） | 开放研究问答 | 事实核查型研究 |
+ | 适用域 | 长程研究任务（有可构建 gold 树的域；单域验证，S1 未到期） | **AI 领域**前沿科研问题（65 题：技术细节 12 / 文献综述 20 / 开放咨询 33；35 个子域） | 事实核查型研究 |
```

**3｜B3 —— 校准机制列（partial，「双人」须改）**

```diff
- | 校准机制 | κ≥0.6 **前置**门禁 + 换位双判（survey 29 bench 中 rank 1 of 2 的前置校准） | judge-human F1 **事后**报告 | 双人评分 |
+ | 校准机制 | κ≥0.6 **前置**门禁 + 换位双判（survey 29 bench 中 rank 1 of 2 的前置校准） | judge-human F1 **事后**报告 | **3 专家/任务**人工评分 + 事后一致性报告（50 题 × 4 agent = 600 报告；PAR 71.33 / OPC 99.54） |
```

**4｜版本漂移脚注（C 段结论，建议加在 §4(a) 事实源那一行）**

```diff
- > 事实源 = `git show aea3d6b:receipts/rubric-v3-gap-analysis.md`（Q1-Q3）。**外部在线复核 unverified**…
+ > 事实源 = `git show aea3d6b:receipts/rubric-v3-gap-analysis.md`（Q1-Q3）。
+ > **外部在线复核已完成**：见 `receipts/r121-paper-compare-verification.md`（2026-11-01，arXiv v1 原文直读）。
+ > 版本状态：三篇 arXiv 均仅 v1（无 v2）；DRB 官方评测器已于 2026-05-11 由 Gemini-2.5-Pro 换为
+ > GPT-5.5（FACT: GPT-5.4-mini），并已发布继任 bench DRB II（arXiv 2601.08536）。
+ > 本表 B1–B4 为**结构性特征**，不随 judge 换代失效；但**分数级**对比须声明 evaluator 版本。
```

### 附：超出本次待核清单的发现（供 Lead 参考，未计入 8 条统计）

1. **§4(a)「重要性信号」行的 RACE 单元格「无显式重要性（criteria 本身即筛选）」与原文不符**：RACE 显式给出 criterion 级权重 `w_{d,k}`（`∑_k w_{d,k} = 1`）与维度级权重 `W_d`（§3.1 Eq.(1)(2)）；只是消融显示权重贡献很小（Table 2：`- No Weights` 72.11 vs `RACE(Full)` 72.56）。更准确的说法是「**有显式权重，但消融显示权重贡献不显著（+0.45）**」。
2. **「校准机制」行的对比口径需注意不对称**：rubric-v3 的 κ≥0.6 是**开评前**门禁（防止 judge 不可用）；ResearcherBench 的 F1 与 DRB 的一致性报告都是**事后**验证。这是「前置 vs 事后」的真实差异，AUDIT 表述正确，维持。
3. **ResearcherBench 的仓库标题已从「Frontiers of Scientific Inquiry」改为「Open-ended AI Research Tasks」**（2026-07-21 README 更新），若在正式文稿中引用其名称，建议以论文 v1 标题为准并注明仓库标题差异。
4. **第三方对 ResearcherBench 的量化刻画可作 A1 的旁证**：ResearchRubrics §2 Table 1 把 ResearcherBench 记为「Human-authored Rubrics ✓ / Expert-Curated ✓ / Open-Ended ✓ / Non-Technical Domains ✗ / LLM-as-Judge ✓，**平均 14 条 rubric/题**」。这独立印证了 A1 的「专家逐题 rubric」定性，同时再次量化排除了 A3 的 2,500+ 归属（65×14 ≈ 910）。**注意**：该表是第三方转述，非 ResearcherBench 原文，只宜作旁证、不宜作主证。
