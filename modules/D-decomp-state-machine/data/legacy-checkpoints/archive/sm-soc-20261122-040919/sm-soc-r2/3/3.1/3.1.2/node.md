# N66: 下游投影1：买家搜索成本系数 k 的动态调整公式。k_new = k_old * (1 - η * ΔH_info)，其中 η 为买家对额外信息的敏感度系数（η

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N14

## Claim

下游投影1：买家搜索成本系数 k 的动态调整公式。k_new = k_old * (1 - η * ΔH_info)，其中 η 为买家对额外信息的敏感度系数（η ∈ [0.5, 1.0]）。若 ΔH_info 为正（信息增加），k_new 将高于 0.6；若 ΔH_info 为负（信息过载/噪声大），k_new 可能低于 0.6。具体数值需通过 A/B 测试中买家平均搜索时长变化率计算得出。

## Corrected Claim

下游投影1：买家搜索成本系数 k 的动态调整公式。k_new = k_old * (1 - η * ΔH_info)，其中 η 为买家对额外信息的敏感度系数（η ∈ [0.5, 1.0]）。若 ΔH_info 为正（信息增加），k_new 将高于 0.6；若 ΔH_info 为负（信息过载/噪声大），k_new 可能低于 0.6。具体数值需通过 A/B 测试中买家平均搜索时长变化率计算得出。

## Evidence

先验知识/题面给定，逻辑校验通过
