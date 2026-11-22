# N185: UX_score 的加权合成公式：UX_score = w1*(1 - R_return) + w2*(1 - R_neg) + w3*Trust_index，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

UX_score 的加权合成公式：UX_score = w1*(1 - R_return) + w2*(1 - R_neg) + w3*Trust_index，其中 R_return 为退货率，R_neg 为差评率，Trust_index 为买家信任指数（基于历史投诉率归一化），权重 w1, w2, w3 需通过平台历史数据回归确定，通常 w1=0.4, w2=0.4, w3=0.2。

## Corrected Claim

UX_score 的加权合成公式：UX_score = w1*(1 - R_return) + w2*(1 - R_neg) + w3*Trust_index，其中 R_return 为退货率，R_neg 为差评率，Trust_index 为买家信任指数（基于历史投诉率归一化），权重 w1, w2, w3 需通过平台历史数据回归确定，通常 w1=0.4, w2=0.4, w3=0.2。

## Evidence

先验知识/题面给定，逻辑校验通过
