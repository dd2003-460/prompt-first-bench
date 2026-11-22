# N116: Groq LPU (若可获取) 的算力为 750 TFLOPS (INT8)，Qwen3-27B 32K tokens prefill 所需计算量为 2 * 2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

Groq LPU (若可获取) 的算力为 750 TFLOPS (INT8)，Qwen3-27B 32K tokens prefill 所需计算量为 2 * 27B * 32768 ≈ 1.76e15 FLOPs，理论 prefill 时间为 1.76e15 / 750e12 ≈ 2.35 秒。

## Corrected Claim

Groq LPU (若可获取) 的算力为 750 TFLOPS (INT8)，Qwen3-27B 32K tokens prefill 所需计算量为 2 * 27B * 32768 ≈ 1.76e15 FLOPs，理论 prefill 时间为 1.76e15 / 750e12 ≈ 2.35 秒。

## Evidence

[质询]Groq LPU 的 750 TFLOPS 算力数值可能因具体芯片版本（如 LPU vs LPU-2）或精度（INT8 vs FP16）不同而存在差异，且实际 prefill 时间受内存带宽和并行策略影响，理论计算值往往低于实际耗时。 | 先验知识/题面给定，逻辑校验通过：计算量公式 2*N*L 符合 Transformer 注意力机制基本复杂度，数值量级 1.76e15 FLOPs 合理，除法运算 1.76e15 / 750e12 ≈ 2.35 正确。
