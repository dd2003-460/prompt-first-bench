# T29: T17 Internal Report Sync (decomposition)

## 分解树

- A. 数字同步（S6/S7 重打分后）
  - A1. §S6 段：0.462→0.461, +0.065→+0.113
  - A2. §S7 段：0.559→0.548, Q1 0.717→0.670, Q2 0.700→0.637
  - A3. Per-Q 总表（line ~271-276）：S6/S7 行更新
  - A4. Hetero-judge 表（line ~314-321）：local total 列更新
- B. Rep diversity 说明修正
  - B1. 原报告若声称"所有 rep 相同"→ 改为 S0-S5 vLLM 非确定性 + S6/S7 temp=0.1+seed
  - B2. 新增一句：2/90 cells partial dup (S1-Q1 r2=r3, S0-Q4 r2=r3)
- C. M7 列补入 per-dim 表（若原表无 M7 列）
- D. 一致性检查：grep 旧数字确认零残留

正交性自检：A(数字) / B(方法论说明) / C(表格结构) / D(验证) — 互不依赖 ✓
完备性：paper v2.0 已改的 6 处数字 + 3 处描述，report 对应位置全覆盖 ✓

## 缺口清单

| 子项 | 缺什么 | 来源 |
|------|--------|------|
| A1-A4 | 无（新数字已在 /tmp/score-s6s7-combined.json 验证） | 本地 |
| B1-B2 | [待核验] report 原文是否真的写了"byte-identical"（需 grep 确认） | 本地 grep |
| C | [待核验] report per-dim 表是否已有 M7 列 | 本地 read |
| D | 无 | 本地 grep |

## 任务表

| # | 动作 | 验收 |
|---|------|------|
| 1 | grep report 中所有旧数字 + "identical"/"temperature" 描述 | 列出需改行号 |
| 2 | 逐行 patch 更新 | grep 旧数字 = 0 hits |
| 3 | commit + push pfb | git log 确认 |