# Bench · Agent 过程效率（r4 · 独立校准版）

> origin: ai · 2026-10-24 · goal-9c250b87（第 4 轮）
> r1 = n=1 初版（89.2）→ r2 = 交叉验证补全（92.7）→ r3 = 校准版（87.84±3.53，自估）→ **r4 = 独立校准版（76.45±7.29，第二 AI 独立打分+裁决）**

## 指标定义（固定落点，下轮引用不重定）

| 指标 | 权重(r3) | 权重(r4 校准后) | 定义 | 可验证口径 |
|------|------|------|------|-----------|
| M1 token 效率 | 25% | 24.61% | 链路固定规则负载 + 重发放大控制 | 规则字节/tokenizer 实测 + 账本 input 口径 |
| M2 任务书行数 | 10% | 11.09% | 任务书 ≤200 行 | wc -l |
| M3 断点通过率 | 20% | 19.59% | 断点 A/B/C 通过且 gate 步骤计入 | 断点证据文件 |
| M4 交叉验证 conf | 15% | 14.70% | ≥2 独立源对关键 claim 的验证质量 | web-llm 回执 + 双源 conf 标注 |
| M5 迭代轮数 | 15% | 14.77% | 达 conf≥0.7 所需迭代轮数 | review.md conf 记录 |
| M6 降级诚实度 | 15% | 15.24% | 降级如实标注不虚构 | 降级条目 × 锚点 |
| M7 验证溯源率（gate） | —（门禁，不计分） | 同左 | 声称成功步骤中挂 ≥1 不可伪造锚点的比例 | 锚点台账 |

## r4 数据（n=3 run · 独立打分 + 裁决）

**打分方法**：DeepSeek（ego-browser space 533 p3）先盲打 18 分（只凭证据，不看自估）→ 对照自估，9 项 |Δ|>15 逐项裁决（哪边对+理由）→ 未裁决项（|Δ|≤15）保留自估。回执：r4/independent-scoring-deepseek.json + r4/adjudication-step2.json。

| Run | 通道 | M1 | M2 | M3 | M4 | M5 | M6 | M7 gate | 加权分(旧权重) | R3 自估 | Δ偏差 |
|-----|------|----|----|----|----|----|----|---------|--------|--------|------|
| run1 | local Lead（全链路重走+锚点+账本） | 55 | 100 | 90 | 70 | 95 | 100 | 7/7 | 81.50 | 91.17 | +9.67 |
| run2 | arena agent mode（14m27s，三问逐答） | 25 | 100 | 86.7 | 45 | 90 | 95 | 7/7（10 锚点） | 68.09 | 89.20 | +21.11 |
| run3 | subagent 任务书变体（执行性审查） | 75 | 95 | 85 | 35 | 100 | 95 | 7/7 | 79.75 | 83.15 | +3.40 |
| **mean±std** | | **51.7±19.9** | **98.3±2.5** | **87.2±2.6** | **50.0±16.7** | **95.0±4.1** | **96.7±2.5** | **21/21=100%** | **76.45±7.29** | **87.84±3.53** | **+11.39** |

**核心发现：自估偏差 +11.39 点（87.84 → 76.45）被独立打分实证**——R2 DeepSeek 预警的「自报 conf 同时是测量对象和测量工具」不是假设而是实测。最大高估源 = M4（独立分 50.0 vs 自估 86.7）：执行锚点 ≠ 独立源，单通道 web_search ≠ ≥2 独立源，上轮双源回执 ≠ 本轮新验证。run2 M1 从 85 砍到 25（12,086 o200k/会话每轮重发的放大效应，自估未计入）。

## 相关矩阵与权重校准（验收 2 · 本轮完成）

- 矩阵（n=3，裁决后分）：r4/bench-r4.json → correlation_n3。15 对中 **8 对 |r|>0.7**：
  r(M1,M5)=+0.9934 / r(M3,M4)=+0.9982 / r(M3,M6)=+0.9425 / r(M4,M6)=+0.9608 / r(M1,M2)=−0.8030 / r(M2,M5)=−0.8660 / r(M2,M3)=+0.7608 / r(M2,M4)=+0.7206
- 调权（goal-9c250b87 验收②公式：每指标取 max|r|，>0.7 → w×(1−|r|/2)，再归一化）：**6 指标全部 max|r|>0.7**（n=3 退化情形，全部被砍 ~×0.5），归一化后相对权重几乎不变（见上表）——**公式在此退化，实质产出是共线证据而非新权重**：M1×M5（省 token↔少迭代，r=0.993）与 M3×M4×M6（链路成功↔验证多↔降级少，r≈0.95-1.0）两个冗余簇坐实。
- 校准后总加权（新权重）：76.82±7.17（旧权重 76.45±7.29，差异 <0.4 点，同退化原因）。
- **caveat**：n=3 Pearson 置信区间极宽，r 仅方向性参考；调权留待 n≥5（R5 候选）。

