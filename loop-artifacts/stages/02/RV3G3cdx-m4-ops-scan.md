# 阶段 02 — RV3G3cdx-m4-independent-source-ops · 现状扫描（r152）

> 范围：两打分器 M4 basis 全文取证 + packet v2 P6 全字段枚举 + bench.md 缺陷 #2 上下文链 + r4 裁决层口径取证。所有数字实跑可复现（命令附后）。

## S1 — 证据源盘点（五源，全部只读）

| # | 源 | 角色 | 关键落点 |
|---|---|---|---|
| E1 | `bench/self-opt-tester/bench.md` | 指标定义 + 缺陷登记 | L13 M4 行 / L29 核心发现 / L67 r3→r4 变化 / L75 缺陷 #2 / L117 收敛点 |
| E2 | `bench/self-opt-tester/r4/independent-scoring-deepseek.json` | 打分器 A（DeepSeek web，盲打 step1） | `key_reasons["run1 M4=50 / run2 M4=45 / run3 M4=35"]` |
| E3 | `bench/self-opt-tester/r4/adjudication-step2.json` | 裁决层（step2，\|Δ\|>15 逐项） | `adjudications.run{1,2,3}_M4` ×3 + `largest_residual_bias` |
| E4 | `bench/self-opt-tester/r5/scoring-claude-r1.json` | 打分器 B（Claude Code，盲打 R5.1） | `scores.run{1,2,3}.M4.basis` ×3 + `protocol` |
| E5 | `bench/self-opt-tester/r5/evidence-packet-r4-v2.json` | 回测数据（P6 节） | `runs.run{1,2,3}.P6_cross_validation` = 2+7+2 条 |

## S2 — 两打分器 M4 basis 原文逐字摘录（判分逻辑反向工程原料）

**E2 DeepSeek key_reasons（三 run 合并一条）**：
> 「锚点≠独立源；web_search 单通道非≥2独立源；run3 无外部交叉」

**E3 裁决层 reason（逐 run）**：
- run1_M4（final 70，winner=self-direction）：「锚点+上轮双源可加，本轮无新增双源；90 偏高 50 偏低，居中」
- run2_M4（final 45，winner=original）：「web_search 单通道=单源低分」
- run3_M4（final 35，winner=original）：「无网络无外部交叉=无验证低分」
- largest_residual_bias：「自估把执行锚点/上轮双源回执/单通道 web_search 过度计入『≥2 独立源』，系统性高估」

**E4 Claude basis（逐 run，均引用同一收紧口径『≥2 独立源（不同 provider 且不同 prompt 模板的回执对）』——该口径字符串与 bench.md L75 括号内建议逐字相同）**：
- run1（45）：「本地双源 2 条一致（conf 0.9/0.85）…不满足——无第二 LLM 通道，**本地双源是同一环境内的两个文件源**」
- run2（50）：「C1-C3 三条关键主张走『内部实测 × 外部 web_search』双源法（E1 3 独立源 conf 0.8 / E2 二手审计 conf 0.6 / E3 多源转引 conf 0.7）…**外部源多为二手转引**。三 run 中最接近收紧口径者，仍差『不同 provider 的 LLM 回执对』」
- run3（30）：「3 缺陷验证=sed 逐行复验 vs read 全文对照——**同一文件的两种读取方式（同源双读），非独立源**…完全不满足（0 个独立第二源）」

**口径一致性结论（S2 核心发现）**：两打分器 + 裁决层的口径表述虽措辞各异，但反例集合完全一致——(α) 执行锚点 (β) 上轮回执转录 (γ) 单通道 web_search（含多 URL）(δ) 同源双读 (ε) 训练知识单源。**零矛盾项**（current-goal 失败降级第 1 条未触发）。唯一张力点见 S5 T1（run1 计分方向：DeepSeek 50 / Claude 45 / 裁决 70）。

## S3 — packet v2 P6 全字段枚举（回测数据基线）

实跑枚举（python json.load，命令见文末）：**11 条** independent_sources（run1×2 / run2×7 / run3×2）+ 3 个 channel_status。
⚠ **勘误**：current-goal (c) 写「共 10 条」——实数 11（run2 为 7 条非 6 条：E1-E6 external + 1 local-measured）。以实跑为准修正。

