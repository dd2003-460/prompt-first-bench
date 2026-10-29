# Goal: RUBRIC-V3-FULL-AUDIT / G5 优化清单（机判化候选 + 并行化候选 + 成本估算）

> 创建：2026-10-30 · ralph loop runner（队首大 goal RUBRIC-V3-FULL-AUDIT 的子 goal G5）
> 依据：`tasks/RUBRIC-V3-FULL-AUDIT-task-brief.md` G5 节 + G4 g4-vulnerability-crosscheck.md「给 G5 的导出」+ R5.2 系列 assert-* 脚本模式

## 【目标】
任务书 G5 = 「机判化候选（哪些判定能写成 assert 脚本）+ 并行化候选 + 成本估算」。交付：
1. **机判化候选表**（C1-C6）：p̃ 多源断言 / κ 回执断言 / W3W4 复算断言 / w2 公式断言 / spearman 一致性断言 / gold 单源检测（登记不实施）。合计 ~9 回合（合并后 ~7）。
2. **并行化候选表**（P1-P5）：p̃ 多 LLM 盲生成 / κ 换位双判 / 第二格实验 / 8 run 重跑 / arena 语义重判。P1/P2/P3 信息边界；P4 BLOCKED by finding #17；P5 风险最低。
3. **成本估算总表**：12 blocker 三级分类（L1×5 ≈ 10 回合 + L2×7 ≈ 22 回合 = ~32 回合）+ 16 major/4 minor 处置建议 + 机判/并行成本汇总。
4. **负面结果声明六条**：W0 退化 / W1 tie-sensitive / new W3 top5_gold tie-sensitive / per-run 无 run 过线 / 语义级重判不可机判 / κ 值计算不可机判。
5. **给 G6 的导出**：建议 G6 前落地 5 项（B10/B3+B11/B6/C4/C3）+ 留给后续 5 项 + 硬约束提醒 3 条。
6. **交付物** `bench/rubric-v3/ablation/g5-optimization-list.md`。

## 【阶段】
rubric-v3 研究级审计链（G1-G6）的第五环。消费 G4 三类「部分规避」结构（降档→强制机械化 / 覆盖缺失→补覆盖 / 强度不足→加固阈值）+ adversarial-check 32 findings（12 blocker）+ R5.2 assert-* 脚本先例，回答「哪些判定可以机械化防住、哪些步骤可以并行加速、各需多少成本」。本 goal 只做设计+成本估算，不实现任何脚本、不执行任何并行步骤（B3 边界）。

## 【SOP 索引】
- `sop/arena-loop-pipeline.md`（唯一 SOP 入口）
- `loop/prompt-first/00-common-review.md` + `01..04.5`（阶段定义）
- `receipts/adversarial-check-rubric-v3.json`（32 findings，本地路径）
- `bench/self-opt-tester/r5/assert-packet-symmetry.py` + `bench/rubric-v3/ablation/scripts/assert-g1-audit.py`（assert 脚本模式参考）
- `bench/rubric-v3/ablation/{prior-estimates,judge-blindtest-r1,hit-matrix,stats-w3w4}.json`（冻结只读）
- `bench/rubric-v3/ablation/g4-vulnerability-crosscheck.md`（G4 导出，上游输入）

## 【验收标准】
1. 六阶段工件齐全于 `loop-artifacts/stages/<N>/`，文件名带前缀 `RV3G5-`
2. 01：四因素分解（F1 交付结构 / F2 机判化来源盘点 / F3 并行化盘点 / F4 成本口径）+ 空缺 G1-G3
3. 02：web-llm 强制步骤执行并留回执（三 provider error → 记录失败继续）+ F1-F5 证据固化 + C1-C5 可行性 + P1-P5 可行性 + 负面结果四条
4. 02.5：反方质询 Q1-Q6（验证范围限定 / tie-sensitivity 削弱 / W1 表述修正 / per-run 一致性 / 成本估算依据 / 保真度风险区分）+ 风险登记 R1-R6 + 对抗核验停止理由
5. 03：行动 DAG（A1-A3）+ 关键判读分支预注册 + 不做的事边界（不实现脚本 / 不替 G6 定稿 / 不改冻结数据 / 不执行并行步骤）
6. 04：交付物落盘（五节结构完整）+ 诚实保留（schema 未定稿 / B2 信息边界 / 16 major 未逐条分级 / web-llm 失效 / 成本单位标注）
7. 04.5：反方检查六条 + verdict pass + repair_stage 无 + 给 G6 的下一步建议（12 blocker 分类表 / tie-sensitivity 限定语 / 5 项 L1 修订可并入 G6）
8. 冻结数据零修改（git status 可查）
9. commit + push 分支 `ralph/rubric-v3-audit-g5` + ls-remote 验证 + merge main + queue 注记

## 【失败降级】
- web-llm 三 provider 均不可用 → 记录失败回执后继续，不阻塞
- 12 blocker 中某条无法分级 → 标"待 G6 判定"而非强行归类
- 机判化候选中有实际不可机判的项 → 移入负面结果声明节
- 并行化候选成本超出本轮可估范围 → 标"信息边界"并说明缺什么信息
- merge 冲突 → 停手登记 APPROVALS，不 force