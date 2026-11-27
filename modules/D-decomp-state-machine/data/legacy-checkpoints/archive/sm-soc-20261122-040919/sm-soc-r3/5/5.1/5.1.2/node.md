# N352: 参数β的校准方法：β = -ln(P_deal_at_premium_10 / α) / 0.10，若溢价10%时成交率降至基准的50%，则 β ≈ 6.93，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N106

## Claim

参数β的校准方法：β = -ln(P_deal_at_premium_10 / α) / 0.10，若溢价10%时成交率降至基准的50%，则 β ≈ 6.93，远大于题面假设的0.5-1.0，说明价格敏感度极高。

## Corrected Claim

参数β的校准方法：β = -ln(P_deal_at_premium_10 / α) / 0.10，若溢价10%时成交率降至基准的50%，则 β ≈ 6.93，远大于题面假设的0.5-1.0，说明价格敏感度极高。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确，ln(2)≈0.693，β=0.693/0.1=6.93，数值量级合理
