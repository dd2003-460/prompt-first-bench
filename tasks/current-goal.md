# Goal: RUBRIC-V3-FULL-AUDIT / G3 W3/W4 收尾（方案补完验证 + 三选项决策矩阵）

> 创建：2026-10-30 · ralph loop runner（队首大 goal RUBRIC-V3-FULL-AUDIT 的子 goal G3）
> 依据：`tasks/RUBRIC-V3-FULL-AUDIT-task-brief.md` G3 节 + G1/G2 产出（G1-contradiction-audit.md / g2-rootcause.md）

## 【目标】
任务书 G3 = 「stats-w3w4.json 的方案补完验证（对照 G2 根因判断哪个方案值得救）」。交付：
1. **F1 验证链复验**：W3/W4 × 8run 分数、7 对 ρ、W0 tie 分析、global top-5 strict 计数全量独立复算 → 结论「JSON 层验证链已闭合」（修正任务书「未走完验证链」表述；真实缺口 = 独立 judge 维度）。
2. **F2 敏感性分级**：W3 高敏感（头部 gap 0.0301→0.0020 + gold 3/5↔1/5 翻转）；W4 排序维度中敏感（8/8 位不变）但构念效度维度高敏感（gold 平均排名 6.4→8.6，与 W3 同幅）→ **W3/W4 都不单独值得救**。
3. **F3 三选项决策矩阵**：O1 改判据（推荐子选项 gold 平均排名，唯一全组合方向一致；top-10 同级备选；post-hoc 声明）/ O2 第三 judge（R5.2-third-scorer 外部阻塞，本轮不可执行）/ O3 接受降级（可行，代价重估为「校准损失为主、正交信息损失未证」两说并存）。推荐路径供 G6 定稿，本 goal 不定稿。
4. **交付物** `bench/rubric-v3/ablation/g3-w3w4-completion.md`（含负面结果声明三条）。

## 【阶段】
rubric-v3 研究级审计链（G1-G6）的第三环。消费 G2 根因（双源 p̃ 偏差 + 判据极严）+ G1 新发现（per-run top-5 无 run 达 3/5、W2-new run1 反超），回答「哪个方案值得救」——答案是都不单独值得救，出路在判据口径（O1）或证据升级（O2）。

## 【SOP 索引】
- `sop/arena-loop-pipeline.md`（唯一 SOP 入口）
- `loop/prompt-first/00-common-review.md` + `01..04.5`（阶段定义）
- `bench/rubric-v3/ablation/{stats-w3w4,stats-recomputed,hit-matrix,prior-estimates,judge-blindtest-r1}.json` + `gold-tree.md`（全部冻结只读）
- `bench/rubric-v3/ablation/{g2-rootcause,G1-contradiction-audit}.md`（前置产出，只读消费）
- `tasks/goal-queue.md`（R5.2-third-scorer 状态读取）

## 【验收标准】
1. 六阶段工件齐全于 `loop-artifacts/stages/<N>/`，文件名带前缀 `RV3G3-`
2. 01：四因素分解（F1 验证链 / F2 敏感性分级 / F3 决策矩阵 / F4 交付结构）+ 空缺 G1-G3
3. 02：web-llm 强制步骤执行并留回执（三 provider error → 记录失败继续）+ F1-F3 全量复算固化
4. 02.5：反方质询 Q1-Q4（叙述层分层 / post-hoc 声明 / W4 双维度拆分 / O3 代价重估）+ 风险登记 R1-R6 + 对抗核验停止理由
5. 03：行动 DAG + 关键判读分支预注册（B1-B3）+ 边界（不改冻结文件、不动 gold set、不实施任何修复、不定稿）
6. 04：交付物落盘 + 诚实保留（叙述层未逐句核验 / O2 不可实测 / 阈值论证留 G6 / 同族边界 / n=8 描述性）
7. 04.5：反方检查五条 + verdict pass + repair_stage 无 + 给 G4 的下一步建议
8. 冻结数据零修改（git status 可查）
9. commit + push 分支 `ralph/rubric-v3-audit-g3` + ls-remote 验证 + merge main + queue 注记

## 【失败降级】
- web-llm 三 provider 均不可用 → 记录失败回执后继续，不阻塞
- R5.2-third-scorer 未完成（外部阻塞）→ O2 标「不可行于本轮」，只给成本/收益/前置条件评估，不实测
- 任一数字复算不一致 → 停收口回 02 修正并重走 02.5，不带错交付