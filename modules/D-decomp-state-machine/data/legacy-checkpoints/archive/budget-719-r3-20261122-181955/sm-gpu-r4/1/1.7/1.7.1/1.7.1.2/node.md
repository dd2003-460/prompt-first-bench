# N223: RTX 4090 的 FP16 算力 82.6 TFLOPS 是理论峰值（Dense），但在 LLM 推理中实际有效算力受限于 Tensor Core 利用率（

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N69

## Claim

RTX 4090 的 FP16 算力 82.6 TFLOPS 是理论峰值（Dense），但在 LLM 推理中实际有效算力受限于 Tensor Core 利用率（通常 60-80%），因此计算 $/TFLOPS 性价比时，应使用有效算力 ~55-65 TFLOPS，修正后的 $/TFLOPS 约为 $25-$31，而非基于理论峰值的 $19-$23。

## Corrected Claim

RTX 4090 的 FP16 理论峰值算力约为 82.6 TFLOPS（Tensor Core）。在 LLM 推理中，受限于内存带宽和 Tensor Core 利用率，实际有效算力通常显著低于峰值（经验上约为峰值的 60-80%），因此计算性价比时应考虑有效算力，而非直接采用理论峰值。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一连续参数（Tensor Core 利用率）在不同离散点的取值，存在严重冗余；且父节点明确界定的范围是 60-80%（有效算力 55-65 TFLOPS），子节点 3 引入了 40% 利用率，超出了父节点定义的讨论范围，导致不完全覆盖父节点逻辑（未覆盖 60-80% 区间内的中间状态，反而引入了范围外数据）。）
