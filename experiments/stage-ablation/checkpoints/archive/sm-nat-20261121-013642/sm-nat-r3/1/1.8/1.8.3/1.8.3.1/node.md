# N166: 工作点1（高命中率/低驻留）：当 H_byte_LRU=0.8 时，T_residence = 128 / (500 * (1-0.8)) = 1.28 天。此

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N55

## Claim

工作点1（高命中率/低驻留）：当 H_byte_LRU=0.8 时，T_residence = 128 / (500 * (1-0.8)) = 1.28 天。此工作点下缓存周转快，对象驻留时间短，更新惩罚极小。

## Corrected Claim

工作点1（高命中率/低驻留）：当 H_byte_LRU=0.8 时，T_residence = 128 / (500 * (1-0.8)) = 1.28 天。此工作点下缓存周转快，对象驻留时间短，更新惩罚极小。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 128 / (500 * 0.2) = 1.28 正确，且高命中率导致低驻留时间符合缓存逻辑。
