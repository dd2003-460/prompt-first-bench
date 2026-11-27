# N113: vLLM 框架在 RTX 4090 上运行 Qwen3-27B INT4 的 PagedAttention 块大小（Block Size）对吞吐量的影响：默认 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

vLLM 框架在 RTX 4090 上运行 Qwen3-27B INT4 的 PagedAttention 块大小（Block Size）对吞吐量的影响：默认 block_size=16 或 32 时，显存分配效率与注意力计算效率的权衡，需量化不同 block_size 对 32K 上下文下 tokens/s 的影响系数。

## Corrected Claim

vLLM 框架在 RTX 4090 上运行 Qwen3-27B INT4 时，PagedAttention 的 block_size 设置会影响显存分配效率与注意力计算效率的权衡，进而影响 32K 上下文下的吞吐量，具体影响系数需通过实验量化。

## Evidence

[质询]该陈述包含具体的经验性数值断言（如默认 block_size 为 16 或 32，以及特定硬件/模型组合下的吞吐量影响系数），这些属于硬件与软件配置的经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

vLLM PagedAttention block size impact throughput long context RTX 4090
