# 调研任务书 — Deep Research Bench 评分标准全景（供 arena agent mode）

> origin: ai · 2026-10-29 · r62
> 目标：把市面上所有"deep research / long-horizon research agent"评测的**评分标准**扒清楚，对照我们自己的 rubric-v3（outcome+process 双层、gold 树节点命中按意外性加权），找出我们的设计在业内坐标系里的位置——哪些是共识做法、哪些是我们独有的、哪些是业内有而我们缺的。

## 背景（最小上下文）

- 我们在建一个 LLM pipeline 产出质量评测：pipeline 输入是一个研究问题（如硬件选型），输出是一棵分解树 + 证据链；对照预先冻结的 gold 树逐节点计分
- 我们的 rubric-v3 结构：**Outcome 层**（O1 候选空间覆盖+低先验候选深度挖掘、O2 矛盾挖掘深度 L1/L2/L3、O3 gold 节点命中按意外性加权 w∝1/P(拆分|父节点)、O4 条件结论质量）+ **Process 层**（P1 是否优先外包调研、P2 是否拆解并行、P3 交叉验证、P4 边界停止分类）。两层分开报告不合并总分
- 关键设计点：① 双层分离（结果好过程差=运气，过程好结果差=执行 bug）；② 深度>广度（深层节点权重更高）；③ 意外性加权（越反直觉的发现分越高，信息论 surprisal 思路）；④ 黑盒标注是能力不是缺陷（显式说"我不知道+区间+怎么测"给分）
- 被对照对象清单见下。每个 bench 要扒到**具体评分维度和权重/公式**，不是泛泛介绍

## 要调研的 bench（每个都要找到官方评分文档/paper 的 scoring section）

### B1 通用 deep research 类
1. **GAIA** (Meta, 2023) — 多步工具使用 QA。看它怎么判对错的（exact match? LLM judge?）
2. **HLE / Humanity's Last Exam** (CAIS, 2025) — 专家级多学科题。看它的 grading protocol
3. **BrowseComp** (OpenAI, 2025) — 浏览器检索难题。看它的 binary/exact-match 设计和为什么不用 LLM judge
4. **ResearcherBench / RE-Bench** 等 2025 年出的 research agent 专项 benchmark（搜 "research agent benchmark 2025"，至少找 3 个）
5. **TheAgentCompany** (CMU, 2024) — 长程办公任务。看它的 partial credit 怎么算
6. **WebArena / VisualWebArena** — web agent 任务完成度。看 success rate vs partial score 的设计
7. **MINT / SWE-bench** 里有没有可借鉴的 partial-credit 机制（SWE-bench 的 pass@k 和 test-based grading）

### B2 推理/数学过程评分类（最接近我们的 process 层）
8. **PRIME / Let's Verify Step by Step** (OpenAI, 2023) — process reward model。看 step-level 标注协议
9. **MATH-Shepherd** (2023) — 自动构造 step-level 数据。看它的正确性判定规则
10. **OmegaPRM / PRM800K** 后续工作 — 有没有解析式（非学习式）的 step reward？
11. **InterCode / R2E** 等 code agent 的过程评估

### B3 科学发现/假设生成类（最接近我们的 O2 矛盾挖掘 + novelty）
12. **ChemCrow / Coscientist** (2023) — 化学实验规划。看它怎么评 plan quality
13. **AI Scientist 系列** (Sakana AI, 2024/2025) — 自动生成论文并评审。看它的 LLM review rubric（这是"LLM 当审稿人打分"的直接先例）
14. **Novelty detection in hypothesis generation** — 搜 "novelty measure scientific hypothesis LLM"，找形式化定义
15. **MLE-bench** (OpenAI, 2024) — ML engineering 竞赛。看 medal-based 绝对标尺 vs relative 的设计

### B4 企业/商业分析类（最接近我们的 TCO/性价比场景）
16. **FinanceBench / FinBen** — 金融问答。看 citation grounding 怎么计分
17. **Toucan / 其他 financial research agent eval** — 如果有
18. **任何 hardware/cloud cost analysis benchmark**（搜 "cloud cost optimization benchmark LLM"，可能没有——没有本身就是发现）

## 每个 bench 的输出格式

```json
{
  "bench": "名字",
  "org_year": "机构+年份",
  "task_type": "任务类型一句话",
  "scoring_dimensions": [
    {"name": "维度名", "how_scored": "具体怎么算（公式/规则/judge prompt 要点）",
     "weight_or_partial_credit": "权重或部分得分机制", "source_url": "出处"}
  ],
  "judge_method": "exact match / LLM judge / human / hybrid + 具体配置",
  "known_limitations": "官方承认或社区批评的评分缺陷",
  "vs_our_rubric": {
    "shared_with_ours": ["与我们相同的设计点"],
    "they_have_we_lack": ["他们有我们没有的"],
    "we_have_they_lack": ["我们有他们没有的"]
  }
}
```

## 最终综合输出（除逐 bench JSON 外还要一份对比总结）

1. **共识矩阵**：≥3 个 bench 都有的评分设计 = 业内共识（我们有没有对齐？）
2. **独有设计清单**：只有我们有的（双层分离？意外性加权？黑盒标注给分？）——各自的风险（可能是过度设计）
3. **缺失清单**：业内普遍有但我们没有的（如 calibration set、judge agreement 报告、multi-judge ensemble）——按重要性排序
4. **对我们的 3 条具体修改建议**（基于以上，不是空话）

写入文件 `receipts/deepresearch-bench-survey.json`（逐 bench）+ `receipts/deepresearch-bench-summary.md`（综合总结）。

约束：中文；每个 bench 必须有 source_url（找不到官方文档就标"未验证"并说明找了哪里）；observed_at 用 ISO8601 带 +08:00 时区。