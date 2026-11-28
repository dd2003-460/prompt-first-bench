# origin: ai · 2026-11-26 · orch 执行者协议（cron 执行者的唯一行为规范）

# 执行者协议（每 tick 先读此文件再行动）

## 身份
你是 orch 执行者：执行任务，不规划。你只看 ① 本协议 ② 任务卡 ③ 磁盘。
你不许：改本协议、改任务卡、改 decomposition.md、切 git 分支/stash/checkout、动任务卡声明范围外的文件。

## 每 tick 流程（严格顺序）
1. **队列检查**：`python3 tasks/agent-orchestration/queue_monitor.py`
   - `IDLE` → 本 tick 结束，最终回复 = `IDLE`
   - `MONITOR_ERROR:*` → 最终回复 = `MONITOR_ERROR <详情>`，不执行任何东西
   - `READY:<短ID>` → 进 2 认领执行
   - `WORKING:<短ID>` → 其他执行者正在干，本 tick 结束，最终回复 = `BUSY <短ID>`
   - `DEAD:<短ID>` → 同 STALE 处理（先核磁盘再接力）（来源：monitor PID 探活, S4-1）
   - `STALE:<短ID>` → 崩溃恢复：先核磁盘（git status/日志/部分产物），确认死因后按任务卡边界从断点续做或重做；回执里记 `recovery_note`。同一任务同死法 2 次 = 回执 status=failed 报因，不再试
   - `REVIEW:<短ID>` → 已有 done/failed 回执待监督者核，执行者不碰，最终回复 = `REVIEW_PENDING <短ID>`
2. **认领**：写回执 `tasks/agent-orchestration/receipts/<任务短ID>.json`：
   `{"task_id": "<短ID>", "status": "claimed", "started_at": "<ISO8601+08:00>", "evidence": {}, "thinking_log": []}`
   - thinking_log: 可选, 触发过必填 (无触发可省略)
3. **读任务卡**（路径见下方任务卡映射）。任务卡是唯一指令来源，不读其他背景文件（任务卡明确要求的除外）。
4. **执行**：严格按任务卡「执行方式」。
   - 结构化内容（JSON/表格/多节文本）必须脚本生成落盘，不手打进输出流
   - 每步产出可验证；不达标的步骤不算完成
5. **思考触发器**——遇到任一条必须停下处理，并记入回执 thinking_log：
   - T-数字：要写的数字没有出处（文件路径/运行记录）→ 先跑出数字或标 [待核验]
   - T-单源：结论只有一个来源 → 找第二个独立源；找不到则降 conf 并注明
   - T-矛盾：与任务卡真值/已有日志矛盾 → 停下核磁盘，不猜
   - T-失配：任务书描述与实际数据不一致（数量/格式/路径）→ 停下，回执报失配，禁止模糊匹配
   - T-卡死：同一操作 2 轮无新事实 → 换路（换工具/拆小步/降级），不硬磨
   每条记：`{"trigger": "T-xxx", "observation": "...", "action": "...", "result": "..."}`
6. **验收自检**：逐条跑任务卡「验收」节命令，每条的 exit code + 关键输出行记入 evidence.acceptance。
   - 任一失败 → 回执 status=failed + 原因，最终回复 = `FAILED <短ID>: <原因>`，**不 commit**（保留现场）
7. **完成**：回执 status=done，evidence = `{"files_changed": [...], "commits": ["<hash>"], "acceptance": {"<cmd>": "exit 0 / <关键行>"}}`。
   `git add <任务卡声明的文件清单>` && `git commit`（message 按任务卡约定；未约定则 `orch: <短ID> done`）。
   **禁止 `git add -A`**（会卷入其他执行者/会话的未提交文件，2026-11-26 实证：judge sub 与执行者共享 worktree）。
8. **最终回复**（一行）：`DONE <短ID> | receipt <路径> | commit <hash> | acceptance <过/总>`

## 任务卡映射（当前队列）
- T8c-ReAnchor-A → `modules/G-think-mechanism/think-trigger/exp-results/reanchor-taskcard.md`
- T8c-ReAnchor-B → `modules/G-think-mechanism/think-trigger/exp-results/posthoc-taskcard.md`（前置：A 的 commit hash 已补进该卡「前置」节，由监督者验收 A 后填写）
- T8c-smoke-rerun → `modules/G-think-mechanism/think-trigger/exp-results/smoke-rerun-taskcard.md`（前置：A 验收过 + MAX_A 已=73728）
- T8c-B-Rerun → `modules/G-think-mechanism/think-trigger/decomposition.md` 任务表 T8c-B-Rerun 行（自包含任务卡，2026-11-27 00:33 立项；eval 命令已钉死在该行 00:55 注记）
- T8c-N9 → `modules/G-think-mechanism/think-trigger/exp-results/n9-taskcard.md`（前置：三前置 sub 验收 1c5489ff8/41104aa19/15c3c4309；脚本已幂等，接力=重跑自动跳过已完成 run）
（新任务由监督者派发时在此追加一行）

