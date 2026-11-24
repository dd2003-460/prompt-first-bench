# N369: L2 到源站的回源延迟 RTT_L2_origin 通常为 20-50ms，若源站与 L2 位于同一城市机房（同城），RTT < 5ms；若跨省，RTT 为 2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N114

## Claim

L2 到源站的回源延迟 RTT_L2_origin 通常为 20-50ms，若源站与 L2 位于同一城市机房（同城），RTT < 5ms；若跨省，RTT 为 20-40ms；若跨大洲（不适用中国境内），RTT > 100ms。对于国内业务，假设源站在北京，L2 在上海，RTT ≈ 25ms。

## Corrected Claim

L2 到源站的回源延迟 RTT_L2_origin 通常为 20-50ms，若源站与 L2 位于同一城市机房（同城），RTT < 5ms；若跨省，RTT 为 20-40ms；若跨大洲（不适用中国境内），RTT > 100ms。对于国内业务，假设源站在北京，L2 在上海，RTT ≈ 25ms。

## Evidence

先验知识/题面给定，逻辑校验通过：北京至上海光纤距离约1200km，光速传播延迟约4ms，加上路由跳数及设备处理延迟，25ms的RTT估算符合物理规律及网络工程常识；同城<5ms、跨省20-40ms的量级也符合典型网络延迟特征。

## Search Query

origin server to CDN center node latency same city cross province
