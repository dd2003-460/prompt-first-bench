# 01 目标分解 — R3.2 run2：goal-template §3.0 成本结构审查

> origin: ai · 2026-10-24 (Asia/Shanghai) · 任务书 bench/r3/run2/task-brief.md（git blob 52d1e2ba）
> 与 run3（执行性审查）正交：本 run 只看 token 成本，不判链路是否"走得好"。

## 目标交付
1. 定位 §3.0 标准链路 9 步中 token 消耗最大的 2-3 步（附输入/输出规模依据）。
2. 给出链路总消耗 −30% 的最小 prompt/SOP 层改动（1-2 个，不动 harness）。
3. 每个建议配可验证度量（跑什么、看什么数）。
4. 产出 01-decomp.md / 02-research.md / 04.5-review.md 于 bench/r3/run2/，commit+push（M7 锚点齐全）。

## 审查对象：§3.0 标准链路（9 步）
源：`bench/self-opt-tester/new-goal-20261023.md`【自主探索循环（标准链路）】（r2 修订后 §3.0 全文复刻，"新 goal 必须含完整链路规则"）+ `bench/self-opt-tester/loop-report.md` 8 步表（r1 实测口径）。

| # | 步骤 | r1 报告旧编号 |
|---|------|--------------|
| 0 | 创建/持 goal（顶层 create_goal；subagent→落盘+报 Lead） | （r2 修订新增） |
| 1 | 找目标（P-1 优先） | 1 |
| 2 | 找 arena 通道 | 2 |
| 3 | 连仓库（ls-remote + 会话内可达验证） | 3 |
| 4 | 让 arena 走 loop 01→04.5（断点 A/B/C） | 4 |
| 5 | 交叉验证（≥2 LLM）+ 推理矛盾漏洞 | 5 |
| 6 | 拿漏洞迭代（conf ≥ 0.7） | 6 |
| 7 | bench（0.9 比例 + 总加权 vs baseline） | 7 |
| 8 | 发布（commit+push+ls-remote） | 8 |
| → | 找新目标（含全节规则，回到 0） | + |

计数口径说明：修订版 0-8 恰为 9 步（找新目标为闭环边）；旧版 8 步+找新目标同样 9 节点。两种口径节点集相同，成本排序不变（如实标注，不强行收敛）。

## 正交成本因子（一条链路周期的 token 分解）
- **F1 固定规则负载 L**：每会话必读文本（loop 7 文件+SOP+任务书）——已测 12,086+527 o200k。
- **F2 转数放大 T**：agent 会话每 turn 重发全部上下文 → 固定部分贡献 ≈ L×T，累积部分三角数级增长。
- **F3 累积上下文 U**：工具输出/工件/思考随阶段增长。
- **F4 会话数 S**：迭代轮 = 任务书重发 → 复制整个会话成本。
- **F5 外部通道 E**：交叉验证外部 LLM 会话 + 回执/组装。
9 步 = 这 5 因子的不同组合（映射见 02/04.5）。

## 已知（可测/已测）vs 空缺（假设，待 02）
已知：规则负载字节/token（wc + tokenizer 实测）；pilot V0/V4 输出体积；r1 步骤 4 工件体积；r2 回执体积；arena 有 compaction（round1 run 笔记）。
空缺：① arena 会话实际 turn 数 T（repo 无记录 → 假设 30-60，conf 0.6）；② arena 侧累计输入 token（平台不暴露 → 模型推估，conf 0.5）；③ compaction 实际触发率（反方风险）；④ 外部 LLM 会话内部 token（DeepSeek 60 页搜索非我方计费口径，只记回执侧）。

## 原子任务
| # | 任务 | 依赖 |
|---|------|------|
| A1 | 实测规则负载/任务书/工件/回执 token（count-tokens.js） | — |
| A2 | 实测 pilot V0/V4 输出与内嵌规则卡体积 | — |
| A3 | 外部来源交叉（agent 循环成本结构文献） | — |
| A4 | 建成本模型，9 步排序，识别 2-3 大头 | A1-A3 |
| A5 | 设计 −30% 最小改动 + 度量方案 | A4 |
| A6 | 三文件落盘 + commit + push + ls-remote 回执 | A5 |

## 02 研究入口
- 测量：`node bench/r3/run2/count-tokens.js`（依赖 gpt-tokenizer，registry.npmjs.org）。
- 内部证据：bench/runs/round3-research-pilot/*（V0/V4 同题对照）、bench/self-opt-tester/*（r1/r2 实况）。
- 外部：agent loop token 成本结构（重发放大/系统提示占比/输出膨胀倍数），≥2 独立源 per 关键主张。
- 失败备用：web_search 不可用 → 只用内部实测 + 标 degraded。

## 判定
pass（正交因子覆盖成本、已知/空缺分离、02 可直接开工）
