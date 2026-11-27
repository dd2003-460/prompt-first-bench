# N669: L40S 在 32K 上下文 INT8 量化下的理论 Decode 吞吐量上限：显存带宽 864 GB/s，INT8 权重 27GB + BF16 KV Cac

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N238

## Claim

L40S 在 32K 上下文 INT8 量化下的理论 Decode 吞吐量上限：显存带宽 864 GB/s，INT8 权重 27GB + BF16 KV Cache 8GB = 35GB，理论上限 = 864 / 35 ≈ 24.7 tokens/s，实测效率系数 0.6-0.8，预计为 14.8-19.8 tokens/s [knowledge: '模型先验知识：Decode 吞吐量 = 显存带宽 / (权重大小 + KV Cache 大小)']

## Corrected Claim

L40S 在 32K 上下文 INT8 量化下的理论 Decode 吞吐量上限：显存带宽 864 GB/s，INT8 权重 27GB + BF16 KV Cache 8GB = 35GB，理论上限 = 864 / 35 ≈ 24.7 tokens/s，实测效率系数 0.6-0.8，预计为 14.8-19.8 tokens/s [knowledge: '模型先验知识：Decode 吞吐量 = 显存带宽 / (权重大小 + KV Cache 大小)']

## Evidence

先验知识/题面给定，逻辑校验通过：Decode阶段为内存带宽瓶颈，吞吐量上限=带宽/每token读取数据量(权重+KV Cache)，计算 864/35≈24.7 正确，效率系数范围合理。
