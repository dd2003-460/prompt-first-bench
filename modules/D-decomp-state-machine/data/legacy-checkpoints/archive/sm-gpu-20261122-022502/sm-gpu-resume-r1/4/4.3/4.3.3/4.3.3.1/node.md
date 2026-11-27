# N259: H200 SXM 运行 Qwen3-27B BF16 时的实际 Decode 吞吐受限于显存带宽瓶颈，理论上限 88.9 tokens/s 需乘以实测效率系数（

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

H200 SXM 运行 Qwen3-27B BF16 时的实际 Decode 吞吐受限于显存带宽瓶颈，理论上限 88.9 tokens/s 需乘以实测效率系数（通常 0.8-0.9，取决于 Kernel 优化和内存访问模式），实际预期吞吐约 71-80 tokens/s。

## Corrected Claim

H200 SXM 运行 Qwen3-27B BF16 时的实际 Decode 吞吐受限于显存带宽瓶颈，理论上限 88.9 tokens/s 需乘以实测效率系数（通常 0.8-0.9，取决于 Kernel 优化和内存访问模式），实际预期吞吐约 71-80 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：H200 SXM 显存带宽约 4.8TB/s，Qwen3-27B BF16 权重约 54GB，理论上限 4800/54 ≈ 88.9 tokens/s 计算正确；效率系数 0.8-0.9 符合业界实测经验，推导自洽。

## Search Query

H200 SXM decode throughput efficiency factor benchmark
