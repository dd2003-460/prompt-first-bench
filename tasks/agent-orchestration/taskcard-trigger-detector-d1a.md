# 任务卡: 触发器三信号检测器 D1a (2026-11-28)
# origin: ai (Lead 派发)
# 背景: 执行者循环要硬触发思考轮, 检测器=机械脚本 (不占模型 token)。设计: tasks/agent-orchestration/trigger-impl-design-20261128.md §1-2。你只需执行。

## 真值 (带出处)
- 三信号定义: 矛盾=本拍要写的事实与任务卡真值节/上拍回执不一致; 卡住=同操作连续 2 拍 git diff 为空; 缺口=产出含具体值但无出处标注 (数字后无 路径/commit/运行号) 或结论来源计数=1
- 回执格式: tasks/agent-orchestration/executor-protocol.md (读该文件的回执 JSON 节, ~30 行, 别读全文)
- 输入输出契约: 输入=上一拍回执 JSON 路径 + 本拍计划文本路径; 输出=trigger.json {signal: none|矛盾|卡住|缺口, evidence: str, count: 同信号累计次数}

## 执行
1. 写 `tasks/agent-orchestration/trigger_detector.py` (stdlib only, ≤80 行):
   - `detect(prev_receipt_path, plan_path) -> dict` 按上面契约
   - 矛盾: 从 plan 文本抽含数字的句子, 与 prev_receipt 的 evidence/数字字段比对 (字符串级, 不做语义)
   - 卡住: prev_receipt 有 last_op 字段且与本次相同 + diff_since 为空 (参数传入)
   - 缺口: 正则 `[\d.]+` 命中但同行无 `(path|commit|运行|@)` 类标注
2. CLI: `python3 trigger_detector.py <prev_receipt> <plan> [--diff-empty]` → stdout 打印 trigger.json
3. commit: 只 add trigger_detector.py, 一条 commit

## 边界
- 不写 selftest (那是 D1b, 你的任务到此为止)
- 不动 executor-protocol.md / 回执 schema (D2 的事)
- 不跑 LLM, 不碰 8787

## 验收 (Lead 核)
- 脚本 ≤80 行, python3 编译过
- 手工喂一个含无出处数字的 plan + 空回执 → 输出 signal=缺口
- 汇报 1 行: 三信号各能触发? + commit hash
