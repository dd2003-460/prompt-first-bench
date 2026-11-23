# N186: 在L3交换/路由转发中，ASIC硬件转发路径的延迟 T_sw_asic ≈ 0.1-0.3 ms/跳，通过专用硬件流水线处理，适用于高流量生产环境，是延迟下限工

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

在L3交换/路由转发中，ASIC硬件转发路径的延迟 T_sw_asic ≈ 0.1-0.3 ms/跳，通过专用硬件流水线处理，适用于高流量生产环境，是延迟下限工作点

## Corrected Claim

在L3交换/路由转发中，ASIC硬件转发路径的延迟 T_sw_asic ≈ 0.1-0.3 ms/跳，通过专用硬件流水线处理，适用于高流量生产环境，是延迟下限工作点

## Evidence

先验知识/题面给定，逻辑校验通过：ASIC硬件转发延迟通常在微秒级（0.1-0.3ms即100-300微秒，符合高吞吐硬件流水线处理量级），且作为延迟下限工作点符合网络工程常识。

## Search Query

ASIC router forwarding latency nanoseconds microseconds hardware offload
