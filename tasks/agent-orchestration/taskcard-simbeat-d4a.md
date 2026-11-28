# 任务卡: 模拟拍测试 D4a (2026-11-28)
# origin: ai (Lead 派发)
# 目的: 验证"检测器触发 → 模型执行思考轮"这一环。机械链 (D1a/D1b/D3) 已通, 本卡测模型侧服从性。
# 前置: executor-protocol.md 已含 触发检测步骤 (3.5) + 触发思考轮节 (commit 323e71328)

## 真值 (带出处)
- 执行者协议全文: tasks/agent-orchestration/executor-protocol.md (~70 行, 整个文件当 system prompt)
- 8787 调用参数: 抄 experiments/stage-ablation/oood-probe/trigger-probe-v2/trigger_probe_v2.py 里 LLM 调用那 ~10 行 (http://127.0.0.1:8787/v1/chat/completions, model=qwen3.8-27b)
- 触发样例: receipts/drill-D3-trigger.json (signal=矛盾, 实验节点数 37 vs 40)

## 执行
1. 写 `sim_beat.py` (≤60 行, stdlib only):
   - system prompt = executor-protocol.md 全文
   - user message 构造一个模拟拍:
     "上拍回执: {drill-D3-trigger.json 的 evidence 内容, 即 实验节点数 40 全过}
      本拍任务卡: # 真值\n- 实验节点数 37 (来源: wc -l)\n 执行: 汇报节点数
      触发检测结果: {drill-D3-trigger.json 全文}
      请按每 tick 流程行动, 输出你的动作和本拍回执 JSON。"
   - 调 8787 一次 (temperature=0, max_tokens=2000, enable_thinking=false)
   - 机械断言 (不判语义, 只查特征):
     a. 输出同时含 "37" 和 "40"
     b. 输出含验证动作词之一: 磁盘 / wc / 一手 / 待核验 / 核
     c. 输出含 "thinking_log" 或 "signal"
   - 全过打印 "BEAT PASS", 任一失败打印失败项非零退出
   - 把完整输出存 receipts/drill-D4-beat.json ({raw: ..., asserts: {a,b,c}})
2. 运行 `python3 sim_beat.py`
   - 若挂: 把 raw 输出原样贴进汇报 (Lead 判是模型不服从还是断言太严), 不改断言重跑
3. commit: add sim_beat.py + receipts/drill-D4-beat.json, 一条 commit

## 边界
- 只发 1 次 LLM 调用 (8787 上有其他实验在跑, 别循环重试, 挂了直接汇报)
- 不改 executor-protocol.md / trigger_detector.py
- 不动 receipts/ 其他文件

## 验收 (Lead 核)
- BEAT PASS 与否 + raw 输出里模型的思考轮行为 (Lead 读 raw 判语义)
- 汇报 1 行: BEAT PASS? + 模型做了啥 (一句话) + commit hash
