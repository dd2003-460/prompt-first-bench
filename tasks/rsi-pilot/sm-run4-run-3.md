# sm-run4-run-3 · pfb 主线状态核验 + 可发表最短路径 (2026-11-28 15:41 核)
# origin: ai · 核对手: gpu-mainline-status-20261127.md (11-27 21:50 快照) · 一手: ps + /tmp/q9-budget-scan-queue.log + data/q9-budget-scan/ + analysis.json

## ① 缺口登记
- 719-r1 落盘时刻: 反驳不了(719 档 3 个 run 各~4h, 串行~12h, 11-28 15:41 仍在跑) → 定案证据=719-r1/2/3 的 json 落盘 + queue.log 出现 rc=0 行。
- 300-r3 json(11-28 14:25)是否有效完整: 未验证(仅看 size/mtime, 未解析) → 定案=analyze_q9e_scan.py 重跑后 300 档 n_runs=3。

## ② 当前状态(claim 逐条核)
1. vLLM 8787 在跑 — **不符**: `ps -p 8787` 空; 但 719-r1 15:41 仍有 LLM 调用(2.5-2.9s), 另有 vLLM 实例在服(端口未知)。
2. K2(run_s1_sm)+K3(run_k3_hw3) 在跑 — **不符**: ps 无 run_s1_sm/run_k3_hw3 进程, 均已停。
3. q9 队列已死(pid 3651 消失) → 主线无进程推进 — **不符**: pid 20729(q9_budget_scan_queue_v2.sh)活着 + 31825(s5_state_machine q9-agi 719)15:41 活跃, 719-r1 在跑。
4. Q9 扫描 8/15 runs 落地 — **不符**: 磁盘 12/15 json 落地(50×3/100×3/150×3/300×3); 719-r1 在跑, r2/r3 未起。
5. resume 脚本已备未起 — **不符**: log 显示 11-27 22:19/22:21/22:51/22:55 已多次起, 11-28 00:42/00:47/13:50 QUEUE-V2 续跑, 300-r2/r3 已落盘。
6. analysis.json 300/719 档=null — 已核(11-27 14:29 未重跑, 300/719 仍 null, 此半句真); 但同句"主端点 gate 命中率全 null"— **不符**: gate_hit_rate_by_budget 50/100/150=0.0 非 null(仅 300/719 null, N-1.1.1.1@100=0.667), "全 null"与一手 json 矛盾。
7. ①②③ 子项 100%(11-22 收口) — 未复核(11-22 历史 commit, 本轮只核 ④⑤ 相关一手)。
8. ⑤ 卡点=D1 排序键待 D 裁 — 未复核(D 是否已裁, 本地无一手证据)。

## ③ 最短路径(3 步)
1. 等 719-r1/2/3 跑完(queue v2 已在跑, 串行~12h; 勿再起脚本, 719 完成后 queue 自行收口) → 落盘后重跑 analyze_q9e_scan.py 补 300/719 档 gate 矩阵 → 出 Q9 主端点(first_100pct_budget)。
2. 并行: D1 排序键裁决报 D 一句话裁(A 惩罚项 vs B 纯 post_acc) → 裁完 gold 冻结, ⑤ 收口。
3. ④+⑤ 齐 → 可发表里程碑: Q9 域全档端点(含 719 顶档) + gold A/B 冻结 + 37-unit rubric。
注: 参考文件"最便宜下一步=起 resume 脚本"已失效(队列在跑); 当前瓶颈=等 719 档, 非重启。

METRIC: 6
