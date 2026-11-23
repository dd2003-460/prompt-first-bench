# N139: 跨域带宽成本增加系数 $\alpha_{cost}$ 的量化：$\alpha_{cost} = P_{backbone} / P_{edge}$，其中 $P_{

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

跨域带宽成本增加系数 $\alpha_{cost}$ 的量化：$\alpha_{cost} = P_{backbone} / P_{edge}$，其中 $P_{backbone}$ 为骨干网流量单价（通常 ¥0.1-0.2/GB，因运营商间结算价高于边缘接入价），$P_{edge}$ 为本地边缘流量单价（¥0.05-0.1/GB），典型比值为 1.5-2.0（即增加 50%-100%，修正原 20%-40% 估算）。

## Corrected Claim

跨域带宽成本增加系数 $\alpha_{cost}$ 的量化：$\alpha_{cost} = P_{backbone} / P_{edge}$，其中 $P_{backbone}$ 为骨干网流量单价（通常 ¥0.1-0.2/GB，因运营商间结算价高于边缘接入价），$P_{edge}$ 为本地边缘流量单价（¥0.05-0.1/GB），典型比值为 1.5-2.0（即增加 50%-100%，修正原 20%-40% 估算）。

## Evidence

先验知识/题面给定，逻辑校验通过
