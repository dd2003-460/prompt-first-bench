# N40: 推理框架开销（vLLM/TensorRT-LLM）在 32K 上下文下的实际显存占用（GB），需排除框架内部缓冲、CUDA 上下文、PagedAttention

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6, N7, N8

## Claim

推理框架开销（vLLM/TensorRT-LLM）在 32K 上下文下的实际显存占用（GB），需排除框架内部缓冲、CUDA 上下文、PagedAttention block table 等额外开销，具体数值需实测或查阅框架文档。

## Corrected Claim

推理框架（如 vLLM/TensorRT-LLM）在 32K 上下文下的显存占用受多种因素影响（包括 KV Cache、框架缓冲、CUDA 上下文等），具体数值需根据实际部署环境实测或查阅最新框架文档，无法仅凭理论推导得出精确值。

## Evidence

[质询]该陈述声称需要排除特定开销并给出具体数值，但缺乏实测数据或官方文档支持，属于经验事实且无来源佐证。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

vLLM TensorRT-LLM 32K context VRAM overhead GB Qwen3
