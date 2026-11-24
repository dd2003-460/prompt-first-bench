# N117: 自建 POP 回源延迟 RTT_self_origin 通常为 30-80ms（取决于 POP 到源站的物理距离和带宽），若 POP 部署在源站附近（<100k

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

自建 POP 回源延迟 RTT_self_origin 通常为 30-80ms（取决于 POP 到源站的物理距离和带宽），若 POP 部署在源站附近（<100km），RTT_self_origin < 10ms；若 POP 分布在 10 个城市，平均回源距离约为 500-1000km，RTT_self_origin ≈ 20-40ms。

## Corrected Claim

自建 POP 回源延迟 RTT_self_origin 通常为 30-80ms（取决于 POP 到源站的物理距离和带宽），若 POP 部署在源站附近（<100km），RTT_self_origin < 10ms；若 POP 分布在 10 个城市，平均回源距离约为 500-1000km，RTT_self_origin ≈ 20-40ms。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别描述了延迟的三个独立组成部分（物理基础RTT、排队延迟、传输延迟），彼此正交且无矛盾。父节点提到的'取决于物理距离和带宽'以及具体场景（<100km, 500-1000km）在子节点中通过公式和参数化得到了覆盖。子节点3中的公式实际上将前两个子节点及传输时间整合起来，符合MECE原则，不存在冗余（即不是同一参数的不同取值，而是不同物理机制的延迟分量）。）

## Search Query

edge server origin server latency distance correlation
