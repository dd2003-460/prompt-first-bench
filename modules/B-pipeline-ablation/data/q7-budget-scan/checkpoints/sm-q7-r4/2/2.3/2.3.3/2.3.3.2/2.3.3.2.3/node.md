# N593: 由于 I/O 线程阻塞与上下文切换，实际有效吞吐下降比例 ΔThroughput = 15%-20%，等效有效容量因子 f_eff = 1.0 - ΔThrou

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N211

## Claim

由于 I/O 线程阻塞与上下文切换，实际有效吞吐下降比例 ΔThroughput = 15%-20%，等效有效容量因子 f_eff = 1.0 - ΔThroughput = 0.80-0.85

## Corrected Claim

由于 I/O 线程阻塞与上下文切换，实际有效吞吐下降比例 ΔThroughput = 15%-20%，等效有效容量因子 f_eff = 1.0 - ΔThroughput = 0.80-0.85

## Evidence

先验知识/题面给定，逻辑校验通过：I/O阻塞导致的吞吐损失通常在10%-30%区间，15%-20%符合工程经验量级，且f_eff计算逻辑自洽。
