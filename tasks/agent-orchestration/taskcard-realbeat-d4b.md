# 任务卡: 真实执行者拍 D4b (2026-11-28) — 取代 D4a-r3
# origin: ai (Lead 派发)
# 换路理由: D4a r1/r2 死因分别是 harness 队列框架错/单轮无工具循环——harness 在模拟一个模拟。
# 真实执行者 = 带工具循环的 agent。本卡直接派 subagent 扮演执行者跑一拍, 端到端验证。

## 你的角色
你是 orch 执行者。行为规范: tasks/agent-orchestration/executor-protocol.md (先读全文, ~80 行)。

## 模拟拍输入 (已备好的状态)
- 队列检查结果: READY:T8c-Drill (队列检查已完成, 从每 tick 流程步骤 3 开始)
- 上拍回执: tasks/agent-orchestration/receipts/T8c-Drill-prev.json (读它)
- 本拍任务卡: tasks/agent-orchestration/receipts/T8c-Drill-plan.md (读它)
- 触发检测结果: tasks/agent-orchestration/receipts/drill-D3-trigger.json (读它, 这是检测器已跑出的结果)

## 执行
按 executor-protocol.md 每 tick 流程从步骤 3 开始:
1. 读任务卡 (T8c-Drill-plan.md)
2. 触发检测: 用给定的 drill-D3-trigger.json (signal=矛盾)
3. 按协议处理: signal != none → 跑触发思考轮 (协议里有 4 步模板)
4. 产出本拍回执: 写到 tasks/agent-orchestration/receipts/T8c-Drill-beat.json
   格式按协议回执节, 必须含 thinking_log (协议触发思考轮节定义了字段)
5. commit: add receipts/T8c-Drill-beat.json, 一条 commit

## 边界
- 你可以用任何工具 (read/grep/terminal) 做验证动作——这是真实的
- 不改协议/检测器/其他 receipts
- 不跑 LLM API (你就是 LLM)
- 回执里的 evidence 必须是真实核出来的 (比如你真读了 prev 回执), 不许编

## 汇报
1 行: 你检测到矛盾了吗 + 思考轮 4 步你各做了啥 (各 5 字内) + commit hash
