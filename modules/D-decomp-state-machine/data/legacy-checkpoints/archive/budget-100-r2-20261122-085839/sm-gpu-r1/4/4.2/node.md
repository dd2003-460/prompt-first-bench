# N22: 在计算受限场景下（Batch>1, Prefill阶段或高并发），单卡吞吐量的理论上限公式为 Throughput_max = (Peak_FLOPS_TFLO

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

在计算受限场景下（Batch>1, Prefill阶段或高并发），单卡吞吐量的理论上限公式为 Throughput_max = (Peak_FLOPS_TFLOPS / FLOPs_per_token) * 1000 tokens/s，其中 FLOPs_per_token ≈ 2 * Num_Parameters，需对比不同精度（BF16 vs FP8 vs INT8）下的实际有效算力利用率（通常仅为峰值的 30%-50%）。

## Corrected Claim

在计算受限场景下（Batch>1, Prefill阶段或高并发），单卡吞吐量的理论上限公式为 Throughput_max = (Peak_FLOPS_TFLOPS / FLOPs_per_token) * 1000 tokens/s，其中 FLOPs_per_token ≈ 2 * Num_Parameters，需对比不同精度（BF16 vs FP8 vs INT8）下的实际有效算力利用率（通常仅为峰值的 30%-50%）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（TFLOPS/1000 = GFLOPS，GFLOPS / FLOPs_per_token = tokens/s），2N 近似符合 Transformer 计算复杂度，30%-50% 利用率符合工程经验。

## Search Query

LLM inference prefill phase compute bound FLOPS utilization efficiency
