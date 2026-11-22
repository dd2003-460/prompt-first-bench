# N245: RTX 5090 官方 TDP 为 575W，但 LLM 推理（Decode 阶段）受显存带宽限制，GPU 利用率通常低于 100%，实际平均功耗 P_avg 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

RTX 5090 官方 TDP 为 575W，但 LLM 推理（Decode 阶段）受显存带宽限制，GPU 利用率通常低于 100%，实际平均功耗 P_avg 需通过实测或负载模型修正；若按 80% 峰值负载估算，P_avg ≈ 460W，这直接影响电源冗余度选择（1000W vs 1200W）及机箱散热设计。

## Corrected Claim

RTX 5090 官方 TDP 为 575W，但 LLM 推理（Decode 阶段）受显存带宽限制，GPU 利用率通常低于 100%，实际平均功耗 P_avg 需通过实测或负载模型修正；若按 80% 峰值负载估算，P_avg ≈ 460W，这直接影响电源冗余度选择（1000W vs 1200W）及机箱散热设计。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 TDP 575W 符合 NVIDIA 官方规格，80% 负载估算 460W 数学自洽，且 LLM Decode 阶段受显存带宽限制导致 GPU 利用率低于 100% 符合硬件原理。

## Search Query

RTX 5090 power consumption LLM inference average watts vs TDP
