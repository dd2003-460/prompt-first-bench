# T31: Source-Filtering Experiment (decomposition)

## 分解树

- A. 过滤策略实现
  - A1. FILTER_KEYWORDS 定义（每 Q 一组 answer-relevant 关键词）
  - A2. filter_sources() 函数：title+snippet 匹配，返回通过子集
  - A3. S7F arm：S7T prompt + filtered sources（0 条通过则 fallback 到无来源）
- B. 实验执行
  - B1. 跑 15 runs (S7F-Q1..Q5-r1..r3), temp=0.1+seed
  - B2. 打分 M1-M6
- C. 三臂对比分析
  - C1. S7 vs S7T vs S7F per-dim delta 表
  - C2. 核心问题：M1 是否从 S7T 的 0.28 恢复到 ≥S7 的 0.56？
  - C3. M6 是否保留（filtered sources 仍有引用价值）？
  - C4. 结论：filtering 是否兑现 §5.1 "source filtering" 修复方向？
- D. 论文更新
  - D1. §5.1 加 S7F 行（三臂对比表）
  - D2. Conclusion 第四条修正（naive→filtered 有改善）

正交性：A(实现)/B(执行)/C(分析)/D(写作) 顺序依赖 ✓
完备性：回答"过滤能否救回 M1" = A+B+C+D ✓

## 缺口清单

| 子项 | 缺什么 | 状态 |
|------|--------|------|
| A1 | 关键词选择是否足够精准（false positive/negative） | [待核验] 需看过滤后实际注入的内容 |
| A3 | 0 条通过时的 fallback 行为（注入空 vs 不注入工具说明段） | [待核验] 设计决策 |
| B1 | 运行时间 ~15 min（同 T30） | — |
| C2 | S7F M1 预期值 | [待核验] 假设 ≥0.50（接近 S7 的 0.56） |
| C4 | 如果 M1 没恢复 → 说明 anchoring 不是唯一机制 | — |

## 任务表

| # | 动作 | 验收 |
|---|------|------|
| 1 | harness 加 S7F arm + filter_sources() | dry-run 显示 filtered sources |
| 2 | 跑 15 runs | 15/15 JSON 落盘 |
| 3 | 打分 + 三臂对比表 | S7/S7T/S7F per-Q delta |
| 4 | 论文 §5.1 更新 | 三臂表 + 结论 |
| 5 | commit + push | git log 确认 |