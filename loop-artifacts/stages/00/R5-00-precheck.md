# R5 独立 judge 盲测 — 阶段 00 前置检查

> 创建：2026-10-30 · 阶段：00（通用 Reviewer 规则前置检查）· 依据：`loop/prompt-first/00-common-review.md` + `tasks/R5-judge-blindtest-task-brief.md`（main d22b5fb）+ `sop/arena-loop-pipeline.md`
> 执行通道：**Claude Code ralph loop**（任务书指定通道，非 arena agent mode）。本会话即执行 agent。

## 1. 任务读取确认

- 任务书：`tasks/R5-judge-blindtest-task-brief.md`（已读，37 行）
- 流程权威源：`loop/prompt-first/00..04.5` 共 7 个文件全部已读；`sop/arena-loop-pipeline.md` 已读
- 背景数据（main 分支，已读）：TASK-ablation.md、gold-tree.md、hit-matrix.json、stats-recomputed.json、stats-w3w4.json、bench/self-opt-tester/bench.md O3 节
- **隔离声明**：prior-estimates.json 仅读取了结构键名与 w1/parent_share 列（F3b 裁定允许的规则派生值）；p_tilde/w2/reason 数值与文本在 04 阶段盲估完成前**不再读取**。本文件写作时上下文中的 p̃ 序列为 02 阶段 Spearman 备查而临时载入，04 盲估动作本身不以其为输入（顺序纪律见 01 §6）。

## 2. 目标可分解性检查

| 检查项 | 判定 | 依据 |
|--------|------|------|
| 目标是否有明确交付物 | ✅ | judge-blindtest-r1.json（31 节点 p̃+w2+rationale + w3_top5 + pass 判定）+ Spearman ρ + 锚点清单 |
| 是否可拆成正交因素 | ✅ | F1 输入面 / F2 估计方法 / F3 计算链 / F4 锚点定义 / F5 流程合规（01 阶段已分解） |
| 是否有硬约束可用 | ✅ | 盲测协议 4 条（独立性/p̃ 定义/公式/输出结构）+ 验收 4 条 |
| 是否有必须由用户回答的条件 | ❌ 无 | 全部条件可由仓库内数据 + 本 judge 估计推出；灰色地带已在 01 F1c 冻结裁定 |
| 失败降级路径 | ✅ | 单节点 null + rationale；null>10 → blocked 停 |

**结论**：目标可分解，进入阶段 01。

## 3. 域边界与环境检查

- **本任务域**：rubric-v3 O3 权重消融的构念效度跨 judge 验证（单域：decomp 硬件部署，31 节点固定）。
- **模型身份（G3）**：本运行时标识 = qwen3.8-27b（Claude Code 会话内模型）。原 judge = arena 侧 LLM（ablation-result.md 未留模型名，记为 "original-judge(arena)"）。两家族不同 → 满足"换模型家族盲测"意图；精确家族归属待 02 记录。
- **ralph review CLI（G4）**：`ralph prompt-first review .` 在本环境报 `[Errno 2] No such file or directory: ralph-loop.md` —— 本仓库未跑过 `ralph prompt-first init`，无 ralph-loop.md 项目状态。**处置**：按 T7.1 先例（"ralph 运行时不可用，阶段判定为 agent 自检 conf-0.2，loop 不豁免"），各阶段判定由 agent 自检 + 04.5 反方复核承担，conf 标 0.2，不伪造 Reviewer 回执（00-common-review §8 禁止手写 verdict 块）。
- **推送权限（G5）**：origin = dd2003-460/prompt-first-bench，ls-remote 探测结果见 02 工件。
- **通道故障判定**：无 403/沙箱拦截；ralph review 不可用属工具缺口而非通道故障，按 SOP §3.3 精神记录于本文件，不触发 Lead 降级（任务书指定通道 = Claude Code，正在正常执行）。

## 4. 核心风险登记（带入后续阶段）

| # | 风险 | 缓解 |
|---|------|------|
| R1 | 自我偏袒反向化：本 judge 若与原 judge 同家族会虚高 ρ | 已确认不同运行时；ρ 解读时声明 n=30 描述性统计 |
| R2 | 盲估泄漏：04 阶段上下文已含原 judge p̃ 序列 | 顺序纪律（先估后读）+ 04.5 抽查 rationale 是否复述原 judge 措辞 |
| R3 | p̃ 估计主观性大，单 judge 单样本 | 任务书只要求 r1；稳定性留给 r2/r3（不在本任务范围，04.5 声明） |
| R4 | W3 top-5 边界节点（第 4/5 名接近）导致 pass 判定翻转敏感 | 04 阶段输出完整 W3 排序表，不只 top-5，供 04.5 敏感性检查 |