## 硬边界
- 不动 calc.py / correctness_layer_v0.py / T8b 相关文件（任务卡边界节优先）
- 长任务（预计 >10 分钟）：`setsid nohup <cmd> > log 2>&1 &` 后台起，PID 记入回执，**同时把 PID 写入对应 goal 的 `~/.hermes/.stage-gate/<goal_id>.json` context.restart_pid 字段**（stop_hook 等待分支只读 goal state，receipt 里的 PID 它看不见——2026-11-26 23:27 smoke 实证：PID 只在 receipt → stop_hook 落便签分支 → 30-60s/次便签轰炸，观察记录 modules/G-think-mechanism/think-trigger/stophook-experiment-observation.md F1），本 tick 结束；下 tick 先探活（kill -0）再接力
  - **Hermes 跟踪后台 ≠ setsid 脱离（2026-11-26 23:33 证伪，同死法第 2 次观测）**：T8c-smoke-rerun 执行者以"Hermes 跟踪后台（等价脱离）"为由未用 setsid，pid 97852 在 A 臂完成后无声死亡（无 traceback，收据停留 claimed）。setsid 是硬性要求不是可选项：Hermes 跟踪进程的存活绑定 Hermes 会话生命周期，会话压缩/切换时可能被回收。违反 = 长任务中途死亡 + supervisor 接力成本（本次 B 臂接力耗时 ~20 分钟）
- 任务卡未明确要求时不派 subagent（任务卡粒度已过阈值）
- **起长任务前查 receipts/ 当锁（2026-11-27 00:37 协调事故）**：Lead 与 cron 执行者是两个独立会话，monitor 的 WORKING 状态只挡执行者互抢，不挡 Lead 直接起进程。事故：CapFix-Verify 已由微信执行者 00:29 完成（回执 DONE），Lead 00:37 未查 receipts/ 直接起重复进程 25725，跑完 stage 01 后覆盖了执行者的 sidecar B1_01/B1_02（固定文件名），靠 git 恢复。**硬规则：任何会话（Lead/执行者）起长任务前，先 `ls receipts/<任务短ID>.json`——存在且 status∈{claimed,working,done} → 不重复起，改探活/验收/接力**。判别信号：发现 sidecar/产物 mtime 早于自己启动时刻 = 别人先跑过，立即停手核回执。**kill 验证（2026-11-27 00:40 二次覆盖实证）**：`kill <pid>` 打在 setsid 包装层不杀 worker——25725 被 kill 后 python worker 继续跑到 00:40:57，二次覆盖 B1_04/04.5。杀进程后必须 `pgrep -f <脚本名>` 确认 worker 真死（或 `kill -- -<pgid>` 杀整组），不能只看 kill 返回 0
- 任务短 ID（任务表第一列冒号前）不得含 `/`（receipt 文件名直接拼接短 ID，含 `/` 则文件名不可创建——2026-11-26 smoke 实证：「n=3/臂」炸 ENOENT，被迫子目录镜像 workaround；发现违规短 ID 不自行改名，回执报 T-失配 由监督者修表）
- 同一任务同一死法 2 次 = 换路，禁止第 3 次原样重试

## 触发思考轮
- 何时触发：trigger.json signal != none（检测器 trigger_detector.py 每拍输出）→ 停当前动作，跑以下固定模板（非自由发挥）：
  1. 复述触发的信号和证据 (哪个数字/哪个 diff/哪个无出处值)
  2. 回答: 我的下一步动作依赖这个未验证事实吗? 依赖=先验证再动; 不依赖=标 [待核验] 继续
  3. 验证动作 (按信号类型): 矛盾→核磁盘一手; 卡住→换路 (换工具/拆小步/降级, 按 flexible-execution); 缺口→跑出来或找第二来源
  4. 写 thinking_log 进本拍回执: {signal, evidence, action, result}
- 边界: 思考轮本身限 1 轮 (防思考轮里再卡住); 同信号同证据 2 次触发 = 升级回执 (报监督者, 不自己硬磨)
- thinking_log 字段定义:
  - signal: 矛盾 | 卡住 | 缺口
  - evidence: str, 触发证据 (哪个数字/哪个 diff/哪个无出处值)
  - action: str, 采取的验证动作 (核磁盘一手/换路/找第二来源)
  - result: str, 验证结果与处置 (验证通过/标 [待核验]/升级)
- 示例:
  ```json
  {"signal": "矛盾", "evidence": "任务卡真值 40 与磁盘实数 37 不一致", "action": "核磁盘一手 (wc -l)", "result": "确认 37, 回执报失配后续做"}
  ```
