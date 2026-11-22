# N95: t检验统计量计算：t = k / SE_k，其中 SE_k 为 k 的标准误。根据 CLT，SE_k = σ_k / sqrt(n)。若 n=100, σ_k=

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

t检验统计量计算：t = k / SE_k，其中 SE_k 为 k 的标准误。根据 CLT，SE_k = σ_k / sqrt(n)。若 n=100, σ_k=20%（周期波动率），则 SE_k=2%，对应 k=10% 时 t=5；若 n=100, σ_k=10%，则 SE_k=1%，对应 k=2% 时 t=2。

## Corrected Claim

t检验统计量计算：t = k / SE_k，其中 SE_k 为 k 的标准误。根据 CLT，SE_k = σ_k / sqrt(n)。若 n=100, σ_k=20%（周期波动率），则 SE_k=2%，对应 k=10% 时 t=5；若 n=100, σ_k=10%，则 SE_k=1%，对应 k=2% 时 t=2。

## Evidence

先验知识/题面给定，逻辑校验通过：t统计量定义及标准误公式符合统计学原理，数值计算（20%/10=2%, 10%/2=5; 10%/10=1%, 2%/1=2）准确无误。
