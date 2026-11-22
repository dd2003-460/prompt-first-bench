# N14: 更新率导致的缓存失效频率：对象平均寿命 T_life = 1/0.01 = 100 天，LRU 缓存中对象的驻留时间 T_res 取决于缓存容量 C 和请求速率

- **status**: verified
- **level**: L2
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

更新率导致的缓存失效频率：对象平均寿命 T_life = 1/0.01 = 100 天，LRU 缓存中对象的驻留时间 T_res 取决于缓存容量 C 和请求速率，失效概率 P_inval = min(1, T_res / T_life)。

## Corrected Claim

更新率导致的缓存失效频率：对象平均寿命 T_life = 1/0.01 = 100 天，LRU 缓存中对象的驻留时间 T_res 取决于缓存容量 C 和请求速率，失效概率 P_inval = min(1, T_res / T_life)。

## Evidence

先验知识/题面给定，逻辑校验通过：T_life计算正确，LRU失效概率模型在逻辑上自洽且量级合理
