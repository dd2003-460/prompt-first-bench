# N188: vLLM 中启用 KV Cache 量化的配置要求与兼容性：vLLM 支持 FP8/INT8 KV Cache 需启用 --kv-cache-dtype fp8

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

vLLM 中启用 KV Cache 量化的配置要求与兼容性：vLLM 支持 FP8/INT8 KV Cache 需启用 --kv-cache-dtype fp8 或 int8 参数。此功能在 NVIDIA Ada Lovelace 架构 (RTX 4090) 上受限于 Tensor Core 对 FP8 的支持情况：RTX 4090 支持 FP8 存储但计算需回退至 FP16/INT8 路径，可能引入额外计算开销。需验证 vLLM 在 RTX 4090 上启用 KV Cache 量化后的实际吞吐量变化。[待核验: vLLM 文档中 RTX 4090 + FP8 KV Cache 的已知问题或性能基准]

## Corrected Claim

vLLM 支持通过 --kv-cache-dtype 参数启用 FP8/INT8 KV Cache 量化。在 NVIDIA Ada Lovelace 架构（如 RTX 4090）上，由于硬件对 FP8 计算单元的支持特性及软件栈优化程度，实际吞吐量变化需具体验证，可能存在因计算路径回退或优化不足导致的性能波动。

## Evidence

[质询]该陈述包含具体的硬件架构特性（RTX 4090/Ada Lovelace 对 FP8 的支持细节）及特定软件（vLLM）的配置行为，属于经验事实。虽然逻辑上自洽（Ada 架构确实引入 FP8 支持，但消费级卡通常缺乏针对 FP8 推理的完整优化路径，导致回退或性能收益有限），但缺乏直接来源证实 vLLM 在 RTX 4090 上启用 FP8 KV Cache 的具体已知问题或性能基准数据。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

vLLM RTX 4090 FP8 KV Cache quantization performance benchmark
