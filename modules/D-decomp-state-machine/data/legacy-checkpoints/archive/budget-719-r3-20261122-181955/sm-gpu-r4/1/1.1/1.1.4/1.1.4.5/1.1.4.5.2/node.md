# N434: RTX 4080 Super 的 TDP 为 320W，在相同 LLM 推理负载下的平均功耗 P_avg 估算：假设其功耗曲线与 4090 类似，Prefill

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N146

## Claim

RTX 4080 Super 的 TDP 为 320W，在相同 LLM 推理负载下的平均功耗 P_avg 估算：假设其功耗曲线与 4090 类似，Prefill 接近 320W，Decode 约为 150-180W。50/50 负载下 P_avg ≈ 0.5 * 320W + 0.5 * 165W = 242.5W。N146 使用的 224W (70% TDP) 同样为保守估计。

## Corrected Claim

RTX 4080 Super 的 TDP 为 320W，在相同 LLM 推理负载下的平均功耗 P_avg 估算：假设其功耗曲线与 4090 类似，Prefill 接近 320W，Decode 约为 150-180W。50/50 负载下 P_avg ≈ 0.5 * 320W + 0.5 * 165W = 242.5W。N146 使用的 224W (70% TDP) 同样为保守估计。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4080 Super TDP 320W 符合官方规格，功耗估算逻辑自洽且量级合理
