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
- **实测 sd + 最终 power 决策表（22:05，用 q7 budget 50/100/150/300 的 12 个独立 run 实测
  run-to-run 方差，替代"假设 sd"）**：
  - 实测 sd（跨 4 档 budget 各 3 rep，保守取最大）：depth=0.093、verified=0.040、
    parent_link=0.028。
  - 配对 TOST 判等效 power（真等效）：
    | 指标 | sd | Δ_min | n=5 | n=10 | n=15 | n=20 |
    | depth | 0.093 | 0.10 | 20% | 42% | 73% | 86% |
    | verified | 0.040 | 0.10 | **94%** | 100% | 100% | 100% |
    | parent_link | 0.028 | 0.05 | 70% | **96%** | 100% | 100% |
  - **⟹ 实验设计结论**：depth 是 TOST 瓶颈（低功效，n=20 才 86%）；verified/parent_link
    方差小、功效高，n=5~10 即可可靠判等效。→ T5 主结论（序列机制效应）应**锚定
    verified + parent_link**（高功效、可防御），depth 仅作辅助（弱功效，判不等效时
    只能读作 underpowered 非"有影响"）。T4 正式实验 n 分配：verified/parent_link 导向
    n=10（25h GPU）已足够，depth 若要可靠判等效需 n≥20（50h）——按预算取舍。
  - GPU 预算（每 run ~50min 实测, 3 臂）：n=5→12.5h / n=10→25h / n=15→37.5h / n=20→50h。
- **null-control wrapper 生命周期审计（22:10，防静默退化成 canonical）**：
  ShuffledList 包装时序 = `_seed_nodes`（赋值 `self.confirmed`）→ `_patch_null_control`
  （包装），顺序正确（wrapper 不被种子绕过）。SM 源码全量 grep `self.confirmed`：
  仅 3 处写操作全是 `.append(...)`（L619/642/701），**无 `self.confirmed = [...]` 重新赋值**
  → 主循环运行中 wrapper 不会被静默丢弃。两个消费者都过 wrapper：L507
  `self.confirmed[-40:]`（_decompose_layer state 块，负切片 ShuffledList 泛化处理）+
  L1385 `judge_necessary_batch(cand_list, self.confirmed, ...)`（完整列表）。
  ⟹ null-control 臂全程保持乱序 state 块，不会中途退化成 canonical（若退化则
  sequence_mechanism_effect 估计被污染）。**注意**：此结论依赖 SM 无重新赋值——
  若日后 SM 加了 `self.confirmed = [...]` 会破坏 wrapper，改 SM 后须重审此条。
- **T4 分析路径 n=5 有方差端到端验证（22:13，此前只测过 n=1 零方差）**：
  用 n=5/臂 + 向 null-control 注入 +0.08 depth 效应的合成 cell 跑 `tpr17_analysis.py`，
  结果统计自洽、方向正确：
  - depth（注入效应）→ TOST equivalent=False（CI 越出 Δ=0.1）+ welch_p=0.031 + d=1.74
    ⟹ 注入效应被正确检出
  - verified/parent_link（无注入）→ TOST equivalent=True（CI 界内）⟹ 正确判等效
  - 零方差指标 → guard "CI 退化为点" + equivalent=True ⟹ 正确
  - operational_total_effect → 方向性 Welch/MWU+bootstrap，无 TOST ⟹ 符合设计
  ⟹ T4 出结果后一键分析的完整链路在有方差数据上方向正确（TOST 符号/CI 方向 bug
  只会在 n≥2 有方差时暴露，本次首次覆盖）。
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
  **明早判据**：pilot 单 run >78min 无新落盘 = 可疑（正常 ~52min，相位感知：从 381 续跑
  ~44 新节点全在慢速段 71s/节点）；9 run 总 >10h 未完 = 查 vLLM 健康 + 首个 cell 日志。
- vLLM 被 q7 719 队列占用（PID 59750/99447）。**相位感知 ETA（22:17 修正，替代 1ffa83b0a 的匀速外推）**：
  实测 r1 速率是相位的——L1 段快（381 节点/62min ≈ 9.7s/节点），L2/L3 段慢（44 节点/52min ≈ 71s/节点，
  晚期 context 大+rework 多）。r2 当前 N386（刚进慢速段，已跑 114min；其 L1 段比 r1 系统性慢 ~1.5x，
  原因未明，可能树结构/负载差异）→ 剩余 ~39 节点按慢速段 71s/节点 ≈ 46min，若 r2 的系统性慢延续则更久：
  **r2 完 ≈ 23:00-23:30，r3（全程 114-170min）完 ≈ 00:55-01:45 → vLLM 释放 ≈ 01:00-01:45**
  （1ffa83b0a 写的 23:49/01:43 是匀速模型单点值，方向对但依据错，以此区间为准）。
  waiter 随后起 9-cell pilot（每 run 从 381 续跑 ~44 新节点 × 71s ≈ 52min，9 run ≈ 7.8h）
  → **pilot 完 ≈ 11-25 08:45-09:30**。严禁 kill/干扰。
- **waiter 残余风险（不改运行中脚本，bash 增量读文件，编辑会破坏执行）**：sanity floor n_nodes≥381
  只抓崩溃（json 未写/损坏）；若某 run 零进度（LLM 拒扩/budget 瞬耗）n_nodes=381 仍过 floor，
  产出退化 cell。明早分析时看 n_llm_calls≈0/tokens≈0 识别（正常 cell 有数百 calls）。
- **run_arm 生产路径哨兵验证（22:22，补 smoke 未覆盖的 run() 路径）**：
  smoke_test 只手工复刻首 prompt，从不调 `run()`；waiter 的 `--mode run` 走 `run_arm`→
  `sm.run(skip_l1=True)`，是另一条路径。用 sentinel（patch sm_mod.call_llm 在首调 raise
  SentinelLLM + no-op _probe_network 保持全 dry）驱动 3 臂 run_arm：
  - 3 臂全部到达 LLM 边界（sentinel 各触发 1 次，SentinelLLM 正常传播，无 OTHER 异常）
  - 真实 run() 构造的首 prompt len=10232（decompose 真 prompt，非 smoke 手工版），3 臂一致
  - skip_l1=True 生效（"[SM] L1 already seeded (381 nodes), skipping decompose"），cell_ckpt
    目录 3 臂均创建
  ⟹ waiter 将执行的生产路径（build_sm(rep,qid)→SM_CKPT_DIR 隔离→run(skip_l1)→臂 patch 在
  run 内执行）在 LLM 边界前无结构性崩溃；零真实 LLM 调用（sentinel 在网络前 raise）。
  这是 T4 起飞的最后一道闸门验证。
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
