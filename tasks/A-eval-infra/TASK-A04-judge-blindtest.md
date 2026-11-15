# origin: ai — 独立 judge 盲测任务书（Claude Code ralph loop 通道）

【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00-common-review.md + 01..04.5（仓库内）。
2. 每阶段产出落盘 loop-artifacts/stages/<N>/，阶段判定 pass 才进下一阶段。
3. 完成后 commit + push（含全部 loop-artifacts/）。
4. 通道故障 → 报告 Lead，由 Lead 降级本地执行，不得静默跳过 loop。

## 目标

验证 W3 = w1×w2 乘法组合权重在**独立 judge** 下是否仍满足构念效度门槛（top-5 高权重节点 ≥3/5 带 gold 专家标记）。r70c 结论：W3 刚过线(3/5)但 p̃ 来自同一 judge（自我偏袒），需换模型家族盲测。

## 背景数据（都在 main 分支，直接读）

- `bench/rubric-v3/ablation/TASK-ablation.md` — 原消融任务书（gold 节点定义、31 节点清单、■瓶颈/★订正标记规则）
- `bench/rubric-v3/ablation/hit-matrix.json` — 8 runs × 31 节点命中矩阵
- `bench/rubric-v3/ablation/prior-estimates.json` — 原 judge 的 p̃/w1/w2 估计
- `bench/rubric-v3/ablation/stats-recomputed.json` — r70b 复算统计
- `bench/self-opt-tester/bench.md` O3 章节 — r70c 结论摘要

## 盲测协议（关键约束）

1. **独立性**：你估 p̃ 时，禁止参考 prior-estimates.json 里的数值。只允许看：节点文本 + 其父节点上下文 + gold 标注的存在性（不看具体 h 值分布）。
2. **p̃ 定义**（与 TASK-ablation.md 一致）：无 gold 的 LLM 在父节点上下文下盲生成该子拆分的先验概率，取值 (0,1]。
3. **公式**：w_v = 1 + min(−log₂ p̃_v, log₂(1/ε))，ε=0.01。w1 用 SHARE 份额（从 hit-matrix 可推导），W3 = w1×w2。
4. **输出**：`bench/rubric-v3/ablation/judge-blindtest-r1.json`，结构：
   ```json
   {"judge": "<你的模型名>", "date": "...", "nodes": {"N-x": {"p_tilde": 0.xx, "w2": x.x, "rationale": "一句话"}, ...}, "w3_top5": ["节点id按W3降序前5"], "construct_validity_pass": true/false}
   ```
5. **验收**：
   - 31 个节点全部有 p̃ + rationale（禁空）
   - W3 top-5 中 ≥3 个带 gold 标记（■瓶颈/★订正）→ construct_validity_pass=true
   - 与原 judge 的 p̃ 做 Spearman ρ（跨 judge 一致性），ρ<0.6 → 标"prior 不稳定，W3 不可信"
   - commit + push 到你的分支，ls-remote 记录落点

## 失败降级

无法完成某节点估计 → p̃ 填 null + rationale 写原因，不虚构。全量 null >10 个 → 回执标 blocked 停。