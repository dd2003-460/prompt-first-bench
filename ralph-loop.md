# RALPH Prompt-First Loop

<!-- ralph-prompt-state
stage: 01
revision: r1
status: running
current_artifact: loop-artifacts/prompt-first/01-factor-decomposition.md
review_status: idle
review_stage: 
review_artifact_sha256: 
review_attempt: 0
review_return_code: 
-->

## 原始任务（请勿改写）

RV3G4-prior-source-assert — G4 强制机械化候选落地：assert 脚本校验 prior-estimates.json 必须记录 ≥N 个独立 p̃ 生成源（source 字段缺失/单源 = FAIL），参考 R5.2 系列 assert-* 模式

## 机械说明

这个文件只保存阶段游标，不评价内容质量。阶段内容全部写在当前 Markdown 工件中。
主工件停止写入后，Stop Hook 自动启动独立 Reviewer。Reviewer 读取 loop/prompt-first 中的规则和当前工件，输出问题、证据缺口与 pass/revise 路由。
只有当前工件对应的 Reviewer 明确 pass，且之后写入 `<!-- ralph: done -->`，才进入下一阶段；revise、缺失、过期或无效回执都留在当前阶段。
不要手动编辑本文件的阶段游标或原始任务；它由 Stop Hook 机械维护。普通项目工件可自由读取和写入。
