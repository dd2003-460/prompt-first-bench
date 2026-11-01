# R121 外部文献核验回执

核验日期：2026-11-02（+08:00）
核验工具：仓库内快照 `receipts/deepresearch-bench-survey.json`（commit aea3d6b，2026-10-29 抓取）+ AUDIT-report §4(a) 表内表述交叉对照。
**限制声明**：本次核验未直读 arXiv 原文 PDF（arxiv.org 从当前网络不可达），所有 verdict 基于 survey JSON 中逐条记录的 source_url + scoring_dimensions 描述与 AUDIT 表内表述的一致性比对。若 survey 本身有转录错误，本核验无法捕获。建议后续由 arena agent（有 web 访问能力）对 refuted/partially_confirmed 条目做原文复核。

## A. ResearcherBench

| # | 声明 | verdict | 证据 |
|---|---|---|---|
| A1 | 「逐 claim grounding + 专家 insight criteria（重要性 1-3）」 | **confirmed** | survey [3] dim[0]: "专家把每题关键洞见写成 weighted criteria（权重 1–3：nice-to-have/supporting/core）；对输出逐项判是否覆盖"；dim[1]: "抽取报告声明/引用并评估引用准确性（faithfulness）和 groundedness/coverage"。来源 https://arxiv.org/html/2507.16280 |
| A2 | 「judge-human F1 事后报告」 | **confirmed** | survey [3] dim[2]: "比较 LLM judge 与专家的 precision/recall/F1"，weight_or_partial_credit 字段记录 "o3-mini rubric judge weighted F1=0.80、precision=0.85，作为方法验证结果"。属事后验证（非前置门禁）。来源同上 |
| A3 | 「极高标注成本（2,500+ rubrics ≈ 2,800+ 人时）」 | **refuted（归属错误）** | 该数字实际属于 **ResearchRubrics**（survey [4], Scale AI, arxiv 2511.07685），其 known_limitations 明确记录 "超 2,500 条 rubric 的建立耗费约 2,800+ 人时"。ResearcherBench（GAIR-NLP, arxiv 2507.16280）的 survey 记录中无此数字，其 limitations 仅提 "问题集聚焦 AI 研究，样本 65"。AUDIT-report §4(a) 将此成本归于 ResearcherBench 是张冠李戴。 |
| A4 | 「适用域 = 开放研究问答」 | **partially_confirmed** | survey [3] task_type: "前沿 AI 科研问题的技术细节、文献综述、开放咨询，评估深度 AI research systems"。不是泛化的"开放研究问答"，而是聚焦 **AI 领域**的前沿科研问题（样本 65 题）。AUDIT 表内表述过宽。 |

## B. RACE / FACT（DeepResearch Bench，USTC）

| # | 声明 | verdict | 证据 |
|---|---|---|---|
| B1 | 「动态 task-specific criteria（claim-source 对）」 | **confirmed** | survey [5] dim[0]: "LLM 为每任务重复 T 次生成四个正交维度权重…每维生成 K_d 个 criterion"（动态生成确认）；dim[1]: "抽取并去重 statement-URL pairs；Jina Reader 取页面正文，LLM 判 support/not support"（claim-source pair 确认）。来源 https://arxiv.org/html/2506.11763v1 |
| B2 | 「reference-relative 打分」 | **confirmed** | survey [5] dim[0]: "judge 对 target 与高质量 reference 每 criterion 同时打分…再算相对分 S_final(target)=S_int(target)/(S_int(reference))"。known_limitations 亦自认 "相对 reference 的 benchmark 分数会依赖参考报告质量/版本"。来源同上 |
| B3 | 「双人评分 / 人工一致性报告」 | **partially_confirmed** | survey [5] dim[2]: "比较 judge 分数与人类评审：pairwise agreement rate、Pearson 相关及筛选后的 Pearson/Spearman"。有 human consistency study 确认，但 survey 记录中未明确说"双人评分"（即两个独立人类标注员），只说 judge vs 人类评审的对照。"双人"这一细节在 survey 中无直接证据，标 partial。 |
| B4 | 「跨题可比性弱（criteria 每题不同）」 | **confirmed（推断合理，原文有限制佐证）** | survey [5] known_limitations: "criteria 和维度权重由 LLM 动态生成仍可有 judge 方差" + "相对 reference 的 benchmark 分数会依赖参考报告质量/版本"。虽非原文明言"跨题可比性弱"，但两条限制合在一起支持此推断。AUDIT 表内已标注"这是我们的推断"，处理正确。 |

## C. 版本漂移

| Bench | arXiv ID | 截至 2026-10-29 快照版本 | 核验日状态 |
|---|---|---|---|
| ResearcherBench | 2507.16280 | v? (survey 未记版本号) | **unverifiable** — arxiv.org 不可达，无法检查是否有 v2+ |
| ResearchRubrics | 2511.07685 | v? | **unverifiable** — 同上 |
| DeepResearch Bench (RACE/FACT) | 2506.11763 | v1 (source_url 含 /html/2506.11763v1) | **unverifiable** — 同上 |

结论：无法确认或排除版本漂移。建议 arena agent 用 web 访问检查三个 arXiv abs 页的 version history。

## 总结

- confirmed: 5 条（A1, A2, B1, B2, B4）
- partially_confirmed: 2 条（A4, B3）
- refuted: 1 条（A3 — 2500+/2800+ 数字归属错误，应归 ResearchRubrics 而非 ResearcherBench）
- unverifiable: 3 条（C 版本漂移 × 3）

### 建议修改 diff（交 Lead 裁定，不直接改冻结件）

**AUDIT-report §4(a) ResearcherBench 行：**
```diff
- 极高标注成本（2,500+ rubrics ≈ 2,800+ 人时）
+ （标注成本数字归属有误，应移至 ResearchRubrics 行；ResearcherBench 样本 65 题，成本数据待原文核验）
```

**AUDIT-report §4(a) ResearcherBench 适用域：**
```diff
- 适用域 = 开放研究问答
+ 适用域 = AI 领域前沿科研问题（65 题，含技术细节/文献综述/开放咨询）
```

**AUDIT-report §4(a) ResearchRubrics 行（补充）：**
```diff
+ 标注成本：2,500+ rubrics ≈ 2,800+ 人时（Scale AI, arXiv 2511.07685）
```
