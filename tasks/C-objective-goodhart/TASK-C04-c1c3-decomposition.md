# C1+C3 分解：D1 扩 rep + 配对检验

> origin: ai · 2026-11-07 · pfb-c1c3-paired-test goal decomp

## 分解树

```
C1+C3 (打赢开源统计硬化)
├── C2. 检索对齐可行性（前置决策，~1h）
│   ├── C2a. 算 D1 pipeline 单次 run 的搜索调用量（grep ablation_harness.py 中 research_hook 逻辑）
│   ├── C2b. 查 duckduckgo_search 免费限额（rate limit / daily cap）
│   ├── C2c. 判断：15 runs × N searches/run 是否超限？
│   └── 决策：够 → 继续 duckduckgo；不够 → 降级声明"检索质量下限配置"或找免费替代
├── C1. D1 扩 rep（~2h 本地计算）
│   ├── C1a. 确认 5 道题（Q1/Q3/Q4 + 选 2 道已有 gold 的题）
│   ├── C1b. 跑 D1 pipeline × 5 题 × 3 rep = 15 runs（duckduckgo 检索 + 27b 生成）
│   ├── C1c. 用 score_s10_v2.py 对 15 runs 打分（rubric-v2）
│   └── C1d. 落盘 d1-scores-v2.json
├── C3. 配对检验（~30min 分析）
│   ├── C3a. S5 对应 5 题的 n=30 数据取 per-question mean（已有）
│   ├── C3b. Per-question paired sign test（Wilcoxon signed-rank 更稳，n=5 时 sign test 功效太低）
│   ├── C3c. Bootstrap CI（10000 resamples, paired difference distribution）
│   ├── C3d. 效应量：Cohen's d on paired differences
│   └── C3e. 分项归因：M1-M5 哪一维拉开差距（per-dimension paired comparison）
└── Q. 质量门
    ├── Q-a. D1 runs 全轮次文本保留（可复现）
    ├── Q-b. 评分用 rubric-v2（已过 κ gate r=0.835）
    └── Q-c. 结论限定声明："27b 家族 + duckduckgo 检索 + AI/ML 域 5 题"
```

## 缺口清单

| 子项 | 缺什么 | 怎么补 |
|------|--------|--------|
| C2a | D1 单次 run 实际搜索次数 | grep research_hook 调用逻辑，数 API calls |
| C2b | duckduckgo_search 当前 rate limit | 读包文档 / 试跑观察 |
| C1a | 选哪 5 道题 | 已有 gold 的：Q1/Q3/Q4/Q6/Q7/Q8/Q9/Q10 → 选覆盖不同子领域的 5 道 |
| C1b | D1 pipeline 能否直接复用 s10_runner 的 call_llm | 看 ablation_harness.py 中 D1 arm 定义 |
| C3b | n=5 时 Wilcoxon 最小 p 值 | 理论值 p≥0.0625（5 对全同向）→ 可能永远不显著 → 需 bootstrap 补充 |
| C3c | [待核验] bootstrap CI 在 n=5 时的可靠性 | 文献：n<10 时 bootstrap 偏乐观，需标注 |
| Q-c | 结论外推边界 | 写进报告：模型/检索/题目域三限定 |

## 关键风险

1. **n=5 功效不足**：即使 S5 真的比 D1 好 0.2，5 个配对的 sign test 也大概率不显著。对策：bootstrap CI + 效应量 + 明确声明"方向性证据，非统计证明"。
2. **D1 检索质量是下限**：duckduckgo 无 key，结果质量不稳定。如果 D1 分数被检索拖低，Δ 会虚高。对策：C2 先判断，必要时降级声明。
3. **S5 的 n=30 是 6 题 × 5 rep**：取 per-question mean 时注意每题 rep 数一致（都是 5）。

## 预期产出

- `runs/d1-rep15-v2.json`（15 runs 原始输出 + v2 分数）
- `runs/c1c3-paired-test.md`（报告：per-question table + 检验结果 + 效应量 + 分项归因 + 限定声明）
- 结论：S5 vs D1 在 AI/ML 域 5 题上的方向性优势 + 置信区间