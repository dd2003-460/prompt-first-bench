# 阶段 02：证据固化 — RUBRIC-V3-FULL-AUDIT / G6 综合报告

> goal: rubric-v3-audit-g6 · 分支 ralph/rubric-v3-audit-g6 · 2026-10-30
> 上游：stages/01/RV3G6-goal-decomposition.md（F1-F4 + 判断点 J1-J4）
> 原则：**不凭记忆搬运数字**——每个要进 AUDIT-report 的关键数字在本阶段做 JSON 层复算或逐字复核，留 evidence。

## E1 · web-llm 强制步骤回执（降级条款生效）

| provider | 结果 |
|----------|------|
| web-llm（三 provider 轮询） | **全部失败**——登录过期（与 G5 02 阶段同一状态，本轮未重新尝试登录，沿用其回执结论） |

处置：按任务书降级条款，外部文献交叉验证不可用；ResearcherBench/RACE 差异表以 `git show aea3d6b:receipts/rubric-v3-gap-analysis.md`（Q1-Q3，含一手细节）为事实源，报告中该节标注「外部在线复核 unverified」。不阻塞。

## E2 · 冻结数据关键数字复算（本 goal 独立执行，非引用前序结论）

复算脚本逻辑：直接读 `hit-matrix.json` + `prior-estimates.json`（orig judge p̃/w1）+ `judge-blindtest-r1.json`（new judge p̃），公式 `w2(p)=1+min(−log₂p, log₂100)`（p=null→1.0）、`O3=Σw·h/Σw`、权重方案 W0 flat / W1=w1 / W2=w2 / W3=w1×w2 / W4=w1+w2。gold strict 集 = {N-2.1, N-3.2.2, N-2, N-4, N-1.3}（r71b 冻结口径）。

| # | 数字 | 落盘来源 | 本 goal 复算 | 一致 |
|---|------|----------|-------------|------|
| E2.1 | w2 公式 62/62（双 judge × 31 节点） | g2-rootcause F1 | 0 mismatch（容差 5e-4） | ✅ |
| E2.2 | W3/W4 orig-judge 8 run 分数 vs stats-w3w4.json | G3 F1 | 0 mismatch（容差 5e-5） | ✅ |
| E2.3 | per-run top-5 gold max（W2/W3/W4 × 双 judge × 8 run） | G1 C4 / G5 负面结果 4 | **max=2**（orig-W2-run1） | ✅ |
| E2.4 | 超几何基线 P(X≥3) n=31,k=5,r=5 | G2 F4 | **0.019899** | ✅ |
| E2.5 | top-10 口径 E[X]=1.61 / P(X≥4)=2.7% / P(X≥3)=17.6% | G3 F3b | 1.6129 / 0.027438 / 0.175751 | ✅ |
| E2.6 | global top-10 gold 计数（4 方案 × 双 judge） | G3 F3b | orig {W1:3,W2:3,W3:4,W4:4} / new {W1:3,W2:2,W3:4,W4:3} | ✅ |
| E2.7 | new W3 global top-5 = {N-4,N-1.1.3,N-5,N-3.2.4,N-2}，strict 顺序下 gold 计数 | G1 C4 记 1/5 | 排序确认；**但 gold 计数见 E3 勘误** | ⚠️ 见 E3 |

## E3 · 勘误（本 goal 新发现，G6 报告必须吸收）

**E3.1 · 「new W3 top5_gold ∈ [1,2] 依赖 tie-break」的机制表述需修正。**
G5 负面结果第 3 条写「当前报告的 1/5 依赖于 id tie-break（N-1 < N-2 alphabetically）」。本 goal 高精度复算（Fraction 精确比较）发现：new W3 下 **N-1 与 N-2 的 w3 值精确相等（均 = 10.0）**——因为两者 p̃_new 均为 0.50（w2=2.0）且 w1 均为 5.0。id tie-break 把 N-1（非 gold）排在 N-2（gold）前面 → top-5 集合 {N-4,N-1.1.3,N-5,N-3.2.4,**N-1**} → gold 计数 **1/5**；若 tie-break 取 N-2 → top-5 换入 N-2 → **2/5**。即 [1,2] 区间确实成立，但机制是「精确并列 + tie-break 选择」而非「近似并列被浮点截断」。G5 的数值区间正确，机制描述偏窄。W4-new 同构（N-1/N-2 精确并列于 7.0）。

