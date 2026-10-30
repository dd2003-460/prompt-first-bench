# CONTINUE_MSG — pfb 工作区

## 当前状态 @ 2026-10-30 +0800（r122 后）

**RV3G6-audit8-erratum goal 收口（六阶段全过，merge main @ a7c549b = r122）**：
- AUDIT-report.md §8 gmr 绝对值勘误 E1-E6 落地：W1 [2.60,6.40]→[8.60,12.40] / W2-orig [7.80,8.00]→[8.20,8.40] / W2-new [5.20,6.60]→[8.80,10.20] / W3-W4-new [6.80,7.00]→[7.40,7.60]；L109 错误结论句「W1 最优可优于 W3-orig」→「仍劣于」（正确值下原句不成立）
- freeze doc §4 byte-exact 块重抄录为 erratum 后文本（单一事实源维持）+ §4.1 处置句更新注记
- 新增 `assert-audit8-erratum.py` 防漂移脚本：21 PASS/0 FAIL + 变异测试有效（改回旧值 exit 1 / 恢复 exit 0）
- 定性结论零改动且更强（W1 连「换 tie-break 反超」可能性都不存在）；冻结数据零修改
- 执行过程问题：claude 子进程 max-turns(200) 耗尽（核心修订完成但 04/04.5/queue/commit 未做）+ 断言脚本语法损坏（f-string 笔误 + byte-exact 比对漏去 BEGIN 注释行）→ Hermes 收口修复两处后全绿。教训：**claude 产出的脚本必须 Hermes 侧实跑验证才算落地**
- U3 未并入项（「gmr 6.4→8.6」口径归属）导出新候选 RV3G6-gmr-caliber-u3 入队

## 下一步（按优先级）

1. **P0 · 取 queue 队首未完成 goal 继续 ralph loop**：当前队首 = RV3G6-o3-claim-rejudge（claim 级独立重判执行，需 arena 会话通道——工具纪律禁 subagent）；备选纯仓库内项：RV3G6-gmr-caliber-u3（U3 口径裁定，工作量小）/ RV3B1-webllm-receipt-per-goal（回执分文件约定，极小）/ RV3B1-prompt-side-freeze（D2 写入 prompt 文件，batch2 R-09 前置）。注意：o3-claim-rejudge 若走 claude -p 派发会撞 web-llm 登录失效 + 248 cell 工作量大概率再爆 max-turns——建议先做小项收口节奏，大项评估拆子 goal
2. **P1 · C3 v3 paired runs**（WORK_QUEUE 最高优先未完成项）：前置 G1 subagent 盲标+仲裁 → G2 judge 实测 → G3-G5 门禁；ninfer HTTP :8000 直跑（不走 arena）。阻塞：judge 家族隔离（ninfer 只有 qwen3.8-27b）等用户决策
3. **P2 · 回 arena 会话 01a18567 取 307 行 survey 原文回填 research/interpretability/literature-survey.md**
4. **P2 · 评估 :8787 node 网关容量竞争根因**（cron 400 too large 元凶），决定是否切直连 :8000
5. **P2 · rubric-v3 遗留 #1「独立 judge 盲测 p̃」**：决定性检验，需 ≥3 个独立 LLM 服务盲估 31 节点 p̃ 对照 prior-estimates.json 算一致性——另开 goal

## 阻塞项

- **judge 家族隔离**：ninfer 只有 qwen3.8-27b（Qwen 家族），C3 v3 的 G2 judge 实测需异源 → 等待用户决策
- **web-llm 三 provider 登录态失效**：perplexity/chatgpt/gemini 全部 error → 需人工浏览器登录（一次性 web-llm-authorize）；各 goal 按失败降级继续（本 goal 已按此口径在 02.5 工件标注 unverified）
- **R5.2-third-scorer 外部依赖**：需 arena 通道或第三本地模型（不同家族）
- **σ_d 无先验数据**：MDE/n_task 反推待 pilot 数据

## 分支状态

- main @ a7c549b（= origin/main，r122 audit8-erratum 已 merge + push 验证）
- ralph/rv3g6-audit8-erratum @ a7c549b（收口分支，可删）
- 历史收口分支（r112-r121 系列，均可删）：ralph/rubric-v3-audit-g1..g5 / ralph/rv3g6-* 等