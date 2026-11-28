# 任务卡: 执行者接入 + 触发演练 D3 (2026-11-28)
# origin: ai (Lead 派发)
# 前置: 检测器 trigger_detector.py (3ff59cb7b, selftest ALL 6 PASS ce8915edc) + 思考轮节 (0d123ead7, executor-protocol.md 末尾)

## 真值 (带出处)
- 执行者每 tick 流程在 executor-protocol.md `## 每 tick 流程（严格顺序）` 节 (行 9 起, ~30 行, 读该节别读全文)
- 检测器 CLI: `python3 trigger_detector.py <prev_receipt> <plan> [--diff-empty]` → stdout trigger.json {signal, evidence, count}
- 思考轮模板: executor-protocol.md `## 触发思考轮` 节 (D2 已加)

## 执行
1. 在 executor-protocol.md `## 每 tick 流程` 节插入一步 (≤6 行, 插在"认领任务"之后、"执行"之前):
   - 跑 `python3 tasks/agent-orchestration/trigger_detector.py <上拍回执> <本拍任务卡路径> [--diff-empty]`
   - signal != none → 按 `## 触发思考轮` 节跑思考轮, thinking_log 进本拍回执
   - signal == none → 直接执行
2. 写演练脚本 `drill_trigger.py` (≤40 行, stdlib):
   - 在 tempfile 造: 假上拍回执 (evidence 含 "节点数 40") + 假任务卡 (真值节含 "节点数 37")
   - 调 trigger_detector.detect() → 断言 signal == "矛盾"
   - 把 detect 输出存 `receipts/drill-D3-trigger.json` (这是演练证据, 放 receipts/ 下)
   - 再喂一组无矛盾输入 → 断言 signal == "none", 存 `receipts/drill-D3-none.json`
   - 全过打印 "DRILL PASS", 失败非零退出
3. 运行 `python3 drill_trigger.py`, 必须 DRILL PASS
4. commit: add executor-protocol.md + drill_trigger.py + receipts/drill-D3-*.json, 一条 commit

## 边界
- 不改 trigger_detector.py / test_trigger_detector.py
- 不动 receipts/ 里已有的真回执 (Q9E-Scan.json 等), 只加 drill-D3-* 两个新文件
- 不跑 LLM, 不碰 8787, 不改 queue_monitor.py

## 验收 (Lead 核)
- 每 tick 流程节多了检测器步骤, 顺序未被破坏 (Lead 会 diff)
- drill_trigger.py 运行 DRILL PASS, 两个 drill 证据文件存在
- 汇报 1 行: 插入位置 + DRILL PASS? + commit hash
