# N344: MI300X 在 Batch Size=4 且上下文=32K 时的显存峰值需考虑 PagedAttention 的 Block Table 开销及非对齐内存分配

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N129, N130, N131

## Claim

MI300X 在 Batch Size=4 且上下文=32K 时的显存峰值需考虑 PagedAttention 的 Block Table 开销及非对齐内存分配损耗，实际峰值显存占用可能达到 185-190GB，逼近 192GB 物理上限，存在 5-10% 的 OOM 风险，需启用 `--max-num-batched-tokens` 限制或降低上下文至 30K 以留足安全边际。

## Corrected Claim

MI300X 在 Batch Size=4 且上下文=32K 时，显存峰值受 PagedAttention 开销及内存分配损耗影响，可能逼近 192GB 物理上限，存在 OOM 风险，建议启用 `--max-num-batched-tokens` 限制或降低上下文长度以留足安全边际。

## Evidence

[质询]具体数值（185-190GB）及OOM风险百分比（5-10%）缺乏通用基准支持，高度依赖具体的模型参数量、量化方式及KV Cache实现细节，属于特定场景下的经验估算而非普适事实。 | 先验知识/题面给定，逻辑校验通过：MI300X显存为192GB，32K上下文下KV Cache开销巨大，接近物理上限符合工程直觉，但具体峰值数值为经验估算，无来源直接支持。

## Search Query

vLLM PagedAttention memory overhead block table size GB
