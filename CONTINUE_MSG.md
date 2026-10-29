# CONTINUE_MSG — pfb 工作区

## 当前状态 @ 2026-10-30 +0800

**RUBRIC-V3-FULL-AUDIT / G3 W3/W4 收尾 goal 收口（六阶段全过，merge main @ f17206d = r110）**：
- F1 验证链闭合：W3 8/8 + W4 8/8 分数精确复算（W4=w1+w2 合成——prior-estimates.json 无 w4 字段）+ ρ 7/7 + tie 4/4 + top-5 strict 计数全通过 → **修正任务书「未走完验证链」表述**，真实缺口 = 独立 judge 维度（文件生成于 blindtest 之前）
- F2 敏感性分级：**W3 高**（头部 gap 0.0301→0.0020 近打平 + global top-5 gold 3/5↔1/5 翻转）；**W4 排序维度中**（8/8 位不变但头部 gap 收窄 0.0185→0.0050）**构念效度维度高**（gold 平均排名 6.4→8.6，与 W3 同幅）→ **W3/W4 都不单独值得救**（共享 p̃ 估计层病根）
- F3 决策矩阵：O1 推荐子选项 = **gold 平均排名口径**（唯一全部 7 方案×judge 组合方向一致：W3/W4 6.4/8.6 vs W1/W2 10.8/11.2），top-10 同级备选（W3 双 judge 均 4/10）；post-hoc model selection 显式声明；O2 外部阻塞本轮不可执行；O3 可行（代价重估 = 校准损失为主：W4-W1 差值 8/8 负 mean −0.0406，正交信息损失未证两说并存）
- 推荐路径（供 G6 定稿，非决策）：O1(gold 平均排名主判据) + O3 式声明并行，O2 挂起
- 交付物 `bench/rubric-v3/ablation/g3-w3w4-completion.md`（含负面结果声明三条）；冻结数据零修改；新候选 RV3G3-goldrank-threshold-proof 入队

## 下一步（按优先级）

1. **P0 · RUBRIC-V3-FULL-AUDIT / G4 漏洞对照**：gap-analysis Q2 五条结构性解释逐条对照我们的协议，标 已规避/未规避/部分规避 + evidence。原文不在工作树，用 `git show aea3d6b:receipts/rubric-v3-gap-analysis.md` 取。交叉引用 g3-w3w4-completion.md §F3 决策矩阵（避免重复推导判据口径类条目）
2. **P1 · G5 优化清单**：机械化候选（可 assert 脚本化的判断，参考 R5.2 系列 assert-* 脚本模式）+ 并行化候选 + 成本估算
3. **P2 · G6 综合报告**：`bench/rubric-v3/AUDIT-report.md` — G1-G5 综合 + rubric-v3 定稿建议（维度保留/修改/废弃 + 理由）+ ResearcherBench/RACE 差异表 + 负面结果声明；G6 拥有 O1/O2/O3 终裁权（消费 RV3G3-goldrank-threshold-proof 若届时已完成）
4. **P2 · RV3G1-semantic-rejudge**：arena 通道补 G1 语义一致率（样本清单已就绪）
5. **P2 · RV3G3-goldrank-threshold-proof**（新入队）：gold 平均排名过线阈值正式论证，纯仓库内推导
6. **P2 · C3 v3 paired runs**（WORK_QUEUE 项）：仍阻塞于 judge 家族隔离，等用户决策
7. **P2 · 回 arena 会话 01a18567 取 307 行 survey 原文回填 research/interpretability/literature-survey.md**
8. **P2 · 评估 :8787 node 网关容量竞争根因**（cron 400 too large 元凶），决定是否切直连 :8000

## 阻塞项

- **judge 家族隔离**：ninfer 只有 qwen3.8-27b（Qwen 家族），C3 v3 的 G2 judge 实测需异源 → 等待用户决策
- **web-llm 三 provider 登录态失效**：perplexity/chatgpt/gemini 全部 error → 需人工浏览器登录（一次性 web-llm-authorize）；各 goal 按失败降级继续
- **R5.2-third-scorer 外部依赖**：需 arena 通道或第三本地模型（不同家族）→ G3 已确认 O2 本轮不可执行
- **σ_d 无先验数据**：MDE/n_task 反推待 pilot 数据

## 分支状态

- main @ f17206d（= origin/main，G3 已 merge + push 验证）
- ralph/rubric-v3-audit-g1 @ 9f8a1f9（收口分支，可删）
- ralph/rubric-v3-audit-g2 @ 7d17452（收口分支，可删）
- ralph/rubric-v3-audit-g3 @ f17206d（收口分支，可删）