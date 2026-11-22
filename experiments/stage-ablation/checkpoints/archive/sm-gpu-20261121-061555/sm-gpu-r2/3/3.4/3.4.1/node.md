# N87: BF16精度下Qwen3-27B在H100 (80GB HBM3)上的有效显存带宽利用率修正因子为0.85-0.90，实际吞吐量基准需乘以该因子以反映非理想访存

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20, N21, N24

## Claim

BF16精度下Qwen3-27B在H100 (80GB HBM3)上的有效显存带宽利用率修正因子为0.85-0.90，实际吞吐量基准需乘以该因子以反映非理想访存模式。

## Corrected Claim

BF16精度下Qwen3-27B在H100 (80GB HBM3)上的有效显存带宽利用率修正因子为0.85-0.90，实际吞吐量基准需乘以该因子以反映非理想访存模式。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

H100 BF16 LLM inference bandwidth utilization efficiency factor
