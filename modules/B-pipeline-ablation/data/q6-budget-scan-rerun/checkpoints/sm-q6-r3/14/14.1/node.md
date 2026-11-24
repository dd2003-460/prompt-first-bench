# N414: 扩容前置时间 T_lead 的分段量化：T_lead = T_procurement + T_installation + T_bandwidth_provis

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N132

## Claim

扩容前置时间 T_lead 的分段量化：T_lead = T_procurement + T_installation + T_bandwidth_provisioning + T_testing，其中 T_procurement ≈ 1-2个月（服务器/网络设备采购），T_installation ≈ 1-2个月（机房上架、布线），T_bandwidth_provisioning ≈ 1-3个月（运营商带宽开通，视地区而定），T_testing ≈ 0.5-1个月（压力测试、灰度发布）；总 T_lead ≈ 3.5-8个月，需根据实际供应链和运营商SLA确定

## Corrected Claim

扩容前置时间 T_lead 的分段量化：T_lead = T_procurement + T_installation + T_bandwidth_provisioning + T_testing，其中 T_procurement ≈ 1-2个月（服务器/网络设备采购），T_installation ≈ 1-2个月（机房上架、布线），T_bandwidth_provisioning ≈ 1-3个月（运营商带宽开通，视地区而定），T_testing ≈ 0.5-1个月（压力测试、灰度发布）；总 T_lead ≈ 3.5-8个月，需根据实际供应链和运营商SLA确定

## Evidence

先验知识/题面给定，逻辑校验通过：各分项时间量级符合IT基础设施扩容的行业常规经验，总和区间（3.5-8个月）与分项之和逻辑自洽。

## Search Query

edge node expansion lead time procurement installation bandwidth provisioning testing
