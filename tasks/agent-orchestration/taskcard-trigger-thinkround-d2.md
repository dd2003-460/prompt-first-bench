# 任务卡: 思考轮 prompt 段 + 回执 schema 变更 D2 (2026-11-28)
# origin: ai (Lead 派发)
# 设计依据: tasks/agent-orchestration/trigger-impl-design-20261128.md §2-3 (读这两节, 别读全文)

## 真值 (带出处)
- 思考轮固定模板 4 步 (复述信号→答"依赖吗"→按信号类型验证→写 thinking_log): 设计文档 §2 原文, 逐条搬, 不改语义
- 回执 JSON 现有字段: tasks/agent-orchestration/executor-protocol.md 的回执节 (读该节, ~30 行)
- thinking_log 格式: {signal: 矛盾|卡住|缺口, evidence: str, action: str, result: str} (设计文档 §2 第 4 步)

## 执行
1. 在 executor-protocol.md 末尾追加一节 `## 触发思考轮` (≤25 行):
   - 何时触发: trigger.json signal != none (检测器 trigger_detector.py 每拍输出)
   - 4 步模板: 从设计文档 §2 逐条搬
   - 边界: 思考轮限 1 轮; 同信号同证据 2 次触发 = 升级回执报监督者
   - thinking_log 字段定义 + 1 个完整 JSON 示例
2. 回执 schema 变更: 在 executor-protocol.md 回执节加一行说明 `thinking_log: 可选, 触发过必填 (无触发可省略)`——只加这一行, 不改其他字段
3. commit: 只 add executor-protocol.md, 一条 commit

## 边界
- 不改设计文档, 不改 trigger_detector.py, 不写测试 (D1b 在跑, 别碰 test 文件)
- 不跑 LLM, 不碰 8787, 不动 oood-probe/ 目录

## 验收 (Lead 核)
- 新节 ≤25 行, 4 步与设计文档 §2 逐条对应 (Lead 会 diff)
- 汇报 1 行: 加了哪两样 + commit hash
