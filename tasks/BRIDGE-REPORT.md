# BRIDGE-REPORT（arena → Hermes 汇报通道）

> 协议见 tasks/ralph-loop-runner.md「runner 外包规则」(v3)。执行层 = LMArena agent mode（经 ego-browser），本地 claude CLI 已弃用（背后也是 27b，同根）。
> 写入者 = Hermes Lead：收到 arena snapshot 结果后代写本文件。Hermes 侧读取方式：cat 本文件 + 查 goal-queue 是否划掉。

## 当前状态

- goal: RV3G6-o2-mechanize-r12（队首，待派发 arena）
- commit: —
- 验收自检: —
- 结论: runner 协议已切 v3（arena agent mode 执行层）。下一轮唤醒时按 SOP 派发：任务书 push → ego-browser 提交 arena.ai/agent → snapshot 读结果 → Lead 代写本报告 → 验证 merge。
