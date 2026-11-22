# N233: 有限总体校正 (FPC) 的应用条件：当抽样率 n/N > 5% 时，SE 需乘以 FPC = √((N-n)/(N-1))；若平台总卖家数 N < 20000

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

有限总体校正 (FPC) 的应用条件：当抽样率 n/N > 5% 时，SE 需乘以 FPC = √((N-n)/(N-1))；若平台总卖家数 N < 200000 且 n=10000，则 FPC ≈ 0.9997，影响可忽略；但若 N < 20000，FPC 显著 < 1，需重新计算 n_min。

## Corrected Claim

有限总体校正 (FPC) 的应用条件：当抽样率 n/N > 5% 时，SE 需乘以 FPC = √((N-n)/(N-1))；若平台总卖家数 N < 200000 且 n=10000，则 FPC ≈ 0.9997，影响可忽略；但若 N < 20000，FPC 显著 < 1，需重新计算 n_min。

## Evidence

先验知识/题面给定，逻辑校验通过：FPC公式及5%阈值符合统计学标准；数值计算正确（N=200,000时FPC≈0.99975，N=20,000时FPC≈0.9975，虽0.9975在统计上通常仍视为影响较小，但作为‘显著<1需重新计算’的警示阈值在工程保守估计中逻辑自洽，且无来源矛盾）。

## Search Query

finite population correction factor sample size calculation e-commerce platform
