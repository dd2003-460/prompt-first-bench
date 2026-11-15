# T53-D35 回执：真实世界迭代 vs 解析先验+泛函梯度下降（文献滚雪球）

- repo: https://github.com/dd2003-460/prompt-first-bench
- branch: `arena/f65a5a27-prompt-first-bench`
- base: `0fb0c1e`（D35 任务书落点修正后）
- commit_sha: `c58bee7`（完整：见 `git log --oneline -1` / 回执提交本身为其子提交）
- 任务书: `tasks/T53-D35-arena-task.md`
- 日期: 2026-11-13
- 执行模式: `loop/prompt-first/` 01 → 02 → 02.5 → 04 → 04.5（SOP: `sop/arena-loop-pipeline.md`）

## 1. 交付物

| 文件 | 作用 | 规模 |
|---|---|---|
| `modules/F-theory/gradient-descent/litsurvey/2026-11-13-d35-realworld-vs-analytic-optimization-survey.md` | 主交付：Q1–Q4 判决 + A/B/结合形式 + 勘误表 + 来源分级 | 373 行 |
| `modules/F-theory/gradient-descent/litsurvey/search-log-d35.json` | 机读检索日志（7 组查询、26 源、判决、反方复核、未找到） | 26 sources |
| `litsurvey-index.md`（仅第 15 行 F-theory） | 覆盖率 65%→80%，记录 gap 推翻与 3 处 ID 勘误 | 1 行 |
| `loop-artifacts/stages/01/T53-D35-01-goal-decomposition.md` | 目标分解 + 预裁定（含 AC 映射） | — |
| `loop-artifacts/stages/02/T53-D35-02-information-research.md` | 调研台账（原文级提取，无 04 引用） | — |
| `loop-artifacts/stages/02.5/T53-D35-02.5-crosscheck.md` | 口径回溯 + 5 条对抗攻击 | — |
| `loop-artifacts/stages/04/T53-D35-04-execution.md` | 执行 + 返工回环记录 | — |
| `loop-artifacts/stages/04.5/T53-D35-04.5-final-review.md` | AC 逐条终审 + 遗留项 | — |
| `loop-artifacts/stages/04/verify-d35.py` | 机检 verifier（21 项） | — |

## 2. 六条判决（摘要）

| 项 | 判决 | conf |
|---|---|---|
| Q1 路线 | 无干净 A-vs-B 对照；证据指向 **B 定函数空间 + A 定步长与停止 + 控制器管漂移** | 0.78 |
| Q2 定理/失败条件 | T1 变差预算（Besbes 2014）+ T2 显著漂移自适应（Suk&Kpotufe 2022 经 2407.08654）+ T3 模型误差定模型用量（MBPO 1906.08253）可拼成判据；**自指档无定理** | 0.72 |
| Q4 防 Goodhart 形式化 | DRO/minimax 只能形式化"对指定裁判族的最坏情况"，**不能**形式化"不可被 hack"；需正交多样性项兜底 | 0.72 |
| Q3 预算 | <20 trials 做结构先验 + 定向单因子探测，BO 降级为可选 | 0.66 |
| gap 交叉验证 | F-旧 "无 prior work 讨论 prompt-induced drift" → **推翻** | 0.85 |
| ID 勘误 | F-旧 3 处 arXiv ID 指向无关论文（2×astro-ph + 1×DeFi），其"ID 已核 0.90"自评不成立 | 0.95 |

## 3. 防 Goodhart / 防泄漏 / 返工回环 三项约束的落实

- **防 Goodhart**：提案目标函数 `J_t = S_α + λ·Div_t − β·Red − γ·Drift_t − δ·Cost`，其中 `Div_t` 为三项跨通道探索多样性（结构熵 / edge-type 覆盖 / 来源域数），且 **λ 冻结不参与搜索**；§4.3 论证了它为何不是单指标陷阱，§8-C3 自陈其局限（"人在回路的结构化搜索"，非"自动发现目标函数"）。
- **防泄漏**：stage 02 与 02.5 中无任何 `T53-D35-04` / `stages/04/` 引用（verifier AC10b 机检通过）。
- **核验返工**：verifier 首跑 `fails=4`（AC7b 结论强度超证据 + AC10/AC11b/AC12 未落地）；AC7b 属实质错误 → **回上游把 conf 0.55 降为 0.30**（改结论不改判据），其余补产物；二跑 `fails=0`。

## 4. verifier 结果

```
$ python3 loop-artifacts/stages/04/verify-d35.py
fails=0  passes=21  total=21（最终运行；log 已覆盖为最终输出。首跑 fails=4 → 回上游修订 AC7b 后二跑仅 AC12 缺 sha → 填回执后三跑全过）
```

## 5. 遗留 / 需 Lead 决策

1. 自指/对抗 MDP 理论**未检索**（不是未找到）——若作为 novelty 关键支撑需补一轮。
2. Besbes 精确指数与 F-旧 `Ω(√(V_T·T))` 口径冲突未解，论文引用前须逐字核。
3. Drift→V_T 预算化"疑似空白"只有 0.3（搜了没找到级），不可作行动前提。
4. 建议在 F-旧 survey 文件头加一行指向 D35 §11 勘误表的指针（本次未擅自改该文件）。
