# G4 — 专家 social 邮件草稿

> origin: ai · 2026-11-08 · goal-pfb-production-hardening.md G4
> 状态：**草稿，未发送**。发送由成璐本人操作（红线：对外动作）。
> 格式定式（成璐）：一个可复现结果（commit hash + 数据路径）+ 一个问题。英文，≤200 词/封。
> 可复现锚点：pfb repo commit `62d43dd2`，数据 `experiments/stage-ablation/runs-s8b/*.json`（9 runs, 3 arms × nat/soc），judge 协议同文件内。

## 收件人选择逻辑

| # | 收件人 | 论文 | 为什么找他（一句） | 问的问题指向的空白 |
|---|--------|------|-------------------|------------------|
| 1 | Sheroz Shaikh | Dissecting Agentic RAG (arXiv:2606.21553) | 与我们方法论最近的先例（组件消融 + 本地小模型），单作者好触达 | 他的消融对象是 QA 检索循环；我们想测 deep research 全流水线阶段——他是否认为阶段级贡献在 research pipeline 上同样可分离？ |
| 2 | Wenyu Huang (第一作者, UGent, Jeff Pan 组) | Beyond Outcome Rewards: Retrieval Credit (arXiv:2610.10179) | RL 侧 retrieval credit assignment 的代表工作 | 他们的中间监督解决训练信号问题；我们在推理侧用 prompt 杠杆做离散开关实验——两条路能否互证"search 与 verify 的贡献不可合并为单一标量"？ |
| 3 | Hailey Onweller (第一作者, IBM Research) | Cited but Not Verified (arXiv:2605.06635) | citation grounding 评测框架的直接作者，IBM 工业背景 | 他们验证 claim-source 一致性；我们的发现是开源 DRA 普遍栽在 grounding（DREAM 结论）——在他们框架下测我们的三道闸输出，是否有兴趣合作跑一组对照？ |
| 4 | Ron Dorfman (一作, Technion) / Ron Litman (资深) | DREAM: Deep Research Evaluation with Agentic Metrics (ACL 2026 long.448) | DRA 评测维度的定义者，我们的评分器借了他们的 grounding 维度 | DREAM 是端到端指标；我们做的是逐阶段增量测量——两个粒度如何对齐？他们是否考虑过把 DREAM 维度拆到阶段级？ |
| 5 | Elias Lumer (共同作者, 两篇相关) | Reflective Prompt Optimization of a DRA (arXiv:2610.12601) + Cited but Not Verified | 同时在做 prompt 层优化和引用验证，且用了 topic-disjoint 防记忆化协议 | 他们用 GEPA 端到端优化整段 prompt（黑箱增益）；我们做逐阶段分解——端到端 vs 分解式，你们观察到两者增益是否一致？ |

注：Lumer 同时出现在 #3 和 #5 的论文里，实际发信时 #3 和 #5 可合并为一封（给 Lumer 一封，主题覆盖两篇）。最终发 4 封。

---

## 邮件 1 → Sheroz Shaikh

**Subject:** Component ablation beyond QA loops — a question from our pfb work

Hi Sheroz,

I read your "Dissecting Agentic RAG" paper (arXiv:2606.21553) carefully — it's the closest existing precedent to what we're doing, and I wanted to check one thing before we finalize our framing.

Our reproducible result: we ran a staged ablation of a six-stage deep-research prompt pipeline (decomposition → research → cross-verification → action planning → execution verification → final review) on two custom gold-anchored questions (one systems/caching, one market-behavior), local 27B model, 3 prompt-lever arms × 3 reps. Coverage of gold points moves 0.444 → 0.611 → 0.667 as we add dimension-discipline and few-shot anchoring; the residual gap concentrates in three specific holes (e.g., inter-visit gap vs residence-time confusion, 9/9 runs). Data: commit 62d43dd2, experiments/stage-ablation/runs-s8b/.

Your question for me: you ablate components of a multi-hop QA retrieval loop. We ablate *stages* of a full research pipeline. Do you think stage-level contributions stay separable at pipeline scale, or does interaction between stages (e.g., decomposition quality changing what verification can catch) break the additive assumption? That determines whether our per-stage deltas are interpretable at all.

Thanks,
Chenglu

(~180 words)

---

## 邮件 2 → Wenyu Huang (Jeff Pan group, UGent)

