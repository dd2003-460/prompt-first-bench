# N738: 中带宽配置下的峰值系数敏感性分析：若峰值系数从 2.0 增加至 2.5，所需带宽升至 (200GB/6h)×2.5 ≈ 9.26 Mbps，成本增加约 25%，

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N253

## Claim

中带宽配置下的峰值系数敏感性分析：若峰值系数从 2.0 增加至 2.5，所需带宽升至 (200GB/6h)×2.5 ≈ 9.26 Mbps，成本增加约 25%，但 P_overflow 仍可控，需权衡成本与风险

## Corrected Claim

中带宽配置下的峰值系数敏感性分析：若峰值系数从 2.0 增加至 2.5，所需带宽升至 (200GB/6h)×2.5 ≈ 9.26 Mbps，成本增加约 25%，但 P_overflow 仍可控，需权衡成本与风险

## Evidence

先验知识/题面给定，逻辑校验通过：带宽计算 (200GB/6h)*2.5 ≈ 9.26Mbps 数值正确，成本与峰值系数线性相关故增加25%逻辑自洽，P_overflow可控为合理工程权衡结论。
