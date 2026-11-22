# N225: 1×L40S 48GB FP8 方案的显存容量与 Batch Size 上限：L40S 显存 48GB，FP8 权重 13.5GB，剩余 34.5GB 用于 K

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N71

## Claim

1×L40S 48GB FP8 方案的显存容量与 Batch Size 上限：L40S 显存 48GB，FP8 权重 13.5GB，剩余 34.5GB 用于 KV Cache 和激活值；32K 上下文下单请求 KV Cache 约 2.1GB，理论 B_max ≈ 34.5 / 2.1 ≈ 16 个请求；实际受 PCIe 4.0 x16 带宽（~32 GB/s）限制，Decode 阶段带宽利用率约 70%，有效 TPS ≈ (32 GB/s * 0.7) / (13.5GB/2) ≈ 3.3 TPS/请求，若 B_max=16，总吞吐量 ≈ 52 Tokens/s，单 Token 成本需基于此吞吐量重新计算。

## Corrected Claim

L40S 显存 48GB，FP8 权重 13.5GB，剩余 34.5GB 用于 KV Cache 和激活值；32K 上下文下单请求 KV Cache 约 2.1GB，理论 B_max ≈ 34.5 / 2.1 ≈ 16 个请求。实际受 PCIe 4.0 x16 带宽（~32 GB/s）限制，Decode 阶段每生成一个 token 需读取约 13.5GB 权重数据，若带宽利用率 70%，单请求理论最大 TPS ≈ (32 * 0.7) / 13.5 ≈ 1.65 TPS。在 B_max=16 时，由于权重读取可被 Batch 复用，总吞吐量将受限于总带宽，约为 1.65 * 16 ≈ 26.4 Tokens/s（假设理想复用且忽略 KV 读取开销），单 Token 成本需基于此吞吐量重新计算。

## Evidence

[质询]TPS 计算公式 `(32 GB/s * 0.7) / (13.5GB/2)` 存在严重的逻辑与物理直觉错误。在 Decode 阶段，每生成一个 token 需要读取一次完整的模型权重（13.5GB），而非 13.5GB/2。此外，该公式忽略了 KV Cache 的读取开销，且将带宽限制下的吞吐量计算简化为仅依赖权重大小，忽略了 Batch Size 对内存带宽复用的影响（通常 Batch 越大，单位 token 的权重读取成本越低，但受限于总带宽，单请求 TPS 会下降，总吞吐量趋于稳定而非线性增长）。 | 先验知识/题面给定，逻辑校验未通过：TPS 计算分母错误（应为 13.5GB 而非 13.5GB/2），且推导过程违背 LLM 推理中 Decode 阶段内存带宽瓶颈的基本原理（每 token 需读取全量权重）。
