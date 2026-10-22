# Q3 run3 评分 — qwen3.6-plus（V0 裸 prompt，本地降级通道）

> origin: ai
> 评分时间：2026-10-23 06:1x Asia/Shanghai
> 评分人：route B 执行 subagent（**探索性自评**；非正式盲评）
> 评分依据：`rubric/scoring.md` D1–D4（100 分制）
> 评分对象：`q3-run3.md` 答案全文
> 匿名处理：评分时隐藏模型名与通道，仅依据输出内容打分。
> degraded: true（arena 故障，本地通道；执行模型 qwen3.8-27b-w8a16 按档映射 qwen3.6-plus）

## 评分锚点（评分者冻结的 Q3 关键事实清单）

1. 阈值定理核心陈述正确：p < p* 时 concatenated 码可指数压低逻辑错误率；p > p* 时失败。
2. 提出者/年份：Gottesman 1996（博士论文）/1997（发表）给出严格证明；Shor 1995 是最早 concatenated 方案（无严格阈值证明）；Steane 1996 同期。
3. 数值：阈值依赖噪声模型/码族/解码器，非常数；surface code + 现实电路噪声 ≈ 1%（Fowler et al. 2012 标准引用）；独立噪声下可达 ~10%。
4. 来源可验证（arXiv 编号 / 期刊卷页）。

## D1 正确性（40）

| 检查项 | 结果 |
|--------|------|
| 阈值定理陈述（p<p* 指数衰减，p>p* 失败） | ✓ |
| Gottesman 1996 博士论文 / 1997 发表 arXiv:quant-ph/9705052 | ✓ |
| Shor 1995 PRA 52 R2493, arXiv:quant-ph/9505026 | ✓ |
| Steane 1996 PRA 52 2697, arXiv:quant-ph/9601021 | ✓ |
| Fowler et al. 2012 PRA 86 032324, arXiv:1202.0928, 阈值 ≈1% | ✓ |
| 阈值依赖噪声模型/码族/解码器 | ✓ |
| 关键事实错误数 | 0 |
| 无来源关键 claim 数 | 0 |

**D1 = 40/40**

## D2 完备性（25）

| 要点 | 覆盖 |
|------|------|
| 定理陈述 | ✓ |
| Gottesman 1996/1997 | ✓ |
| Shor 1995 | ✓ |
| Steane 1996 | ✓ |
| surface code 1%（Fowler 2012） | ✓ |
| 独立噪声 ~10% | ✓ |
| 阈值依赖性讨论 | ✓ |
| Bravyi-Kitaev 独立噪声分析 | ✓ |
| 未覆盖：Aliferis-Gottesman-Preskill (AGP) 1999 通用噪声严格阈值证明（arXiv:quant-ph/9811069，1999 年 "Quantum accuracy threshold for fault-tolerant quantum computation"，这是**通用非独立噪声下严格阈值存在性证明**，比 Gottesman 稳定子框架更一般） | ✗ 漏 1 个里程碑（-5） |

**D2 = 20/25**（-5：漏 AGP 1999）

## D3 结构正交（20）

- 三节（定理陈述 → 数值/提出者/年份表 → 来源 → 依赖性注意）无重叠；
- 表格与来源列表各司其职；
- 「注意」节独立处理数值依赖性，与正文不冲突；
- 无冗余。

**D3 = 19/20**（-1：Shor 1995 行说「虽未给严格阈值证明」与后文依赖节略有信息重叠，轻微）

## D4 置信度标注（15）

- 来源覆盖：全部关键 claim 有 arXiv/期刊完整引用 ✓（5 条来源）
- conf 标注：无 ✗（V0 不要求 conf；按 rubric 字面来源 100% / conf 0% → 折半）

**D4 = 7.5/15**

## 总分

| 维度 | 得分 |
|------|------|
| D1 | 40 |
| D2 | 20 |
| D3 | 19 |
| D4 | 7.5 |
| **总分** | **86.5** |

## 判定

**86.5 ≥ 80 → success**

## 备注

- 探索性自评，非正式盲评。
- 与 round1-v0 q3-run1（同模型同档，arena 通道）对比需在报告层做，本文件不直接引用未读文件的具体分数。
- 降级说明同 q2-run3：本地模型 qwen3.8-27b-w8a16 与 arena 上 qwen3.6-plus 可能有版本差异，横向对比需注意。
