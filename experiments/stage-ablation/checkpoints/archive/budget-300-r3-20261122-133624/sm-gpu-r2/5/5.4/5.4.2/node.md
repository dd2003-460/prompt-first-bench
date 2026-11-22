# N152: 电力成本项 C_power 的动态修正：实际功耗并非恒定 TDP，而是随负载波动。对于 Decode 阶段（带宽受限），功耗约为 TDP 的 60-70%；对于

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

电力成本项 C_power 的动态修正：实际功耗并非恒定 TDP，而是随负载波动。对于 Decode 阶段（带宽受限），功耗约为 TDP 的 60-70%；对于 Prefill 阶段（计算受限），功耗接近 TDP。加权平均功耗 P_avg = P_decode * (T_decode / T_total) + P_prefill * (T_prefill / T_total)，需根据具体工作负载比例计算。

## Corrected Claim

电力成本项 C_power 的动态修正：实际功耗并非恒定 TDP，而是随负载波动。对于 Decode 阶段（带宽受限），功耗约为 TDP 的 60-70%；对于 Prefill 阶段（计算受限），功耗接近 TDP。加权平均功耗 P_avg = P_decode * (T_decode / T_total) + P_prefill * (T_prefill / T_total)，需根据具体工作负载比例计算。

## Evidence

先验知识/题面给定，逻辑校验通过：Decode阶段受内存带宽限制，计算单元空闲率高，功耗低于TDP（60-70%符合工程经验）；Prefill阶段计算密集，功耗接近TDP；加权平均公式符合时间加权平均的物理定义。

## Search Query

GPU power consumption decode vs prefill inference load percentage TDP
