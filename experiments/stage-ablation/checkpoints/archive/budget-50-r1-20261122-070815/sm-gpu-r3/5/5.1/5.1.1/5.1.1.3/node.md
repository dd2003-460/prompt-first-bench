# N339: Qwen3-27B 在 A100 80GB 上运行 BF16 精度时，若使用 vLLM PagedAttention，其实际显存利用率约为 85-90%，剩余 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N120

## Claim

Qwen3-27B 在 A100 80GB 上运行 BF16 精度时，若使用 vLLM PagedAttention，其实际显存利用率约为 85-90%，剩余 8-12GB 用于 KV Cache 和激活值，导致在 32K 上下文下最大并发 Batch Size 受限为 1-2，若 Batch Size > 2 则触发 OOM 或显著降频，此约束直接决定了单卡 A100 在低并发场景下的性价比上限。

## Corrected Claim

Qwen3-27B 在 A100 80GB 上运行 BF16 精度时，若使用 vLLM PagedAttention，模型权重占用大部分显存，剩余空间用于 KV Cache 和激活值，导致在 32K 上下文下最大并发 Batch Size 受限，具体数值取决于系统配置，通常较低。

## Evidence

[质询]数值量级与具体参数（85-90%利用率、1-2并发、32K上下文）高度依赖具体的vLLM版本、量化策略及系统配置，属于经验事实而非第一性原理可推导的固定常数；且'显著降频'表述模糊，通常OOM是硬错误而非降频。 | 经验事实，逻辑自洽但缺来源支持
