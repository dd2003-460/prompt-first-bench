# K7 GPU 批记账 off-by-one 错位 — provenance 核验 (2026-11-24)

## 发现

GPU K7 budget-scan 批（`data/t53b/runs_budget_scan/gpu_budget{B}_r{R}.json`，15 个记账 json）的
`n_nodes` 和 `answer` 字段**系统性错位一个 run**：记账 rN 记录的是 run r(N+1) 的数据。

## 决定性证据（answer 文本逐字匹配）

| 记账文件 | 记账 n_nodes | 记账 answer 逐字匹配 |
|---|---|---|
| gpu_budget50_r1 | 175 | archive **r2** 的 synth |
| gpu_budget50_r2 | 103 | archive **r3** 的 synth |
| gpu_budget50_r3 | 136 | （无 r4，孤儿） |
| … 全 15 个 run 同模式 … | | |
| gpu_budget719_r1 | 665 | archive **r2** 的 synth |
| gpu_budget719_r2 | 747 | archive **r3** 的 synth |
| gpu_budget719_r3 | 709 | （孤儿） |

`n_nodes` 同样错位：记账 rN 的 n_nodes = archive r(N+1) 树的节点数。

## 哪一侧是 ground truth

**archive 树**（`experiments/stage-ablation/checkpoints/archive/budget-{B}-r{R}-*/runs-s5-sm-gpu.json`）：
- 内部自洽：`n_nodes` 字段 = `nodes` 数组长度 = 末轮 `n_total`（15/15 全自洽）
- git HEAD 版本一致（非 mid-write 快照）
- 目录按时间戳顺序命名（budget-50-r1-070815 → r2-073512 → r3-075106）

**记账 json** 不含 `nodes` 字段（只有 `n_nodes` 标量 + `answer` 文本），judge_v1 通过
`load_run_nodes` 的 archive 回退逻辑实际打分用的是 archive 树，不是记账 json。

结论：**记账侧标错位**（runner 写记账时 off-by-one，或归档时目录名错位），archive 树是 ground truth。
无法从现有数据区分是 (a) 记账循环 off-by-one 还是 (b) archive 目录标错——但不影响修正，因为
judge 打分的对象（archive 树）是确定的、在 git 里的。

## 影响面（逐项核验）

| 声明 | 来源 | 是否受影响 | 修正 |
|---|---|---|---|
| cov 分层均值 0.259/0.264/0.278/0.358/0.352 | judge_v1 直接读 archive 树 | **否**（每层 3 棵树的集合不因标签错位而变） | 已重算复现 719=0.352/50=0.259 |
| draft §1 realized ranges (103–175/…/665–747) | 记账 n_nodes | **是** | archive 口径：103–423/123–314/122–392/364–415/381–747 |
| draft §4.3 cor(cov,n_nodes)=+0.563 | 记账 n_nodes × archive cov（错配） | **是** | 正确口径（同棵 archive 树）= **+0.602**（t=2.72, df=13, p≈0.019） |
| draft §4.3 "1.0 step reached only at 665–747 nodes" | archive 树 max_depth | **否**（b719_r2=665/r3=747 正是 max_depth=5 的两棵树） | 不变 |
| depth~n_nodes r=+0.944 (n=30) | 待核（rep-scan + K7 池化） | 待核 | — |

## Q6 批不受影响

Q6 记账 json **内嵌 `nodes` 字段**（无 archive 回退），`n_nodes` 字段 = `nodes` 数组（15/15 自洽）。
Q6 无此错位 → 跨域 cov 段（0.058→0.167）安全。

## 对 headline 的影响

**无**。cov 分层均值（headline 的"coverage rise-to-plateau"）不受影响。受影响的是
realized node count 的逐 run 描述和 size-confound 相关系数——后者修正后反而更强（+0.602 显著）。
低档 realized 节点数被原 draft 低估（b50 实际到 423 不是 175），这**强化**"soft cap、
budget 不是干净 IV"的论点。

## 待办

- [ ] 定位 runner 写记账的 off-by-one 源码行（可选，不影响数据修正）
- [ ] 核 depth~n_nodes r=+0.944 的 n_nodes 来源（若来自记账则需重算）
- [x] 修 draft §1 realized ranges → archive 口径
- [x] 修 draft §4.3 cor → +0.602 + provenance caveat

## 附：Q6 719 深度墙 confound 纠正（2026-11-24 02:30）

一度误判"深度墙没约束 Q6、模型自然饱和 4 层"——**错**。原因：拿 rerun 的 719 r1
（`q6-budget-scan-rerun/q6-719-r1-20261124-012603.json`，cache 隔离、本来就带 max_depth=4 墙）
当拆墙批评了。真正的拆墙批（`q6_719_nodepth_queue.sh`，`--max-depth 10`）输出到
`q6-719-nodepth/`、文件名 `q6-719-nd-r*`，是 relay phase 2，**尚未开跑**。

深度墙**确实 binding**：Q6 719 原批 3 rep 都在 max_depth=4 停，但停止时 gain 仍
0.889–0.909（高）、frontier 仍 54–94 节点（非空）、low_gain_streak=0 → 模型还想展开
但被墙拦。rerun 719 r1 同（gain=0.916, frontier=85）。

**对 draft 无影响**：跨域段"Q6 719 档撞深度墙、cov 与深度墙 regime confound、拆墙批是
clean test"的 caveat 本来就对，未改。拆墙批仍是需要的 clean test，排队中。
