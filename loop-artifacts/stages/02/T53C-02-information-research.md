# T53C 阶段 02：SOTA 分数取证记录

- 任务书：`tasks/T53C-sota-research.md` @ `ac1b481`
- 产出：`research/sm-bench-sota-table.json`（12 个系统行 / 12 条 URL / 0 条逐题分数）
- 通道：`web_search`（定位）+ `fetch_page`（arxiv HTML、官网、ICLR proceedings PDF 逐页取表）

## 1. 检索轨迹

| # | 动作 | 结果 |
|---|---|---|
| 1 | web_search `DeepResearcher 2504.03160 HotpotQA 2Wiki EM F1 table` | 命中大量二手聚合站（sota2/emergentmind），未直接采信 |
| 2 | web_search `GAIA leaderboard 2025 OpenAI 67.36 WebThinker Tongyi 70.9` | 拿到 OpenAI 67.36 / Tongyi 70.9 的二手转述，作为待核线索 |
| 3 | fetch_page `arxiv.org/html/2504.03160`（chunk 2-4） | ✅ **一手 Table 1**：DeepResearcher/Search-r1-base/Search-r1-instruct/R1-Searcher/Search-o1 的 NQ/TQ/HotpotQA/2Wiki F1+MBE |
| 4 | fetch_page `arxiv.org/html/2510.24701`（chunk 4-5） | ✅ **一手 Table 1**：Tongyi 七榜 + OpenAI DR / Gemini DR / Kimi / GLM / DeepSeek-V3.1 / o3 对照 |
| 5 | fetch_page `openai.com/index/introducing-deep-research/`（chunk 2） | ✅ **一手**：GAIA pass@1 74.29/69.06/47.6/67.36、cons@64 72.57、HLE 26.6 |
| 6 | fetch_page `deepresearch-bench.github.io`（chunk 0-1） | ✅ 官网页 v1 Table 1（OpenAI 46.98 / Gemini 48.88 / Perplexity 42.25 / Grok 40.24） |
| 7 | fetch_page ICLR 2026 proceedings PDF（chunk 2-3） | ✅ **camera-ready Table 1**：含 Tongyi 40.46、DeepResearcher 10.77、LangChain ODR(GPT-5) 50.60，且数值与官网页 v1 有漂移 |
| 8 | web_search `"DeepResearch Bench" RACE leaderboard` | ⚠️ 第三方 aiwiki.ai 给 OpenAI 80.7 / Gemini 82.3，与一手来源冲突且无法复算 → **判为不可用来源** |

## 2. 关键判断

1. **逐题分数不存在**：5 题是 pfb 自建 sm-bench，不在任何公开 test set 内。按任务书规则一律 `null` + 写原因，不估算。已建立 q1-q5 → 最近公开 benchmark 的映射（见 JSON `per_question_mapping`）。
2. **两套指标不能混**：短答案 F1（NQ/TQ/HotpotQA/2Wiki）与长报告 RACE 衡量的能力不同；DeepResearcher 就是反例（HotpotQA F1 52.8 vs RACE 10.77）。→ pfb 的 5 题属前者，选 baseline 必须按前者选。
3. **同一 benchmark 只用一版表格**：DeepResearch Bench 统一用 ICLR camera-ready（46.45/49.71/40.46/10.77/50.60），官网页 v1 的 46.98/48.88/42.25 只作版本漂移记录（contradictions.X1）。排名在两版之间一致（Gemini ≥ OpenAI > Perplexity > Grok），结论不受影响。
4. **口径陷阱**：GAIA 有 pass@1 67.36 与 cons@64 72.57 两个数，二手报道常混用 → JSON 里显式分字段。

## 3. 未采信 / 待核

- WebSailor-v2（GAIA 74.1）：只有 sota2 聚合站，未回溯原论文 → 放 `unverified_candidates`。
- aiwiki.ai 的 RACE 80.7/82.3：与一手表差距近一倍，判为不可用。
- LangChain ODR 的 GPT-4.1 版（RACE 43.44）与 GPT-5 版（50.60）都在一手表里，主表只收录 GPT-5 版并注明 backbone。
