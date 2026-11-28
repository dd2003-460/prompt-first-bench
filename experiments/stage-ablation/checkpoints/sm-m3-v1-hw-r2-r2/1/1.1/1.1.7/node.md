# N40: 由于 V100 (SM 70) 缺乏 Tensor Core 对 FP8 的原生支持，vLLM 中的 'fp8 KV cache' 必然降级为 FP16 存储或

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6, N7, N8

## Claim

由于 V100 (SM 70) 缺乏 Tensor Core 对 FP8 的原生支持，vLLM 中的 'fp8 KV cache' 必然降级为 FP16 存储或使用 CPU offload；若降级为 FP16，单 token KV 占用翻倍至 16 MB，最大并发 Token 数减半至 ~3072 tokens

## Corrected Claim

由于 V100 (SM 70) 缺乏 Tensor Core 对 FP8 的原生支持，vLLM 中的 'fp8 KV cache' 会降级为 FP16 存储；若降级为 FP16，单 token KV 占用相比 FP8 翻倍，最大并发 Token 数相应减半（具体数值取决于模型架构和序列长度，非固定 16 MB 或 3072 tokens）。

## Evidence

[质询]数值量级严重错误：单 token KV 占用不可能达到 16 MB（通常仅为 KB 级别），且 V100 不支持 FP8 导致降级为 FP16 是正确逻辑，但由此推导出的具体内存占用和并发数数值完全违背硬件常识。 | 先验知识/题面给定，逻辑校验失败：V100 确实无 FP8 支持，但单 token KV 大小通常为几 KB 而非 16 MB，量级错误导致后续推导无效。

## Search Query

vLLM FP8 support V100 fallback FP16 KV cache