## Token 绝对口径（r4 精确切分，验收 3 · 完成）

**方法**：bili.log（/Users/a1-6/.local/state/billion-context/bili.log，88,315 行）per-request `[acp-usage] input=NNNNN` 行 × session 前缀 startswith 匹配 × 时间窗切分；窗口锚点=run1 末请求 input=53,364 与 run1/token-ledger.json contextTokens 精确相等。数据：r4/token-split.json。

| Run | 窗口 (UTC 10-23) | requests | input 合计 | output | cache |
|-----|------------------|----------|-----------|--------|-------|
| run1 | 16:21:51.875–16:25:26.363（含 R3 kickoff+run1 执行+run3 派发） | 10 | **500,972** | 不可测* | 0 |
| run2（Lead 侧） | 16:26:13.946–16:34:47.439（任务书/push/监控） | 19 | **1,127,157** | 不可测* | 0 |
| run2（arena 侧） | arena 会话 01a1699d，14m27s | 外部 | **unverified**（本地无账本；规则负载 12,086 o200k/会话每轮重发=实测） | — | — |
| run3 | 16:25:23.178–16:35:20.658（sub bd8e9193 全量） | 20 | **621,696** | 不可测* | 0 |

\* bili per-request 只记 input，无 output 行；session 级 output 累计 123,324（含 R1-R4 全时代）不可按 run 切分，如实标注。
**压缩净省=不可测**：需要「不压缩反事实」基线，账本无此字段；可证事实=压缩后 context 稳定 ≤63K 未爆窗。
**可比性判定（维持 r3）**：run 级 input（0.5-1.1M）与外部数据点同档（DP1 SWE-bench 1,183,537 tok/trace conf 0.9 / DP2 OSWorld 598.7K conf 0.6 / DP3 per-harness 347-974K conf 0.8）——**token 效率结论=同量级；优势在过程纪律（断点+M7 gate+降级诚实）不在 token 绝对量**。

## 验收逐条判定（goal-9c250b87 · R4）

1. **独立打分器** → **PASS**：第二 AI（DeepSeek）盲打 18 分 + 9 项 |Δ|>15 逐项裁决 + 最大残留偏差一句话；两条回执落盘（independent-scoring-deepseek.json / adjudication-step2.json）
2. **权重校准** → **PASS（退化情形如实标注）**：n=3 Pearson 15 对算全，8 对 |r|>0.7，按 goal 公式调权+推导记录；6 指标全被砍属 n=3 退化，实质产出=两冗余簇证据，调权重算留 n≥5
3. **token 精确切分** → **PASS**：run 级 input 500,972 / 1,127,157(+arena external) / 621,696；output 不可测与 cacheSamples=0 均如实标注未虚构
4. **bench.md r4 落盘** → **PASS**（本文件）
5. **push pfb + ls-remote + R5 goal 落盘** → 本次交付

## r3→r4 变化解释

| 变化 | 原因 |
|------|------|
| 总加权 87.84 → 76.45（−11.39） | 自估偏差被独立打分实证，M4/M1 两指标砍分最大 |
| M4 86.7 → 50.0 | 「独立源」口径收紧：锚点/上轮回执/单通道 web_search 不再计入 |
| M1 82.7 → 51.7 | run1 累计未切分属推断扣分 + run2 重发放大 85→25 |
| M5 91.7 → 95.0 | run3 按「1 轮=满分」上调（自估 90 偏低被裁决纠正） |
| std 3.53 → 7.29 | 真实方差被释放（自估把 run 间差异抹平了） |

## 已知缺陷（进 R5）

1. n=3 相关/调权退化——需 n≥5 run 才能有效校准权重
2. M4「独立源」口径仍依赖裁决者主观——需操作化定义（如：不同 provider 且不同 prompt 模板的回执对）
3. output token 与压缩净省不可测（bili 账本字段缺失）——需 provider 侧 cache 上报或换账本口径
4. run2 arena 侧 token 总量 unverified（外部系统无账本）
5. ~~独立打分器仍只 1 个~~ **已解决（R5.1, r75-r77）**：Claude Code 盲打 18 数值分 + 3 gate 判定；Cohen's κ(3bin)=0.55 moderate agreement；分歧根源定位 = r4 evidence packet 缺 M2 行数/M5 轮数字段（结构性偏低，非尺度差异）→ 见下「R5.1 打分器间一致性」节
6. 权重向量实质未变（退化的副产品）——bench 分数目前=「过程纪律审计分」，不是通用 agent 能力分

