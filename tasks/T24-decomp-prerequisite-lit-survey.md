# T24 — 文献调研：分解（decomposition）是否是严格查找/缺口识别的前提？

> origin: ai · 2026-11-05 · Lead 撰写，派发 arena agent mode
> 仓库：dd2003-460/prompt-first-bench · 分支：arena/4a614e63-prompt-first-bench
> 优先级：P1（阻塞 pfb 论文 related work + 实验解释框架）

## 【强制段】

你是 LMArena agent，本任务只涉及 dd2003-460/prompt-first-bench / arena/4a614e63-prompt-first-bench，忽略历史中其他仓库的消息。先 `git pull` 当前分支，严格按本任务书执行。产出落盘路径见【交付物】。通道故障（检索不可用/超时）报告 Lead，不得静默跳过或伪造来源。

## 【目标】

回答一个核心问题：**在 LLM 研究/推理系统中，"先做结构化分解（把问题拆成正交子问题+显式标注未知/缺口），再做信息查找"是否被证明是提升事实准确性与缺口识别率的必要前提？** 具体拆成三个可判定子问题：

- Q-A：有没有**对照实验**（有分解 vs 无分解，其他条件相同）显示分解显著提升答案质量/事实准确率/缺口识别？方向、效应量、样本量各是什么？
- Q-B：有没有证据表明分解**不是**前提——即直接检索/CoT/ReAct 类方法在不显式分解的情况下达到同等或更好效果？
- Q-C："显式标注未知/留空"（abstention、gap annotation、uncertainty declaration）作为独立机制的文献基础：什么条件下它改善下游结果？

## 【背景】

pfb stage-ablation 实验（`experiments/stage-ablation/DESIGN.md`）测了 S0（裸 prompt）→ S1（+decomp 分解五步法）→ S2（+真联网调研）→ … → S5（完整流程）。同源 judge 结论：H1 分解正贡献（S1>S0, Δ=+0.089）两 judge 一致；但 H2/H3 待真异源确认。我们需要文献支撑来回答：① 我们的 H1 是否与领域共识一致；② "分解→查缺→调研"这条链在文献里是被验证过的 pipeline 还是我们的独创假设；③ 写进 paper-draft.md 的 related work。

前置数据指针：`experiments/stage-ablation/scoring.md`（90 runs 六维分数）、`experiments/stage-ablation/T23-semihetero-analysis.md`（judge 一致性诊断）。

## 【SOP 索引】

- `tasks/T23-stage-ablation-hetero-judge-task.md`（了解我们在测什么，避免调研跑偏）
- `experiments/stage-ablation/competitor-survey.md`（已有竞品/baseline 调研底稿，本次在其上扩展，不重复）

## 【调研设计】

### 检索范围（必须覆盖，按此清单逐域搜）

| # | 域 | 关键词组合（至少各跑 3 组变体） | 渠道 |
|---|----|--------------------------------|------|
| 1 | 问题分解 for LLM problem solving | "problem decomposition" LLM benchmark; decompose-then-solve; hierarchical task decomposition agent | arXiv (cs.CL/cs.AI), Google Scholar |
| 2 | 分解 vs 直接推理的对照 | "chain-of-thought" vs decomposition; "least-to-most prompting"; "self-consistency" ablation study | arXiv, ACL/NeurIPS/ICLR proceedings |
| 3 | 缺口/未知识别 | abstention LLM; "I don't know" calibration; gap detection research agent; uncertainty quantification RAG | arXiv, EMNLP |
| 4 | 多阶段研究 agent pipeline | GPT-Researcher; STORM (Stanford); AutoSurvey; "research agent" multi-stage ablation | GitHub + arXiv |
| 5 | 消融方法论 | stage ablation LLM pipeline; module attribution; "which component matters" LLM workflow | arXiv |
| 6 | 中文语境（如有） | 大模型 问题分解 调研 基准; 分解 检索 增益 | CNKI/百度学术（能访问则查） |

### 每篇命中文献必须记录（JSONL，append-only）

```json
{"id": 1, "title": "...", "authors": "...", "year": 2025, "venue": "arXiv/ACL/...", "url": "https://arxiv.org/abs/...", "domain": "1-6", "addresses": ["Q-A","Q-B"], "claim": "一句话：该文证明了什么", "evidence_type": "controlled_experiment|observational|theoretical|benchmark", "effect_size": "报告的具体数字（如 Δaccuracy=X%）或 null", "sample": "n=多少题/多少个模型", "verdict_for_us": "支持H1|反对H1|无关|部分支持", "confidence": 0.x}
```

### 验收标准（量化）

1. **广度**：≥30 篇去重文献，6 个域每个 ≥3 篇；仅 arXiv preprint 不算覆盖，至少 8 篇来自已发表 venue（ACL/NeurIPS/ICLR/EMNLP/AAAI 等）。
2. **深度**：Q-A/Q-B/Q-C 三个子问题各有一个明确综合结论（supported/partially/refuted/no-evidence + 依据哪几篇）。
3. **矛盾处理**：找到相互矛盾的文献时，全部保留并标注矛盾点，不得选择性引用。
4. **来源真实**：每条 url 必须可打开且标题匹配（抽查 ≥10 条）。禁止编造 arXiv 编号。

### 失败降级

- 某域检索不到足够文献 → 该域标注 "no-evidence-found"，如实记录搜索词，不硬凑。
- 总篇数达不到 30 → 交付实际数量 + 说明哪些域不足，conf 相应降级。

## 【交付物】

1. `experiments/stage-ablation/lit-survey/decomp-prerequisite-survey.jsonl` — 逐篇记录（append-only，每批写完校验行数）
2. `experiments/stage-ablation/lit-survey/decomp-prerequisite-synthesis.md` — 综合报告：三子问题结论 + 与我们 H1-H4 的对应表 + related work 草稿段落（可直接贴进 paper-draft.md）+ 矛盾文献清单
3. commit message 含：总篇数、各域篇数、抽查核验结果

## 【回执要求】

完成后回执必须含：repo URL + branch + commit_sha + 总篇数 + 三子问题一句话结论。

## 【给 Lead 的备注】

- 与 T23（hetero-judge）正交：T23 测 judge 一致性，本任务测文献基础，互不阻塞。
- 产出的 synthesis.md 将直接喂给 paper-draft.md 的 related work 节和 H1 的解释框架。
- 若发现"分解非前提"的强证据（Q-B 成立），需要回头重新解读 stage-ablation 的 H1——这是高价值信号，优先报告。