**E3.2 · gold mean rank 的 tie-sensitivity 范围需以「精确并列组」为准，G5 的 [9.60,13.40] 用了过宽的舍入分组。**
本 goal 按精确值分组重算（gmr = Σ rank(g)/5，rank 从 0 计，并列组内位置在 [k(k−1)/2, k(2m−k−1)/2] 间变动）：

| 方案-judge | 精确 gmr 范围 | G5/G3 引用值 | 说明 |
|-----------|--------------|-------------|------|
| W1-orig / W1-new | **[2.60, 6.40]** | G5 称 [9.60,13.40]（1-based） | 换算 1-based = [3.60, 7.40]；G5 的 9.60/13.40 来自把 4 位小数舍入后的宽并列组（如 w1=2.604 的 3 节点组被拆散/合并），**过宽**。精确值：w1 只有 3 个含 gold 的并列组（{5.0:5 节点含 N-2,N-4}、{2.0:7 节点含 N-2.1,N-1.3}、{3.396:4 节点含 N-3.2.2}） |
| W2-orig | [7.80, 8.00] | G3 引 9.2（1-based ≈ 8.2） | 基本一致（单对并列 N-1.3/N-1.3.1 @4.6439） |
| W3-orig / W4-orig | **5.40（无并列含 gold，tie-robust）** | G3 引 6.4（1-based） | ✅ 一致（0-based 5.4 + 1） |
| W3-new / W4-new | [6.80, 7.00] | G3 引 8.6（1-based ≈ 7.6） | 略偏：精确上界 7.0（1-based 8.0），G3 的 8.6 同样来自宽舍入分组；方向不变 |

**判读**：(i) G5 的 tie-sensitivity *定性结论*（W1 评估对 tie-break 敏感、W3/W4 更稳健）在精确值下**依然成立且更强**——W3/W4-orig 完全 tie-robust（单值 5.40），W1 范围跨度 3.8（精确）vs W3-new 仅 0.2。(ii) 但 G6 报告引用具体数值时必须用精确值，不得沿用 G5 的宽舍入数。(iii) W1-new 与 W1-orig 的 gmr 范围完全相同（w1 与 judge 无关，并列结构不变）——这本身是 W1 作为主公式的一个性质：其构念效度弱点是结构性的（top-5 全是 L1 根节点 N-1..N-5），不随 p̃ 来源变化。

## E4 · 前序交付物结论复核（逐条核对，供 R1 汇总节引用）

| 前序结论 | 出处 | 复核方式 | 状态 |
|----------|------|----------|------|
| C1 ρ_orig=0.456 / ρ_new=0.629 / cross=0.688 | G1 §2-C1 | 数值与 assert-g1-audit.py S2 输出行及 blindtest JSON cross_judge_spearman 字段一致 | ✅ 可引用 |
| C2 三红旗 N-1/N-1.1/N-5.3 | G1 §2-C2 | p̃ 值与 hit 计数逐格对照 prior-estimates/hit-matrix | ✅ 可引用 |
| C4 W3 翻转 3/5↔1/5 + per-run max=2 | G1 §2-C4 | E2.3/E2.7 复算 | ✅（1/5 侧带 E3.1 限定） |
| F1 公式排除 62/62 | G2 | E2.1 复算 | ✅ |
| F2 双源 p̃ 偏差（共同高估 + 保守下界） | G2 | N-1/N-2 双 judge p̃ 0.45/0.50 与 0.25/0.50 复核；保守下界 5 节点清单复核 | ✅ |
| F4 超几何 P(X≥3)=1.99% | G2 | E2.4 复算 | ✅ |
| G3 验证链闭合（8/8+8/8+7/7+4/4） | G3 F1 | E2.2 抽验 W3/W4 分数全 8 run | ✅ |
| G3 gold-mean-rank 方向一致性（W3/W4 优于 W1/W2，7 组合全同向） | G3 F3b | 用 E3.2 精确值重验：W3/W4-orig 5.40 < W1 中位 ~4.5? —— **注意**：0-based 下 W1 范围 [2.60,6.40] 的下界低于 5.40，「方向一致」只在 *落盘顺序值*（W1=10.8/11.2 1-based）意义上成立；精确 tie-robust 意义下 W1 的最优 tie-break（3.60）反而优于 W3（6.40）。**这是 E3.2 暴露的新问题，见 E5** | ⚠️ 见 E5 |
| G4 S2 未规避（硬证据 a/b/c） | G4 | 文件头/§4/O2 条款原文复核（origin/rubric-v3 DRAFT） | ✅ 可引用 |
| G5 12 blocker L1×5/L2×7 ≈ 32 回合 | G5 3b | 分级逻辑复核（文本修订 vs 协议重设计） | ✅ 可引用（成本为估算非实测） |

