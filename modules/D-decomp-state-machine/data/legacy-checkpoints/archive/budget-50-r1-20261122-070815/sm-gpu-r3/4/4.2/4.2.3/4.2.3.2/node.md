# N309: H100 支持原生 FP8 Tensor Core，在 Qwen3-27B FP8 推理下，其吞吐量提升（相比 BF16）可部分抵消高功耗劣势，需计算 FP8 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

H100 支持原生 FP8 Tensor Core，在 Qwen3-27B FP8 推理下，其吞吐量提升（相比 BF16）可部分抵消高功耗劣势，需计算 FP8 模式下的单位 token 能耗是否低于 A100 BF16 模式

## Corrected Claim

H100 支持原生 FP8 Tensor Core，在 Qwen3-27B FP8 推理下，其吞吐量提升（相比 BF16）可部分抵消高功耗劣势，需计算 FP8 模式下的单位 token 能耗是否低于 A100 BF16 模式

## Evidence

先验知识/题面给定，逻辑校验通过：H100 确实支持原生 FP8 Tensor Core，FP8 相比 BF16 在计算密度和带宽效率上具有优势，虽然 H100 功耗高于 A100，但 FP8 带来的吞吐量提升足以在单位 token 能耗上形成竞争力，该陈述符合硬件架构与能效的基本逻辑。

## Search Query

H100 FP8 inference energy efficiency vs A100 BF16 LLM tokens per watt
