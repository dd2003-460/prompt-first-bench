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
- vLLM 被 q7 719 队列占用（PID 59750/99447）。21:19 核验：r1 已完成（18:28 落盘 1.2MB json），
  **r2 仍在跑**（stdout 21:19 还在写），r3 未开始 → 释放时间晚于早前 ~24:15 估计，
  实际约深夜~凌晨（r2+r3 各 ~2.5-3h）。严禁 kill/干扰。
- 每 cell n≥5 + bootstrap CI（judge 噪声 ~0.1，n=3 会假阳性）；checkpoint 分开统计（Handoff Tax：效应随方向反转，不混池）。
- 若声称"序列无影响"需等效性检验（预设最小重要效应），不能用"不显著"代替"相同"。
- claim 边界：stateful pipeline suffix-ablation 设计，不说"恢复相同隐状态/KV"（F2b 4）。
- runner 已就绪：`tpr17_runner.py --mode run --arm {canonical,verify-off,null-control} --checkpoint {r1,r2,r3} --rep N --budget 719`。
- 冒烟已 9/9 过（3 臂 × 3 checkpoint，零 LLM 调用）；compute_metrics 在 3 checkpoint 数值自洽。
