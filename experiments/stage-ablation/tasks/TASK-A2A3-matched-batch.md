# ⛔ VOID — 勿执行（2026-11-26 13:35 Lead 撤销）
# 本卡基于过期压缩快照误判"A2/A3 未完成"而派生；核验发现二者 11-24 已完成：
#   A2 K1 恢复记账 = commit 848996a30（30/30 主文件, results-sm-matched.json 重建）
#   A3 K2 matched stats = reports/t53b/stats-sm-vs-bare-matched.md（nat Δ+0.131 p=0.016 / gpu Δ+0.105 p=0.022 显著）
# 证据见 decomposition-research-agi-budget.md「批后执行记录」表。已派 sub 已 stop，无脏数据。
# 教训已入 subagent-delegation skill（pre-dispatch 核验缺口）。本卡仅作事故记录保留。

# 任务卡 A2+A3：matched 批恢复记账 + 出 stats

# origin: ai
# 派发: 2026-11-26 · Lead 规划 · sub 纯执行（本地计算，零 LLM，不碰 vLLM）
# 上游: research-agi-budget 分解树 A 分支（experiments/stage-ablation/tasks/decomposition-research-agi-budget.md）
# 背景: A1 监控的批已结束（driver pid 87154 已退出，数据全在 checkpoints/archive/ 的 81 个 sm-* 目录）。
#       driver bug 导致 runs_sm_matched/ 空，数据散在 archive → A2 恢复记账；A3 出 SM vs bare stats。

## 只读这些输入（不读其他，不联网，不碰 vLLM 8787）
1. `experiments/stage-ablation/tasks/decomposition-research-agi-budget.md` — A 分支定义（A2 映射规则 + A3 口径）
2. `experiments/stage-ablation/checkpoints/archive/` — 81 个 sm-{nat,soc,gpu}-* 目录（每个含 runs-s5-sm-{qid}-synth.json，judge 分数已在里面：coverage/depth_score/judge）
3. `experiments/stage-ablation/ablation_stats.py` — 现成统计脚本（spec 驱动，--spec 参数）
4. `experiments/stage-ablation/spec/` — spec 目录（找 matched 批的 spec；没有就按 archive 实际数据建一个）
5. `experiments/stage-ablation/bare_arm_batch_matched.py` — bare 臂 driver（看 bare 数据落盘路径）
6. `experiments/stage-ablation/runs/` — 可能的 bare 数据位置（D1-Q* 命名）

## S1 A2 恢复记账（纯数据操作，零 LLM）
- 按 archive 目录名的时间戳 + qid + round 匹配，把 81 个 sm-* 目录的 synth json 汇聚到 `runs_sm_matched/`（拷贝或 symlink 均可，选不破坏原数据的）。
- 映射表落盘 `runs_sm_matched/MAPPING.md`：archive 目录名 → qid → round → synth json 路径。
- 缺口对账：nat/soc/gpu 各应有 10 轮 matched（nat 10/soc 10/gpu 10），实际 archive 有 nat 21/soc 26/gpu 18 目录（含多轮/重跑），MAPPING 里标清哪些是 matched 批的、哪些是别的实验的（用时间戳窗口 11-22 前后 + spec 交叉核对），[待核验] 的标出来。
- commit。

## S2 A3 出 matched 批 stats
- 用 ablation_stats.py（或按它的口径手写最小统计）：SM 臂 vs bare 臂，同负载，per-qid coverage/depth 均值±SE + 95%CI + Welch t + MWU + δ。
- bare 臂数据位置从 bare_arm_batch_matched.py 的落盘逻辑找（找不到就在报告里标缺口，不编）。
- n<8 的组只报点估计+区间+功效不足声明（ablation_stats.py 的机判边界，照抄它的口径）。
- 产出 `experiments/stage-ablation/matched-batch-stats-20261126.md`：
  - 每 qid 两臂 n/mean/SE/CI + Welch/MWU p + δ
  - 缺口清单（哪组 n 不足、bare 缺什么）
  - 一行结论（SM vs bare 方向 + 置信度，n 不足就明说"功效不足不下方向结论"）
- commit。

## 硬约束
- 零 LLM 调用（judge 分数已在 synth json 里，只算不判）。
- 不碰 vLLM 8787（另一个 sub 在跑 T8c 正式批，独占中）。
- 不移动/删除 archive 原数据（只拷贝/symlink 到 runs_sm_matched/）。
- 增量 commit（S1 一个、S2 一个）。
- 最终汇报 ≤15 行：映射覆盖数/缺口 + stats 表路径 + 一行结论 + commit 链。

## 验收（Lead 对照核）
- [ ] runs_sm_matched/MAPPING.md 存在，81 目录全有归属（matched/其他/[待核验]）
- [ ] stats 文件存在，3 qid × 2 臂数字齐全，n<8 组有功效声明
- [ ] 无 LLM 调用痕迹（grep 报告无"重判/重打分"）
- [ ] commit 链 ≥2
