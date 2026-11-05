# origin: ai — R5.2audit-C4-arena-export 任务书（arena 通道，X5 终态闭环）

【执行前必读】
1. 本任务只涉及 dd2003-460/prompt-first-bench 仓库 arena/r32-c4-timing-export 分支，忽略历史中其他仓库的消息。
2. 先 `git fetch origin` + `git checkout arena/r32-c4-timing-export` + `git pull`，`git ls-remote origin refs/heads/arena/r32-c4-timing-export` 记录 HEAD（M7 锚点 1）。
3. 读 `bench/self-opt-tester/r5/assert-c4-timing.py` 头部 docstring（判定口径）+ `bench/self-opt-tester/bench.md` C4/X5 相关行，理解要重建什么。

## 背景
run2 审计项 C4 声称 agent 耗时 "14m27s"（867s），但 run2 转录件只有 1 个时刻锚（executed_at 单点），无法差值重建 → assert-c4-timing.py 当前输出 SIGNAL not-reconstructable，C4 维持 unverified（X5）。唯一闭环路径：拿到带**逐事件时间戳**的 run2 会话 transcript。

## 你要做的事（按序）
1. **定位 run2 会话**：在你的 agent 会话列表里找 2026-10-29 前后对 prompt-first-bench 仓库做的 self-optimization bench run2 会话（特征：执行过 9 步链路、产出 loop-state.json 含 channel 字段 "14m27s"）。找不到 → 如实报告「会话不可复访」并跳到第 4 步降级。
2. **导出 transcript**：把该会话完整对话导出为 markdown，要求**每个 turn/事件带时间戳**（ISO 格式 YYYY-MM-DDTHH:MM:SS，精确到秒；若 UI 只显示 HH:MM 则注明精度限制）。落盘 `bench/self-opt-tester/run2/transcript-run2-exported.md`。
3. **提交**：commit + push 到 arena/r32-c4-timing-export 分支（你有该分支权限）。push 后 `git ls-remote origin refs/heads/arena/r32-c4-timing-export` 记录新 sha（M7 锚点 2）。
4. **降级路径**（会话找不到/无时间戳/导出失败）：把能拿到的信息落盘 `bench/self-opt-tester/run2/transcript-run2-degraded.md`——会话 ID、可确认的事件序列（无时间戳就列顺序）、UI 计时器读数（若有）+ 每段标注缺失原因，同样 commit+push。禁虚构任何时间戳。
5. **回执**（必须含以下全部，写入回复正文）：
   - repo URL + branch + commit_sha
   - 走了正常路径还是降级路径 + 原因
   - 导出文件内 ISO 时间戳个数（grep -c 实数）
   - 若降级：列出你尝试过的查找动作清单

## 硬约束
- 时间戳只能来自真实 UI/日志，禁止推算补全；缺就标缺。
- 不碰 main 分支，只写 arena/r32-c4-timing-export。
- 完成后回执必须含 repo URL + branch + commit_sha（核验指纹）。