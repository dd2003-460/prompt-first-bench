# 任务卡: 模拟拍测试修正重跑 D4a-r2 (2026-11-28)
# origin: ai (Lead 派发)
# 死因 (Lead 已判): r1 挂是 harness 框架错, 不是模型不服从。协议每 tick 第一步=查队列, 队列空→IDLE。
# r1 的 user message 直接塞任务没给队列结果, 模型正确地先查队列 (输出 IDLE + 想跑 queue_monitor)。
# 修正: user message 喂入队列检查结果, 让模拟拍符合协议前提。断言 a/b/c 不变。

## 执行
1. 改 `tasks/agent-orchestration/sim_beat.py` 的 user message 构造 (~5 行):
   - 开头加一行: "队列检查结果: READY:T8c-Drill (queue_monitor.py 输出, 已替你跑完)"
   - 保留原有 上拍回执/本拍任务卡/触发检测结果 三段
   - 结尾指令改为: "队列已就绪, 请按每 tick 流程从步骤 3 开始行动 (队列检查已完成), 输出你的动作和本拍回执 JSON。"
2. 重跑 `python3 sim_beat.py` (单次 8787 调用, temperature=0, 不重试)
   - 断言 a/b/c 与 r1 相同, 不改
   - raw 覆盖写 receipts/drill-D4-beat.json (加字段 "round": 2)
3. commit: add sim_beat.py + receipts/drill-D4-beat.json, 一条 commit

## 边界
- 只改 user message 构造, 不改断言/不改协议/不改检测器
- 8787 单次调用, 挂了直接汇报 raw, 不重试
- 不动 receipts/ 其他文件

## 验收 (Lead 核)
- BEAT PASS? + raw 里模型是否进了思考轮 (Lead 读 raw 判语义)
- 汇报 1 行: BEAT PASS? + 模型行为一句话 + commit hash
