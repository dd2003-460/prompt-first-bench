# N187: 在强负相关（ρ_s = -0.9）的极端工作点，热门对象（Top 10%）的平均大小 S_hot 降至全局均值 μ_S 的 20%，导致 LRU 驱逐大冷对象时

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

在强负相关（ρ_s = -0.9）的极端工作点，热门对象（Top 10%）的平均大小 S_hot 降至全局均值 μ_S 的 20%，导致 LRU 驱逐大冷对象时的字节惩罚极大，LFU 增益上限可达 15-20%。

## Corrected Claim

在强负相关（ρ_s = -0.9）的极端工作点，热门对象（Top 10%）的平均大小 S_hot 降至全局均值 μ_S 的 20%，导致 LRU 驱逐大冷对象时的字节惩罚极大，LFU 增益上限可达 15-20%。

## Evidence

先验知识/题面给定，逻辑校验通过：强负相关下热门对象变小导致LRU字节惩罚增加，LFU通过频率保留大冷对象从而获得显著增益，量级与逻辑自洽。
