# N265: A100 的 BF16 峰值算力 312 TFLOPS 是理论值，实际 Prefill 有效算力约为 200-240 TFLOPS (65-77% 利用率)，需

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N81

## Claim

A100 的 BF16 峰值算力 312 TFLOPS 是理论值，实际 Prefill 有效算力约为 200-240 TFLOPS (65-77% 利用率)，需基于 A100 在 27B 模型上的实测 Prefill 吞吐（tokens/s）计算有效算力系数 η_eff_A100，并与 RTX 4090 的 η_eff_4090 对比，以评估在相同 FLOPs 需求下的相对延迟。

## Corrected Claim

A100 的 BF16 峰值算力约为 312 TFLOPS（理论值），实际 Prefill 有效算力通常低于峰值，需基于实测吞吐计算有效算力系数 η_eff_A100，并与 RTX 4090 的 η_eff_4090 对比，以评估在相同 FLOPs 需求下的相对延迟。

## Evidence

[质询]该陈述包含具体的经验性数值（A100 BF16 峰值 312 TFLOPS、实际利用率 65-77%、有效算力 200-240 TFLOPS），这些属于硬件规格和实测性能数据，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

A100 LLM inference prefill throughput benchmark 27B model effective TFLOPS
