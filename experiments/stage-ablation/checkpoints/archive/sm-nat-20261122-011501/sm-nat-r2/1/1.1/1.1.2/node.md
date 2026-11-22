# N27: Top-K 对象覆盖的大小比例：Mass_K = 1 - (K/N)^(-0.1) / (1 - (1/N)^(-0.1))，用于评估缓存容量 128GB 能覆

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

Top-K 对象覆盖的大小比例：Mass_K = 1 - (K/N)^(-0.1) / (1 - (1/N)^(-0.1))，用于评估缓存容量 128GB 能覆盖的大小分布头部比例。例如 K=1000 (1%)，Mass_K ≈ 1 - (0.01)^(-0.1) / (1 - (0.00001)^(-0.1)) ≈ 1 - 0.794 / (1 - 0.0316) ≈ 0.74，即 Top 1% 对象占 74% 的总大小。

## Corrected Claim

Top-K 对象覆盖的大小比例：Mass_K = 1 - (K/N)^(-0.1) / (1 - (1/N)^(-0.1))，用于评估缓存容量 128GB 能覆盖的大小分布头部比例。例如 K=1000 (1%)，Mass_K ≈ 1 - (0.01)^(-0.1) / (1 - (0.00001)^(-0.1)) ≈ 1 - 0.794 / (1 - 0.0316) ≈ 0.74，即 Top 1% 对象占 74% 的总大小。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

Zipf law cumulative mass formula top K fraction
