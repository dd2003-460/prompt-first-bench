# N23: 推理延迟分解公式：Latency = T_prefill + T_decode；其中 T_prefill ≈ L * M * P / (2 * FLOPS * 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

推理延迟分解公式：Latency = T_prefill + T_decode；其中 T_prefill ≈ L * M * P / (2 * FLOPS * MFU)，T_decode ≈ L * (M + KV_len) / (2 * FLOPS * MFU)，L=27B, M=32K, P=32K, KV_len=32K

## Corrected Claim

推理延迟分解公式：Latency = T_prefill + T_decode；其中 T_prefill ≈ L * M * P / (2 * FLOPS * MFU)，T_decode ≈ L * (M + KV_len) / (2 * FLOPS * MFU)，L=27B, M=32K, P=32K, KV_len=32K

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM inference latency prefill decode formula MFU
