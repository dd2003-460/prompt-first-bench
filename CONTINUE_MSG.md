# CONTINUE_MSG — pfb 工作区

## 当前状态 @ 2026-10-30 +0800

**RUBRIC-V3-FULL-AUDIT / G5 优化清单 goal 收口（六阶段全过，merge main @ 1b20906 = r112）**：
- 机判化候选 C1-C6：p̃ 多源断言（~2回合，含 schema 提案）/ κ 回执断言（~2回合，含 schema 提案）/ W3W4 复算断言（~3回合，含 spearman）/ w2 公式断言（~1回合）/ spearman 一致性断言（~1回合）/ gold 单源检测（登记不实施）。合计 ~9 回合（合并后 ~7）。
- 并行化候选 P1-P5：P1 p̃ 多 LLM 盲生成（信息边界·外部依赖不可控）/ P2 κ 换位双判（信息边界·异族 judge 阻塞）/ P3 第二格实验（信息边界·gold 构建+对齐设计）/ P4 8 run 重跑（BLOCKED by finding #17 变体未冻结，需先修 DRAFT ~2回合）/ P5 arena 语义重判（风险最低，样本清单已就绪，~3回合）。
- 成本估算总表：12 blocker 三级分类——L1 文本修订×5（B3/B6/B9/B10/B11）≈ 10 回合 + L2 协议重设计×7（B1/B2/B4/B5/B7/B8/B12）≈ 22 回合 = **~32 回合**。B2 完整修复路径（异族 judge/双 gold）= 信息边界。16 major 粗略分布 ~8 L1 + ~8 L2（逐条处置属 G6 范围）。
- 负面结果声明六条：W0 构念效度退化（flat 权重完全平局）/ W1 gmr tie-sensitive [9.60,13.40]（"W1 最差"表述需修正）/ new W3 top5_gold tie-sensitive [1,2]（id tie-break 下 1/5，其他规则可能 2/5）/ per-run 无 run 过线（max=2，所有 scheme×judge）/ 语义级重判不可机判 / κ 值计算本身不可机判。
- G6 导出：建议前落地 5 项（B10 变体冻结 / B3+B11 §4 题面修订 / B6 计分规则统一 / C4 w2 断言 / C3 W3W4 复算断言，合计 ~10 回合）；硬约束提醒 3 条（S2 限定语 / 32 findings 处置表 / tie-sensitivity 限定语）。
- 交付物 `bench/rubric-v3/ablation/g5-optimization-list.md`（五节结构）；冻结数据零修改；新候选 RV3G5-blocker-disposition-table 入队。

## 下一步（按优先级）

1. **P0 · RUBRIC-V3-FULL-AUDIT / G6 综合报告**：`bench/rubric-v3/AUDIT-report.md` — G1-G5 综合 + rubric-v3 定稿建议（维度保留/修改/废弃 + 理由）+ ResearcherBench/RACE 差异表 + 负面结果声明；G6 拥有 O1/O2/O3 终裁权（消费 RV3G3-goldrank-threshold-proof 若届时已完成；应用 S2 硬约束——O3 数字必须声明「相对 Lead-gold」；32 findings 处置表至少 12 blocker 逐条采纳/拒绝/延后；tie-sensitivity 限定语强制执行）。交叉引用 g5-optimization-list.md §5「给 G6 的导出」
2. **P1 · RV3G5-blocker-disposition-table**（新入队）：adversarial-check 32 findings 逐条处置表，消费 G5 成本估算 3b 节 L1/L2 分级，锁定每条最终成本；属 G6 定稿核心输入但可独立先行
3. **P2 · RV3G1-semantic-rejudge**：arena 通道补 G1 语义一致率（样本清单已就绪）
4. **P2 · RV3G3-goldrank-threshold-proof**：gold 平均排名过线阈值正式论证，纯仓库内推导
5. **P2 · RV3G4-prior-source-assert / RV3G4-kappa-receipt-assert**：G4 强制机械化候选落地，工作量小，纯仓库内
6. **P2 · C3 v3 paired runs**（WORK_QUEUE 项）：仍阻塞于 judge 家族隔离，等用户决策
7. **P2 · 回 arena 会话 01a18567 取 307 行 survey 原文回填 research/interpretability/literature-survey.md**
8. **P2 · 评估 :8787 node 网关容量竞争根因**（cron 400 too large 元凶），决定是否切直连 :8000

## 阻塞项

- **judge 家族隔离**：ninfer 只有 qwen3.8-27b（Qwen 家族），C3 v3 的 G2 judge 实测需异源 → 等待用户决策
- **web-llm 三 provider 登录态失效**：perplexity/chatgpt/gemini 全部 error → 需人工浏览器登录（一次性 web-llm-authorize）；各 goal 按失败降级继续
- **R5.2-third-scorer 外部依赖**：需 arena 通道或第三本地模型（不同家族）→ G4 确认为 S2 闭环前置条件之一（双 gold 或异源 judge 二选一）
- **σ_d 无先验数据**：MDE/n_task 反推待 pilot 数据
- **DRAFT 变体矩阵未冻结**（finding #17 blocker）：P4 8 run 重跑 BLOCKED；G6 定稿需先完成 B10 修订

## 分支状态

- main @ 1b20906（= origin/main，G5 已 merge + push 验证）
- ralph/rubric-v3-audit-g1 @ 9f8a1f9（收口分支，可删）
- ralph/rubric-v3-audit-g2 @ 7d17452（收口分支，可删）
- ralph/rubric-v3-audit-g3 @ f17206d（收口分支，可删）
- ralph/rubric-v3-audit-g4 @ 5b0a62b（收口分支，可删）
- ralph/rubric-v3-audit-g4-fix @ 9946960（勘误分支，可删）
- ralph/rubric-v3-audit-g5 @ 1b20906（收口分支，可删）