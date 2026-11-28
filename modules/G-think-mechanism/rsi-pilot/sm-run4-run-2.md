# pfb 主线状态核验 (核 11-27 21:50 快照 vs 11-28 15:41 一手事实)
# origin: ai · 核验源: data/q9-budget-scan/ + /tmp/q9-budget-scan-queue.log + ps/lsof

## ① 当前状态 (逐条 claim → 判定 + 一手证据)
| 参考文件 claim | 判定 | 一手证据 |
|---|---|---|
| ④ "Q9 扫描 8/15 runs 落地 (50/100/150 各3+300-r1)" | 不符 | data/ 有 q9-300-r2-20261127-225528.json + q9-300-r3-20261128-135044.json → 实为 10/15 落地, 719-r1 在跑 |
| ④ "resume 脚本已备未起" | 不符 | queue.log: QUEUE-V2 started 11-28 13:50:44, 300-r3 rc=0 wall_s=2080 → resume 已执行 |
| 进程 "K2(run_s1_sm)+K3(run_k3_hw3) 21:44/46 起在跑" | 不符 | ps 无 run_s1_sm.py / run_k3_hw3.py → 两者已死/结束 (距快照已 ~18h) |
| 进程 "q9 队列已死(pid 3651 消失)→ 主线当前无进程推进" | 不符 | ps: pid 31825 s5_state_machine.py --qid q9-agi --max-nodes 719 (2:25PM 起)+pid 20729 queue_v2.sh; 719-r1.stdout mtime 15:41:31 实时写 → 主线正在推进 |
| 进程 "vLLM 8787 在跑(有活跃 curl)" | 已核 | lsof: 8787 LISTEN(node 99411); curl 56427 POST 127.0.0.1:8787/v1/chat/completions |
| ④ "analysis.json 300/719 档=null, 主端点 gate 全 null" | 已核 | analysis.json(mtime 11-27 14:29) 300/719 仍 null, 未随新 run 重算 |
| 进程 "无 subagent 在推进五子项" | 无法证伪 | ps 见 agent-teams core 队(method/logic/reviewer, qwen3.8-27b-mtp), 非五子项归属, 不判 |

## ② 最短路径 3 步 (到可发表里程碑)
1. 等 719-r1 落盘 (~1-2h, 别 kill) → 补 719-r2/r3 (先修 ModuleNotFoundError:'prompts', 11-27 22:19 曾 rc=1) → Q9 扫描 15/15 齐。
2. 重跑 analyze_q9e_scan.py 补 300/719 档 gate 矩阵 → 出主端点 (gate 命中率首次 100% 的最小预算) + threshold_diag 全档 verdict。
3. 报 D 裁 D1 排序键 (A 惩罚项 vs B 纯 post_acc) → 裁完 gold 冻结, ⑤ 收口 → 五子项全绿, 可发表。

METRIC: 4
