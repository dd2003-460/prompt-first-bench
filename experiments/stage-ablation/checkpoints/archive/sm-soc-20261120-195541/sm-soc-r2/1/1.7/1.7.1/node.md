# N40: 价格锚定提示对卖家挂价的预期下调幅度 δ 并非固定为 0.10，其实际值取决于提示信息的显著性（视觉权重 W_vis）与卖家对基准价的信任度（Trust_fac

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11, N12, N13

## Claim

价格锚定提示对卖家挂价的预期下调幅度 δ 并非固定为 0.10，其实际值取决于提示信息的显著性（视觉权重 W_vis）与卖家对基准价的信任度（Trust_factor），计算公式为 δ = δ_base * W_vis * Trust_factor，其中 δ_base 为基准调整率，需通过 A/B 测试确定。

## Corrected Claim

价格锚定提示对卖家挂价的预期下调幅度 δ 并非固定为 0.10，其实际值取决于提示信息的显著性（视觉权重 W_vis）与卖家对基准价的信任度（Trust_factor），计算公式为 δ = δ_base * W_vis * Trust_factor，其中 δ_base 为基准调整率，需通过 A/B 测试确定。

## Evidence

先验知识/题面给定，逻辑校验通过
