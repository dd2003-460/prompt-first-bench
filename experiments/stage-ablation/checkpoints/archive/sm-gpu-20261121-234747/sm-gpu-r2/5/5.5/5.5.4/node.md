# N134: 输出分布偏移的量化指标：KL散度D_KL(P_BF16 || P_quantized)，通过采样1000条prompt计算两种精度下输出token分布的KL散度

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

输出分布偏移的量化指标：KL散度D_KL(P_BF16 || P_quantized)，通过采样1000条prompt计算两种精度下输出token分布的KL散度，阈值设为<0.1为可接受，>0.5为不可接受

## Corrected Claim

输出分布偏移的量化指标：KL散度D_KL(P_BF16 || P_quantized)，通过采样1000条prompt计算两种精度下输出token分布的KL散度，阈值设为<0.1为可接受，>0.5为不可接受

## Evidence

先验知识/题面给定，逻辑校验通过
