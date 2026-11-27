# N402: 价格监控机制的触发频率与数据源：建议每月检查一次主要零售商（如 B&H, Best Buy, 京东/天猫）的 GPU 价格。若 RTX 4090 价格连续 2 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N126

## Claim

价格监控机制的触发频率与数据源：建议每月检查一次主要零售商（如 B&H, Best Buy, 京东/天猫）的 GPU 价格。若 RTX 4090 价格连续 2 个月高于 $1,840 (基准 $1,600 * 1.15)，则标记为 'Price Alert'，并启动 TCO 重评估流程，对比 L4 和 AMD 方案的当前 TCO。

## Corrected Claim

价格监控机制的触发频率与数据源：建议每月检查一次主要零售商（如 B&H, Best Buy, 京东/天猫）的 GPU 价格。若 RTX 4090 价格连续 2 个月高于 $1,840 (基准 $1,600 * 1.15)，则标记为 'Price Alert'，并启动 TCO 重评估流程，对比 L4 和 AMD 方案的当前 TCO。

## Evidence

先验知识/题面给定，逻辑校验通过：1.15倍系数计算正确（1600*1.15=1840）；2. 每月监控及连续2个月触发机制符合常规价格监控逻辑；3. 提及的零售商（B&H, Best Buy, 京东/天猫）均为主流GPU销售平台，数据源合理。

## Search Query

GPU price monitoring tool API monthly update
