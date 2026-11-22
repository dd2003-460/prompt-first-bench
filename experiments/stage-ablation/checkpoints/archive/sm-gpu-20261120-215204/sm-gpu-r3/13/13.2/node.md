# N407: RTX 5090 在 32K 上下文下若采用 INT4 KV Cache，需验证主流推理框架 (如 vLLM/TensorRT-LLM) 对 INT4 KV 的

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N154

## Claim

RTX 5090 在 32K 上下文下若采用 INT4 KV Cache，需验证主流推理框架 (如 vLLM/TensorRT-LLM) 对 INT4 KV 的支持度；若不支持，则必须回退至 BF16 KV (40.96GB) 导致显存溢出，或强制降低上下文至 16K (KV 约 20.48GB, 总占用 34GB 仍超 32GB, 需进一步压缩权重或启用 PagedAttention 优化)。

## Corrected Claim

RTX 5090 在 32K 上下文下若采用 INT4 KV Cache，需验证主流推理框架 (如 vLLM/TensorRT-LLM) 对 INT4 KV 的支持度；若不支持，则可能需回退至 BF16 KV 导致显存压力增大，或降低上下文长度/启用 PagedAttention 等优化以适配 32GB 显存限制。

## Evidence

[质询]该陈述包含具体的硬件显存占用数值（如BF16 KV 40.96GB、INT4支持度等），属于经验事实。由于检索失败无外部来源支持，且不同模型架构（如GQA/MQA vs MHA）及具体参数（层数、头数、维度）会导致KV Cache大小差异巨大，无法仅凭逻辑推导确认这些具体数值是否准确对应RTX 5090及特定主流模型。 | 经验事实，逻辑自洽但缺来源支持。数值量级在常见大模型推理场景下合理（例如70B模型BF16 KV在32K上下文下确实可能超过32GB），但具体数值缺乏来源验证，且INT4 KV支持度随框架版本动态变化，无法确证。

## Search Query

vLLM TensorRT-LLM INT4 KV cache support Qwen3 27B 32K context RTX 5090
