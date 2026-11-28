# sm-run4 run-4: pfb 主线状态核验 + 到可发表最短路径（2026-11-28 15:47 一手核验）

## ① 当前状态（逐条对照参考文件 gpu-mainline-status-20261127.md，21:50 快照）

| 参考文件 claim | 判定 | 一手证据 |
|---|---|---|
| ① matched 批 100%（30/30, commit 848996a30） | 已核 | git cat-file -t 848996a30=commit |
| ② prompt 去污染 100%（64f714dbc / 76d964360+801167fb6） | 已核 | 三 commit 均存在 |
| ③ merge 消融 100%（Δ=-0.0132） | 已核 | git log d756647f0「确实已完成 11-22 07:08」 |
| ④ 8/15 runs 落地（50/100/150 各3+300-r1） | **不符** | 实际 12/15 落地：300-r2(23:48)+300-r3(14:25) 新增，各 300 节点、sha 各异非伪产物；719-r1 在跑（pid 31825，14:25 起，1861 次 LLM call，stdout 15:49 活跃） |
| 「resume 脚本已备未起」 | **不符** | 队列日志：RESUME 22:19/22:55 + QUEUE-V2 00:42/00:47/13:50 多次已起，300-r2 rc=0 落盘 |
| 「主线当前无进程推进」 | **不符** | ps：queue v2 pid 20729（13:50 起）+ 719-r1 pid 31825 均在跑 |
| 「K2(run_s1_sm)+K3(run_k3_hw3) 21:44/46 起在跑」 | **不符** | ps 无任何 run_s1_sm/run_k3_hw3 进程，OOD 线已停 |
| 「analysis.json 300/719 档=null，主端点全 null」 | 已核（仍真） | analysis.json 现值：300/719=null，first_100pct_budget=null；但内容停在 11-27 12:14（fc64654ea），未反映 300-r2/r3 落盘 |
| 「analysis.json 未提交 (M)」 | **不符** | git status：analysis.json 已跟踪已提交，当前仅 q9-719-r1.stdout 为 M |
| ⑤ D1 排序键待 D 一句话裁 | 已核 | AB-comparison.md 仍「待 D 裁 D1 即冻结」，建议=B 纯 post_acc+A 惩罚项降诊断指标 |
| vLLM 8787 在跑 | 已核 | lsof: 127.0.0.1:8787 LISTEN（node proxy.mjs）；719-r1 LLM call 1-3s 正常返回 |

另：quarantine-20261127/ 有 11-27 16:11 kill 伪产物 7 件（sha 铁证=300-r1 拷贝），已隔离未删，不影响现 12 件。

## ② 到可发表里程碑最短路径（3 步）

1. **补齐 719 档**：719-r1 已在跑（~1h 量级，盯 ckpts/719-r1 落盘）；719-r2/r3 死因=resume wrapper 跑错 cwd（`No module named 'prompts'`），从 experiments/stage-ablation/ 目录重起即可，3 runs ~4h。→ 15/15 runs 齐。
2. **重跑 analyze_q9e_scan.py**：补 300/719 档 gate 矩阵，出 Q9 域主端点（gate 命中率首次 100% 的最小预算；现 50/100/150 档命中率 0.0，主端点大概率指向 300/719）+ commit analysis.json。→ ④ 收口。
3. **D1 一句话裁决**（B 纯 post_acc，A 惩罚项降诊断指标——AB-comparison.md 已有建议）→ gold 冻结、⑤ 收口 → 五子项全绿，可发表材料齐。

METRIC: 5
