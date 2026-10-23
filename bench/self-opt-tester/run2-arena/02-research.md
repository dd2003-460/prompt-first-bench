# 02 信息调研 + 02.5 交叉核验 — R3.2 run2：§3.0 成本结构

> origin: ai · 2026-10-24 · 含 02.5（按任务书 3 文件产出约定并入本文件）

## 02 调研路径与通道（如实）
- `ralph prompt-first web-llm`：**degraded**——sandbox 无 ralph 可执行文件（`ralph …` → command not found，exit 127；`which ralph` exit 1）。
- `ego-browser`：**degraded**——同样不存在（exit 1）。→ 无第二 LLM 交叉通道，关键主张改用"内部实测 × 外部独立来源"双源法，逐条标 conf；不虚构回执。
- 可用通道：本地 git/wc/tokenizer 实测 + web_search（外部来源，观察时间 2026-10-23/24）。

## 实测数据（全部可复跑：`node bench/r3/run2/count-tokens.js`，exit 0，回执 token-counts.txt）
| # | 测量 | 值（o200k） | 含义 |
|---|------|------------|------|
| M1 | 规则负载 = loop 7 文件 + SOP | **12,086**（39,858B；cl100k 15,367） | 步骤 4 每会话固定输入 F1 |
| M2 | 其中示例/案例段 | 3,535 ≈ loop 文件的 38% | 瘦身候选上限 |
| M3 | 任务书（本 run）/003/goal 文本 | 527 / 473 / 890 | 步骤 0/交接成本 |
| M4 | pilot V0 输出（3 题） vs V4 输出 | 1,749 vs 11,256 = **6.44×** | 全流程输出膨胀 F3（输出侧） |
| M5 | V4 pilot 发送 prompt 内嵌规则卡 | 997-1,324 | **实况先例：~1.1k 规则卡驱动全流程**（对照 M1 全量 12,086） |
| M6 | r1 链路工件（步骤 4 输出实况，7 文件） | 3,984 | 工件输出基线 |
| M7 | r2 交叉验证回执（3 JSON） | 3,397 | 步骤 5 我方侧存档体积；另 DeepSeek 会话搜索 41+19=60 页（receipt note，非我方计费） |
| M8 | V4 pilot 质量分（BC/GAIA/HLE 基础分） | 91 / 91 / 98（V0：81/76/79，+10/+15/+19） | 砍流程的质量代价依据 |

## 成本模型（步骤 4 会话输入推估，conf 0.5）
输入 ≈ L×(T−t₀) + U_avg×T；L≈12.6k（M1+M3），T≈30-60（空缺①假设：6 阶段×5-10 turn+探索+门禁），U_max≈25-50k（规则+repo 读取+工具输出+工件）。
→ 固定部分 ≈ 0.3-0.7M，累积部分 ≈ 0.5-1.1M，**合计 ≈ 1.0-1.8M o200k/会话**。修正项：arena 有 compaction（round1 gemini run 笔记）→ 实际可能偏低，故 conf 0.5，结论只用数量级。

## 外部来源（web_search，观察于 2026-10-23/24）
| 主张 | 来源 | conf |
|------|------|------|
| E1 agent 循环每 turn 重发全部上下文，输入成本随转数呈三角数/O(N²) 增长 | augmentcode.com guide（2026-06-18）；neelmishra.github.io agent-cost-management；ai-tldr.dev（2026-06-13） | 0.8（3 独立源） |
| E2 re-sent context 占 agent 账单大头（一次审计 62%，system prompt 8%；另一拆解 system prompt 重复占 35%） | leanopstech.com 审计（2026-05-14）；aipromptshub.co（2026-06-20） | 0.6（二手审计，口径不一已记录） |
| E3 Anthropic：agent ≈4× chat token，multi-agent ≈15×；token 用量解释 80% 性能方差 | "How we built our multi-agent research system"（经 theaiengineer.substack / valdemird.com / perform.digital 多源转引） | 0.7（原始未直接抓取，多源一致） |
| E4 AGENTS.md 类仓库上下文文件可使每会话推理成本 +20% 以上且收益甚微 | augmentcode.com guide（同 E1 页） | 0.5（单源） |
| E5 工具输出截断可省 60-90% | "Engineering Best Practices: Building Production Agents"（经 arihantdeva blog 转引，2026-05/06） | 0.5（转引） |
| E6 Anthropic context editing 在 100-turn 评测省 84% | parallel.ai（2026-10-11，转引 Anthropic context engineering） | 0.5（转引） |

## 02.5 交叉核验（关键主张双源）
| 主张 | 内部源 | 外部源 | 结论 |
|------|--------|--------|------|
| C1 固定规则负载是步骤 4 输入主导成分之一（≈1/3） | 模型：12.6k×40/1.4M ≈ 36% | E2（35% / 62% 口径） | 一致 ✓ |
| C2 全流程相对裸 prompt 有 ~5-7× token 膨胀 | M4（6.44× 输出侧） | E3（4×-15× 区间） | 同数量级 ✓ |
| C3 规则文本大幅瘦身不必然伤质量 | M5+M8（1.1k 卡片→91/91/98） | E4（加规则文件 +20% 成本而收益甚微） | 方向一致，**待 Q3 重跑实证**（conf 0.5） |
| 矛盾记录：E2 内部两口径（8% vs 35%） | — | leanopstech vs aipromptshub | 解释：是否含工具定义/轨迹口径不同；不强行收敛，本模型自口径 36% 落在区间内 |
| 降级记录：无 ≥2 LLM 交叉通道（ralph/ego-browser 均缺） | exit 127 / exit 1 回执 | — | 按双源法替代，M4 顶格 conf 0.8，模型推估 conf 0.5 |

## 未解决空缺（交给 03/04）
- T（turn 数）无实测 → 度量方案（04.5 Q3）要求 run 文件记录会话读入清单+turn 数，下轮补实测。
- compaction 触发率未知 → 作为 04.5 反方风险项。

## 判定
pass（关键主张双源覆盖；degraded 如实标注；模型只用于数量级排序）
