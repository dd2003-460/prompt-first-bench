# N185: 在L3交换/路由转发中，CPU软件转发路径的延迟 T_sw_cpu ≈ 0.5-2.0 ms/跳，主要受OS调度与上下文切换影响，适用于低流量或调试场景，是延迟

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

在L3交换/路由转发中，CPU软件转发路径的延迟 T_sw_cpu ≈ 0.5-2.0 ms/跳，主要受OS调度与上下文切换影响，适用于低流量或调试场景，是延迟上限工作点

## Corrected Claim

在L3交换/路由转发中，CPU软件转发路径的延迟 T_sw_cpu ≈ 0.5-2.0 ms/跳，主要受OS调度与上下文切换影响，适用于低流量或调试场景，是延迟上限工作点

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

software routing packet processing latency milliseconds context switch
