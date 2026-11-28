# 任务卡: 触发器检测器 selftest D1b (2026-11-28)
# origin: ai (Lead 派发)
# 被测对象: tasks/agent-orchestration/trigger_detector.py (commit 3ff59cb7b, 已验证三信号可触发)

## 执行
1. 写 `tasks/agent-orchestration/test_trigger_detector.py` (stdlib only, ≤60 行):
   - 6 个 case, 每个构造临时输入文件 (tempfile), 调 detect(), 断言 signal 字段:
     - 缺口: plan 含无出处数字 "精度 0.92" (行内无 path/commit/运行/@) + 空回执 → 缺口
     - 矛盾: plan 含 "得分 0.87" + 回执 evidence 含 "0.92" 同主题词 → 矛盾
     - 卡住: 回执 last_op=X + 再次传同 last_op + diff_empty=True → 卡住
     - none: plan 全是有出处数字 ("精度 0.92 @run-12") + 空回执 → none
     - none: 空 plan + 空回执 → none
     - count 累计: 同 case 连调两次, 第二次 count=2
   - 输出: 全过打印 "ALL 6 PASS", 任一失败打印失败 case 名并以非零码退出
2. 运行 `python3 test_trigger_detector.py`, 必须 ALL 6 PASS
   - 若某 case 挂: 先看是测试构造错还是检测器 bug。构造错→改测试; 检测器 bug→在汇报里写明 bug 位置, 不改检测器 (改检测器是 Lead 决定)
3. commit: 只 add test_trigger_detector.py, 一条 commit

## 边界
- 不改 trigger_detector.py (bug 只汇报)
- 不跑 LLM, 不碰 8787, 不动 oood-probe/ 目录 (另一任务在跑)

## 验收 (Lead 核)
- 测试文件 ≤60 行, 运行输出 ALL 6 PASS
- 汇报 1 行: PASS 数 + 有无检测器 bug + commit hash
