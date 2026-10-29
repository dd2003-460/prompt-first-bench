# 阶段 01：目标分解 — RUBRIC-V3-FULL-AUDIT / G3 W3/W4 收尾

> goal: rubric-v3-audit-g3 · 分支 ralph/rubric-v3-audit-g3 · 2026-10-30
> 上游任务书: tasks/RUBRIC-V3-FULL-AUDIT-task-brief.md（队首大 goal，G1-G6 串联）
> 前置: G1 完成（矛盾清单 C1-C4 + per-run top-5 新发现，G1-contradiction-audit.md）；G2 完成（根因 = 双源 p̃ 偏差 + 判据极严，三修复选项 O1/O2/O3，g2-rootcause.md）。本 goal 消费两者。

## 因素分解

任务书 G3 = 「stats-w3w4.json 的方案补完验证（对照 G2 根因判断哪个方案值得救）」，拆成四个正交因素：

### F1 · stats-w3w4.json 内部一致性复验（验证链是否真的「走完」）
- 已知条件：stats-w3w4.json 落盘了 W0-W4 × 8run 分数、7 对 Spearman ρ、W0 tie 分析、global top-5 构念效度计数（strict 口径 1/2/3/2）、conclusion（「W3 唯一过线但不得写入正式 rubric」）。文件自述 verification = 「24 分数与 stats-recomputed.json 精确一致；ρ 七对比与 ablation-result.md 报告值全部一致」。
- 待验证：(a) W3/W4 分数按 `O3=Σw·h/Σw` 从原始数据复算是否精确一致（W4 权重 = w1+w2，prior-estimates.json 无 w4 字段，需按公式合成）；(b) 7 对 ρ 复算是否与落盘值一致；(c) W0 tie 分析与 gap 数值复核；(d) global top-5 集合与 strict 计数复核（含 W1/W4——此前 G1/G2 只核过 W2/W3）。
- 判定标准：全项精确一致 → 验证链闭合，「未走完验证链」的说法修正为「验证链已闭合但缺独立 judge 维度」（见 F3）。

### F2 · W3/W4 在 G2 根因下的幸存评估（哪个方案值得救）
- 已知条件：G2 结论 = 主根因在 p̃ 估计层（双源偏差），公式层排除；W3 的 3/5 过线依赖 orig judge 对 gold 节点的低 p̃（N-2.1 p̃=0.01, N-3.2.2 p̃=0.03）。
- 待验证：
  - F2a W3-new（blindtest p̃）下：分数/排序/global top-5 gold 计数变化（G1 已产出 1/5，本 goal 补 W4 侧）。
  - F2b W4 的结构位置：W4=w1+w2 是加法混合，w1（SHARE 规则分）占比 vs w2（surprisal）占比各多少？若 w1 主导 → W4 天然比 W3 抗 p̃ 噪声（乘性放大被加法稀释）→ 用 ρ(W3,W4) 与 ρ(W1,W4) 量化。
  - F2c 排序稳定性：五方案 × 双 judge 共 9 个排序（W0-W4 orig + W2/W3/W4 new）下 run6/run1 头部格局是否稳定（G1 发现 W2-new 下 run1 反超 run6）。
- 判定标准：给出每个方案的「p̃ 敏感性分级」（低/中/高）+ 证据数字。

### F3 · 三选项决策矩阵（O1/O2/O3 对照 G1+G2 证据）
- 已知条件：G2 落盘三选项——O1 改判据口径（top-10/AUC/gold 平均排名）/ O2 第三 judge 重测（依赖 R5.2-third-scorer）/ O3 接受降级（W3 不进正式公式，rubric-v3 定稿 W1-only + W3 experimental）。
- 待验证：
  - F3a O2 可行性核查：R5.2-third-scorer 当前状态（queue 显示未完成，外部阻塞——需 arena 通道或异源模型；judge 家族隔离是已知阻塞项）。
  - F3b O1 候选口径预评估：用现有数据试算 top-10 口径（global top-10 gold 计数）与 gold 平均排名口径，看双 judge 下是否收敛（若两 judge 在新口径下结论一致 → O1 可解；仍翻转 → O1 也不够）。
  - F3c O3 成本：W1-only 定稿意味着放弃 surprisal 维度——W1 自身的构念效度如何（global top-5 gold 计数 + 排序质量）。
- 判定标准：输出决策矩阵（选项 × 成本/收益/风险/前置条件），标注推荐路径但**不定稿**（定稿权在 G6）。

### F4 · 交付物结构
- g3-w3w4-completion.md：F1 复验表 + F2 敏感性分级 + F3 决策矩阵 + 负面结果声明（哪些「值得救」的判断被证伪）。
- 边界：不改冻结文件（stats-w3w4.json 只读；新数字落新文件）；不动 gold set；不实施任何修复。

## 空缺清单

| # | 空缺 | 类型 | 影响 |
|---|------|------|------|
| G1 | R5.2-third-scorer 数据（O2 的前置） | 外部阻塞（queue 确认未完成） | O2 只能标「不可行于本轮」，不能实测 |
| G2 | 异源 judge（非 qwen 家族） | 外部阻塞（judge 家族隔离，等用户决策） | 所有「跨 judge」结论限同族范围（继承 G2 R4） |
| G3 | ablation-result.md 原文中 W3/W4 段落细读 | 仓库内可查 | F1(d) 需要核对报告叙述与 JSON 是否一致 |

## 阶段 02 研究入口

- 仓库内材料足够：F1/F2/F3b 全部可从 JSON 复算；F3a 从 queue 状态读取。
- web-llm 强制步骤预期三 provider 仍失效 → 记录失败回执后继续，不阻塞。

## 判定

分解完成：四个叶子因素（F1 验证链闭合 / F2 敏感性分级 / F3 决策矩阵 / F4 交付结构）覆盖任务书 G3 全部要求且显式对接 G1/G2 产出；空缺 G1-G3 均有处置路径。→ 进入 02。