# sm-run4-run-1: pfb 主线状态核验（对 11-27 21:50 快照逐条核一手事实）
# origin: ai · 2026-11-28 15:43 · 一手源: data/q9-budget-scan/ + /tmp/q9-budget-scan-queue.log + ps + git log

## ① 缺口登记（自驳不掉）
| 陈述 | 为何反驳不了 | 定案证据 |
|---|---|---|
| ① nat Δ+0.131 p=.016 / gpu Δ+0.105 p=.022 | commit 848996a30 仅证 30/30 记账，Δ/p 未从原始 stats 复算 | stats 文件复算 |
| ⑤ AB 对照 7 项口径独立收敛 | 文件存在 (q9-gold-skeleton-AB-comparison.md)，7 项未逐条核 | 对照 gold A/B 逐条核 |

## ② 当前状态（claim → 已核/不符 + 一手证据）
- ① matched 批 30/30, commit 848996a30 — 已核 (git log 11-22 06:55 K1 记账恢复 30/30)
- ② prompt 去污染 64f714dbc/76d964360/801167fb6 — 已核 (三 commit 均存在, message 吻合)
- ③ merge 消融 A≈B — 已核 (e2d13789b: A0.4129≈B0.4261, Δ=-0.0132 吻合)
- ④ "8/15 runs 落地" — 不符: 实际 11/15 完成 (300-r2 11-27 23:48 rc=0, 300-r3 11-28 14:25 rc=0) + 719-r1 在跑 (pid 31825, 257 节点/719)
- ④ "resume 脚本已备未起" — 不符: 队列日志有 4 次 resume 启动 (22:19/22:21/22:51/22:55) + 3 次 queue_v2 (00:42/00:47/13:50)
- ④ "q9 队列已死→主线无进程推进" — 不符: queue_v2 pid 20729 + 719-r1 pid 31825 在跑 (etime 1:15, stdout 更新至 15:41)
- ④ "analysis.json 300/719=null, gate 全 null" — 已核 (analysis.json mtime 11-27 14:29 仍 null, 待 719 完成后重跑)
- ④ "未提交 (M)" — 不符: 300-r2 已提交 (10a8ed9bf 11-28 00:36); 300-r3 现 untracked
- ④ "原队列 14:47 死" — 不符: 300-r1 14:47 启动, 15:27 完成 rc=0 (队列日志), 实际死于 15:27 后
- ⑤ D1 排序键待 D 裁决 — 已核 (11-27 21:50 后无裁决/冻结 commit; 题面/gold A/B/AB-comparison 文件均在)
- vLLM 8787 在跑 — 已核 (lsof 127.0.0.1:8787 LISTEN; /v1/models 返回 qwen3.8-27b-mtp)
- K2 run_s1_sm.py + K3 run_k3_hw3.py "在跑" — 不符: ps 无此二进程; s1-sm-arm.log "S1 arm done: 40 nodes, state=rework"; k3-hw3.log "ALL K3 DONE"; 最新 ckpt mtime 11-27 22:06 (双双已完成)

## ③ 最短路径（3 步）
1. 等 719-r1→r2→r3 由 queue_v2 自动跑完 (r1 已跑 1h15m, 预计 3×~45min-1h) → 重跑 analyze_q9e_scan.py 补 300/719 档 → 出 Q9 主端点 (gate 命中率首次 100% 的最小预算) → commit 数据+分析, ④ 收口
2. D1 排序键裁决报 D 一句话裁定 (建议: A 惩罚项降级为诊断指标, 题面字面支持 B) → gold 冻结, ⑤ 收口
3. 五子项 100% → 组论文素材 (E-SYNTH budget=300 工作点 + Q9 AGI 域 + gold 骨架) → 可发表里程碑
METRIC: 6
