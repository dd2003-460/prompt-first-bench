# 任务 001：prompt-first 流程消融调研

【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00-common-review.md + 01..04.5（仓库内）。
2. 每阶段产出落盘 loop-artifacts/stages/<N>/，阶段判定 pass 才进下一阶段。
3. 完成后 commit + push（含全部 loop-artifacts/）。
4. 通道故障（403/沙箱）→ 报告 Lead，由 Lead 降级本地执行，不得静默跳过 loop。

## 任务目标（1-2 句）

调研 **prompt-first 流程（1-loop）究竟有没有提升、对不同 AI 模型提升如何**：用固定任务集做流程变体消融（V0 裸 prompt → V5 完整 1-loop），量化每个流程要求的边际提升 + 模型维度差异。

## 研究问题（对应 goal 验收维度）

1. **拆解任务对最终成功率**：V1 - V0 的 success 率差
2. **正交完备对最终成功率**：V1 内部再分 V1a（只分解不要求正交/完备）vs V1b（正交+完备+递归原子）的差
3. **每个具体要求的提升**：02.5 交叉验证（V3-V2）、逐阶段落盘+pass 门禁（V5 的落盘部分 vs 不落盘）、04.5 反方复核（V4-V3）
4. **跨模型**：上述消融 × arena 可用模型矩阵（模型不可控则记限制）

## 执行步骤

1. 读 `rubric/scoring.md`（任务集 5 题 + V0-V5 变体定义 + 评分维度）
2. 走 1-loop 01-03（目标分解/调研/行动分解），工件落盘 `loop-artifacts/stages/`
3. 执行 04：对每个 (task 1-5 × variant V0-V5 × model)：
   - 构造该变体的 prompt（V0=裸问题；Vk=加上 k 之前所有流程要求）
   - 产出完整输出（**非摘要**）→ `bench/runs/<task>/V<k>-<model>/run1.md`
   - 按 rubric 评分 → `run1-score.md`
   - 注意：V1a/V1b 是 V1 的两个子变体，只跑 task 1-2（控制预算）
4. 每 (task) 汇总 → `bench/runs/<task>/summary.md`
5. 走 04.5 反方复核（重点：评分是否自利偏差——评分者=执行者时，用可验证事实题压低自利空间；结论要能被人复核）
6. 汇总报告 `bench/runs/FINAL-REPORT.md`：
   - 变体 × 模型 success 率矩阵
   - 边际提升表（V1-V0, V2-V1, V3-V2, V4-V3, V5-V4，各带 n 和置信说明）
   - 结论：prompt-first 是否提升（分模型）/ 每个要求的边际 / 成本（token/时间）与收益比
7. commit + push 全部工件

## 评分标准

引用 `rubric/scoring.md`（D1 正确性 40 / D2 完备性 25 / D3 结构正交 20 / D4 置信度标注 15；≥80 success）。

## 验收标准

- 5 题 × 6 变体（V0-V5，含 V1a/V1b 子变体）全部 run 落盘，完整输出非摘要
- 每题 summary + FINAL-REPORT 含边际提升表 + 跨模型结论
- 每个结论带 conf + 样本数 n
- 全部 commit + push 到本仓库

## 预算控制（防失控）

- 默认模型若不可控/太多 → 只跑 arena 默认 1-2 个模型，其余模型记 N/A
- V1a/V1b 只跑 task 1-2
- 每 run 输出 ≤ 4000 token；超长截断并在 score 里标注
