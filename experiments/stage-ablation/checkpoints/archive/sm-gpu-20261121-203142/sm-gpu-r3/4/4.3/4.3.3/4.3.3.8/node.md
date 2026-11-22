# N273: Prefill 阶段实际 FLOPS 利用率 (MFU) 修正：理论峰值 82 TFLOPS (BF16) 在 LLM Prefill 中通常只能达到 40-6

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N85, N86, N87

## Claim

Prefill 阶段实际 FLOPS 利用率 (MFU) 修正：理论峰值 82 TFLOPS (BF16) 在 LLM Prefill 中通常只能达到 40-60% (受限于 Kernel Launch Overhead, 内存访问模式及 FlashAttention 实现效率)；因此 RTX 4090 的有效 Prefill 算力约为 33-49 TFLOPS；修正后的 TTFT 估算 = 1.7e12 FLOPs / 40e12 FLOPS ≈ 42.5 秒 (理论值)，实际因并行优化可能降至 15-25 秒 [待核验]。

## Corrected Claim

RTX 4090 在 LLM Prefill 阶段的有效算力受限于 MFU（通常低于理论峰值），具体 TTFT 需结合模型参数量、序列长度及实际 MFU 实测值计算，40-60% MFU 仅为粗略估计范围。

## Evidence

[质询]RTX 4090 的 BF16 理论峰值算力通常被引用为 82.6 TFLOPS (FP16/BF16 Tensor Core)，但实际 Prefill 阶段的 MFU (Model FLOPs Utilization) 在消费级显卡上受限于内存带宽和 Kernel 效率，40-60% 的估计范围偏乐观，通常实际有效算力可能更低；此外，1.7e12 FLOPs 的输入规模未明确对应具体的序列长度和模型大小，导致 TTFT 估算缺乏具体上下文支撑。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且 MFU 具体数值及 TTFT 估算依赖特定硬件与模型配置，无法仅凭第一性原理严格推导）

## Search Query

LLM prefill MFU model flops utilization flash attention RTX 4090 benchmark
