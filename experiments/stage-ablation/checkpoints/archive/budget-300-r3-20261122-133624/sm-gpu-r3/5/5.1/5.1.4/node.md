# N115: RTX 5090 的显存容量为 32GB，在 INT8 下运行 Qwen3-27B 的显存占用为 32.59GB，略超 32GB 限制，需启用 PagedAtt

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

RTX 5090 的显存容量为 32GB，在 INT8 下运行 Qwen3-27B 的显存占用为 32.59GB，略超 32GB 限制，需启用 PagedAttention 或限制上下文至 24K 以保稳定。

## Corrected Claim

RTX 5090 的显存容量为 32GB，在 INT8 下运行 Qwen3-27B 的显存占用预计接近或略超 32GB，需启用 PagedAttention 或限制上下文长度以保稳定。

## Evidence

[质询]显存占用数值（32.59GB）过于精确且缺乏来源支持，属于经验事实；此外，Qwen3-27B 在 INT8 下的基础权重约为 27GB，加上 KV Cache 和激活值，32.59GB 的估算虽在量级上合理，但具体数值无法从第一性原理严格推导，且不同推理框架（如 vLLM, TGI）的开销差异可能导致实际占用波动，该精确数值可能具有误导性。 | 经验事实，逻辑自洽但缺来源支持；RTX 5090 显存 32GB 为已知规格，INT8 下 27B 模型占用略超 32GB 符合一般推理显存估算逻辑，但具体数值 32.59GB 无外部来源直接验证。
