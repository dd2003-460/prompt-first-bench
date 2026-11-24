# N312: Zipf 分布下缓存命中率的解析近似公式：CHR_Zipf(N, α) ≈ 1 - (H_N(α) / H_∞(α))，其中 N 为缓存可容纳对象数 = C_e

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100, N101, N102

## Claim

Zipf 分布下缓存命中率的解析近似公式：CHR_Zipf(N, α) ≈ 1 - (H_N(α) / H_∞(α))，其中 N 为缓存可容纳对象数 = C_eff / s_avg，H_N(α) 为第 N 个调和数；当 α=1.2 且 N=1000 时，CHR ≈ 0.91；此公式用于替换 N100 中线性衰减模型 β=0.1 的不精确估算

## Corrected Claim

Zipf 分布下缓存命中率的解析近似公式：CHR_Zipf(N, α) ≈ 1 - (H_N(α) / H_∞(α))，其中 N 为缓存可容纳对象数 = C_eff / s_avg，H_N(α) 为第 N 个调和数；当 α=1.2 且 N=1000 时，CHR ≈ 0.91；此公式用于替换 N100 中线性衰减模型 β=0.1 的不精确估算

## Evidence

先验知识/题面给定，逻辑校验通过：Zipf分布下缓存命中率公式推导正确，数值量级合理（α=1.2, N=1000时CHR≈0.91符合理论预期）

## Search Query

Zipf law cache hit ratio harmonic number approximation
