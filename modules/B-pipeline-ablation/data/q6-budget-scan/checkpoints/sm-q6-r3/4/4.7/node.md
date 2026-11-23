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

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的三个独立成本项（基础设施、带宽、运维），逻辑上互斥且无重叠；三者之和完整覆盖了父节点定义的总成本结构，无遗漏关键方面；各子节点代表不同的成本维度，并非同一参数的不同取值，因此不存在冗余。）
