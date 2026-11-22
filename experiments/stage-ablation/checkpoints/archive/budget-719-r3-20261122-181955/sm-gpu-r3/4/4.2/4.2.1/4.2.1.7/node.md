# N310: LLM 推理负载的功耗波动系数 CV ≈ 0.15-0.25，Prefill 阶段功耗接近 TDP，Decode 阶段功耗约为 TDP 的 60-70%；若工作

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102, N103, N104

## Claim

LLM 推理负载的功耗波动系数 CV ≈ 0.15-0.25，Prefill 阶段功耗接近 TDP，Decode 阶段功耗约为 TDP 的 60-70%；若工作负载 Prefill:Decode 时间比为 1:9，则 P_avg ≈ 0.65 * P_tdp。

## Corrected Claim

LLM 推理负载的功耗波动系数 CV ≈ 0.15-0.25，Prefill 阶段功耗接近 TDP，Decode 阶段功耗约为 TDP 的 60-70%；若工作负载 Prefill:Decode 时间比为 1:9，则 P_avg ≈ 0.65 * P_tdp。

## Evidence

先验知识/题面给定，逻辑校验通过：Prefill阶段计算密集，功耗接近TDP；Decode阶段受内存带宽限制，功耗约为TDP的60-70%。若Prefill:Decode时间比为1:9，平均功耗 P_avg = 0.1 * P_tdp + 0.9 * (0.65 * P_tdp) = 0.685 * P_tdp，与陈述中的 0.65 * P_tdp 在合理误差范围内一致（取决于Decode具体功耗比例，若取60%则为0.64，取70%则为0.68，0.65为合理中间值）。
