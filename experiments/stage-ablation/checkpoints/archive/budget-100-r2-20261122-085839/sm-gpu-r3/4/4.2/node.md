# N22: 在计算受限场景下（Batch>1, Prefill阶段或高并发），单卡吞吐量的理论上限公式为 Throughput_max = (Peak_FLOPS_TFLO

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

在计算受限场景下（Batch>1, Prefill阶段或高并发），单卡吞吐量的理论上限公式为 Throughput_max = (Peak_FLOPS_TFLOPS / FLOPs_per_token) * 1000 tokens/s，其中 FLOPs_per_token ≈ 2 * Num_Parameters，需对比不同精度（BF16 vs FP8 vs INT8）下的实际有效算力利用率（通常仅为峰值的 30%-50%）。

## Corrected Claim

在计算受限场景下（Batch>1, Prefill阶段或高并发），单卡吞吐量的理论上限公式为 Throughput_max = (Peak_FLOPS_TFLOPS / FLOPs_per_token) * 1000 tokens/s，其中 FLOPs_per_token ≈ 2 * Num_Parameters，需对比不同精度（BF16 vs FP8 vs INT8）下的实际有效算力利用率（通常仅为峰值的 30%-50%）。

## Evidence

父节点级核验未通过：不完备（子节点仅覆盖了特定硬件（RTX 4090）和特定模型（Qwen3-27B）在BF16精度下的参数，缺失了父节点中强调的'不同精度对比（FP8/INT8）'、'实际有效算力利用率（30%-50%）'以及'高并发/Prefill阶段'等关键理论要素，导致无法完整支撑父节点关于理论上限公式及利用率分析的论述。）

## Search Query

LLM inference prefill phase compute bound FLOPS utilization efficiency
