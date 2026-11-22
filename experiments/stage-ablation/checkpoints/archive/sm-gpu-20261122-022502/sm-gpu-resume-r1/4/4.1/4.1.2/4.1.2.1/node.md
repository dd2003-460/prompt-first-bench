# N241: H100 SXM 运行 Qwen3-27B BF16 时的实际 Decode 吞吐受限于 HBM3 带宽与 PCIe/NVLink 通信开销：理论 30.6 t

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N88

## Claim

H100 SXM 运行 Qwen3-27B BF16 时的实际 Decode 吞吐受限于 HBM3 带宽与 PCIe/NVLink 通信开销：理论 30.6 tokens/s (N88) 假设纯带宽瓶颈，但 BF16 矩阵乘法在 H100 (989 TFLOPS) 上的计算时间极短 (~0.02ms/token)，故确为 Bandwidth-Bound。然而，若使用 vLLM 等框架，CUDA 内核启动及内存拷贝开销可能导致实际吞吐降至 25-28 tokens/s，需通过 `nvidia-smi` 监控 HBM 利用率验证。

## Corrected Claim

H100 SXM 运行 Qwen3-27B BF16 时的 Decode 吞吐主要受限于 HBM3 带宽。虽然 BF16 矩阵乘法在 H100 上计算时间极短，确认为 Bandwidth-Bound，但 vLLM 等框架的内核启动及内存拷贝开销会导致实际吞吐低于纯带宽理论值。具体数值需通过 nvidia-smi 监控 HBM 利用率及实际基准测试验证。

## Evidence

[质询]该陈述包含具体的经验性数值（如理论吞吐30.6 tokens/s、实际吞吐25-28 tokens/s、计算时间~0.02ms/token），这些属于硬件性能与特定模型推理的实测/估算数据，无法仅从第一性原理严格推导得出，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

H100 SXM Qwen 27B BF16 decode throughput actual vs theoretical bandwidth bottleneck
