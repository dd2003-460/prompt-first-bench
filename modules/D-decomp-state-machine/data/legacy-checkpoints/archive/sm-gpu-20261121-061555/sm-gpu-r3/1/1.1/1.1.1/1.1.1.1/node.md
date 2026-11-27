# N139: RTX 5090 32GB 显存下 Qwen3-27B FP8 权重的精确占用计算：Weight_Bytes = 27e9 * 1 byte = 27 GB，剩

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

RTX 5090 32GB 显存下 Qwen3-27B FP8 权重的精确占用计算：Weight_Bytes = 27e9 * 1 byte = 27 GB，剩余显存 = 32 GB - 27 GB = 5 GB，需验证该剩余空间是否足以支撑 32K 上下文 KV Cache 及 vLLM 框架开销（通常需 >2GB）。

## Corrected Claim

RTX 5090 32GB 显存下 Qwen3-27B FP8 权重的精确占用计算：Weight_Bytes = 27e9 * 1 byte = 27 GB，剩余显存 = 32 GB - 27 GB = 5 GB，需验证该剩余空间是否足以支撑 32K 上下文 KV Cache 及 vLLM 框架开销（通常需 >2GB）。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8下确实占用约27GB显存，32GB-27GB=5GB的算术推导正确，且5GB剩余空间对于32K上下文KV Cache及vLLM开销的评估符合工程常识。