## O3 权重消融实验（r70 · rubric-v3 surprisal 条件概率权重）

> 任务书：`bench/rubric-v3/ablation/TASK-ablation.md`（r69）· 结果：`ablation-result.md` + `stats-recomputed.json`（r70/r70b, 85908e8）

**公式**：w_v = 1 + min(−log₂ p̃_v, log₂(1/ε))，ε=0.01（封顶 ≈8）。p̃ = judge 估计"无 gold 的 LLM 在父节点上下文下盲生成该子拆分的先验概率"——即你说的"更深的矛盾更难发掘 → 概率小 → 信息量大 → 赋权高"。

**设计**：W0 flat / W1 importance（SHARE 份额）/ W2 surprisal × 8 个真实 C0 run（同一 prompt 独立产出），31 个 gold 节点逐节点命中判定（h∈{0,1}，每个 h=1 附原文证据）。

**核心结果**：

| 对比 | Spearman ρ | 含义 |
|---|---:|---|
| W0 vs W1 | 0.9698 | importance 权重几乎不改排序 |
| **W0 vs W2** | **0.8102** | **surprisal 权重分歧最大——它确实在重新排序** |
| W1 vs W2 | 0.9048 | 两套加权方向部分一致 |

- 权重确实改变排序：run2/run6、run3/run7 在 W0 下打平，W2 下因高权重节点覆盖差异拉开（如 N-4 w1=5、N-3.2.4 w2=4.84）
- **构念效度初检未过线**：W2 top-5 权重节点仅 2/5 带 gold 专家标记（■瓶颈/★订正），低于预设门槛 3/5 → **surprisal 高 ≠ 重要性高**，纯意外性会 overweight "罕见但无用"的节点
- **W3 = w1×w2（乘法组合）唯一过线**（3/5），但刚过线且根因未除：p̃ 来自同一 judge 模型（自我偏袒），需独立 judge 盲测才能写入正式 rubric
- judge 稳定性自检 10/10 = 100%（同 judge 复判，非跨 judge 可靠性）

**局限**：n=8 描述性统计；单域（硬件部署）；单 judge。结论边界 = "小样本支持权重影响排序，不支持 surprisal 单独作为重要性代理"。

**独立 judge 盲测 r1（r73 · Claude Code ralph loop 通道）**：换 fresh-context subagent 盲估 p̃（物理隔离 prior-estimates.json，grep 验证无泄漏）。结果：**W3 top-5 构念效度 1/5 → pass=false**（原 judge 自评 3/5 是自我偏袒产物）；跨 judge Spearman ρ=0.688（≥0.6 门槛，方向稳定但弱一致，新 judge p̃ 分布整体右移、w2 动态范围被压缩）。04.5 反方复核确认 pass 判定对 tie-break 稳健。**最终裁定：surprisal 权重方案（含 W3 乘法组合）在独立验证下不成立，不进正式 rubric**；保留为负结果记录。

**与 Pearson 折权的关系**：正交。Pearson 相关矩阵折权（|r|>0.7 → w×(1−|r|/2)）处理指标间冗余去重；本节 surprisal 权重处理节点级信息量/发现难度。前者管"哪些指标重复"，后者管"哪个发现更值钱"。


## R5.1 打分器间一致性（r75-r77 · Claude Code 第二独立打分器）

**方法**：Claude Code 盲打（时序屏障：打完才读 DeepSeek 分数值，04-execution-log 留痕）→ per-metric Spearman ρ (n=3 纯描述) + Cohen's κ（2 raters，3 档离散化 low<40/mid 40-70/high>70）。工件：`r5/scoring-claude-r1.json` + `r5/scorer-agreement-r1.json`。

**结果**：
- **κ=0.55（moderate agreement，Landis-Koch 0.41-0.60 档）**，po=0.7222/pe=0.3827。高基率效应已校正（high 档 12/18 点）。
- per-metric ρ：M1=1.0 / M3=M4=M5=0.5 / M2=M6=−0.5（n=3 只有 6 种秩置换，ρ∈{−1,−0.5,0,+0.5,+1}，不支持推断，仅描述）
- **|Δ|>15 分歧 4 项全在 M2（run1/run2，各 −50）与 M5（run1 −30、run3 −35）**，逐项对照后裁定倾向均指向 Claude Code 侧——但根因不是打分能力分歧：**r4 给 DeepSeek 的 evidence packet 缺「任务书行数」和「达 conf≥0.7 所需轮数」两个字段**，DeepSeek 自认因此系统性偏低。这是输入证据包不完整导致的结构性偏差，补齐字段后预期分歧消失（→ 实际落地见 R5.2 节：输入对称已断言通过；κ 变化待第三打分器实测）。
- 两打分器收敛点：M4 三项全 low/mid 边界（交叉验证确实是弱项）、M1 run2 低分（重发放大）——**核心结论（M4 是最大高估源）跨打分器稳健**。

