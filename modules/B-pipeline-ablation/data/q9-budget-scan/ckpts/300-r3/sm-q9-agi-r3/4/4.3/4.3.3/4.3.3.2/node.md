# N262: 低吞吐长时本地工作点：假设日均N_cycles=5 (每4.8h一循环，含长RAG/复杂推理), 单循环电费=4.608元; 结合N83长上下文Token量(1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N85

## Claim

低吞吐长时本地工作点：假设日均N_cycles=5 (每4.8h一循环，含长RAG/复杂推理), 单循环电费=4.608元; 结合N83长上下文Token量(16300)，本地单Token成本 ≈ 2.83e-7 元/Token

## Corrected Claim

低吞吐长时本地工作点：假设日均N_cycles=5 (每4.8h一循环，含长RAG/复杂推理), 单循环电费=4.608元; 结合N83长上下文Token量(16300)，本地单Token成本 ≈ 2.83e-7 元/Token

## Evidence

先验知识/题面给定，逻辑校验通过：单Token成本 = 单循环电费 / 单循环Token量 = 4.608 / 16300 ≈ 2.827e-7 元/Token，与陈述中的 2.83e-7 元/Token 在精度范围内一致，计算逻辑自洽。
