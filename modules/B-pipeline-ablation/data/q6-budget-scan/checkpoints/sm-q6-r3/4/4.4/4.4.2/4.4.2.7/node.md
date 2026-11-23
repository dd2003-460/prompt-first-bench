# N223: PAR（峰值/均值比）对缓存命中率的影响模型：H_avg = H_base * (1 - k_par * (PAR - 1))，其中k_par=0.1-0.2，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69, N70, N71

## Claim

PAR（峰值/均值比）对缓存命中率的影响模型：H_avg = H_base * (1 - k_par * (PAR - 1))，其中k_par=0.1-0.2，PAR=3时H_avg下降20-40%，导致P99延迟上升

## Corrected Claim

PAR（峰值/均值比）对缓存命中率的影响模型：H_avg = H_base * (1 - k_par * (PAR - 1))，其中k_par=0.1-0.2，PAR=3时H_avg下降20-40%，导致P99延迟上升

## Evidence

先验知识/题面给定，逻辑校验通过