**残余风险**（04.5 自查登记）：盲打前读过 bench.md r4 数据表（含混合分），存在锚定残余；M7 按 gate 口径记 pass/fail 不产生连续分（避免给门禁指标虚构分数）。

**R5.2 建议**（由本次分析导出）：evidence packet 模板固化 M2 行数 + M5 轮数字段 → 消除结构性分歧源；第三打分器（不同模型家族）把 κ 从 2-rater 升到 Fleiss'κ。

## 外部 baseline 对比（r2/r3 结论维持）

- 实锤：lm-eval-harness（accuracy 层）/ HELM（结果层）/ promptfoo（LLM 评测）——「过程纪律」维度在开源方案中**缺位**（URL 见 r2 bench）
- token 量级与开源 agent 系统同档（r3 三数据点），不可作同质基线直接比较
- 结论维持：本 bench 在「过程纪律」维度无可比开源 baseline；0.9 比例口径下高于「缺位基线」（无可比分=无对手），该声明的边界=同任务类型

## R5.2 evidence packet 模板固化（r102 · Claude Code ralph loop 通道）

**目标**：消除 R5.1 定位的结构性分歧源——原 r4 packet（`r4/independent-scoring-deepseek.json` evidence_packet 字段，单行摘要）缺 M2 行数 + M5 轮数字段。本 goal 不改任何已有分数值，只修输入面。

**交付物**：
1. **模板 v2**：`r5/evidence-packet-template-v2.md` —— P1-P6 必填 schema（P1 任务书行数 / P2 达 conf≥0.7 轮数 / P3 per-run token 切分 / P4 断点 A/B/C 状态 / P5 降级条目 / P6 交叉验证源清单），每字段三件套（值+source_path+source_quote），null 政策区分"证据缺口型（允许+必填 reason）"与"未提取型（禁止）"
2. **packet v2**：`r5/evidence-packet-r4-v2.json` —— r4 三 run 按模板补齐，全部字段从原始证据一手/准一手提取
3. **对称性断言**：`r5/assert-packet-symmetry.py` —— 67 PASS / 0 FAIL（exit 0）：P1-P6×3run 全非空或 null+reason；R5.1 的 4 项 |Δ|>15 分歧点对应字段存在、承载值非空、source_path 可达

**补齐结果表**（关键值，完整三件套见 packet v2）：

| 字段 | run1 | run2 | run3 |
|------|------|------|------|
| P1 M2 行数 | **24**（一手：git show d96f5db:tasks/003… \| wc -l） | **25**（一手：wc -l run2-arena/task-brief.md） | null/~45 自估（任务书为派发消息文本，无落盘文件） |
| P2 M5 轮数 | **1 轮，conf 0.75**（loop-state-r1.json 原文 "done (V1-V5, conf 0.75)"） | **1 轮**（inferred：A1-A7 单序列无 revise；终态 conf 无数值记录 → null+conf_note） | **2 轮**（self-reported：bench-row "2 轮内完成"；自纠 1 次有 S4 独立锚点） |

**矛盾登记（02.5）**：
- X1：commit 8d7487e（gate-evidence 记的断点 A push hash）不在 pfb 本地对象库（cat-file fatal，fetch 后仍无）→ 不影响取值（改以 d96f5db git 对象为一手来源，三源一致）
- X2：**原 packet "run3 任务书25行" 张冠李戴**——25 行实为 run2 task-brief.md 实测值。摘要式 packet 双重失败（缺失+错配）的实例化证据

**对第三打分器的使用说明**（下一 goal 直接引用）：送分时用 `r5/evidence-packet-r4-v2.json` 替代原单行摘要；打分回执格式沿用 r4/r5 已有 JSON schema（模板 v2 只管输入包，不动回执）；打完后可重算 Cohen's κ（vs DeepSeek/Claude Code 两基线）并升级为 Fleiss'κ（3 raters）。

**边界声明**：对称性断言只证明**输入面对称**（4 个分歧点的字段现在两边都能看到同源证据），不预测新 κ 值——判断尺度差异（若有）只有第三打分器能分离。
