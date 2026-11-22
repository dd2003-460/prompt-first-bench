# N49: 2×RTX 4090 方案中，KV Cache 分片导致的显存碎片化开销约为总 KV Cache 的 5-10%（即 32K 上下文下约 0.8-1.7 GB）

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

2×RTX 4090 方案中，KV Cache 分片导致的显存碎片化开销约为总 KV Cache 的 5-10%（即 32K 上下文下约 0.8-1.7 GB），加上通信缓冲区预留（约 1-2 GB），实际可用显存效率从 100% 降至 85-90%，具体数值取决于推理框架（如 vLLM 或 TensorRT-LLM）的分页策略。

## Corrected Claim

2×RTX 4090 方案中，KV Cache 分片及通信缓冲区预留会导致一定比例的显存开销，实际可用显存效率通常低于 100%，具体损耗比例（如 5-15%）高度依赖于推理框架（如 vLLM 或 TensorRT-LLM）的分页策略及上下文长度配置。

## Evidence

[质询]数值量级与具体百分比（5-10%碎片化、85-90%效率）属于特定框架和配置下的经验观测值，缺乏通用理论推导支持，且不同推理框架（vLLM vs TensorRT-LLM）的分页策略差异可能导致实际开销显著偏离此区间，存在将特定场景数据泛化为通用规律的风险。 | 经验事实，逻辑自洽但缺来源支持（source=knowledge，但具体数值为经验参数，非第一性原理可严格推出，且无外部来源验证具体百分比范围）
