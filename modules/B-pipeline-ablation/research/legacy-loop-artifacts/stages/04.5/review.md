# V3 Benchmark Hardening — 阶段 04.5 反方复核 (review.md)

> origin: ai · 2026-11-06 · 上游: stages/04/execution-log.md @ 8439759
> 角色: 反方审稿人视角, 不重新开展无边界研究

## 1. 原始任务回应核对

任务卡 tasks/v3-hardening.md 的 A/B/C/D 四项全部有落盘证据 (见 execution-log.md 回执表)。B2 异族 judge 量化按任务卡失败降级条款标注 blocked-on-external + conf-0.2, 未静默跳过。

## 2. 反方挑战 (假设我是审稿人)

**弱点 1: 同族 judge 系统性偏袒**。qwen3.8-27b 判 qwen3.8-27b 的输出, M6 sourcing 在 S5 臂拿到 1.000 —— 如果 judge 偏爱"看起来像自己写的引用格式", M5/M6 驱动的 +0.190 效应量可能被高估。缓解: 相对排序 (S5>S1>S0) 在同族 bias 下大概率保持 (bias 对各臂近似均匀), 但绝对值不可外推。已在 RESULTS-FINAL.md L1 标注 conf-0.2。**残余风险: 若未来异族 judge 重评后 S5-S0 delta 缩到 <0.1, "hook 效应大"的结论需降级为"中等"。**

**弱点 2: n=15/arm, 5 题 × 3 rep**。题目间方差与臂效应混淆; Q5 的权重 override (M1=0.40) 意味着总均值里 Q5 占比被放大。sign test 对方向稳健但对效应量估计粗糙 (只用了符号没用幅度)。缓解: 已报告 mean_delta 和 CI。**残余风险: 换一批题目后 delta 可能波动 ±0.05。**

**弱点 3: S8D 不可复现**。7 条 run 的 prompt 丢失, 无法排除 S8D 实际测试了别的东西。已标 non-reproducible 并排除出主分析 —— 处理正确, 但这 7 条 run 的算力成本沉没, 且 S8D=0.722 恰好落在 Arena 附近, 读者可能误读。**建议: 在 paper-draft 中不再引用 S8D 数字。**

**弱点 4: bootstrap-cis.json 与 stats-v3.json 数值不一致** (前者 S0 total=0.397 B=1000, 后者 S0 total=0.615 B=10k)。这是两次不同 rescore 的产物 (f876e1e 前 vs 后), 旧文件未删。两个文件并存会让读者困惑。**处置: 本复核判定 bootstrap-cis.json 为陈旧产物, RESULTS-FINAL.md 以 stats-v3.json 为准 (Provenance 节已写明); 建议后续清理旧文件或加 SUPERSEDED 标记。**

## 3. 结论是否超出证据

RESULTS-FINAL.md 四条 Key Findings:
- F1 "memory hook effect is real and large" —— p=0.001 支持 significant, 但 "large" 是相对于 ns 的 S1 而言; 绝对值 0.805 受同族 judge 影响。**措辞可接受, 已带 caveat。**
- F2 "decomposition alone does not help" —— 严格说只能讲 "no measurable value at n=15", 不能排除小效应。**RESULTS-FINAL.md 原文写的是 'adds no measurable value' —— 措辞正确。**
- F3/F4 无问题。

## 4. 交付物真实性核验

- RESULTS-FINAL.md: 存在, commit f876e1e, 表格完整 ✓
- stats-v3.json: 存在, bootstrap_ci + paired_deltas 字段齐全 ✓
- scores-v3.json (45) + scores-v3-secondary.json (16): 存在 ✓
- score.py @ f876e1e: 存在 ✓
- stages/04/execution-log.md: 存在, commit 8439759, 已 push ✓

## 5. 未完成项与残余风险

| # | 项 | 状态 | 影响 |
|---|----|------|------|
| U1 | 异族 judge 重评 (B2) | blocked-on-external | 绝对分数 conf-0.2, 相对排序可信度较高 |
| U2 | n≥30/arm 扩展 | future work | 小效应 (<0.05) 检测力不足 |
| U3 | S8D prompt 恢复 | 不可行 | 该臂永久 non-reproducible |
| U4 | bootstrap-cis.json 陈旧文件清理 | 待做 | 文档一致性风险 (低) |

## 6. 最有价值的下一步

1. 用 T23-semihetero-analysis.md 里的 semi-hetero 通道 (若有可用异族模型) 对 S0/S5 各 5 条 run 重评, 验证 delta 方向保持。
2. 清理 bootstrap-cis.json (加 SUPERSEDED 头注或移入 archive/)。
3. 将 RESULTS-FINAL.md 的核心表并入 paper-draft.md §Results, 替换旧数字。

## 7. 交接判定

链条完整 (任务卡 → 执行日志 → 统计产物 → 最终报告), 下一位使用者可仅凭 stages/04/ + stages/04.5/ + RESULTS-FINAL.md 继续工作。**verdict: pass-with-notes** (U1/U4 不阻塞 goal complete)。

repair_stage: null