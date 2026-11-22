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

父节点级核验未通过：不完备（子节点正交（分别定义模型侧参数和硬件侧参数），但不完备。父节点明确要求对比不同精度（BF16 vs FP8 vs INT8）下的算力利用率，而子节点仅提供了 BF16 单一种类的参数，缺失了 FP8/INT8 的硬件峰值算力及对应的 FLOPs 计算（若参数不变则 FLOPs 相同，但硬件峰值不同），且未包含“实际有效算力利用率（30%-50%）”这一关键修正因子的具体数值或来源，导致无法直接根据子节点复现父节点公式的完整计算逻辑。）

## Search Query

LLM inference prefill phase compute bound FLOPS utilization efficiency
