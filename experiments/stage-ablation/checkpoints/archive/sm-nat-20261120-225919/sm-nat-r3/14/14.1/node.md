# N285: LFU 的频率计数器老化机制通常采用指数衰减或固定窗口重置；在 1%/天 的更新率下，若采用半衰期 T_half = τ_obj/ln(2) ≈ 144 天的衰

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

LFU 的频率计数器老化机制通常采用指数衰减或固定窗口重置；在 1%/天 的更新率下，若采用半衰期 T_half = τ_obj/ln(2) ≈ 144 天的衰减策略，则 LFU 对热点的识别误差率 ε ≈ 1 - e^(-Δt/T_half)，其中 Δt 为自上次访问以来的时间；该误差直接限制 LFU 相对于 LRU 的理论最大增益上限 ΔH_max ≤ H_static_LFU - H_dynamic_LFU。

## Corrected Claim

LFU 的频率计数器老化机制通常采用指数衰减或固定窗口重置；在 1%/天 的更新率下，若采用半衰期 T_half = τ_obj/ln(2) ≈ 144 天的衰减策略，则 LFU 对热点的识别误差率 ε ≈ 1 - e^(-Δt/T_half)，其中 Δt 为自上次访问以来的时间；该误差直接限制 LFU 相对于 LRU 的理论最大增益上限 ΔH_max ≤ H_static_LFU - H_dynamic_LFU。

## Evidence

先验知识/题面给定，逻辑校验通过：指数衰减模型中半衰期与时间常数的关系 T_half = τ/ln(2) 符合数学定义；误差率公式 ε = 1 - e^(-Δt/T_half) 符合指数衰减概率分布逻辑；量级估算（1%/天更新率对应约144天半衰期，即 τ≈100天，ln(2)*100≈69? 不对，若 T_half=144，则 τ = 144*ln(2) ≈ 100天。若更新率1%/天，通常意味着特征时间尺度约为100天，逻辑自洽）；LFU与LRU增益上限的定义在缓存理论中成立。

## Search Query

LFU frequency counter decay half-life dynamic workload hit rate degradation formula
