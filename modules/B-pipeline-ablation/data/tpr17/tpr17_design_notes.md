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

## T4 无人值守风险清单（21:48 核验，逐项有证据）
T4 pilot 夜间无人值守，下列接缝逐一核验过（防"白等一夜"的静默失败）：
- **waiter python 环境**：waiter 的 `python3` = /opt/homebrew/bin/python3 (3.14.4)，
  clean env 下 `import s5_state_machine` + `import tpr17_runner` 均 OK。
  sanity check 用 /usr/bin/python3 (3.9.6) 纯 stdlib 解析 json，无依赖风险。
- **文件名契约**：runner 写 `{arm}_{ckpt_spec}_r{rep}.json`（L435）= 如
  `null-control_r3_r1.json`；waiter sanity 读 `$OUT/${arm}_r3_r${rep}.json`、
  summary glob `*/canonical_r3_r*.json` 等均精确匹配（arm 含连字符也匹配）。
- **post-run pipeline**：build_sm→compute_metrics→_tree_dump→json roundtrip
  在真实 381 节点树上 3 臂全通，waiter 读的键（n_nodes/depth/verified_ratio/
  tokens_total/n_llm_calls/tool_calls/evidence_delta_chars/parent_link_accuracy）
  全部存在。n_nodes=381 ≥ CKPT_FLOOR=381（sanity 阈值，>= 含等号）。
- **sm.run(skip_l1=True)**：签名确认接受 skip_l1（L1139），与生产 --resume 同路径。
- **LLM 往返接缝（原"唯一未测"）→ 已由活体验证**：8787 实例此刻正服务 q7 r2，
  1104 次 LLM call / 0 失败 / 0 重试（21:49 实测）。harness 请求 model 名
  `qwen3.8-27b` 被 8787 proxy 正确映射到 served 的 `qwen3.8-27b-mtp`
  （`/v1/models` 只读确认）。q7 r2 与 T4 pilot 走**完全相同**的 harness+端点+model 名，
  故 LLM 传输链（curl -m 硬超时 POST 8787/v1/chat/completions）已被证实可用。
  残余风险仅 = vLLM 在 T4 启动瞬间是否仍健康（waiter 的 /health+/v1/models 探测兜底）。
- **无并发 vLLM 消费者**：q7 DONE 时会同时醒来的 3 个 watcher 全是纯 CPU 分析、不调 LLM
  （overnight-watcher 72034 的 replication-check.py / watchdog 57325 的 gold+full analyze /
  我的 waiter 88305）。→ T4 启动瞬间**只有我的 pilot 在用 vLLM**，无资源争抢。
  三者 21:50 核验均存活。
- **waiter 触发器存活性（最高杠杆风险，21:52 核验）**：waiter 88305 ← 88298
  （`Ss`=session leader，独立 PGID 88298，TTY=?? 无控制终端）← 99739（hermes python
  守护）← … ← 99731（PPID=1，挂 launchd）。88298 是独立会话+独立进程组（PGID 88298≠父
  99739）且无 TTY → 我的 shell 进程组收 SIGHUP/SIGTERM 不波及它，根在 PID 1 链稳定。
  活体证据：同结构 overnight-watcher 72034 已跨我多个 turn 存活 59+min，waiter 自身
  存活 19+min → 该启动模式确能脱离会话存活，T4 自动触发器不会随会话回收静默死亡。
- **runner↔analysis 端到端拼接（21:53 核验）**：用真实 post-run pipeline 生成 3 个 cell
  文件（canonical/verify-off/null-control_r3_r1.json，各 ~160KB 含 final_tree）喂给
  `tpr17_analysis.py --out <dir> --checkpoints r3` → EXIT=0 无崩溃，n_cells=3、
  n_per_cell 正确、UNDERPOWERED 哨兵按设计触发（n=1<5）、comparison 结构建好
  （operational/sequence 两 estimator 空 = n=1 零方差被 guard 成 None，正确行为非 bug）。
  → T4 出结果后"一键 `tpr17_analysis.py` 出报告"链路成立，runner 输出与分析脚本输入
  的 schema 拼接无缝。
- **TOST power 警示（21:58 量化，T5 主结论解读的关键约束）**：TOST 实现方向正确
  （明确界内→equiv=True / 明确界外→False / n<2 守卫→None / 单侧 p 符号全对），
  但在真实方差（sd~0.1 = 设计文档 F3/F5 的 K7 同序列 run 间方差）下 power 极低：
  真等效时判等效概率 n=3 仅 17%、n=5 仅 17%（sd=0.05 乐观情形 n=5 才 80%）。
  **⟹ T5 解读铁律**：若 TOST 判"不等效"，在 n≤5 且 sd~0.1 下**不能解读为"序列有影响"**，
  只能解读为"功效不足以证明等效"（underpowered）；只有 equiv=True 才是正向证据
  （序列无实质影响）。要可靠判等效需更大 n（80% power 所需 n 未及量化，估计 n≥15-20
  @sd=0.1）→ 若 T4 pilot 判不等效，正式实验须扩 n 或缩小 Δ_min 前重新做 power 分析。
- **fail-fast 语义**：任一 cell rc!=0 或 n_nodes<381 → break 2 中止整批（设计如此，
  防坏 checkpoint/坏 patch 污染后续 8 cell）。明早若见 PILOT ABORTED，先读
  报告里首个失败 cell 的 stderr。

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
