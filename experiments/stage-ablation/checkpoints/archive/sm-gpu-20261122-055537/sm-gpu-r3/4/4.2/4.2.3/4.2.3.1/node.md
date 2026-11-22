# N224: 2x RTX 4090 双卡方案的 GPU 部分满载功耗为 2 * 450W = 900W，基于单卡 TDP 450W 的线性叠加假设，忽略双卡互联带来的额外计

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

2x RTX 4090 双卡方案的 GPU 部分满载功耗为 2 * 450W = 900W，基于单卡 TDP 450W 的线性叠加假设，忽略双卡互联带来的额外计算开销。

## Corrected Claim

2x RTX 4090 双卡方案的 GPU 部分满载功耗为 2 * 450W = 900W，基于单卡 TDP 450W 的线性叠加假设，忽略双卡互联带来的额外计算开销。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 单卡 TDP 确为 450W，双卡线性叠加计算 2*450=900W 符合物理直觉与工程常识，忽略互联开销的假设在纯计算负载下合理。
