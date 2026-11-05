# 03 — RV3G3-threshold-crossdomain-reverify 核销轮 · 行动分解

> goal: queue 队列卫生修复 + 核销验证 · 分支 ralph/rv3g3-threshold-crossdomain-reverify-close · 2026-10-30

| # | 动作 | 落点 | 验收 |
|---|------|------|------|
| A1 | 回归基线实跑（X3 表七脚本，仓库根执行，输出+exit code 全捕获） | 04 工件内联记录 | 七项全部与 X3 预期一致；任一不一致 → 失败降级 |
| A2 | crossdomain 输出 byte-exact 复核（od -c 尾部字节 = `\n` 结尾、无 stderr 混入） | 04 工件内联记录 | 两行 stdout 与 X3 第一行逐字相等 |
| A3 | queue L28 翻转：`- [ ]` → `- [x]`，日期 (2026-10-30, r145) 并入既有注记头，追加核销句「r145 核销轮——97d2adf 收口 message 声称划掉但 checkbox 漏翻，本轮补翻 + 基线复验零漂移」 | tasks/goal-queue.md L28 | diff 面 = 该行 1 处替换 |
| A4 | 新导出候选追加（queue 底部，≥1） | tasks/goal-queue.md 末尾 | 见下 |
| A5 | 冻结面终验（git status + git diff main --stat 十件冻结文件） | 04 工件 | 改动面 ⊆ {goal-queue.md, current-goal.md, stages/*} |

**A4 新导出候选（两条）**：

1. `RV3G3cdx-batch2-schema-lint` —— batch2 三输入文件的 schema lint 独立化：assert-goldrank-crossdomain.py 的 schema 校验目前与 (a)(b) 判定同脚本（exit 2 fail-loud 分支），batch2 数据到来前可先落一个轻量 lint-only 入口（或 CLI flag `--lint-only`），供数据提供方在写入 bench/rubric-v3/ablation/batch2/ 前自验，降低 RV3G3-batch2-arrival-closure 执行时的往返成本。纯仓库内，~5 回合。产投比依据：r140 docstring 已预注册字段级 schema（lint 规则零新增设计成本）。
2. `RV3G3cdx-queue-hygiene-sweep` —— queue 卫生例行扫描：对「已完成区 + 新导出候选区」全部 `[x]`/`[~]` 行做 message↔状态一致性抽查（commit message 声称的动作 vs queue 实际状态位），防 97d2adf 型漏翻复发。纯仓库内 grep/git show 工作，~3 回合，可在任意空闲轮执行。产投比依据：本轮即为该缺陷的实证实例（message 说「划掉」、状态仍 `[ ]`，跨 r141-r144 四轮无人发现）。