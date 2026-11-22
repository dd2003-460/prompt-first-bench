# N416: RTX 3090 理论 Prefill 吞吐量上限计算：基于 BF16 稠密算力 35.6 TFLOPS（Tensor Cores），Prefill 计算量约为

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N137, N138, N139

## Claim

RTX 3090 理论 Prefill 吞吐量上限计算：基于 BF16 稠密算力 35.6 TFLOPS（Tensor Cores），Prefill 计算量约为 2 * 27e9 * 32768 FLOPs/token，理论上限 ≈ 35.6e12 / (2 * 27e9 * 32768) ≈ 20.2 tokens/s（单 token 处理时间约 50ms），实际受内存带宽瓶颈影响可能更低。

## Corrected Claim

RTX 3090 BF16 稠密算力约为 71.2 TFLOPS。对于 27B 参数模型，单 token Prefill 计算量约为 2 * 27e9 = 54e9 FLOPs。理论峰值吞吐量约为 71.2e12 / 54e9 ≈ 1318 tokens/s。若考虑 32k 序列的总计算量，处理时间约为 (2 * 27e9 * 32768) / 71.2e12 ≈ 0.025 秒，即吞吐率约为 1.3M tokens/s（针对长序列 Prefill）。实际受内存带宽和计算效率影响，数值会显著降低，但原陈述中的 20.2 tokens/s 和 50ms/token 的推导存在算术和逻辑错误。

## Evidence

[质询]数值量级错误：RTX 3090 的 BF16 稠密算力（Tensor Cores）约为 35.6 TFLOPS 是错误的，实际约为 71.2 TFLOPS（FP16/BF16 带 FP32 累加）或更高（若使用 FP16 累加）。此外，Prefill 阶段的计算量公式 2 * 27e9 * 32768 暗示模型参数量为 27B 且序列长度为 32768，但通常 Prefill 吞吐量计算基于单 token 的 FLOPs（即 2 * 参数量），而非整个序列的总 FLOPs 除以算力得到单 token 时间，除非该公式意在计算处理整个 32k 序列的时间。若按单 token 计算，FLOPs 应为 2 * 27e9，此时吞吐量约为 35.6e12 / (2 * 27e9) ≈ 659 tokens/s（理论峰值），而非 20.2 tokens/s。20.2 tokens/s 更接近于处理整个 32k 序列的时间（35.6e12 / (2 * 27e9 * 32768) ≈ 0.0202 s? 不，35.6e12 / (1.76e15) ≈ 0.02 s，即 50ms 处理 32k tokens，即 640k tokens/s 的吞吐率，或者 50ms 处理一个 32k 的 prompt，即 20.2 prompts/s? 不，20.2 tokens/s 意味着每个 token 50ms。如果 50ms 是处理 32k tokens 的时间，那么吞吐率是 32768/0.05 ≈ 655k tokens/s。如果 50ms 是处理 1 token 的时间，那么 FLOPs/token 必须是 35.6e12 / 0.05 = 7.12e14 FLOPs，这远大于 2*27e9。因此，陈述中的数值推导存在严重的逻辑或算术错误。 | 逻辑校验失败：RTX 3090 BF16 算力数值错误（应为 ~71 TFLOPS 而非 35.6 TFLOPS，35.6 可能是 FP32 或 FP16 无 Tensor Core 加速的数值，或者是 FP16 带 FP32 累加的一半？实际上 3090 FP16 Tensor Core 是 71.2 TFLOPS）。更关键的是，吞吐量计算逻辑混乱：若分母是 2 * 27e9 * 32768，这是处理 32k 长度序列的总 FLOPs，除以算力得到的是处理该序列的时间（约 0.02 秒），而非单 token 时间。若声称单 token 时间 50ms，则 FLOPs/token 需为 7.12e14，与 2*27e9 不符。因此数值推导不自洽。
