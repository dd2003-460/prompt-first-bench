# N177: 理想 LFU 字节命中率理论上限：H_lfu_max = 1 - (1 - 1)^{0.1} = 100%，因为 K_lfu_max > N，所有对象均可驻留，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

理想 LFU 字节命中率理论上限：H_lfu_max = 1 - (1 - 1)^{0.1} = 100%，因为 K_lfu_max > N，所有对象均可驻留，无未命中。

## Corrected Claim

理想 LFU 字节命中率理论上限：H_lfu_max = 1 - (1 - 1)^{0.1} = 100%，因为 K_lfu_max > N，所有对象均可驻留，无未命中。

## Evidence

先验知识/题面给定，逻辑校验通过：当缓存容量 K 大于对象总数 N 时，LFU 策略可容纳所有对象，首次访问后不再产生未命中，理论命中率上限为 100%。
