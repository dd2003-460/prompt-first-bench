# APPROVALS — 审批队列

| 日期 | 事项 | 来源 | 依据 | 分支 |
|---|---|---|---|---|
| 2026-11-01 | o3-claim-list.md §4.3 措辞修改（κ 预注册下限 → 具体公式数字 κ_fleiss<0.6 β沿用 γ降SIGNAL） | KAPPA-U1K1-DISPOSITION 执行 D4 | D P1 双判者对照播报确认处置通道 | ralph/kappa-u1k1-execution |

## [2026-11-26 19:30] T5-r: CLAUDE.md 调度器节合入 main（保护文件）
- 内容：从 thinkmech-review 分支移植 CLAUDE.md「触发词：先压后展」调度器节（已验证版本，pfb-thinkmech worktree 现存）
- 原因：D 2026-11-26 质疑 learn-to-think 未完全应用；核验发现 T5 半应用（ROUTING.md 已落 main d6d1b09bc，调度器节仅存 thinkmech-review 分支）
- 回滚点：pfb main 当前 HEAD（d6d1b09bc 之后）
- 状态：待 D 批准

## [2026-11-26 19:35] T6-L: stage-gate 仓新增 mechanisms 模块（框架源码改动）
- 内容：新增 stage_gate/mechanisms/{registry.json,check.py} + gate 推进前活性检查 + project-tidy 巡检接线
- 性质：新增模块（不改现有 hook 行为），回滚点=改动前 stage-gate HEAD
- 状态：按 T1/T4 先例执行（新增模块可逆，git revert 可回滚），改完告知 D
