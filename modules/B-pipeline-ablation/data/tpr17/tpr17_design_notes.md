# T-PR-17 T4/T5 设计笔记（执行前必读）

# origin: ai
# 生成: 2026-11-24 T1 深化 + compute_metrics 验证副产物。T4 正式 run 前过一遍。

## 数据事实（已核验，非推测）

### checkpoint 来源
- `experiments/stage-ablation/checkpoints/archive/budget-719-r1-20261122-143216/sm-gpu-{r1,r2,r3}`
- r1=L1 完成(33 节点) / r2=L2(132) / r3=L3(381)，同一 seed 同一 gpu 题。
- 注意：r1 归档目录名是 budget-719-**r1**（K7 budget-719 扫描的第 1 个 run），里面装了该 run 的 sm-gpu-r1/r2/r3 三轮落盘。

### T5 parent_ids bug（根因 + 影响，详见 t5_impact.json）
- 根因：`s5_state_machine.py` L1359-1364，gap_check 补充节点 `NodeRecord(...)` 构造时**未传 parent_ids**（默认 `[]`）；gap_check 只收 claim 文本 → 真 parent 磁盘不可恢复（永久丢失）。
- 命中全部 3 checkpoint：gap 节点 r1=5 / r2=9 / r3=14（累积，每轮净增 5/4/5）。
- checkpoint 级 max_depth 未失真（健康节点达同 level）；但**个体 depth 失真**：经 gap 节点的链被压低，r3 达 95/381=25%。
- 对 3 臂是 common-mode（同 checkpoint 同坏链）→ 臂间差分抵消。
- **T5 分析约束**：depth 用 level 字段修复（depth≥level）或 gap 节点重挂 level-1 最近节点；parent-link 正确率指标天然含这批坏链（r1=0.82/r2=0.93/r3=0.96），跨臂比较时是常数偏移。

### 续跑语义（影响 T4 公平性，已核验）
- 续跑（`run(skip_l1=True)`）**不 re-verify 既有 pending 节点**：r1 的 5 个 pending（恰是 gap 节点 N31-35）在 r2 里仍是 pending。→ 3 臂都继承同一批未核验节点，common-mode，T4 公平性 OK。
- **verified 状态非单调**：r1 里 verified 的 N12/N13/N14 在 r2 被 rework 周期重开成 pending（evidence 从 16 字符 stub 补到 247-356 字符，进了 r2 rework_events）。→ "verified 比例"指标随轮次非单调上升，T5 解读时别当成单调累积量。
- r3 有 1 个生产重复 claim（compute_metrics dup=1）→ precision 指标非零基线，跨臂比较时留意。

## T4 执行约束
- **pilot 时长实测校准（2026-11-24 21:45，来自 q7 r1 完整 run，同代码路径同 regime）**：
  q7 r1 = 719 节点/4 轮/6843s(114min)，per-round n_new=35/90/255/334。
  第 4 轮（380→719，334 新节点）墙钟 ≈ 43-52min（verify 起点 19:30:03 → DONE 20:22:11，
  不含第 4 轮 decompose 则 52min 为下界）。T4 pilot 每 run 从 381 续跑至 719（338 新节点）
  ≈ 同 regime → **每 run ~45-55min，9 run 串行 ≈ 7-8h**（与 Lead 全 run pace 粗估 0.89h/run
  吻合，粗估被实测背书）。LLM call 延迟 mean 4.3s/median 2.4s/p90 8.4s/max 240s，
  晚期/早期比仅 1.07x（context 增长效应小，均匀 pace 假设成立）。
  **明早判据**：pilot 单 run >70min 无新落盘 = 可疑（正常 ~50min）；
  9 run 总 >10h 未完 = 查 vLLM 健康 + 首个 cell 日志。
- vLLM 被 q7 719 队列占用（PID 59750/99447）。**实测校准 ETA（21:44）**：
  r2 起跑 20:22:37（已跑 81.6min），按 r1 实测 114min/run → r2 ≈ 22:17 完，
  r3 ≈ 23:31 完 → **vLLM 释放 ≈ 23:30-23:45**，waiter 随后起 9-cell pilot
  （~7-8h）→ **pilot 完 ≈ 次日 07:00-07:30**。严禁 kill/干扰。
- 每 cell n≥5 + bootstrap CI（judge 噪声 ~0.1，n=3 会假阳性）；checkpoint 分开统计（Handoff Tax：效应随方向反转，不混池）。
- 若声称"序列无影响"需等效性检验（预设最小重要效应），不能用"不显著"代替"相同"。
- claim 边界：stateful pipeline suffix-ablation 设计，不说"恢复相同隐状态/KV"（F2b 4）。
- runner 已就绪：`tpr17_runner.py --mode run --arm {canonical,verify-off,null-control} --checkpoint {r1,r2,r3} --rep N --budget 719`。
- 冒烟已 9/9 过（3 臂 × 3 checkpoint，零 LLM 调用）；compute_metrics 在 3 checkpoint 数值自洽。
- run 路径（build_sm→run(skip_l1=True)→compute_metrics）用**组合验证**而非 stub dry-run：
  seeding 已镜像 production --resume（8 个 SM 级字段全核验一致）+ run() 是生产代码（产出 r1/r2/r3
  的就是它）+ compute_metrics 已验证。未做 stub dry-run 的原因：call_llm 在 ~6 处被调用且返回格式
  各异（decompose/edge/parent_check/rework/contradiction），单一 stub 无法正确满足所有 → stub run
  测的是 stub 不是 runner，false-confidence 风险高。T4 起 run 前如需端到端演练，建议用真实 vLLM
  跑 1 个最小 cell（budget 小、1 rep）先验证，而非 stub。
