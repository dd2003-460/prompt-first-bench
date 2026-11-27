# GPU 主线 (research-agi-budget) 状态快照 2026-11-27 21:50

# origin: ai · 来源: decomposition-research-agi-budget.md 对账 + 磁盘核验 + ps/git log

## 五子项完成度
| 子项 | % | 状态/卡点 |
|---|---|---|
| ① matched 批+记账 | 100% | ✅ 11-22 收口 (30/30, stats commit 848996a30, nat Δ+0.131 p=.016 / gpu Δ+0.105 p=.022) |
| ② prompt 去污染 | 100% | ✅ 11-22 (64f714dbc, 9 领域旧词清零) + 11-27 S1 剥离版 (76d964360+801167fb6, 非注释域味=0) |
| ③ merge 消融 | 100% | ✅ 11-22 (Δ=-0.0132, A≈B, merge 非瓶颈) |
| ④ 预算控制实验 | ~75% | 设计✅ + GPU/Q6/Q7 域收口✅ (拐点~300) + E-SYNTH✅ (7b1dd89a8, 推荐工作点 budget=300)。**卡点: Q9-AGI 域扫描 8/15 runs 落地 (50/100/150 各3 + 300-r1), 原队列 14:47 死 (macOS 休眠), resume 脚本已备未起 (300-r2/3+719×3 共 5 runs ~4h); analysis.json 300/719 档=null, 主端点 gate 命中率全 null, 未提交 (M)** |
| ⑤ AGI 题面+gold | ~85% | 题面✅ (q9-agi-question-v0.md, D 三默认立场 11-27 冻结: 预算150/5因子/post_acc) + gold A (29叶) & B 交叉验证✅ + AB 对照✅ (16:50, 7 项口径独立收敛) + rubric units✅ (37 units)。**卡点: D1 排序键公式待 D 一句话裁 (A: post_acc×(150/n_realized) 惩罚项 vs B: 纯 post_acc; 题面字面支持 B, 建议 A 惩罚项降级为诊断指标); 裁完即冻结, B 的 D4 三点 (库维护盈亏/节点成本异质/吞吐锚) 并入 A** |

## 在跑的进程 (ps 核验)
- vLLM 8787 在跑 (qwen3.8-27b-mtp, 有活跃 curl 调用)
- oood-probe K2 (run_s1_sm.py, S1 气象) + K3 (run_k3_hw3.py, 硬件域三臂) 21:44/46 起在跑 —— 属子项⑦ OOD 线, 非五子项主线
- **q9 扫描队列已死** (pid 3651 消失, 无 300-r2 起 log 行) → 主线当前无进程推进
- 无 subagent 在推进五子项

## 最便宜下一步 (单步)
`setsid nohup bash experiments/stage-ablation/q9_budget_scan_resume.sh` (5 runs ~4h, 同负载前提注意 K2/K3 并发会拉长墙钟) → 落盘后重跑 `analyze_q9e_scan.py` 补 300/719 档 gate 矩阵, 出 Q9 域主端点 (gate 命中率首次 100% 的最小预算)。并行零成本: 把 D1 排序键裁决 (AB-comparison.md 一节) 报 D 一句话裁定, 裁完 gold 冻结, ⑤ 收口。
