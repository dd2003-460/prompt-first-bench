# stop_hook 思考注入实验 · 观察记录（2026-11-26 23:23 部署）

## F1 · 忙循环（23:27-23:29 实证，QQ 会话）
- 现象：两轮计数器 228→234，10-60s/次停止→续推，便签高频轮换
- 根因（机制缺口，非噪音）：stop_hook 等待分支 `elif _alive:` 靠 `_alive_wait_pids` 从 **goal state JSON**（`~/.hermes/.stage-gate/*.json` context 的 restart_pid/pid 等键）读 PID。smoke 的 PID 97852 只记在 **receipt**（cron 执行者写的）→ goal state 无 PID → 等待分支不触发 → 落便签分支 → 每次核日志=短 turn=再触发便签
- 定性：11-26 上午"微观碎片化"的复发变体（4问刷屏→便签高频）；根因=执行者协议只要求"PID 记入回执"，stop_hook 的等待感知只读 goal state，两个系统的 PID 登记不互通
- 修复（两层）：①即时——97852 写入 research-agi-budget.json context.restart_pid（后 B 臂接力改 1383）②根因——executor-protocol.md 硬边界节加"PID 同时写 goal state context.restart_pid"
- 附带发现：执行者 pid 97852 死于 `WROTE arm_a` 后（无 traceback、无 B 臂行、收据停留 claimed）；supervisor 接力只跑 B 臂（mode=b 保留 A 臂数据），死因按任务卡规则不盲目重跑
- 状态：①②已落地；B 臂 pid 1383 在跑

## 基线对照（progress.log）
- 旧 stop_hook 时代(00:51-15:36): think-trigger 命中 6 次（T1×2 + T4×4）
- think-guard 时代(19:44-22:23): 7 次
- 新模式(23:23-00:01): 0 次。定量核查（00:01 统计）：窗口内 stop-hook 事件 175 条
  （halt-removed 43 / inbox-skip 34 / continue-goal 31 / 便签 29 / 等待静音 9 等），
  `.think-trigger.json` ts=00:01 证明检查每轮都在跑且正确未命中——该时段每轮
  思考均远超 430 字符/调用阈值（分析/写报告/交叉验证期），T1 条件不成立；
  无重复报错，T4 不成立。**0 命中 = 机制正确区分"薄思考"与"深度思考"，
  非故障**。实验真正变量=覆盖面（HALT/weixin 门移除后全会话全停止事件生效），非频率
