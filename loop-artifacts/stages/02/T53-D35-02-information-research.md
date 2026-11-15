# T53-D35 阶段 02：信息调研台账（不含任何执行阶段产物）

- 上游：`loop-artifacts/stages/01/T53-D35-01-goal-decomposition.md`
- 边界：本文件**只记录调研所得**；不引用、不推测 stage 04 的任何产物或其结论
- 落盘位置：本文 + `modules/F-theory/gradient-descent/litsurvey/search-log-d35.json`

## 1. 检索执行记录

| # | 引擎 | 查询 | 有效命中 |
|---|---|---|---|
| Q1-a | web_search(depth 2) | arXiv iterative prompt optimization feedback loop distribution drift stale evaluations LLM self-improvement | 2611.07123, 2601.02683, 2603.25681 |
| Q1-b | fetch_page | arxiv.org/html/2611.07123 chunk 0 | PromptOps 摘要 + §1 + §2 |
| Q1-c | fetch_page | arxiv.org/html/2611.07123 chunk 3 | §3.3 Controller + §4.1 setup + §4.2 screening |
| Q1-d | fetch_page | arxiv.org/html/2601.02683 chunk 0 | HAPO 摘要 + intro + related |
| Q1-e | fetch_page | arxiv.org/html/2507.19457 chunk 0 | GEPA 摘要 + §1 |
| Q1-f | fetch_page | arxiv.org/html/2603.25681v3（经搜索摘录） | §6.1/§7.1/§7.3 |
| Q2-a | search(depth 1) | "When to Trust Your Model" MBPO arXiv number | 1906.08253 确认 |
| Q2-b | fetch_page | arxiv.org/abs/1906.08253 | MBPO 摘要 |
| Q2-c | search(depth 1) | Besbes Gur Zeevi non-stationary rewards arXiv 1406 | NeurIPS 2014（无 arXiv 版）|
| Q2-d | search(depth 1) | Suk Kpotufe Adaptive Nonstationary Bandits arXiv id | 2407.08654, 2505.18871（转述）|
| Q2-e | fetch_page | arxiv.org/abs/2407.08654 | Hölder 非平稳动态 regret |
| Q4-a | fetch_page | arxiv.org/abs/1908.05659 | DRO review |
| 勘-a | fetch_page | arxiv.org/abs/2101.05574 | ❌ astro-ph（ID 错误证据）|
| 勘-b | fetch_page | arxiv.org/abs/1403.3919 | ❌ astro-ph（ID 错误证据）|
| 勘-c | fetch_page | arxiv.org/abs/2202.06384 | ❌ cs.GT FairTraDEX（ID 错误证据）|
| 勘-d | search(depth 1) | AdaPrompt arXiv id 2202.04824 | ✅ 两个独立参考文献列表一致 |

通道说明：bash curl 无外部出网（白名单仅 github/npm/pypi），全部外部检索走 `fetch_page` / `web_search`；arxiv abs 与 html 通道均正常。

## 2. 关键提取（原文级，供判决引用）

1. **PromptOps (2611.07123)**：judge drift = "a loss of agreement between a fixed judge and the intended human evaluation policy under a changing evaluation stream"；"drift can emerge solely from changes in the stream of cases being evaluated"；"changes that correct known failures can introduce regressions on previously well-handled cases"；Controller 在窗内误差 ≥τ 触发、w 轮冷却；实验只允许访问过去观测（"never future ones"），500-turn 流，pass 落在 t=20/50/95/163/265/417；结论 "recovery after recalibration rather than invariance"、"adaptation can cause specialization"、"neither optimization algorithm choice nor update timing generalizes universally"。
2. **HAPO (2601.02683)**：摘要即写 "current prompt optimization methods often induce **prompt drift**, where new prompts fix prior failures but impair performance on tasks the prompt previously handled successfully"；给 Drift(t) 定义与阈值早停；用 UCB 选编辑位置；11/12 场景最优、平均 +7.21%。
3. **GEPA (2507.19457)**：语言比稀疏标量奖励信息量更大；Pareto 前沿保留实例级 top-k；比 GRPO 平均 +6%（最多 +20%）、rollout 少至 1/35；比 MIPROv2 聚合 +13% vs +5.6%；held-out 仅星标呈现。
4. **MBPO (1906.08253)**：悲观界过紧 → 用经验模型误差决定模型使用量，短 rollout 分支即可。
5. **Besbes/Gur/Zeevi (NeurIPS 2014)**：变差预算 V_T 与最小可达 regret 直接挂钩；**无 arXiv 版**。
6. **2407.08654 / 2505.18871**：平滑非平稳环境下动态 regret 为 T^{2/3} 型，可自适应不预知非平稳度；有 safe arm 时可快于 √T。
7. **DRO review (1908.05659)**：min_θ sup_{Q∈𝒰} E_Q[L] 的标准形态；与 robust opt / 风险厌恶 / 机会约束的关系。
8. **2603.25681**：持续适配下固定 benchmark 会 stale 或因 superficial shortcut 被过拟合；对 proxy reward 优化会扭曲行为；data autophagy 降质降多样性。

## 3. 本轮推翻的既有判断（交叉验证义务的交付）

F-旧 与根索引记："无 prior work 讨论 prompt-induced drift（conf 0.70，待 arena 交叉验证）"。

**本轮结论：推翻。** 依据：HAPO（2026-01，显式定义 + 可计算 Drift(t)）、PromptOps（2026-11，judge drift + 触发控制器）、2603.25681（§6.1 明确 benchmark stale/被 superficial shortcut 过拟合）。三篇独立，其中两篇给出可计算指标。

**可保留的残余空白**（弱得多）：把 drift 指标接进变差预算理论（V_T）的工作**未找到**——属"搜了没找到"级证据，需 Lead 二次交叉验证。

## 4. 顺带发现的 ID 勘误（调研副产品，必须上报）

| F-旧 写法 | 实际 | 证据 |
|---|---|---|
| MBPO = 2101.05574 | astro-ph 宇宙学（cosmic distance duality） | arxiv abs 原文 ① |
| Besbes 2014 = 1403.3919 | astro-ph 宇宙学（relic gravitational waves） | arxiv abs 原文 ① |
| Suk & Kpotufe 2022 = 2202.06384 | cs.GT FairTraDEX（DeFi） | arxiv abs 原文 ① |
| AdaPrompt `[待核验]` | **2202.04824** | 两个独立参考文献列表 ① |

正确值：MBPO → **1906.08253**；Besbes → NeurIPS 2014 pp.199–207（无 arXiv）；Suk & Kpotufe → 未定位 arXiv ID，引 AISTATS 2022 或经 2407.08654 转述。

## 5. 本阶段不确定性

- Q3（<20 trials 预算）本轮**零新增实证**，只有 PromptOps §4.2 "screening not ranking" 与新老口径一致性两条间接支撑。
- 自指（策略改变环境）的对抗性 MDP 理论**本轮未检索**，不得据此发表"不存在理论"的结论，只能记"未覆盖"。
- Besbes 的精确指数未逐字核到；F-旧 写的 `Ω(√(V_T·T))` 标 `[待核验]`，不进判决。
