【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00..04.5
2. 每阶段产出落盘 loop-artifacts/stages/<N>/
3. 完成后 commit + push
4. 通道故障 → 报告 Lead 降级，不得静默跳过

# T44: Related Work Update (Nov 2026)

## 目标
更新 paper §2 Related Work，补充 2026-09~11 最新文献（当前引用止于 2026-07），确保无遗漏重要竞品。

## 背景
Paper 现有 §2 三小节：2.1 LLM Agent Evaluation, 2.2 Structured Prompting/CoT, 2.3 Self-Assessment/Calibration。
核心定位：no-tool prompt ablation + 7-dim rubric + arena channel（frontier model × real tools）。

## 调研范围（web_search）
1. **LLM agent benchmark 2026 H2**：新发布的 agent evaluation benchmarks（特别关注 no-tool / parametric-only 设定）
2. **Prompt structure ablation**：2026 年新的 prompting technique 对比研究（特别是 decomposition vs CoT vs ToT 的量化比较）
3. **LLM-as-judge 2026**：judge reliability、self-preference bias、cross-family validation 的最新工作
4. **Deep research agents**：DREAM/DeepResearch Bench 之后的新竞品（Perplexity Deep Research, OpenAI deep research, Gemini deep research 的学术评估）
5. **Calibration 2026 H2**：verbalized vs logprob confidence 的新结果

## 约束
- 每个引用必须给 arXiv ID 或 DOI（无来源不写）
- 区分"直接竞品"（同设定）vs"相关但不同设定"（有工具/不同任务）
- 标注哪些需要加入 §2 哪一小节
- 如果发现与本文结论矛盾的工作，单独列出并分析差异来源

## 产出
- `loop-artifacts/stages/04/T44-related-work-update.md`：
  - 新增引用列表（≥8 篇，每篇：作者/年份/arXivID/一句话定位/归入哪个小节）
  - 建议修改文本（直接可贴进 paper 的段落）
  - 矛盾/张力清单（如有）
- commit message: "T44: related work update Nov 2026"
- push 到当前分支

## 失败降级
- web_search 不可用 → 用 parametric knowledge + [UNVERIFIED] 标注（conf-0.2）
