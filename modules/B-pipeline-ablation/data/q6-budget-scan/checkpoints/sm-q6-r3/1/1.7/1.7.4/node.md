# N39: 回源RTT = 边缘节点到源站的物理距离 d_origin / 2.0e8 * 2 * 1.05 + 网络排队延迟；源站部署在核心机房时，边缘节点到源站距离通常

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

回源RTT = 边缘节点到源站的物理距离 d_origin / 2.0e8 * 2 * 1.05 + 网络排队延迟；源站部署在核心机房时，边缘节点到源站距离通常为 200-500km，回源RTT约为 2-5ms 加上排队延迟。

## Corrected Claim

回源RTT = 边缘节点到源站的物理距离 d_origin / 2.0e8 * 2 * 1.05 + 网络排队延迟；源站部署在核心机房时，边缘节点到源站距离通常为 200-500km，回源RTT约为 2-5ms 加上排队延迟。

## Evidence

父节点级核验未通过：不完备（子节点分别解释了公式中的两个主要组成部分（物理距离/传播延迟和排队延迟），彼此正且无冗余。但父节点明确指出了常数项（光速 2.0e8、系数 2 和 1.05 代表往返及安全余量/处理开销），子节点仅解释了变量部分，未涵盖常数因子及其物理/工程含义，因此不完备。）

## Search Query

origin server RTT from edge node China data center
