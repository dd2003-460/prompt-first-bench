# origin: ai — R5.1 第二独立打分器任务书（Claude Code ralph loop 通道）

【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00-common-review.md + 01..04.5（仓库内）。
2. 每阶段产出落盘 loop-artifacts/stages/<N>/，阶段判定 pass 才进下一阶段。
3. 完成后 commit + push（含全部 loop-artifacts/）。
4. 通道故障 → 报告 Lead，由 Lead 降级本地执行，不得静默跳过 loop。

## 目标

给 self-opt-tester bench 加第二个独立打分器（你 = Claude Code），对 r4 的 3 run × 7 指标盲打 21 分，与 DeepSeek 独立分做打分器间一致性分析（per-metric Spearman ρ + 全量 pairwise κ），回答 bench.md 已知缺陷 #5：「独立打分器仍只 1 个——需第二独立打分器做打分器间一致性」。

## 背景数据（main 分支直接读）

- `bench/self-opt-tester/bench.md` — 指标定义表（M1-M7 固定口径）+ r4 数据表 + 已知缺陷清单
- `bench/self-opt-tester/r4/independent-scoring-deepseek.json` — DeepSeek 盲打 18 分 + 裁决记录（**你的打分禁止参考此文件里的数值**，只允许看指标定义和 run 证据）
- `bench/self-opt-tester/run2-arena/`、`r5/run5/task-brief.md`、`r4/` 目录 — 各 run 的证据材料（锚点、账本、回执）

## 盲打协议（关键约束）

1. **独立性**：打分时禁止读 independent-scoring-deepseek.json 的分数值。允许看：指标定义（bench.md 表格）+ 每个 run 的原始证据文件。
2. **口径**：严格按 bench.md 指标定义表的「可验证口径」列打分，0-100，每项附一句话依据（引用具体证据文件路径）。
3. **输出**：`bench/self-opt-tester/r5/scoring-claude-r1.json`：
   ```json
   {"scorer": "claude-code", "date": "...", "scores": {"run1": {"M1": {"score": xx, "basis": "..."}, ...}, "run2": {...}, "run3": {...}}}
   ```
4. **一致性分析**（打完后再读 DeepSeek 文件做对比，这一步允许）：
   - per-metric Spearman ρ（3 个 run 点，n=3 只做描述不做推断，声明即可）
   - 分歧项清单：|Δ|>15 的 (run, metric) 对，逐项写双方依据对照 + 你的裁定倾向（不覆盖任何一方，只标倾向）
   - 落盘 `bench/self-opt-tester/r5/scorer-agreement-r1.json`
5. **验收**：
   - 21 分全有 score+basis（禁空）
   - 分歧项全部有对照分析
   - commit + push 到你的分支，ls-remote 记录落点

## 失败降级

某 run 证据不足以打某指标 → score=null + basis 写缺什么，不虚构。null >5 项 → 回执标 blocked 停。