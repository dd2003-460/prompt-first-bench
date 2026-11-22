# N140: GMV 与佣金收入的非线性关系修正项：由于支付通道费（Payment Processing Fee）通常为固定比例（如 Stripe 的 2.9% + $0.3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N57, N58, N59

## Claim

GMV 与佣金收入的非线性关系修正项：由于支付通道费（Payment Processing Fee）通常为固定比例（如 Stripe 的 2.9% + $0.30），平台净佣金收入 $R_{net} = GMV \times (r_{fee} - r_{pay}) - N_{orders} \times C_{fixed}$，其中 $r_{pay}$ 为支付通道费率，$C_{fixed}$ 为单笔固定成本，这意味着 GMV 每增加 1%，净收入增加量并非恒定为 1.02%，而是随订单数量 $N_{orders}$ 和平均订单价值 $AOV$ 动态变化。

## Corrected Claim

GMV 与佣金收入的非线性关系修正项：由于支付通道费（Payment Processing Fee）通常为固定比例（如 Stripe 的 2.9% + $0.30），平台净佣金收入 $R_{net} = GMV \times (r_{fee} - r_{pay}) - N_{orders} \times C_{fixed}$，其中 $r_{pay}$ 为支付通道费率，$C_{fixed}$ 为单笔固定成本，这意味着 GMV 每增加 1%，净收入增加量并非恒定为 1.02%，而是随订单数量 $N_{orders}$ 和平均订单价值 $AOV$ 动态变化。

## Evidence

先验知识/题面给定，逻辑校验通过
