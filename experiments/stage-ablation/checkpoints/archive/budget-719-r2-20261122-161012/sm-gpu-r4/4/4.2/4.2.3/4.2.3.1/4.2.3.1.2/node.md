# N510: 工作点2（中性价比-INT4优化）：RTX 4090 在 INT4 权重+INT4 KV 配置下，理论 Decode 吞吐为 1008 GB/s / 13.76

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N210

## Claim

工作点2（中性价比-INT4优化）：RTX 4090 在 INT4 权重+INT4 KV 配置下，理论 Decode 吞吐为 1008 GB/s / 13.768 GB ≈ 73.2 tokens/s，考虑 70% 效率后实际约为 51.2 tokens/s，远超交互阈值，但需评估 INT4 KV 对长文本生成质量的潜在累积误差影响。

## Corrected Claim

工作点2（中性价比-INT4优化）：RTX 4090 在 INT4 权重+INT4 KV 配置下，理论 Decode 吞吐为 1008 GB/s / 13.768 GB ≈ 73.2 tokens/s，考虑 70% 效率后实际约为 51.2 tokens/s，远超交互阈值，但需评估 INT4 KV 对长文本生成质量的潜在累积误差影响。

## Evidence

先验知识/题面给定，逻辑校验通过：1008/13.768≈73.2，73.2*0.7≈51.2，计算无误且符合INT4量化下带宽受限场景的估算逻辑。