## E5 · G3「gold-mean-rank 唯一方向一致指标」论断的边界修正（02.5 重点攻击对象）

G3 F3b 的核心论据是「gold 平均排名是唯一在全部 7 个方案×judge 组合下方向一致的指标」（W3/W4 6.4/8.6 优于 W1/W2 10.8/11.2，1-based 落盘顺序值）。E3.2 的精确复算暴露其边界：

1. **落盘顺序值 vs tie-robust 值是两回事**。G3 用的 10.8/11.2/9.2/6.4/8.6 全部是「按落盘节点顺序排并列」的单点值。W1 的落盘顺序恰好是其 *最差* tie-break 之一（1-based 10.8，精确范围 [3.60,7.40] 的上端附近）；而 W1 的 *最优* tie-break（3.60）优于 W3-orig 的 6.40。
2. **「方向一致」的正确表述**：在 *同一 tie-break 规则*（落盘顺序）下，W3/W4 优于 W1/W2 在 7/7 组合成立——这是真的。但该规则的任意性意味着：换一个合法 tie-break，W1 可以反超 W3。因此 gold-mean-rank 作为主判据的价值不在「它比 top-5 计数稳健」（这点成立），而在「**它是连续量、头部 3 席交换只引起 O(1/5) 级扰动而非 0/1 翻转**」——top-5 计数是 3/5↔1/5 的二元翻转，gmr 是 6.4→8.6 的连续移动。
3. **对定稿建议的影响**：推荐路径不变（O1 改判据仍是最优子选项），但理由表述要从「唯一方向一致」改为「对头部席位交换的扰动幅度最小（连续量 vs 离散翻转）」，且必须同时声明「gmr 的具体数值带 tie-break 敏感性，跨方案比较须在预注册 tie-break 规则下进行」。

## E6 · 差异表素材固化（ResearcherBench / RACE，源自 gap-analysis aea3d6b）

| 轴 | rubric-v3 | ResearcherBench | RACE/FACT |
|----|-----------|-----------------|-----------|
| 评分粒度 | 31 节点树 × 8 维度（5/5 最细） | 逐 claim grounding + 专家 insight criteria 1-3 | 动态 task-specific criteria（claim-source 对） |
| 部分分 | 0/1/2 三档 + 层级倍率（5/5 rank 1） | 部分支持 | reference-relative |
| 校准机制 | κ≥0.6 前置门禁 + 换位双判（4/5 rank 1 of 29） | judge-human F1 事后报告 | 双人评分 |
| 重要性信号 | **surprisal（模型发现率 p̃）**——survey 空白 | 专家重要性 1-3 | 无（criteria 即重要性） |
| gold 结构 | 单一 Lead 构建推理树 | 专家逐题设计 | 动态生成（无固定树） |
| 已知暴露面 | S2 同源偏置（未规避） | 成本高（2500+ rubrics ≈ 2800+ 人时） | 可比性弱（criteria 每题不同） |

**surprisal 空白声明**（gap-analysis Q3 已确认）：用「盲生成频率」作节点重要性权重在 survey 覆盖的 bench 中无先例——这是 rubric-v3 的真实方法论贡献点，**但其有效性恰是 G1-G3 证伪的对象**（p̃ 估计不稳定 + 稀有≠重要）。定稿建议须同时保留这一声明与负面结果。

## verdict

**pass** — 7 项关键数字复算通过；发现 2 处需勘误/边界修正（E3.1 tie 机制、E3.2/E5 gmr 范围与「方向一致」论断边界），均已定位到 G5/G3 的具体表述，G6 报告将吸收。进入 02.5。