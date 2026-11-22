# N126: A100 SXM4 在 Qwen3-27B (BF16) 32K 上下文下的 T_prefill 理论下限为 2.35s，基于公式 T_prefill = (2

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N48

## Claim

A100 SXM4 在 Qwen3-27B (BF16) 32K 上下文下的 T_prefill 理论下限为 2.35s，基于公式 T_prefill = (2 * 27.2e9 * 32000) / (19.5 TFLOPS * 0.5 MFU)；A100 BF16 峰值算力 19.5 TFLOPS，Prefill 阶段 MFU 通常 40-50% (计算受限)，取 50% 计算：1.74e15 FLOPs / (19.5e12 * 0.5) ≈ 17.8s (此处需修正：2*Params*Tokens 为 2*27.2e9*32000=1.74e15，A100 峰值 19.5 TFLOPS=19.5e12，1.74e15/19.5e12=89s (纯计算)，考虑 MFU 50% 则 178s，此值极高，表明 32K 长上下文 Prefill 在 A100 上极慢，需重新核对 FLOPs 公式或 A100 算力规格，A100 实际 BF16 Tensor Core 峰值为 312 TFLOPS (Sparse) / 156 TFLOPS (Dense)，修正后：1.74e15 / (156e12 * 0.5) ≈ 22.3s)

## Corrected Claim

A100 SXM4 (BF16 Dense 156 TFLOPS) 在 Qwen3-27B 32K 上下文下的 Prefill 理论计算时间下限约为 22.3s (基于 50% MFU)，而非 2.35s。

## Evidence

[质询]陈述内部存在严重的数值矛盾和逻辑错误：1. 标题声称理论下限为 2.35s，但正文推导过程得出 17.8s、89s、178s 或 22.3s，数值量级完全不符；2. 计算过程自相矛盾，例如 1.74e15 / (19.5e12 * 0.5) 的结果应为 178s 而非 17.8s；3. 对 A100 算力的引用混乱，19.5 TFLOPS 并非 A100 的标准 BF16 峰值（通常为 312 TFLOPS Sparse 或 156 TFLOPS Dense），且后续修正后的 22.3s 仍与标题的 2.35s 相差一个数量级。 | 逻辑校验失败：陈述内部数值推导前后矛盾，且最终结论（2.35s）与推导过程（~22s 或更高）严重不符，存在硬逻辑错误。

## Search Query

NVIDIA A100 BF16 dense tensor core TFLOPS specification
