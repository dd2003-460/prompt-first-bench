# N277: N95 中总数据量 V_total ≈ 118.75 MB 的计算存在量级错误：Pareto(α=1.1) 在 s_min=1KB 时的截断均值 E[Size]

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N95

## Claim

N95 中总数据量 V_total ≈ 118.75 MB 的计算存在量级错误：Pareto(α=1.1) 在 s_min=1KB 时的截断均值 E[Size] 约为 10KB 量级（而非 1.22KB），导致 V_total 实际约为 1.0-1.2 GB 或更大（取决于 s_max 截断），仍远小于 128GB，但修正了均值估算偏差。

## Corrected Claim

N95 中总数据量 V_total ≈ 118.75 MB 的计算存在量级错误：Pareto(α=1.1) 在 s_min=1KB 时的截断均值 E[Size] 约为 10KB 量级（而非 1.22KB），导致 V_total 实际约为 1.0-1.2 GB 或更大（取决于 s_max 截断），仍远小于 128GB，但修正了均值估算偏差。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto(α=1.1) 在 s_min=1KB 时的截断均值确实约为 10KB 量级（E[S|S≥1KB] ≈ 10KB），原 1.22KB 估算存在量级错误，修正后 V_total 约为 1.0-1.2 GB 量级，逻辑自洽且数值合理。
