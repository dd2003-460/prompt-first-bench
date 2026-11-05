# 阶段 01：目标分解 — RUBRIC-V3-FULL-AUDIT / G1 矛盾审计

> goal: rubric-v3-audit-g1 · 分支 ralph/rubric-v3-audit-g1 · 2026-10-30
> 上游任务书: tasks/RUBRIC-V3-FULL-AUDIT-task-brief.md（队首大 goal，G1-G6 串联）
> 前置: 无（G1 是链首）。注：机判脚本 assert-g1-audit.py 与样本清单 g1-sample-cells.json 已在 r108 随 G2 收口入库并跑通（exit 0），本 goal 补齐 loop 工件 + 矛盾清单交付物；G2 已消费本 goal 的 S2/S3/S4 信号做根因解剖。

## 因素分解

任务书 G1 = 「hit-matrix 8run×31node 全量重判抽检（随机 30% 节点独立重判，报一致率）+ prior-estimates 的 p̃ 分布合理性检查（有没有系统性偏高/偏低）+ 输出矛盾清单（每条带 evidence 引用）」，拆成四个正交因素：

### F1 · hit-matrix 结构完整性与 O3 分数可复算性
- 已知条件：hit-matrix.json 为 8 run × 31 node 矩阵，每 cell 含 h∈{0,1} 与 evidence（h=1 非空 / h=0 为 null 的政策）；stats-recomputed.json 有 W0/W1/W2 × 8run 落盘分。
- 待验证：(a) 矩阵结构零破损（run/node 集合、h 值域、evidence 政策）；(b) 用 hit-matrix + prior-estimates 按 `O3 = Σw·h/Σw` 复算 24 个分数是否与落盘值精确一致（容差 5e-5）。
- 研究路径：机判脚本 A1/A2 断言。
- 判定标准：24/24 精确一致 → 数据层自洽，矛盾只能来自「标注 vs 原文」或「p̃ vs 经验」两层，不能来自计算层。

### F2 · 抽检协议设计与一致率口径（任务书核心要求）
- 已知条件：248 个 cell（8×31），任务书要求「随机 30% 节点独立重判，报一致率」。
- 待验证 / 设计决策：
  - F2a 抽样确定性：固定种子（20261030）抽 75/248 ≈ 30%，样本清单落盘 g1-sample-cells.json，任何人重跑得到逐位相同样本（A4 断言）。
  - F2b 一致率的可行口径：**语义级独立重判**（fresh-context judge 盲读 run 原文重判 h）需要 subagent 通道——ralph-loop-runner 工具纪律禁止开 subagent，本轮不可执行。**降级口径**：对抽检内全部 h=1 cell 做 evidence 逐字核验（S1：evidence 空白归一后必须逐字出现在对应 run 原文中）→ 交付「形式一致率」（evidence 锚点有效率），语义重判标 unverified 并登记降级理由。
  - F2c 覆盖度：75 cell 落在多少个不同节点上（防抽检只覆盖少数节点造成假阴性）。
- 判定标准：S1 全过 → 抽检范围内 h=1 判定全部有文本锚点；覆盖率 ≥ 25/31 节点视为足够分散。

### F3 · p̃ 分布合理性检查（系统性偏高/偏低）
- 已知条件：prior-estimates.json 有 orig judge 的 31 节点 p̃（N-0 为 null）；judge-blindtest-r1.json 有独立 judge 的 p̃；8run 经验命中率 hr = Σh/8 可从 hit-matrix 直接算出。
- 待验证：
  - F3a 方向性相关：p̃ 与 hr 的 Spearman ρ（排除 N-0，n=30）。若 ρ 低 → p̃ 不是命中率的单调函数，存在系统性偏差（S2 信号，阈值 ρ<0.5 触发 LOW-CORR）。
  - F3b 二项式红旗：零命中但 P(全miss|p)= (1-p)⁸ < 0.05，或全命中但 P(全hit|p)= p⁸ < 0.05 的节点——先验与 8 次观测在统计上不自洽（S3 信号）。
  - F3c 跨 judge 漂移：双 judge w2 差距 top-3（S4 信号，供 G2 消费）。
- 判定标准：给出每个信号的数值 + 受影响节点清单，作为矛盾清单 C 类条目的证据源。

### F4 · 矛盾清单分类学（交付物结构）
- 已知条件：任务书要求「输出矛盾清单（每条带 evidence 引用）」。
- 设计：四类矛盾，每类给判定规则 + 实例 + evidence（JSON path / file:line）：
  - **C1 弱相关型**：p̃ 与经验命中率整体不相关（F3a 触发时成立）。
  - **C2 二项式红旗型**：单节点先验与 8 次观测统计不自洽（F3b 触发时成立）。
  - **C3 零命中高 p̃ 型**：hr=0 且 p̃≥0.2 的节点——「从未出现」却给了不低的先验，gold 标注争议候选（需人工细读 rationale 才能定论，本 goal 只列清单）。
  - **C4 构念效度依赖型**：W3 的 top-5 gold 计数随 judge 变化（orig 3/5 → new 1/5）——同一公式、同一 hit-matrix，仅换 p̃ 来源结论翻转。这是「矛盾」的最高形态：不是数据错，是判据对输入敏感。
- 判定标准：每类至少一条实例 + evidence 引用；无法定论的条目显式标「待人工」而非硬判。

## 空缺清单

| # | 空缺 | 类型 | 影响 |
|---|------|------|------|
| G1 | 语义级独立重判（subagent 盲重判 75 cell） | 工具纪律阻塞（禁 subagent） | F2 一致率只能交付形式口径（S1 evidence 逐字核验），语义一致率标 unverified |
| G2 | C3 清单节点的 rationale 细读（判断零命中高 p̃ 是标注争议还是合理保守） | 仍需人工 | 本 goal 只列清单不定论；G2 已部分消费（保守下界效应） |
| G3 | 第三 judge 数据（R5.2-third-scorer 未完成） | 外部阻塞 | F3c 只有双 judge；三 judge 一致性留给后续 |

## 阶段 02 研究入口

- 仓库内材料完全够用：F1/F2/F3 全部可由 JSON + runs-C0-run*.md 复算（脚本已就绪）；F4 由 F1-F3 信号汇总。
- web-llm 强制步骤预期三 provider 仍失效（上次回执 error）→ 记录失败回执后继续，不阻塞。

## 判定

分解完成：四个叶子因素（F1 数据自洽 / F2 抽检协议 / F3 p̃ 分布 / F4 矛盾分类）覆盖任务书 G1 的全部三项要求；空缺 G1-G3 均已登记且有处置路径（降级/移交/外部阻塞）。→ 进入 02。