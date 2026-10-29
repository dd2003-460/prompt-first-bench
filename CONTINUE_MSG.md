# CONTINUE_MSG — pfb 工作区

## 当前状态 @ 2026-10-30 +0800

**RUBRIC-V3-FULL-AUDIT / G4 漏洞对照 goal 收口（六阶段全过，merge main @ 5b0a62b = r111）**：
- gap-analysis Q2 五条结构性解释逐条判定（判定对象 = 当前可运行完整链条；规则：草案写了但从未执行的防护最多判部分规避）：
  - **S1 构念错配 = 部分规避（未到期）**：DRAFT §3.1 显式域限定 + 执行未越界，但第二格/T17 本仓缺席 → 「有意识的单域使用」≠「已验证的域适配能力」（02.5 Q1 从「已规避」降级）
  - **S2 唯一 gold 路径偏置 = 未规避（最严重）**：硬证据三条均仓库内——(a) gold-tree 单作者单 calc.py 链 (b) DRAFT §4 三问与 O4 gold 答案形状同构（V1 实验 O1 优势被构造性保证）(c) O2 条款「新深层矛盾不在本次计分内」砍掉抗同源出口 → **前序全部 top-5 分析（G1 C4/G2/G3）都是「相对 Lead-gold」**
  - **S3 可靠性成本 = 部分规避（降档）**：DRAFT ≥3 LLM 盲生成 p̃ 协议 vs TASK-ablation Step 2 实际单 judge 自评；κ 门禁无执行回执（unverified 非断言失败）
  - **S4 可比性 = 部分规避（子项分裂）**：版本依赖已管控（冻结元数据字段）/ 跨域可比性主动放弃无补偿
  - **S5 surprisal = 部分规避（强度不足）**：三重事前防护（ε 截顶+命名纪律+消融前置）被实证穿透（ρ=0.688、|Δw2|≥2 共 7 节点、top-5 翻转）
- 负面结果声明三条：「S1 已规避」「paper 协议完整 = 风险受控」「blindtest = 独立校验」均推翻或限定为同族
- 核心模式：三种「部分规避」结构不同（降档/覆盖缺失/强度不足）→ 对应 G5 三类优化动作（强制机械化/补覆盖/加固阈值）
- G6 硬约束导出：S2 未闭环前定稿文档必须声明 O3 数字「相对 Lead-gold」；adversarial-check 28 findings（verdict=revise，9 blocker）需处置表；前序 loop 引用带「单源 gold + 同族双 judge」双重限定
- 交付物 `bench/rubric-v3/ablation/g4-vulnerability-crosscheck.md`（四列汇总表 + 五节 + 负面结果 + G5/G6 导出）；冻结数据零修改；新候选 RV3G4-prior-source-assert / RV3G4-kappa-receipt-assert 入队

## 下一步（按优先级）

1. **P0 · RUBRIC-V3-FULL-AUDIT / G5 优化清单**：机械化候选（优先消费 G4 三类输入：p̃ 来源断言脚本 + κ 门禁回执断言，参考 R5.2 assert-* 模式；成本估算须含 adversarial-check 9 blocker 修复成本供 G6 取舍）+ 并行化候选（验收项 = 「有没有人真的跑过」而非「协议里写了没有」，S3 教训）+ 成本估算。交叉引用 g4-vulnerability-crosscheck.md「给 G5 的导出」节
2. **P1 · G6 综合报告**：`bench/rubric-v3/AUDIT-report.md` — G1-G5 综合 + rubric-v3 定稿建议（维度保留/修改/废弃 + 理由）+ ResearcherBench/RACE 差异表 + 负面结果声明；G6 拥有 O1/O2/O3 终裁权（消费 RV3G3-goldrank-threshold-proof 若届时已完成；应用 S2 硬约束 + 28 findings 处置表至少 9 blocker）
3. **P2 · RV3G1-semantic-rejudge**：arena 通道补 G1 语义一致率（样本清单已就绪）
4. **P2 · RV3G3-goldrank-threshold-proof**：gold 平均排名过线阈值正式论证，纯仓库内推导
5. **P2 · RV3G4-prior-source-assert / RV3G4-kappa-receipt-assert**（新入队）：G4 强制机械化候选落地，工作量小，纯仓库内
6. **P2 · C3 v3 paired runs**（WORK_QUEUE 项）：仍阻塞于 judge 家族隔离，等用户决策
7. **P2 · 回 arena 会话 01a18567 取 307 行 survey 原文回填 research/interpretability/literature-survey.md**
8. **P2 · 评估 :8787 node 网关容量竞争根因**（cron 400 too large 元凶），决定是否切直连 :8000

## 阻塞项

- **judge 家族隔离**：ninfer 只有 qwen3.8-27b（Qwen 家族），C3 v3 的 G2 judge 实测需异源 → 等待用户决策
- **web-llm 三 provider 登录态失效**：perplexity/chatgpt/gemini 全部 error → 需人工浏览器登录（一次性 web-llm-authorize）；各 goal 按失败降级继续
- **R5.2-third-scorer 外部依赖**：需 arena 通道或第三本地模型（不同家族）→ G4 确认为 S2 闭环前置条件之一（双 gold 或异源 judge 二选一）
- **σ_d 无先验数据**：MDE/n_task 反推待 pilot 数据

## 分支状态

- main @ 5b0a62b（= origin/main，G4 已 merge + push 验证）
- ralph/rubric-v3-audit-g1 @ 9f8a1f9（收口分支，可删）
- ralph/rubric-v3-audit-g2 @ 7d17452（收口分支，可删）
- ralph/rubric-v3-audit-g3 @ f17206d（收口分支，可删）
- ralph/rubric-v3-audit-g4 @ 5b0a62b（收口分支，可删）