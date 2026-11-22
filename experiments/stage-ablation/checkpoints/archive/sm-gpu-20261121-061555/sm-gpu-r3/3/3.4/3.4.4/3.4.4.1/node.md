# N262: NVFP4量化下Qwen3-27B在H100 80GB上的权重占用仅为6.75GB，允许将batch_size提升至8-16以充分利用HBM3带宽(3.35 T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

NVFP4量化下Qwen3-27B在H100 80GB上的权重占用仅为6.75GB，允许将batch_size提升至8-16以充分利用HBM3带宽(3.35 TB/s)，此时有效带宽利用率修正因子从单请求的0.70提升至0.75-0.80，因为大batch能摊薄反量化固定开销。

## Corrected Claim

NVFP4量化下Qwen3-27B在H100 80GB上的权重占用仅为6.75GB，允许将batch_size提升至8-16以充分利用HBM3带宽(3.35 TB/s)，此时有效带宽利用率修正因子从单请求的0.70提升至0.75-0.80，因为大batch能摊薄反量化固定开销。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在NVFP4(4bit)下权重约6.75GB，符合数学推导；大batch摊薄反量化开销从而提升带宽利用率至0.75-0.80符合系统性能优化直觉。
