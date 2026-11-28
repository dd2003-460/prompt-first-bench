# sm-run4-run-5: pfb 主线状态核对 + 最短路径（2026-11-28 15:47 一手事实）
# origin: ai · 核对对象: tasks/stage-ablation/gpu-mainline-status-20261127.md（快照 11-27 21:50）

## ① 缺口登记（自驳不掉/不可验证）
| 陈述 | 为何反驳不了 | 定案证据 |
|---|---|---|
| ⑤ rubric 37 units | gold-q9-units.json 是 10 键 dict，37 units 未对上 | 定位定义 37 units 的文件并计数 |
| ⑤ D1 排序键待 D 一句话裁 | 依赖 D 动作，盘上无痕迹 | D 答复或 APPROVALS 台账条目 |
| "无 subagent 在推进五子项" | subagent 未必是 ps 可见进程 | subagent 会话台账/任务回执 |

## ② 当前状态（claim 逐条核）
- ①②③ 完成（30/30 记账/去污染/merge 消融 Δ=-0.0132）：已核 — git log 命中 848996a30、64f714dbc、76d964360+801167fb6、59a8a4128
- ④ "8/15 runs 落地"：不符 — data 目录 12/15（50/100/150/300 各 3 全 rc=0，719 未落）
- ④ "原队列 14:47 死"：已核 — queue log 300-r1 后断档，22:19 起 resume 多次
- ④ "resume 脚本已备未起"：不符 — log 显示 resume×4 + QUEUE-V2×3；719-r1 在跑（pid 31825，14:25:24 起，elapsed 1h24m），queue pid 20729 存活
- ④ "analysis.json 300/719=null、gate 全 null"：已核 — analysis.json（11-27 14:29）300/719 档全 None
- "vLLM 8787 在跑 (qwen3.8-27b-mtp)"：不符 — 8787 是 node proxy（proxy.mjs），真实推理后端是 8788 ninfer serve.py（已跑 12 天）
- "K2/K3 (run_s1_sm/run_k3_hw3) 21:44/46 起在跑"：不符 — ps 均无此进程；ood-probe 最新产物 12:30 t53b 判决（该线已推进过）
- "q9 队列已死 → 主线当前无进程推进"：不符 — queue_v2 + 719-r1 在跑（同上）
- ⑤ 题面冻结/gold AB 对照：部分已核 — q9-agi-question-v0.md、questions/Q9-agi-pure.txt 存在；37 units 见缺口表

## ③ 最短路径（3 步）
1. 零干预等队列跑完：719-r1 进行中（~1.5-2h/run），r2/r3 接棒，setsid 脱离会话，共 ~4-6h → 15/15
2. 重跑 modules/B-pipeline-ablation/analyze_q9e_scan.py 补 300/719 档 gate 矩阵 → Q9 域主端点（gate 命中率 100% 的最小预算）+ commit
3. 报 D 一句话裁 D1 排序键（建议 A 惩罚项降级为诊断指标）→ 裁完冻结 gold，⑤ 收口 → 五子项全闭，论文材料齐（Q9 预算曲线+AGI 题面+gold+rubric）

METRIC: 5
