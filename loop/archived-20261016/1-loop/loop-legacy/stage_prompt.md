# RALPH 当前阶段执行 Prompt

此文件名为历史兼容别名，内容协议统一由 `stage_prompt_fieldcentric.md` 提供。
运行时不会再启用 task card、强制 auditor card 或 `RALPH_TASK_CARD` 派发门禁。

请使用当前阶段目录中的增量字段文件：

```text
ralph field-init .
ralph field-apply . loop-artifacts/stages/<stage>/<revision>/fields.json
ralph apply . loop-artifacts/stages/<stage>/<revision>/advance.json
```

字段缺失时多轮补写；JSON 错误只修复草稿并重复 `field-apply`，不要直接编辑 `loop-state.json`。
