# Goal: PFB Production Hardening (v2, 2026-11-09)

**状态**: ACTIVE（替代 goal-pfb-full-run.md — 该文档的 S0/A3/A4×500 矩阵已被用户指令取消，数据冻结于 runs-prod/）
**来源**: 成璐 2026-11-09 "看看现在的goal，质检标准，计划，退出条件，如果让你长期自主执行有什么计划吗"

## 一句话目标

让 S5（分解→检索→验证→综合管线）**稳定超过 S0（裸 27b）**，在 nat 题上 mean cov ≥ 0.634（S0 当前值），并在 GPU 题上 depth ≥ 0.50；然后产出可发表级别的消融报告。

## 当前真实状态（2026-11-09 核对）

| 项 | 状态 |
|---|---|
| S0/A3/A4 量产 (runs-prod/) | **已冻结**：nat 391+30+30, soc 30+60+60。用户判定"够了"，不再续跑 |
| s5-prod nat | ✅ 100/100 完成。mean cov=0.533 < S0 的 0.634 → **不达标** |
| s5-prod soc | 🔄 10/100 进行中 (PID 57416) |
| v13 × 50 reps (GPU) | 🔄 6/50，r5 截断失败 (max_tokens)，有效 5。~3.5h 剩余 |
| T52 撞车调研 (arena) | 🔄 派发中，报告未落盘 |
| 已知缺陷 | ① P4 综合阶段 hedging（有 verified 数字却输出定性描述）② research_hook snippet 抽取可能为空 ③ P1 输出超 max_tokens 无重试 |

## 分阶段计划（长期自主执行）

### Phase 1: 修管线（本周内，不依赖新数据）
1. **P4 prompt 修复**：加指令"基于已验证事实做最大幅度定量推导，不要因个别缺失数据整体降级为定性描述"。改完用现有 fact table 离线重放 5 个 rep 验证（不调 LLM 全链）。
2. **research_hook snippet 诊断**：检查 .research-cache/ 里 snippet 字段是否为空；若空，定位是哪个通道（DDG lite / webfetch / web-LLM）没抽到正文。
3. **P1 max_tokens 提升 + 截断重试**：v13 r5 事故根因。max_tokens 从当前值提到 8192，parse 失败时自动 retry 一次（temperature 降到 0.3）。
4. **质检门禁 G1**：Phase 1 完成 = 三项修复 commit + 离线重放显示 P4 输出含具体数字的比例从 ~12% 提升到 ≥40%。

### Phase 2: 状态机重构（等 Phase 1 通过）
把线性 P1→P2/P3→P4 改成允许回退的状态机：
- 状态：P1_DECOMPOSE / P2_SEARCH / P3_VERIFY / P4_SYNTHESIZE / P4_EVALUATE
- 回退触发：P4_EVALUATE 发现某 verified 节点的具体数字没进最终答案 → 回 P4 重综合；P2 返回空内容 → 回 P1 换查询词重分解该分支
- 终止：S_α 收敛（Δ<ε）或预算耗尽或 max_iterations
- **前置**：Phase 1 的 snippet 修复必须先过，否则回退拿到还是空壳
- **质检门禁 G2**：GPU 单 rep smoke × 3，depth 均值 ≥ 0.50 且无死循环（单 rep wall < 30min）

### Phase 3: 补跑对比（状态机版 vs S0）
- S5-v2 (状态机) × nat 100 reps + gpu 50 reps
- 与冻结的 S0-nat (391 reps) 同 judge 对比
- **质检门禁 G3**：S5-v2 nat mean cov ≥ 0.634（追平 S0）且 ≥25% reps 达到 cov≥0.8；gpu depth 均值 ≥ 0.50

### Phase 4: 论文与发布
- 跨臂消融报告（S0/A3/A4/S5-v1/S5-v2 × nat/soc/gpu）
- underdetermined 题的条件指标（verified 节点 gold 覆盖 + [待核验] 计数）
- 数据推 prompt-first-bench.git；T51/T52 撞车结论写入 related work
- **退出条件 E1**：报告含全部矩阵 + 统计显著性检验（bootstrap CI 不重叠或 p<0.05）

## 退出条件（何时停）

| 条件 | 动作 |
|---|---|
| G3 达成（S5-v2 ≥ S0） | 停止迭代管线，进 Phase 4 收尾 |
| G3 连续 2 轮未达成且改动已穷尽（P4/检索/状态机都试过） | 停下汇报：给出差距归因分析，等用户定方向（换题/换模型/接受负结果写成 analysis paper） |
| 8787 不可用 > 4h | 暂停所有 run，保留断点，恢复后自动续 |
| v13 50-rep 显示 depth 方差过大（std > 0.15） | 先查方差来源（哪类 rep 崩），不盲目加 rep |

## 自主执行规则（无人值守期间）

1. **每 2h 自检一次**：进程还活着？新 JSON 在产出？error 率 < 5%？任一异常 → 修 or 跳过坏 rep 继续。
2. **断点恢复**：失败的 rep 删文件重跑；同一 rep 连挂 2 次 → 标记 skip 并记录原因，不卡死整批。
3. **不擅自扩大范围**：不加新臂、不改题面、不动 S0 冻结数据。这些需要用户点头。
4. **对外动作一律不做**：邮件、Zenodo/arXiv 上传、公开 repo push 之外的任何外发 → 只留草稿和清单。
5. **决策日志**：每个非平凡决定（skip 哪个 rep、改哪个参数）写进本文件的 Decision Log 节。

## Decision Log
- 2026-11-09: S0/A3/A4 冻结不续跑（用户指令 "s0怎么还在，关了吧"）
- 2026-11-09: RT-RAG 判定不适合对标，改为以 S0 为 baseline（详见 chat 记录）
- 2026-11-09: Phase 顺序定为 修管线→状态机→补跑→论文；snippet 修复是状态机的硬前置
- 2026-11-09: **修正两个错误诊断**（文件证据推翻了之前基于 raw[:3000] 截断存储的误判）：
  - (a) v13 r5 不是 max_tokens 截断——usage out=2128 < 8000，是模型 ~2100 token 处主动停笔。修复 = _extract_json 截断兜底 + retry 降温度（commit 5a3b6c17），对 r5 raw 实测可恢复 10/11 节点
  - (b) research_hook snippet 不是空的——全量审计 609 sources 全部有内容（arxiv 中位 500ch, ddg 222ch, web_llm 101ch）。真正的问题是 **local_corpus 通道污染**：_LOCAL_CORPUS_DIRS 只含 D1-gpu-research 语料，对 nat 题（CDN/Pareto/LRU）grep 出的"命中"全是 GPU 硬件文档。nat 100 reps 共 1506 个节点，evidence 里大量出现"参考来源[1]为GPU硬件规格...与该节点无关"——P3 在拿不相关的本地文档做核验，把本该 verified 的节点打成 degraded。修复方向：local_corpus 按题域过滤（或 nat/soc 题禁用该通道），待实现