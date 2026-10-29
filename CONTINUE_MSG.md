# CONTINUE_MSG — pfb 工作区

## 当前状态 @ 2026-10-30 06:40 +0800

**RUBRIC-V3-FULL-AUDIT / G2 构念效度根因 goal 收口（六阶段全过，merge main @ 7d17452）**：
- F1 公式层排除：双 judge 62/62 w2 按公式精确复算一致
- F2 主根因（双源）：(a) 双 judge 共同零命中高估——N-1/N-2（hr=0）占 new top-5 两席；(b) 新 judge 保守下界效应——5 节点 p̃≤0.1→≥0.3，gold N-3.2.2 被挤出 top-5（w3 20.58→7.89）
- F3/F4 判据层：gold set 维持冻结（r71b）；top-5≥3/5 超几何基线 P(X≥3)=1.99% 极严，单 judge 通过与否均不构成强证据
- R4 边界：双 judge 同族（qwen3.8-27b），结论限同族范围
- 工件：bench/rubric-v3/ablation/g2-rootcause.md（含 31 节点附录表 + 三修复选项 O1/O2/O3）+ stages/01-04.5 RV3G2-* + G1 机判脚本 assert-g1-audit.py 入库
- goal-queue 已注记 G2 完成

## 下一步（按优先级）

1. **P0 · RUBRIC-V3-FULL-AUDIT / G1 loop 工件补齐**：机判脚本已跑通（exit 0，S1-S4 信号产出）但六阶段 loop-artifacts 缺失。开子 goal ralph/rubric-v3-audit-g1：01 分解（抽检协议/p̃ 分布检查设计）→ 02 web-llm（预期失败回执）→ 02.5 → 03 → 04（跑脚本落数字：A1-A4 PASS + S2 ρ_orig=0.456 LOW-CORR / S3 三红旗 N-1,N-1.1,N-5.3 / S4 w2 gap top3）→ 04.5 → commit merge。注意任务书要求「随机 30% 节点独立重判报一致率」——脚本目前做的是 evidence 逐字核验（S1），语义级独立重判需 subagent 盲重判 75 样本 cell，若本轮做不完就登记降级（evidence 逐字核验作为形式一致率交付，语义重判标 unverified）
2. **P1 · G3 W3/W4 收尾**：消费 g2-rootcause.md 三选项；启动前先查 R5.2-third-scorer 状态决定路径（O2 依赖它）
3. **P2 · C3 v3 paired runs**（WORK_QUEUE 项）：前置 G1 盲标+仲裁 → G2 judge 实测（仍阻塞于 judge 家族隔离，等用户决策）→ G3-G5 门禁
4. **P2 · 回 arena 会话 01a18567 取 307 行 survey 原文回填 research/interpretability/literature-survey.md**
5. **P2 · 评估 :8787 node 网关容量竞争根因**（cron 400 too large 元凶），决定是否切直连 :8000

## 阻塞项

- **judge 家族隔离**：ninfer 只有 qwen3.8-27b（Qwen 家族），C3 v3 的 G2 judge 实测需异源 → 等待用户决策
- **web-llm 三 provider 登录态失效**：perplexity/chatgpt/gemini 全部 error → 需人工浏览器登录（一次性 web-llm-authorize）；各 goal 按失败降级继续
- **R5.2-third-scorer 外部依赖**：需 arena 通道或第三本地模型（不同家族）
- **σ_d 无先验数据**：MDE/n_task 反推待 pilot 数据

## 分支状态

- main @ 7d17452（= origin/main，G2 已 merge + push 验证）
- ralph/rubric-v3-audit-g2 @ 7d17452（收口分支，可删）