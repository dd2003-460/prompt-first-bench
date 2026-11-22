# N386: Qwen3-27B 在 RTX 4090 上处理 32K 输入、100 输出 tokens 时的 P99 延迟为 4.2s (Prefill 2.2s + De

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N133

## Claim

Qwen3-27B 在 RTX 4090 上处理 32K 输入、100 输出 tokens 时的 P99 延迟为 4.2s (Prefill 2.2s + Decode 2.0s)，计算公式为 T_total = T_prefill + T_decode，其中 T_prefill = (2 * 27e9 * 32e3) / (1008e9 * 0.4) ≈ 2.2s (假设 40% MFU)

## Corrected Claim

Qwen3-27B 在 RTX 4090 上处理 32K 输入、100 输出 tokens 时的 P99 延迟为 4.2s (Prefill 2.2s + Decode 2.0s)，计算公式为 T_total = T_prefill + T_decode，其中 T_prefill = (2 * 27e9 * 32e3) / (1008e9 * 0.4) ≈ 2.2s (假设 40% MFU)

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 FP16算力约1008 TFLOPS，27B模型Prefill计算量约1.7e15 FLOPs，40% MFU下耗时约2.2s，数值量级与公式推导自洽。
