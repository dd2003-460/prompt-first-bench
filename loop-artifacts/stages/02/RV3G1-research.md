# 阶段 02：资料搜集与证据固化 — RUBRIC-V3-FULL-AUDIT / G1 矛盾审计

> goal: rubric-v3-audit-g1 · 2026-10-30
> web-llm 回执：`loop-artifacts/prompt-first/02-web-llm-cross-check.md`（ok=true, successful_provider_ids=[] —— perplexity/chatgpt/gemini 三 provider 全部 error，登录态失效；按任务书失败降级条款记录失败后继续本地证据提取，不阻塞）

## 仓库内证据固化（F1-F4 全量复算）

所有数字以下列只读文件为源：`bench/rubric-v3/ablation/{hit-matrix.json, prior-estimates.json, judge-blindtest-r1.json, stats-recomputed.json, stats-w3w4.json, gold-tree.md, runs-C0-run1..8.md}`。机判脚本 `scripts/assert-g1-audit.py`（r108 入库，exit 0，确定性种子 20261030）。

### F1 · 数据自洽 — 成立

- **A1 矩阵结构**：8 run × 31 node 零破损；h∈{0,1} 全域成立；evidence 政策（h=1 非空 / h=0 null）248/248 cell 成立。
- **A2 O3 复算**：W0/W1/W2 × 8run = 24 个分数按 `Σw·h/Σw` 复算，与 stats-recomputed.json **24/24 精确一致**（容差 5e-5）。W3/W4 另对 stats-w3w4.json 复核亦精确一致（04 执行记录 A2 节）。
- → 计算层排除：任何矛盾不可能来自公式或落盘分错误。

### F2 · 抽检协议与形式一致率

- **A4 样本确定性**：seed=20261030 从 248 cell 抽 75（≈30.2%），与落盘 g1-sample-cells.json 逐位一致；抽检构成 h=1:35 / h=0:40。
- **S1 evidence 逐字核验**：抽检内 35 个 h=1 cell 的 evidence 字符串，空白归一后**全部逐字出现**在对应 run 原文（runs-C0-run*.md）中 → 形式一致率 35/35 = 100%（抽检范围内）。
- **覆盖度**：75 cell 落在 30/31 个不同节点上（仅 N-5.1 未被抽中），无节点聚集假阴性风险。
- **口径声明（诚实保留）**：任务书要求「独立重判报一致率」，语义级盲重判需 fresh-context subagent——ralph-loop-runner 工具纪律禁止开 subagent，本轮未执行。**交付口径 = 形式一致率**（evidence 锚点有效率 100%），语义一致率标 unverified。注意 S1 只能证明「h=1 有文本依据」，不能证明「h=0 判对了」（漏判方向无法用逐字核验覆盖）——这是该口径的固有边界。

### F3 · p̃ 分布合理性 — 发现系统性偏差信号

**F3a 方向性相关（S2，n=30 排除 N-0，Spearman 含并列秩平均）**：

| 口径 | ρ(p̃, hr) | 判读 |
|------|-----------|------|
| orig judge | **0.456** | < 0.5 阈值 → LOW-CORR 信号触发：orig p̃ 与 8run 经验命中率相关弱，存在系统性偏差 |
| new judge (blindtest) | 0.629 | 过线——新 judge 的 p̃ 与经验命中率单调性更好 |
| cross-judge ρ(p̃_orig, p̃_new) | 0.688 | 方向稳定但远非一致 |

**F3b 二项式红旗（S3，基于 orig p̃，α=0.05）**：

| node | 观测 | p̃_orig | 统计量 | 矛盾表述 |
|------|------|---------|--------|----------|
| N-1 | 0/8 零命中 | 0.45 | P(全miss)=(0.55)⁸=0.0084 | 先验认为近半概率出现，却 8 次全 miss——先验偏高或 run 系统性漏判 |
| N-1.1 | 8/8 全命中 | 0.35 | P(全hit)=0.35⁸=0.000225 | 先验认为偏低概率，却 8 次全 hit——先验偏低 |
| N-5.3 | 8/8 全命中 | 0.05 | P(全hit)=0.05⁸=5e-11 | 同上，幅度极端 |

**F3c 跨 judge 漂移（S4，|Δw2| top-3）**：N-2.1（Δ4.91）、N-1.3.1（Δ4.32）、N-3.2.2（Δ3.74）——三个节点的 w2 因换 judge 而近乎翻倍/腰斩，且其中两个（N-2.1/N-3.2.2）是 gold 标记节点。→ 已移交 G2 做根因解剖（G2 结论：双源 p̃ 偏差，见 g2-rootcause.md）。

### F4 · 矛盾清单汇总（四类，实例与 evidence 详见交付物 G1-contradiction-audit.md）

- **C1 弱相关型**：ρ_orig=0.456 < 0.5（S2 输出行 + 可复算脚本）。
- **C2 二项式红旗型**：N-1 / N-1.1 / N-5.3 三节点（S3 输出行）。
- **C3 零命中高 p̃ 型**：hr=0 且 p̃_orig≥0.2 共 3 节点——N-1(0.45)/N-1.3.2(0.20)/N-2(0.25)；若放宽到 p̃_new≥0.25 则 6 节点（+N-1.1.2(0.3)/N-1.3.1(0.3)/N-2.1(0.3)/N-3.1.1(0.5)，后四个是 new judge 抬升的，属 G2 保守下界效应范畴）。
- **C4 构念效度依赖型**：同一 hit-matrix + 同一 W3 公式，仅换 p̃ 来源，global top-5 gold 计数 3/5（orig）→ 1/5（new）翻转。top-5 集合 diff：orig {N-3.2.2, N-3.2.4, N-2.1, N-2, N-1.1.3} → new {N-4, N-1.1.3, N-5, N-3.2.4, N-1}，进出 3 席。

## 暂定结论（供 02.5 对抗核验）

1. **数据层自洽**（F1：24/24 精确复算 + 248/248 结构断言）——矛盾不在计算层。
2. **形式一致率 100%（35/35 抽检 h=1 cell）**，但这是降级口径；语义级独立重判未执行（工具纪律），标 unverified。
3. **p̃ 存在系统性偏差信号**：orig judge ρ=0.456 弱相关 + 3 个二项式红旗节点；偏差方向双向（既有高估 N-1 也有低估 N-1.1/N-5.3），不是单向校准问题。
4. **最高形态矛盾是 C4**：W3 判据结论对 p̃ 来源敏感（3/5↔1/5 翻转）——这不是「谁的数据错了」，而是判据本身的问题，移交 G2/G6。

## 仍未解决

- 语义级独立重判（空缺 G1）：需 subagent 通道，登记降级。
- C3 六节点的 rationale 细读（空缺 G2）：本 goal 只列清单，定论移交人工/G2（G2 已部分消费）。
- 外网文献（p̃ 偏差类型的命名与先例）：web-llm 三 provider 失效，标 unverified，不阻塞。