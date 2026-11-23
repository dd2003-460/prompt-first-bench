# N40: 全自建策略的 P99 延迟成本函数 $C_{self}(T, s)$：$C_{self} = C_{infra}^{self} + C_{bandwidth}^

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

全自建策略的 P99 延迟成本函数 $C_{self}(T, s)$：$C_{self} = C_{infra}^{self} + C_{bandwidth}^{self} + C_{ops}^{self}$，其中 $C_{infra}^{self} \approx 10 \times 50,000 \text{ ¥/month}$（服务器+机柜），$C_{bandwidth}^{self} = \text{Traffic}_{daily} \times P_{95}^{self}$（$P_{95}^{self} \approx 0.05-0.15 \text{ ¥/GB}$），$C_{ops}^{self} \approx 5-10 \text{ 人} \times 20,000 \text{ ¥/month}$。

## Corrected Claim

全自建策略的 P99 延迟成本函数 $C_{self}(T, s)$：$C_{self} = C_{infra}^{self} + C_{bandwidth}^{self} + C_{ops}^{self}$，其中 $C_{infra}^{self} \approx 10 \times 50,000 \text{ ¥/month}$（服务器+机柜），$C_{bandwidth}^{self} = \text{Traffic}_{daily} \times P_{95}^{self}$（$P_{95}^{self} \approx 0.05-0.15 \text{ ¥/GB}$），$C_{ops}^{self} \approx 5-10 \text{ 人} \times 20,000 \text{ ¥/month}$。

## Evidence

先验知识/题面给定，逻辑校验通过
