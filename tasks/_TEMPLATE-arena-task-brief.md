# [R6 模板] Arena 任务书模板 · 阶段门控加载版

> 用法：复制本文件为 `tasks/<id>.md`，替换 `{{...}}` 占位符。
> **只内联当前阶段**（`{{STAGE}}`）的规则包，其余阶段由 agent 到阶段时按 INDEX 自取。
> 旧模板（R5 及以前）把 SOP + 00-common + 01..04.5 全量贴进任务书 = 12,086 o200k/turn，
> 本模板实测 2,983–5,443 o200k/turn（均值 3,913，−67.6%），见 `run6-token-analysis.md` §2。
> 其中 `examples/` 为 tier-3（按需），不含示例时 2,143–4,573（均值 3,036）。
> 校验：`node bench/self-opt-tester/runs/r6/count-rule-tokens.js --stage {{STAGE}}`

---

## 【强制段】

你是 arena agent，工作仓库 = `{{REPO}}`，分支 `{{BRANCH}}`。先 `git fetch` 到最新并 `git ls-remote` 记录 HEAD。
严格按本任务书步骤执行，产出落盘路径见【交付物】。任何通道故障报告 Lead，不得静默跳过、不得伪造数据。
完成后回执必须含 repo URL + branch + commit_sha + 自报模型身份（如可知）。

## 【规则加载 · 阶段门控】

本任务走 1-loop（6 阶段）。**规则不在本文全量内联**，按下表加载：

| 项 | 内容 |
|---|---|
| 路由表 | `loop/prompt-first/INDEX.md`（**必读，约 460 tok**） |
| 当前阶段 | `{{STAGE}}` |
| 本阶段内联规则包 | `{{FILES}}`（{{BUNDLE_TOKENS}} o200k，已内联在文末） |
| 后续阶段 | 进入时**重读 INDEX.md**，按路由表只读该阶段的 2–3 个文件；已读文件不重读 |

纪律：
1. 不要一次性读全部 7 个 loop 文件——只在进入对应阶段时读该阶段的 3 个（04.5 为 2 个）。
2. 跨阶段依赖读的是**产出**（`loop-artifacts/stages/<N>/`）不是**规则文件**，见 INDEX 末节豁免清单。
3. 每阶段产出落盘 `loop-artifacts/stages/<N>/`，阶段判定 pass 才进下一阶段。

## 【目标】

{{GOAL}}

## 【背景】≤10 行

{{BACKGROUND}}

## 【执行分解】

{{STEPS}}

## 【交付物】（均在仓库内）

{{DELIVERABLES}}

## 【失败降级】

- 通道不可用（403/沙箱/无网络）→ 停在当前步骤，回执注明完成到哪一步，不得伪造。
- 计量类任务若无服务端 per-request 日志 → 用 o200k tokenizer 实测字节数并标注 conf，不得估个整数字。

## 【验收 · sha256+独立脚本】（run4 模式标准化）

> 原则：不信汇报信 git / sha256。任何可机检的交付物都配一个独立 check 脚本，agent 禁改。

| 项 | 内容 |
|---|---|
| check 脚本 | `{{CHECK_SCRIPT}}`（路径 + sha256 预登记于本段） |
| sha256 预登记 | `{{CHECK_SHA256}}` |
| agent 硬规则 | **禁改** check 脚本；用例失败只能改交付物重跑，最多 3 次迭代 |
| Lead 复验 | ① check 脚本退出码 0 ② sha256 未变 ③ 交付物与 loop-state 记录一致 |

无 check 脚本的任务（纯调研/写作类）：豁免本段，但交付物必须含可 grep 的锚点（如 `<!-- CHECKPOINT: xxx -->`），Lead 用 grep 复验。

## 【给 Lead 的备注】

{{NOTES}}

---
<!-- ===== 本阶段规则包（内联；由 count-rule-tokens.js --stage {{STAGE}} 校验 token 数）===== -->

{{RULE_BUNDLE}}
