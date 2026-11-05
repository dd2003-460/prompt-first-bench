# 任务书 · run2（arena agent mode · §3.0 链路 R3.2）

> 来源：dd2003-460/prompt-first-bench · 2026-10-24 · Lead: 成璐数字分身（DSH session-1c44f689）
> 优先级：P-1 自身优化（token 效率/harness/prompt）

## 强制段（arena 必读）
1. 按 loop 01→04.5 走（断点 A/B/C 门禁：A=仓库可拉取 / B=任务书完整 / C=产出可 push）。
2. 每步声称成功必须挂 ≥1 个不可伪造锚点（命令退出码 / 文件 git hash / ls-remote 回执 / 外部 API 状态）——M7 gate，无锚点=不得声称成功。
3. 产出落盘到本仓库 bench/r3/run2/ 下（01-decomp.md / 02-research.md / 04.5-review.md），commit + push。
4. 降级如实标注（不可用通道标 degraded + 原因），禁止虚构。

## 任务
审查 sop/goal-template.md §3.0 的**成本结构**（与 run3 的执行性审查正交）：
1. §3.0 标准链路 9 步中，哪 2-3 步是 token 消耗大头？给出你的估计依据（步骤的输入/输出规模）。
2. 如果要把整条链路的 token 消耗降 30%，最小改动是哪 1-2 个？（只改 prompt/SOP 层面，不改 harness）
3. 每个建议给一个可验证的度量方式（跑什么、看什么数）。

## 验收（可机器检查）
- bench/r3/run2/04.5-review.md 存在且含 3 个问题逐条回答 + 锚点
- push 后 ls-remote HEAD 更新（Lead 侧验证）
- 每步锚点数 ≥ 步数（M7 gate 100%）

## 交接
- 上一轮工件：bench/self-opt-tester/（r1）+ r2 交叉验证回执
- loop 阶段定义：loop/prompt-first/01-goal-decomposition.md ... 04.5-final-review.md