| run | 条目 | nature | conf | source 摘要 | channel_status 摘要 |
|---|---|---|---|---|---|
| run1 | [0] | transcription | 0.85 | r2 双源回执（execution-log 引用） | degraded-partial：本地双源可用，外部 LLM 不可达（ego-browser 缺失） |
| run1 | [1] | local-measured | null | loop-state-r1.json chain_steps.5_cross_validate | （同上） |
| run2 | [0] | external | 0.8 | augmentcode.com; neelmishra.github.io; ai-tldr.dev（3 URL） | 无 ≥2 LLM 交叉通道（ralph exit 127 / ego-browser exit 1）→ 按'内部实测 × 外部独立来源'双源法替代，M4 顶格 conf 0.8 |
| run2 | [1] | external | 0.6 | leanopstech.com; aipromptshub.co（2 URL） | （同上） |
| run2 | [2] | external | 0.7 | Anthropic multi-agent 文（经 substack/valdemird/perform.digital 转引） | （同上） |
| run2 | [3] | external | 0.5 | augmentcode.com guide（同 E1 页） | （同上） |
| run2 | [4] | external | 0.5 | 'Engineering Best Practices'（经 arihantdeva blog 转引） | （同上） |
| run2 | [5] | external | 0.5 | parallel.ai（转引 Anthropic context engineering） | （同上） |
| run2 | [6] | local-measured | 0.8 | run2 count-tokens.js → token-counts.txt | （同上） |
| run3 | [0] | local-measured | 0.8 | run3/03-review.md defect cite（sed 逐行 + read 全文） | 无网络（subagent 独立 session）——交叉验证仅限本地双源，外部源 unverified |
| run3 | [1] | local-measured | null | execution-log.md bench-row M4 basis '无外部 LLM 源，unverified' | （同上） |

**schema 缺口实证**：`nature` 枚举仅 3 值（external/local-measured/transcription），**无 provider 字段、无通道维度字段**——「不同 provider 且不同 prompt 模板」的判定在当前 schema 下不可机判（current-goal 失败降级第 3 条触发条件确认存在）。

## S4 — bench.md 上下文链（缺陷 #2 的前后文约束）

- L13 指标定义行：「M4 交叉验证 conf | 15% | 14.70% | **≥2 独立源对关键 claim 的验证质量** | web-llm 回执 + 双源 conf 标注」——「固定落点，下轮引用不重定」（L9 声明）⇒ 本 goal 的操作化定义**不得改变 M4 指标语义**，只能把「独立源」一词从主观裁量变为可判据。
- L29：「最大高估源 = M4（独立分 50.0 vs 自估 86.7）：执行锚点 ≠ 独立源，单通道 web_search ≠ ≥2 独立源，上轮双源回执 ≠ 本轮新验证」——三个反例类的首次成文。
- L117：「两打分器收敛点：M4 三项全 low/mid 边界…核心结论（M4 是最大高估源）跨打分器稳健」——操作化定义的验收锚：新规则须复现「三 run 全 low/mid」的方向性结论。

## S5 — 待裁定张力点（02.5 输入）

- **T1 — run1 计分方向分裂**：DeepSeek 50 / Claude 45 / 裁决 70（winner=self-direction，理由「锚点+上轮双源可加…居中」）。注意：裁决 70 的理由**部分违反了自家 key_reasons 的反例集**（「锚点+上轮双源可加」vs E2「锚点≠独立源」+ E3 largest_residual_bias「上轮双源回执…过度计入」）——裁决层与打分层口径不一致实例。操作化定义须对此给出明确处置（候选：裁决 70 登记为「口径过渡期人工居中」，新规则下 run1 应落在哪一侧由回测定）。
- **T2 — 回测口径**：新规则计数对象 = P6 `independent_sources` 条目（11 条），还是打分器 basis 中引用的原始证据形态？裁定倾向 = 前者（可机判、有 schema 锚点），后者仅作对账参照。
- **T3 — conf 与计数的关系**：conf=null 的两条（run1[1]/run3[1]）是「通道状态记录」而非 claim 验证——是否计入独立源总数？裁定倾向 = 不计入（它们是 channel_status 的冗余转录，claim 本身是负向陈述「不可达/无源」）。

## 复现命令

```bash
# S3 枚举
python3 -c "
import json
d=json.load(open('bench/self-opt-tester/r5/evidence-packet-r4-v2.json'))
n=0
for run in ['run1','run2','run3']:
    p6=d['runs'][run]['P6_cross_validation']
    n+=len(p6['independent_sources'])
print(n)"   # → 11
```