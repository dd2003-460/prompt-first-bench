# N22: 性能数据溯源：所有吞吐量/延迟数据必须标注来源（官方基准测试 vs 第三方实测 vs 理论计算）；例如 NVIDIA 官方声称 H100 在 LLaMA-70B

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

性能数据溯源：所有吞吐量/延迟数据必须标注来源（官方基准测试 vs 第三方实测 vs 理论计算）；例如 NVIDIA 官方声称 H100 在 LLaMA-70B 上达到 X tokens/s，但实际部署可能受驱动、框架、批处理大小影响而降低 20-40%

## Corrected Claim

性能数据溯源：所有吞吐量/延迟数据必须标注来源（官方基准测试 vs 第三方实测 vs 理论计算）；例如 NVIDIA 官方声称 H100 在 LLaMA-70B 上达到 X tokens/s，但实际部署可能受驱动、框架、批处理大小影响而降低 20-40%

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GPU LLM inference benchmark real world vs official
