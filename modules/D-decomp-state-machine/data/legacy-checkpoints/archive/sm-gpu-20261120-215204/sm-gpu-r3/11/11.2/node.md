# N403: AMD MI300X 运行 BF16 Qwen3-27B 的 Prefill (32K) 理论耗时约为 2.6 秒 (计算量 1.77 TFLOPs / (53

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N152

## Claim

AMD MI300X 运行 BF16 Qwen3-27B 的 Prefill (32K) 理论耗时约为 2.6 秒 (计算量 1.77 TFLOPs / (5300 GB/s 带宽限制下的有效算力估算，假设 MFU 40% 且受带宽瓶颈制约，有效算力约 680 TFLOPS 或更保守按带宽折算))，实际需考虑 ROCm 算子优化不足导致的 1.5-2x 延迟，预计 4-5 秒，优于 RTX 4090 双卡但劣于 A100。

## Corrected Claim

AMD MI300X 运行 BF16 Qwen3-27B 的 Prefill (32K) 理论耗时估算存在数量级错误。若计算量为 1.77 TFLOPs，理论耗时约为 2.6 毫秒；若实际耗时为 2.6 秒，则隐含的计算量或有效算力估算有误。实际性能需基于准确的 FLOPs 统计和 MFU 重新评估，但原陈述中的数值推导不成立。

## Evidence

[质询]数值量级与逻辑推导存在严重矛盾：1.77 TFLOPs 的计算量在 680 TFLOPS 的有效算力下，理论耗时应约为 0.0026 秒（2.6 毫秒），而非 2.6 秒。陈述中声称的 2.6 秒耗时与给定的计算量和算力参数在数量级上相差 1000 倍，且‘受带宽瓶颈制约’通常意味着计算时间由数据搬运决定，但 32K 序列的 Prefill 阶段主要是计算密集型（Compute-bound），除非模型极小或序列极短，否则不会完全受带宽限制导致如此高的延迟。此外，将 1.77 TFLOPs 误读或计算错误为 2.6 秒是明显的逻辑/算术错误。 | 逻辑校验失败：计算量 1.77 TFLOPs / 680 TFLOPS ≈ 0.0026s，与声称的 2.6s 相差三个数量级，存在硬逻辑错误。
