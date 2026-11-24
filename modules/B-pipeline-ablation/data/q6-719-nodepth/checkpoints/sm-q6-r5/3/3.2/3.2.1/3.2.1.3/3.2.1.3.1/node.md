# N653: 公有云出网流量 Traffic_out_cloud 的敏感性分析：当 H_cloud 从 0.90 降至 0.85（缓存容量不足或热点变化），Traffic_o

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N219

## Claim

公有云出网流量 Traffic_out_cloud 的敏感性分析：当 H_cloud 从 0.90 降至 0.85（缓存容量不足或热点变化），Traffic_out_cloud 从 200GB/day 增至 300GB/day，导致月度带宽成本 C_bw_cloud 增加 50%，凸显命中率对成本的非线性影响。

## Corrected Claim

公有云出网流量 Traffic_out_cloud 的敏感性分析：当 H_cloud 从 0.90 降至 0.85（缓存容量不足或热点变化），Traffic_out_cloud 从 200GB/day 增至 300GB/day，导致月度带宽成本 C_bw_cloud 增加 50%，凸显命中率对成本的非线性影响。

## Evidence

先验知识/题面给定，逻辑校验通过：命中率从0.90降至0.85，未命中流量从10%增至15%（相对增加50%），若基础流量恒定，出网流量及对应带宽成本线性增加50%，数值量级与逻辑自洽。
