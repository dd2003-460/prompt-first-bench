# T37-B: Related Work 调研 + 交叉验证

【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00..04.5
2. 每阶段产出落盘 loop-artifacts/stages/<N>/
3. 完成后 commit + push
4. 通道故障 → 报告 Lead 降级，不得静默跳过

## 任务

为 `experiments/stage-ablation/paper-draft.md` §2 (Related Work) 补充引用，从当前 10 篇扩到 ≥20 篇。

### 当前已有（不重复）
CoT (Wei 2022), ToT (Yao 2023), Xiong 2023, Kadavath 2022, DREAM ACL2026, ScientistTwo arXiv:2609.19644, GAIA, AgentBench, τ-bench, LoCoMo

### 需覆盖的子领域（每个 ≥1 篇，优先 2024-2026）
1. **LLM agent benchmarks**（GAIA/AgentBench 之外的新 benchmark，如 WebArena, SWE-bench, MLE-bench）
2. **Prompt engineering / structured prompting**（beyond CoT/ToT：self-consistency, least-to-most, plan-and-solve）
3. **Calibration / confidence elicitation**（beyond Xiong/Kadavath：verbalized confidence, logprob-based, multi-sample）
4. **RAG evaluation & retrieval quality**（RAGAS, ARES, or similar RAG-specific eval frameworks）
5. **Deep research agents**（OpenAI Deep Research, Perplexity, GPT Researcher, STORM — 找有 paper 的）
6. **Ablation methodology in ML/NLP**（如何设计 ablation study 的方法论论文）

### 验收
- 产出 `loop-artifacts/stages/02/research.md`：每篇含 (title, authors, venue/year, arXiv ID or URL, 1-sentence relevance to our work)
- ≥10 篇新文献，每篇标注属于上述哪个子领域
- 交叉验证：每篇的 arXiv ID / venue 通过 ≥2 个独立源确认（arxiv.org + DBLP/ACL Anthology/Semantic Scholar）
- 矛盾记录：若某篇信息不一致（如年份、venue），记录矛盾点

### 失败降级
arena 不可用 → 报告 Lead，Lead 走 ego-browser 本地调研（conf-0.2）