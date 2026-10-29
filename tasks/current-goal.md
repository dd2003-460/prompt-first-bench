# Goal: RUBRIC-V3-FULL-AUDIT / G1 矛盾审计（loop 工件补齐 + 矛盾清单交付）

> 创建：2026-10-30 · ralph loop runner（队首大 goal RUBRIC-V3-FULL-AUDIT 的子 goal G1）
> 依据：`tasks/RUBRIC-V3-FULL-AUDIT-task-brief.md` G1 节 + `tasks/goal-queue.md` 队首行进度注记（「G1 机判脚本已跑通(exit 0)但 loop 工件待补」）

## 【目标】
任务书 G1 = 「hit-matrix 8run×31node 全量重判抽检（随机 30% 节点独立重判，报一致率）+ prior-estimates 的 p̃ 分布合理性检查（有没有系统性偏高/偏低）+ 输出矛盾清单（每条带 evidence 引用）」。
机判脚本 `bench/rubric-v3/ablation/scripts/assert-g1-audit.py` + 样本清单 `g1-sample-cells.json` 已在 r108 随 G2 收口入库并跑通（exit 0，确定性 seed 20261030），本 goal 补齐：
1. **六阶段 loop 工件**（前缀 RV3G1-，stages/01..04.5）。
2. **矛盾清单交付物** `bench/rubric-v3/ablation/G1-contradiction-audit.md`：C1-C4 四类矛盾（弱相关 / 二项式红旗 / 零命中高 p̃ / W3 结论对 p̃ 来源敏感），每条带 evidence（JSON path / file:line / 脚本输出行）+ 双 judge 31 节点全量对照表 + 四方案分数表。
3. **一致率口径降级声明**：语义级独立重判需 subagent（工具纪律禁止）→ 交付形式一致率（抽检 35 个 h=1 cell 的 evidence 逐字核验 = 35/35 100%，仅覆盖 h=1 方向），语义级标 unverified，补数路径 = arena 通道复用已落盘 75 样本清单。

## 【阶段】
rubric-v3 研究级审计链（G1-G6）的第一环。数据层自洽已由 A1/A2 断言确立（24/24 O3 复算精确一致），矛盾只可能来自「标注 vs 原文」「p̃ vs 经验」两层。G2 已完成并消费本 goal 的 S2/S3/S4 信号（g2-rootcause.md），本 goal 与 G2 互为引用不重复归因。

## 【SOP 索引】
- `sop/arena-loop-pipeline.md`（唯一 SOP 入口）
- `loop/prompt-first/00-common-review.md` + `01..04.5`（阶段定义）
- `bench/rubric-v3/ablation/scripts/assert-g1-audit.py`（机判脚本，只读消费不改）
- `bench/rubric-v3/ablation/{hit-matrix,prior-estimates,judge-blindtest-r1,stats-recomputed,stats-w3w4}.json` + `gold-tree.md` + `runs-C0-run1..8.md`（全部冻结只读）

## 【验收标准】
1. 六阶段工件齐全于 `loop-artifacts/stages/<N>/`，文件名带前缀 `RV3G1-`
2. 01：四因素分解（F1 数据自洽 / F2 抽检协议 / F3 p̃ 分布 / F4 矛盾分类学）
3. 02：web-llm 强制步骤执行并留回执（三 provider error → 记录失败继续）+ F1-F4 证据固化
4. 02.5：反方质询（一致率虚高 / ρ 分辨率伪影 / C4 越界）+ 风险登记 + 对抗核验停止理由
5. 03：行动 DAG（owner=agent）+ 关键判读分支预注册 + 边界
6. 04：脚本重跑 exit 0 逐字输出 + 矛盾清单落盘 + new-judge 复算发现（W2-new run1 反超 / per-run top-5 无 run 达 3/5）
7. 04.5：反方复核 verdict + repair_stage
8. 冻结数据零修改（git status 可查）
9. commit + push 分支 `ralph/rubric-v3-audit-g1` + ls-remote 验证 + merge main + queue 注记

## 【失败降级】
- web-llm 三 provider 均不可用 → 记录失败回执后继续，不阻塞
- 语义级独立重判不可执行（禁 subagent）→ 按任务书失败降级条款登记信息边界，交付形式一致率口径，不阻塞
- 脚本重跑出现 FAIL → 回 02 重查 F1，不得带病交付