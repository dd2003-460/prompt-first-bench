# pfb 主线状态核对 + 到可发表里程碑最短路径（2026-11-28 15:49 核）
# origin: ai · 一手证据: modules/B-pipeline-ablation/data/q9-budget-scan/ + /tmp/q9-budget-scan-queue.log + ps/kill-0
# 参考文件: tasks/stage-ablation/gpu-mainline-status-20261127.md（21:50 快照, 已过时 ~18h）

## ① 当前状态（每条 已核/不符 + 一手证据）
1. [不符] "Q9 扫描 8/15 runs 落地(…300-r1)" → 现 11/15: 50/100/150 各3 + 300 全3。证据: ls q9-300-*.json = 3 个(r1 14:47 / r2 22:55 / r3 11-28 13:50 落盘)。
2. [不符] "resume 脚本已备未起" → 已多次起跑: log 见 RESUME started 22:19/22:21/22:51/22:55 + QUEUE-V2 started 00:42/00:47/13:50。证据: /tmp/q9-budget-scan-queue.log 末段。
3. [不符] "q9 队列已死 / 主线当前无进程推进" → 有活进程: PID 20729 q9_budget_scan_queue_v2.sh + PID 31825 s5_state_machine.py(--max-nodes 719) 均 kill-0 ALIVE; q9-719-r1.stdout mtime=15:49:31(=now, 4220 行, 正在跑)。
4. [已核] "vLLM 后端在跑" → 8787 端口有 LISTEN(proxy.mjs), 719-r1 持续 LLM call done(缓存命中), 后端存活。
5. [已核] "analysis.json 300/719 档=null, 主端点 null" → 仍 null; 该 json mtime=14:29, 在 150-r3/300/719 落盘前生成, n_runs_per_budget 300:0/719:0/150:2 已偏旧, 需重跑刷新。
6. [新增·参考未预见] 719-r2/r3 已失败: q9-719-r2/r3.stdout = ModuleNotFoundError: No module named 'prompts'(队列脚本 cwd 不对; r1 从 stage-ablation 目录起故正常)。719 档实际 0/3 落地。

## ② 到可发表里程碑最短路径（3 步）
可发表里程碑 = Q9-AGI 域主端点(gate 命中率首次 100% 的最小预算) + ⑤ gold 冻结。
S1 修 719-r2/r3 启动环境(正确 cwd/PYTHONPATH 使 `import prompts` 可解析)+ 与 r1 并发跑完 → 719 档 3/3 落地(瓶颈: r1 已跑 ~1.5h, 719 节点预计还需数小时)。
S2 719 全落盘后重跑 modules/B-pipeline-ablation/analyze_q9e_scan.py → 补 300/719 gate 矩阵 + 出主端点 first_100pct_budget。
S3 并行零成本: 报 D 一句话裁 D1 排序键(A=post_acc×(150/n_realized) 惩罚项 vs B=纯 post_acc; 题面字面支持 B)→ 裁完 gold 冻结, ⑤ 收口 → 5 子项全绿, 可发表。

METRIC: 3
