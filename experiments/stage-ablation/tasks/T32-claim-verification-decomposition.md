# T32: Claim-Level Verification (decomposition)

## 分解树

- A. S7V arm 实现（two-pass generation）
  - A1. Pass 1: S7F prompt → 生成初稿答案 + 引用来源编号
  - A2. Pass 2: 将初稿 + 来源全文喂回模型，指令"逐条核验数字断言，删除无来源支持的数字，标注哪些被删了"
  - A3. 最终输出 = Pass 2 的修正版答案
  - A4. harness 支持 S7V arm（两次 API 调用，temp=0.1+seed）
- B. 实验执行
  - B1. 跑 15 runs (S7V-Q1..Q5-r1..r3)
  - B2. 打分 M1-M6
- C. 四臂对比分析
  - C1. S7/S7T/S7F/S7V per-dim delta 表
  - C2. 核心问题：M1 是否恢复到 ≥S7 的 0.771？
  - C3. M6 是否保留（verification 后仍有引用）？
  - C4. Pass 2 删除了多少断言？（量化 source anchoring 的规模）
  - C5. 结论：claim-level verification 是否兑现 §5.1 修复方向？
- D. 论文更新
  - D1. §5.1 加 S7V 行（四臂对比表）
  - D2. Conclusion 第四条最终版
  - D3. §5.4 ecological validity 更新

正交性：A(实现)/B(执行)/C(分析)/D(写作) 顺序依赖 ✓
完备性：回答"generation-level verification 能否完全恢复 M1" = A+B+C+D ✓

## 缺口清单

| 子项 | 缺什么 | 状态 |
|------|--------|------|
| A2 | Pass 2 prompt 设计（如何精确指令"逐条核验"而不让模型重新生成整个答案） | [待核验] 需 dry-run 看效果 |
| A3 | Pass 2 可能引入新错误（模型在"修正"时幻觉） | [待核验] 需对比 Pass1 vs Pass2 的 M1 |
| B1 | 运行时间 ~30 min（两次调用 × 15 runs） | — |
| C2 | S7V M1 预期值 | [待核验] 假设 ≥0.70（接近 S7 的 0.771） |
| C4 | 如果 Pass 2 删除过多 → 答案变空泛，M4/M5 可能下降 | — |
| D1 | 四臂表是否需要 per-Q 展开（还是只放 mean） | [待核验] 看数据分布决定 |

## 任务表

| # | 动作 | 验收 |
|---|------|------|
| 1 | harness 加 S7V arm (two-pass) | dry-run 显示两次调用 |
| 2 | 跑 15 runs | 15/15 JSON 落盘（含 pass1_text + final_text） |
| 3 | 打分 + 四臂对比表 | S7/S7T/S7F/S7V per-Q delta |
| 4 | 论文 §5.1 更新 | 四臂表 + 结论 |
| 5 | commit + push | git log 确认 |