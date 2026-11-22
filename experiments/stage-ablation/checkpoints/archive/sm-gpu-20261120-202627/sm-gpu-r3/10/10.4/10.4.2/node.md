# N452: 数据中心级服务器（如 A100/H100 节点）单次硬件故障的平均修复时间 (MTTR_Datacenter) 分解为：远程诊断时间 (<0.5h) + 热插拔

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N148

## Claim

数据中心级服务器（如 A100/H100 节点）单次硬件故障的平均修复时间 (MTTR_Datacenter) 分解为：远程诊断时间 (<0.5h) + 热插拔更换时间 (<0.5h, 若支持) 或 冷启动维护窗口 (4-8h, 若需关机)，总 MTTR 预期区间为 0.5-8 小时，中位数约 1-2 小时。

## Corrected Claim

数据中心级服务器（如 A100/H100 节点）单次硬件故障的平均修复时间 (MTTR_Datacenter) 分解为：远程诊断时间 (<0.5h) + 热插拔更换时间 (<0.5h, 若支持) 或 冷启动维护窗口 (4-8h, 若需关机)，总 MTTR 预期区间为 0.5-8 小时，中位数约 1-2 小时。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

data center GPU server mean time to repair MTTR hot swap
