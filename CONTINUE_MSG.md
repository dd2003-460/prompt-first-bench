# CONTINUE_MSG — pfb 工作区

## 当前状态 @ 2026-10-30 +0800

**RUBRIC-V3-FULL-AUDIT / G1 矛盾审计 goal 收口（六阶段全过，merge main @ 9f8a1f9 = r109）**：
- F1 数据自洽确立：A1 结构 248/248 PASS + A2 O3 复算 24/24 精确一致（W3/W4 另 16/16）→ 计算层排除
- F2 抽检：seed 20261030 抽 75/248（30.2%），覆盖 30/31 节点；**形式一致率 35/35=100%**（h=1 方向 evidence 逐字核验，S1）；语义级独立重判 unverified（禁 subagent，降级登记 + arena 补数路径已入队 RV3G1-semantic-rejudge）
- F3 p̃ 分布：ρ_orig=0.456 LOW-CORR / ρ_new=0.629 / cross=0.688；二项式红旗 3 节点（N-1 高估 / N-1.1+N-5.3 低估——双向偏差）
- F4 矛盾清单 C1-C4 落盘 `bench/rubric-v3/ablation/G1-contradiction-audit.md`（每条带 evidence + 31 节点双 judge 对照表 + 四方案分数表 + 负面结果声明）
- **新发现供 G3**：(a) per-run top-5 口径下四方案（W2/W3×orig/new）无任何 run 达 ≥3 gold 标记（max=2，run4/run5 全 0）——blindtest 的 global top-5 已是较宽松口径；(b) W2-new 下 run1 反超 run6（W2 方案的 run 排序对 p̃ 来源不稳定）
- 冻结数据零修改；工件 stages/01-04.5 RV3G1-* + current-goal 改写

## 下一步（按优先级）

1. **P0 · RUBRIC-V3-FULL-AUDIT / G3 W3/W4 收尾**：消费 g2-rootcause.md 三选项（O1 改判据 / O2 第三 judge / O3 接受降级）+ G1 新发现（per-run 口径更不可能通过 → O1 若走应优先 top-10/AUC 类降头部敏感性方案）。启动前先查 R5.2-third-scorer 状态决定 O2 可行性。stats-w3w4.json 补完验证链走完
2. **P1 · G4 漏洞对照**：gap-analysis Q2 五条结构性解释逐条对照协议（receipts/rubric-v3-gap-analysis.md，git show aea3d6b 取）
3. **P2 · G5 优化清单 / G6 综合报告**（AUDIT-report.md 含 ResearcherBench/RACE 差异表 + 负面结果声明）
4. **P2 · RV3G1-semantic-rejudge**（新入队）：arena 通道补 G1 语义一致率
5. **P2 · C3 v3 paired runs**（WORK_QUEUE 项）：仍阻塞于 judge 家族隔离，等用户决策
6. **P2 · 回 arena 会话 01a18567 取 307 行 survey 原文回填 research/interpretability/literature-survey.md**
7. **P2 · 评估 :8787 node 网关容量竞争根因**（cron 400 too large 元凶），决定是否切直连 :8000

## 阻塞项

- **judge 家族隔离**：ninfer 只有 qwen3.8-27b（Qwen 家族），C3 v3 的 G2 judge 实测需异源 → 等待用户决策
- **web-llm 三 provider 登录态失效**：perplexity/chatgpt/gemini 全部 error → 需人工浏览器登录（一次性 web-llm-authorize）；各 goal 按失败降级继续
- **R5.2-third-scorer 外部依赖**：需 arena 通道或第三本地模型（不同家族）
- **σ_d 无先验数据**：MDE/n_task 反推待 pilot 数据

## 分支状态

- main @ 9f8a1f9（= origin/main，G1 已 merge + push 验证）
- ralph/rubric-v3-audit-g1 @ 9f8a1f9（收口分支，可删）
- ralph/rubric-v3-audit-g2 @ 7d17452（收口分支，可删）