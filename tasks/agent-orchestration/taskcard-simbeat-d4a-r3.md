# 任务卡: 模拟拍 2 轮 D4a-r3 (2026-11-28)
# origin: ai (Lead 派发)
# 死因 (Lead 已判): r2 模型输出 tool_call(cat receipts/T8c-Drill.json) 就停了——单轮裸调用无工具执行循环。
# 换路: 2 轮模拟。Round1 模型请求 cat → 执行 cat 把结果喂回 → Round2 看是否进思考轮。
# 同任务第 3 次, 死法不同 (r1=队列框架, r2=单轮无工具循环), 合规换路非原样重派。

## 前置准备 (你来做, ~3 行)
- 在 receipts/ 下放 `T8c-Drill.json`, 内容:
  {"status":"done","evidence":{"smoke":"实验节点数 40 全过"},"last_op":"run-smoke"}
  (这是模拟的"上拍回执", 让模型 cat 时能拿到真实内容)

## 执行
1. 改 `tasks/agent-orchestration/sim_beat.py` 支持 2 轮 (~20 行改动):
   - Round 1: 同 r2 的 user message (含队列检查结果+上拍回执摘要+本拍任务卡+触发检测结果)
   - 解析 Round1 输出: 若含 tool_call/Bash 命令 → 提取命令, subprocess 执行 (timeout=5s)
   - 把 tool 结果作为新 message 加入 messages (role=tool 或 user, 视 API 格式)
   - Round 2: 再调一次 8787 (同参数 temperature=0)
   - 若 Round1 无 tool_call (直接文字输出) → 跳过 Round2, 直接断言 Round1
   - 断言 a/b/c 检查**最终轮**输出 (Round2 或 Round1)
2. 运行 `python3 sim_beat.py` (最多 2 次 8787 调用)
   - 断言 a/b/c 与 r1/r2 相同, 不改
   - raw 存 receipts/drill-D4-beat.json (加 "round": 3, "rounds_used": 1 或 2)
3. commit: add sim_beat.py + receipts/T8c-Drill.json + receipts/drill-D4-beat.json, 一条 commit

## 边界
- 最多 2 次 8787 调用 (Round1 + Round2), 不循环
- 不改断言/不改协议/不改检测器
- receipts/T8c-Drill.json 是新文件, 不动其他 receipts
- 挂了直接汇报 raw, 不重试

## 验收 (Lead 核)
- BEAT PASS? + rounds_used + 最终轮模型行为 (Lead 读 raw 判语义)
- 汇报 1 行: BEAT PASS? + rounds_used + 模型行为一句话 + commit hash
