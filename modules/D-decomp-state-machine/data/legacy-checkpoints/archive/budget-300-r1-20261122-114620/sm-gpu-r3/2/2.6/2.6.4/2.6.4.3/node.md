# N266: Decode 阶段的实际有效带宽利用率 η_eff 通常受限于内存访问模式与缓存未命中，对于大模型单用户推理，η_eff 经验值约为 0.8-0.9，因此实际吞

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N82

## Claim

Decode 阶段的实际有效带宽利用率 η_eff 通常受限于内存访问模式与缓存未命中，对于大模型单用户推理，η_eff 经验值约为 0.8-0.9，因此实际吞吐为理论峰值 28.8 tokens/s 乘以 η_eff，即 23-26 tokens/s

## Corrected Claim

Decode 阶段的实际有效带宽利用率 η_eff 通常受限于内存访问模式与缓存未命中，对于大模型单用户推理，η_eff 经验值约为 0.8-0.9，因此实际吞吐为理论峰值 28.8 tokens/s 乘以 η_eff，即 23-26 tokens/s

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

A100 decode throughput effective bandwidth utilization LLM inference
