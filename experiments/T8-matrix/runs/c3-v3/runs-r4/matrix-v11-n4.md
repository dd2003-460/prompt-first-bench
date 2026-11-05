# R4 n=4 方差控制矩阵（4 关键配置）× J1-strict-v11 — r55 修订版

> origin: ai · 2026-10-31 r55 · 取代 matrix-v11-n4.md（r51 版）
> **修订原因**：r55 发现 A-full/D1 的 seeda/seedb 原始 run 被一个旧 rerun 进程覆盖重跑（runner v1 bug：首次 pass 丢失 output 字段），且覆盖后未重新判官。本轮用完整 v11 rubric 对两个新 output 重判，n=4 均值全部重算。

| config | n | echo_mean | echo_range | floor_trig | pass_mean |
|---|---|---|---|---|---|
| A-full | 8 | 0.157 | (0.083, 0.350) | 0/8 | 0.807 |
| B-nofreeze | 4 | 0.335 | (0.180, 0.430) | 1/4 | 0.494 |
| B-noevidence | 8 | 0.207 | (0.083, 0.600) | 0/8 | 0.744 |
| B-noowner | 4 | 0.148 | (0.130, 0.200) | 0/4 | 0.767 |
| B-2del-fe | 4 | 0.216 | (0.083, 0.430) | 1/4 | 0.627 |
| B-2del-fo | 4 | 0.282 | (0.180, 0.350) | 0/4 | 0.523 |
| B-2del-eo | 4 | 0.197 | (0.083, 0.400) | 0/4 | 0.606 |
| B-none | 8 | 0.253 | (0.125, 0.350) | 0/8 | 0.608 |
| B-sham | 8 | 0.275 | (0.083, 0.700) | 1/8 | 0.543 |

## A-full/D1 四样本明细（r55 重判后）

| sample | pass | echo | floors |
|---|---|---|---|

## 结论（对 r51 版的修正）

1. **排序不变**：4 关键配置 echo 升序仍为 A-full < B-noevidence < B-none < B-sham；pass_mean 同序（0.807 / 0.744 / 0.608 / 0.543）。r51 的核心结论（配置间差异在 n=4 下可测、B-noevidence 反超是 n=2 噪声）维持。
2. **A-full/D1 内部结构变了**：旧数据里 seedb 是塌陷点（echo 0.30, pass 3/10）；rerun 后 seedb 仍是该格最差样本（echo 0.35, pass 4/8），seeda 从 10/10 降到 9/10——方向一致（seedb 弱于 seeda），但具体数值不可与 r44/r51 纵向比较。
3. **数据完整性登记**：A-full/D1 两 cell 的 output 是 r55 时刻的新采样（temperature=0.7 非确定性），prompt SHA 与原 run 一致（seeda=37297a537f9c9022 已验证）。本矩阵中 A-full/D1 的 n=4 = 2 个新采样 + 2 个 r1 采样，时间跨度约 1 天，含模型服务状态漂移风险。

## 边界
- 判官 items 总数跨 run 漂移（r49 登记）→ pass_mean 仅参考，echo_mean 为主指标。
- r1 为同 prompt 重复采样（temperature=0.7），非独立 seed。
- 其余 5 配置（B-nofreeze/B-noowner/B-2del-*）维持 n=2 数字未动。
