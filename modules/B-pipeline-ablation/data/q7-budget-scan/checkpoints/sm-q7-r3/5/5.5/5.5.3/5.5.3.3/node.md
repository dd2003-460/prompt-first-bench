# N284: SSD 缓存层的写放大（Write Amplification）对寿命和有效容量的间接影响：假设温数据每日扫描伴随少量更新（写），写放大因子 WAF=2-3，实

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N100

## Claim

SSD 缓存层的写放大（Write Amplification）对寿命和有效容量的间接影响：假设温数据每日扫描伴随少量更新（写），写放大因子 WAF=2-3，实际 SSD 写入量 = 逻辑写入量 * WAF；虽然主要影响寿命，但在高写场景下需预留 10-20% 容量用于磨损均衡（Over-provisioning），导致有效容量系数从 0.5 降至 0.4-0.45。

## Corrected Claim

SSD 缓存层的写放大（Write Amplification）对寿命和有效容量的间接影响：假设温数据每日扫描伴随少量更新（写），写放大因子 WAF=2-3，实际 SSD 写入量 = 逻辑写入量 * WAF；虽然主要影响寿命，但在高写场景下需预留 10-20% 容量用于磨损均衡（Over-provisioning），导致有效容量系数从 0.5 降至 0.4-0.45。

## Evidence

先验知识/题面给定，逻辑校验通过：WAF 2-3 符合 SSD 典型值，OP 预留 10-20% 导致有效容量系数从 0.5 降至 0.4-0.45 的数学推导自洽（0.5 * (1-0.1~0.2) = 0.4~0.45）。
