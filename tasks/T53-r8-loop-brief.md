# 任务书：T53 状态机 r8 监控 + 后续迭代循环

## 你是谁
你是 T53 decomp 状态机的执行层 teamer。你负责跑循环、盯进程、落盘证据；Lead（承）只汇报你的成果，不替你决策。遇到方案选择，写进交接文件并继续做可逆的事，不要停。

## 当前状态（2026-11-11 23:40 快照）
- r8 在跑：pid 25038，`python3 experiments/stage-ablation/s5_state_machine.py gpu --resume checkpoints/sm-gpu-r2.json`，日志 `runs-s5-sm-gpu-r8-console.log`
- 起点：r2 checkpoint 125 节点（L1×5 + L2×32 + L3×88），skip_l1=True
- 硬顶：max_nodes=150 / max_depth=4 → 本轮最多 +25 节点
- 刚生效的 prompt 改动（已提交）：P1H_INDEX 逐父节点停止判 + 硬停门禁三条（定义式未展开 / 待填参数有来源 / ≤L2 类别级描述 → 必须产子节点）
- 关注点：新门禁是否逼出 L4 节点；还是模型又集体收树（+0 saturation）

## 你的循环（每轮做这些）
1. **查活**：`kill -0 <pid>` 看 r8 是否还活着；`tail runs-s5-sm-gpu-r8-console.log` 看最新进度行（`[SM] rN: +X (total Y)`）。
2. **卡死判定**：日志超过 25 分钟无新行 且 进程活着 → 查 `lsof -p <pid> | grep TCP` 看它连在哪（8787 = LLM 调用中正常；ego-browser 超时后无动作 = 卡死）→ 卡死就 kill，从最新 checkpoint resume 重跑，事件记入交接文件。
3. **完成判定**：日志出现 `[T53 SM] DONE` 或 `FATAL` → 读 `runs-s5-sm-gpu.json`，统计：总节点数、各层级分布（重点 L4 数量）、leak_hits、rework_events 数、rounds_log 每轮 gain。
4. **结果分析**（DONE 后做一次）：
   - 新门禁有没有起作用？对照 r4 终态（133 节点全 ≤L3，r2 起 +0）看这次 L3/L4 增量。
   - 如果 L4 = 0 且 +0 saturation 重现 → 这是 prompt 层面的失败，把诊断写进 `research/sm-thinking-sop.md`（新增 Decision 13），不要自己改代码硬试第二次——报告给 Lead 定夺。
   - 如果 L4 > 0 → 记录哪些父节点触发了下钻（claim 原文摘录 3-5 条），验证硬停门禁哪一条命中的。
5. **落盘**：所有发现追加到本文件下方「## 交接记录」节，带时间戳。关键数字同时更新 `tasks/T53-decomp-state-machine.md` 的状态行。
6. **git**：每次有新结论落盘后 commit（--no-verify，pre-commit hook 已知损坏）。

## 边界
- 可以改：prompt 文本（s5_pipeline.py 里的 P1* 常量）、state machine 配置（max_nodes/max_depth/停止阈值）、checkpoint 管理逻辑。
- 不能改：泄漏检查逻辑（_check_output_leak）、AC 验收口径、题目本身。
- 任何改动先 commit 再跑，保证可回滚。
- 连续两次同样方式失败（比如 resume 后又卡死在同一位置）→ 停下写诊断，等 Lead。

## 交接记录
（teamer 从这里开始追加，格式：`### [YYYY-MM-DD HH:MM] 事件`）
### [2026-11-11 23:45] Lead 决策：r8 作废，改跑 r9
- D 指出树形应该是 ~6×6×6（每父节点子数受控），不是 6×20。实测 r2 ckpt：L1 各 18 子、L2 最高 21 子——扁平化爆炸。
- 已修：s5_state_machine.py 加 max_kids_per_parent=8（单父扇出上限，超出按 n-gram 距离保留最近的），已 commit。
- **操作**：kill pid 25038（r8 还在跑旧代码，无价值），从 checkpoints/sm-gpu-r2.json resume 重跑为 r9：
  `python3 experiments/stage-ablation/s5_state_machine.py gpu --resume checkpoints/sm-gpu-r2.json > runs-s5-sm-gpu-r9-console.log 2>&1`
- r9 预期形态：125 + 最多 25（撞 max_nodes=150），新增节点应集中在硬停门禁命中的 L3→L4 下钻，且每个父节点 ≤8 子。
- 分析时额外看：fanout cap 日志行（`[SM] fanout cap`）触发次数 = 模型还想铺多宽的信号。

### [2026-11-12 00:02] Lead：teamer 会话已退出，监控由 Lead 接管
- teamer（sa-0-65a6cd0f）已不在 spawn tree（其结果会作为完成消息到达）。她第一次 resume 时 kill 不彻底导致双实例并发写 checkpoint（事故详情见 T53-teamer-goal-brief.md 交接记录）。
- 当前 r9 = pid 29238（session proc_f6b304594a9f），从 checkpoints/sm-gpu-clean-r2.json（117 节点）起步，日志 runs-s5-sm-gpu-r9-console.log。
- **本文件作废**，后续以 `tasks/T53-teamer-goal-brief.md` 为准（含完整大目标 + 汇报纪律）。
