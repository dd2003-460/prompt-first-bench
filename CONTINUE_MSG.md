# CONTINUE_MSG — pfb 工作区

## 当前状态 @ 2026-10-30 05:30 +0800

**T8-matrix-run-r1 goal 完成（六阶段全过 + M8 计分 + design.md 回填）**：
- 域：团队文件协作/网盘选型（30 人研发团队，预算 ≤¥30,000/年）
- 推荐方案：坚果云 Team Standard（¥10,800/年，预算余量 64%）
- 备选：飞书标准版（能力优先）/ Nextcloud 自托管（自主可控）/ Seafile Pro（细粒度权限）
- M8 = **1.00**（形式真实性满分；核验强度受 web-llm 缺失压在 0.2 档）
- 三域趋势：0.93 → 1.00 → 1.00（平坦，无退化）
- 工件：stages/T8r1-{00,01,02,02.5,03,04,04.5} + runs/tselect-vfull-filecollab/{cost-model.json, m8-scorecard.md} + design.md 第 3 行回填

## 下一步（按优先级）

1. **P0 · commit + push T8 r1 全部工件**（本轮 A7 未执行——需 git add + commit + push + ls-remote 验证）
   - 新文件：loop-artifacts/stages/0{0,1,2,2.5,3,4}/T8r1-*.md + stages/04.5/T8r1-04.5-review.md + experiments/T8-matrix/runs/tselect-vfull-filecollab/ + experiments/T8-matrix/design.md（修改）
   - 分支：ralph/t8-matrix-run-r1（当前 HEAD = 026f868）
2. **P1 · C3 v3 paired runs**（WORK_QUEUE 最高优先未完成项）：前置 G1 subagent 盲标+仲裁 → G2 judge 实测 → G3-G5 门禁；ninfer HTTP :8000 直跑。G2 仍阻塞（judge 家族隔离），G3-G5 方案层可继续
3. **P2 · 回 arena 会话 01a18567 取 307 行 survey 原文回填 research/interpretability/literature-survey.md**
4. **P2 · 评估 :8787 node 网关容量竞争根因**（cron 400 too large 元凶），决定是否切直连 :8000
5. **新发现**：rubric-v3 遗留工作 #1「独立 judge 盲测 p̃」是决定性检验——若要做，另开 goal（≥3 个独立 LLM 服务盲估 31 节点 p̃）

## 阻塞项

- **G2 judge 家族隔离**：ninfer 只有 qwen3.8-27b（Qwen 家族），需异源 judge → **等待用户决策**（选项见 receipts/g2-judge-status-update.json）
- **web-llm 三 provider 登录态失效**：perplexity/chatgpt/gemini 全部 error → 需人工浏览器登录（一次性 web-llm-authorize）
- **σ_d 无先验数据**：MDE/n_task 反推待 pilot 数据

## 分支状态

- 本地：ralph/t8-matrix-run-r1 @ 026f868（+ 未 commit 的 T8 r1 工件）
- 远程：origin/main @ 026f868（已同步到 r78c）