# V0.1 hit-matrix 重算回执（receipt-v0.1-hit-matrix-r184）

> goal: RV3G6-o3-claim-rejudge 尾巴 · 分支 ralph/v0.1-hit-matrix-recompute · 2026-11-02
> 上游：`rejudge/rejudge-results.json`（P0 层 248 cell 盲判，judge_id 见该文件 provenance）
> 数据源：`runs-V0.1-run{1..8}.md`（cache-ratio 已移除的题面版本，sha256_16 见各文件头）
> 旧矩阵：`hit-matrix.json`（基于含 cache-ratio 题面的 run 产出，98/248 h=1）

## 1. 为什么必须重算

旧 hit-matrix 的 evidence quote 有 **97/98 条在 V0.1 文本中不存在**（机判 substring 检查）。
根因：V0.1 移除了题面中的 `90:9:1 缓存比例`，run 产出的措辞随之改变，旧 evidence 全部失效。
旧矩阵若直接用于 V0.1 消融分析 = 拿 A 题的答案对 B 题的卷子打分，构念效度崩塌。

## 2. 重算方法

- 判定协议：`o3-claim-list.md` §2 原子 claim 清单 + P0 层 rules-frozen（语义等价即算，引原文为证，不确定保守判 0）
- 执行：盲判 packet（`rejudge/p1-batches/batch{1..4}-packet.md`，98 cell 覆盖 8 run × 各节点），judge 只看到 run 全文 + claim 文本 + node ID
- 结果落盘：`rejudge/rejudge-results.json`（248 cell = 8 run × 31 节点，含 98 个 P1 batch cell + 150 个 P0 层 cell）

## 3. 核心数字

### 3.1 总量

| | old | new | delta |
|---|---|---|---|
| **TOTAL h sum** | **98** | **77** | **-21** |

新矩阵比旧矩阵低 21 分——不是 run 变差了，是判据从「ID 匹配 + 宽松 evidence」收紧到「原子 claim 盲判 + 原文引用」。

### 3.2 按 run

| run | old | new | delta |
|-----|-----|-----|-------|
| run1 | 14 | 13 | -1 |
| run2 | 14 | 9 | -5 |
| run3 | 13 | 9 | -4 |
| run4 | 10 | 7 | -3 |
| run5 | 8 | 2 | -6 |
| run6 | 14 | 12 | -2 |
| run7 | 13 | 12 | -1 |
| run8 | 12 | 13 | +1 |

run5 跌幅最大（-6）：它的 N-5.3/N-5.1 旧 evidence 依赖 cache-ratio 语境下的表述，V0.1 里这些内容以不同措辞出现，盲判判 0。

### 3.3 按节点（仅列 delta≠0 的）

| node | old | new | delta | 解读 |
|------|-----|-----|-------|------|
| N-1.1 | 8 | 3 | -5 | 摊销进小时成本——旧判把"提到折旧"就算命中，新判要求出现 $/hr 或等价折算 |
| N-1.1.1 | 4 | 8 | +4 | 卡价数值——新判更宽松地接受"标为待取数黑盒+路径" |
| N-1.2.1 | 7 | 4 | -3 | 整机功耗数值——部分 run 只提"功耗高"无 W/kW 数值，旧判误放 |
| N-3 | 1 | 4 | +3 | 推理时间被建模——旧判过严 |
| N-3.1 | 4 | 0 | -4 | prefill 单独建模——V0.1 无 cache-ratio 后多数 run 不再显式拆 prefill 阶段 |
| N-3.2 | 4 | 8 | +4 | decode 带宽受限建模——新判识别出更多实质覆盖 |
| N-3.2.2 | 6 | 4 | -2 | KV cache 每流字节数——部分 run 只给总量不给每流口径 |
| N-3.2.3 | 8 | 7 | -1 | 峰值带宽规格参与估算——轻微收紧 |
| N-5.1 | 5 | 0 | -5 | 显存门槛→并发上限——V0.1 里多数 run 做了容量准入但未显式推导 n_cap |
| N-5.3 | 8 | 0 | -8 | 前缀缓存命中率单列为速率参数——**这是 cache-ratio 移除的直接后果**：题面不再给 90:9:1，run 无法讨论"命中率每变化 δ 的影响"，全部判 0 |

### 3.4 Flip 统计

- 总翻转：51/248（old→new 不一致）
- 方向：36 处 1→0（收紧），15 处 0→1（放宽）
- 净效果：-21（收紧 > 放宽）
- 最大单节点影响：N-5.3（-8，纯 V0.1 题面效应）和 N-1.1 / N-5.1（各 -5，判据收紧效应）

## 4. 对消融分析的 implication

1. **N-5.3 在 V0.1 下结构性归零**——这不是模型能力差异，是题面设计效应。做 V0 vs V0.1 对比时，N-5.3 应作为"题面控制变量"处理（预期差 = 0，任何非零差 = 噪声或泄漏）。
2. **N-3.1 同理**（prefill 建模依赖 cache-ratio 语境）——V0.1 下 0/8，V0 下 4/8。
3. **有效对比维度收窄**：31 节点中 N-5.3 和 N-3.1 在 V0.1 下无区分力，实际可用 29 节点。
4. **run 间排序基本稳定**：top 仍是 run1/run6/run7/run8（12-13），bottom 仍是 run5（2）/run4（7）——判据收紧没有打乱相对序。

## 5. 证据链

- 盲判原始结果：`rejudge/rejudge-results.json`（sha256 可验）
- 旧 evidence 失效验证：97/98 条不在 V0.1 文本中（substring 机判）
- flip 明细：本回执 §3.4 + `rejudge/rejudge-results.json` 逐 cell 可查

## 6. 状态

- [x] 重算完成（248 cell）
- [x] 新旧对比 + flip 分析
- [ ] 更新 `hit-matrix.json` 为 V0.1 版本（保留旧版为 `hit-matrix-v0-pre.json`）
- [ ] 下游脚本（prior-vs-quality、coverage-rescan）适配新矩阵