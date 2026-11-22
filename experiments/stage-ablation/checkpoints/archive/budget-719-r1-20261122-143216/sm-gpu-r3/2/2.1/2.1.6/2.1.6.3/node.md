# N204: 2×RTX 3090 方案在 TP=2 下，由于 PCIe Gen4 x16 互联限制，通信开销占比预计为 15%-25%，导致实际 Decode 吞吐量相比单

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N61

## Claim

2×RTX 3090 方案在 TP=2 下，由于 PCIe Gen4 x16 互联限制，通信开销占比预计为 15%-25%，导致实际 Decode 吞吐量相比单卡理论峰值下降 15%-25%，具体数值需结合 vLLM 的 custom all-reduce 优化效果评估

## Corrected Claim

2×RTX 3090 方案在 TP=2 下，受 PCIe Gen4 x16 互联带宽限制，通信开销会显著影响实际 Decode 吞吐量，具体下降比例需结合 vLLM 的 custom all-reduce 优化效果及实际负载评估。

## Evidence

[质询]该陈述包含具体的经验性数值范围（15%-25%），这属于特定硬件配置和软件优化下的性能指标，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 3090 tensor parallelism 2x PCIe Gen4 communication overhead Qwen3 27B decode speed loss
