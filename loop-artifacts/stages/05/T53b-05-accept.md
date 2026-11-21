# T53b 三路消融 — 阶段 05 验收（stage-gate: t53b-ablation）

> origin: ai · 2026-11-21 · 执行通道：CC 总线（tasks/T53-bus/），非标准 loop 通道
> 工件映射：本 goal 的 01-04 等价工件在 tasks/T53-bus/（decomposition.md = 01/03，anomaly-watchlist.md = 02.5 异常台账，verify.md = 04），loop-artifacts/stages/01..04.5 无 T53b 条目属通道差异非缺失。

## 验收标准逐项检查（goal-T53b-verify.md §3，不许抽样）

| # | 标准 | 判定 | 证据 |
|---|---|---|---|
| 1 | 60 run 全完成 + JSON 落盘 | 达标（62/62） | ablation-runs/*.json 62 个；r09 缺口 11-21 13:43 重跑补 |
| 2 | 每 run 有 judge 评分 | 达标 | 62/62 有 coverage+depth（judge_v2_depth） |
| 3 | 统计汇总 mean±SE+95%CI | 达标 | verify.md §消融主口径表（含 t/p） |
| 4 | r7 复现（gpu ≥3 轮 L1 不确定性维度） | 达标（11/13） | verify.md §r7（任务书单关键词口径；初版自构造双关键词误判 FAIL 已修正，commit 7f7d373d9） |
| 5 | SM_SEED=42 固定可复现 | 部分达标 [残留] | 机制生效（driver:59 + SM:32-34）；run 文件无 seed 字段，证据链缺口，E1 补 |
| 6 | 统计量带口径限定 | 达标 | verify.md 头部口径行（per-run / tie-break 无 / qwen3.8-27b×1 non-IRR / webllm 缺席限定） |

## 结论对标（goal-T53b-verify.md §4）

- 消融主假设：formula 臂在 nat（depth p=0.008）/ soc（cov p=0.006）显著优，gpu 无差异（n 不足）→ **成立（部分）**
- r7 方向信号（text 臂 9/10 vs formula 臂 2/10 命中不确定性 L1 维度）与主假设方向相反，n 不足 → 记入 E1 观察项
- 口径限定：webllm 缺席条件下的 S5 消融，不外推到 webllm 可用场景（E2 配对实验补）

## 残留项（不回 03，理由）

1. seed 落盘缺口：重跑 62 run 代价 30h+，证据缺口不影响已出结论的效度（机制已核验生效）
2. r7 方向信号：探索性观察项，非验收判据本身（判据已达标）
3. T2 复现：降级为抽 2 代表轮次各重跑 1 次（~1h），敏感性分析已排除"好轮次是噪声"风险
4. gpu n<8：离群剔除后功效不足，Δ 只作方向参考

## 下一 goal

E1 通用修复实验（decomposition.md 主线：实例折叠 + 冗余检测 + 信息密度度量），观察项含 r7 方向信号 + seed 落盘。
