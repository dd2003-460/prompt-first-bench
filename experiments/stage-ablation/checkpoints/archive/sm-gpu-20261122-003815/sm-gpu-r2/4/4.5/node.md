# N26: Prefill 阶段计算瓶颈分析：Prefill 是计算密集型，所需算力 (TFLOPS) ≈ 2 * N_params * seq_len / time_bu

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

Prefill 阶段计算瓶颈分析：Prefill 是计算密集型，所需算力 (TFLOPS) ≈ 2 * N_params * seq_len / time_budget。对于 32K 上下文 Prefill，若要求 1s 完成，需算力 ≈ 2 * 27e9 * 32768 / 1s ≈ 1.76 PFLOPS (FP16/BF16)。

## Corrected Claim

Prefill 阶段计算瓶颈分析：Prefill 是计算密集型，所需算力 (TFLOPS) ≈ 2 * N_params * seq_len / time_budget。对于 32K 上下文 Prefill，若要求 1s 完成，需算力 ≈ 2 * 27e9 * 32768 / 1s ≈ 1.76 PFLOPS (FP16/BF16)。

## Evidence

先验知识/题面给定，逻辑校验通过：Prefill 阶段主要执行矩阵乘法，计算量约为 2 * 参数量 * 序列长度，数值推导 2 * 27e9 * 32768 ≈ 1.76e15 FLOPS 正确，符合大模型推理算力估算的基本原理。
