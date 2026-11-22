# N191: Offloading 方案的吞吐上限公式：T_decode_offload ≈ Σ(T_layer_i) + T_compute_per_layer，由于 PC

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

Offloading 方案的吞吐上限公式：T_decode_offload ≈ Σ(T_layer_i) + T_compute_per_layer，由于 PCIe 传输与 GPU 计算通常串行化（除非使用双缓冲/流水线），瓶颈为 max(T_transfer, T_compute)。对于 BF16 权重，T_transfer (17ms/layer) >> T_compute (~0.1ms/layer)，因此 T_decode_offload ≈ 64 * 17ms ≈ 1.09s/token，即 ~0.9 tokens/s

## Corrected Claim

Offloading 方案的吞吐上限公式：T_decode_offload ≈ Σ(T_layer_i) + T_compute_per_layer，由于 PCIe 传输与 GPU 计算通常串行化（除非使用双缓冲/流水线），瓶颈为 max(T_transfer, T_compute)。对于 BF16 权重，T_transfer (17ms/layer) >> T_compute (~0.1ms/layer)，因此 T_decode_offload ≈ 64 * 17ms ≈ 1.09s/token，即 ~0.9 tokens/s

## Evidence

先验知识/题面给定，逻辑校验通过：BF16下PCIe传输延迟（~17ms）远大于GPU单层计算延迟（~0.1ms），串行执行时瓶颈确为传输，总耗时估算符合物理直觉与工程常识。