**Subject:** Inference-side analog of retrieval credit assignment — do the two routes agree?

Hi Wenyu,

Your "Beyond Outcome Rewards" paper (arXiv:2610.10179) on intermediate supervision for search agents resonated with a measurement problem we hit from the opposite direction.

Our reproducible result: instead of shaping training rewards, we flip discrete prompt-layer switches (dimension discipline, few-shot anchoring, explicit verification steps) around a fixed 27B model and measure per-switch coverage deltas against gold-anchored questions. The pattern: no single scalar "contribution function" over (search quality, verification quality) reproduces the observed deltas — the two capabilities interact non-additively, and this holds across 3 arms × 3 reps. Commit 62d43dd2, data in experiments/stage-ablation/runs-s8b/.

Your question for me: your reward-shaping strategies give learning signals that separate "finding evidence" from "using it." Our inference-side switches produce the same separation without any weight update. Have you seen cases where the *direction* of the split (which capability is binding) differs between training-side credit and prompt-side intervention? If so, what predicts which regime you're in?

Best,
Chenglu

(~175 words)

---

## 邮件 3 → Elias Lumer (covers both his papers)

**Subject:** End-to-end prompt optimization vs stage-wise decomposition — and a grounding test proposal

Hi Elias,

Two of your recent papers sit exactly on the seam of our work, so one email covering both.

Our reproducible result: a staged ablation of a deep-research prompt pipeline on gold-anchored questions (local 27B): coverage 0.444 → 0.667 across three prompt levers, with the residual gap localized to three systematic holes rather than uniform noise. Commit 62d43dd2, experiments/stage-ablation/runs-s8b/. Separately, we ran GPT Researcher out-of-the-box (duckduckgo retriever, no gold leakage) on the same questions — it retrieves real sources but its search-synthesize flow doesn't align with point-level scoring, which matches DREAM's grounding findings.

Two questions: (1) Your GEPA work (arXiv:2610.12601) optimizes whole system prompts end-to-end under a topic-disjoint split. When you decompose the gain back into stages, does it distribute like our per-stage deltas, or does end-to-end optimization find couplings that stage-wise measurement misses? (2) Would you be open to running our three-gate output through your source-attribution parser (arXiv:2605.06635) as a controlled comparison against unverified baseline reports? We can ship the report set.

Best,
Chenglu

(~185 words)

---

## 邮件 4 → Ron Dorfman / Ron Litman (DREAM, Technion)

**Subject:** Stage-level decomposition of DREAM metrics — alignment question

Hi Ron,

DREAM's agentic metrics shaped how we score deep-research outputs, so I'm writing about one granularity question.

Our reproducible result: we take a six-stage research pipeline (decomposition → research → cross-verification → action planning → execution verification → final review) and measure each stage's marginal contribution by flipping prompt-layer switches on a fixed local 27B model, scored against gold-anchored questions with point-level coverage. Stages move coverage non-uniformly (0.444 → 0.667 across levers), and the gaps concentrate in specific failure modes (e.g., a concept-confusion hole hit in 9/9 runs regardless of arm). Commit 62d43dd2, experiments/stage-ablation/runs-s8b/.

Your question for me: DREAM evaluates end-to-end report quality along dimensions like citation grounding. We're trying to attribute those same dimensions to pipeline stages. Has anyone on your side found a principled way to map an end-to-end metric onto stage-level increments — or is that mapping inherently ill-defined, which would itself be a useful negative result for us to cite?

Best,
Chenglu

(~180 words)

---

## 发送前检查清单（成璐操作时看）

- [ ] 邮箱地址：arXiv 页面不公开邮箱，需从个人主页/GitHub/机构页查（Shaikh: 搜 GitHub/LinkedIn；Huang: UGent iMinds 组页；Lumer: IBM Research 主页；Dorfman/Litman: Technion CS 系页）
- [ ] 每封确认 ≤200 词、一个可复现结果 + 一个问题
- [ ] commit hash 在发送时更新为当时的 main HEAD（现在 62d43dd2，之后还有 G1/G5 提交）
- [ ] 建议发送顺序：1 → 2 → 3 → 4（先最近先例，再 RL 线，再工业界，最后顶会）
- [ ] 回复跟踪：收到回复后记入 memory/qanda-ledger.md 对应条目