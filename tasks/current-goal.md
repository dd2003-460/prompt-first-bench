# origin: ai — 当前 goal（2026-10-31 stop-hook 唤醒 · r52）

【目标】R5 run5 本地降级执行：arena 通道不可用（ls-remote 无新分支、仓库内无 ego-browser），按任务书「降级如实记录，禁虚构」条款走本地 :8787 qwen3.8-27b 单源链路。9 步链路中需外部交叉验证的步骤（步骤 4/5）标 unverified+登记边界，其余 7 步完整执行。产出 m8-proposal.md + 回执。

【阶段】收口（r52）— 9 步完成 7 完整 + 2 unverified，main @ 12ca0dc；queue 核销 r53 @ f2531ec。下一步：取 goal-queue 下一可执行项（当前 8 项全部 blocked-on-human/external，除 RV3G3cdx-m4-u3-first-blind-judge 前置仍未满足——v3 packet 未产出）。

【SOP 索引】bench/self-opt-tester/r5/run5/task-brief.md（9 步定义）；loop/prompt-first/01..04.5 精简走法（01 分解 + 03 行动 + 04.5 反方复核）。

【验收标准】
- bench/self-opt-tester/run5/m8-proposal.md 落盘（M8 定义 + M8/M3 共线性判断 + 依据）
- 回执 JSON 落盘 run5/receipt-r52-local.json（9 步锚点清单 + M1-M8 自评 + 降级声明）
- 步骤 4/5 的文献调研用仓库内已有材料（gap-analysis survey 等）替代，标 unverified
- commit+push main

【失败降级】:8787 不可用 → 登记边界跳过取下一 goal
