# N343: ETPD 分子中 Tokens_per_second 的修正项：需使用有效吞吐 Effective_TPS = Raw_TPS * (1 - Batch_Uti

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N118

## Claim

ETPD 分子中 Tokens_per_second 的修正项：需使用有效吞吐 Effective_TPS = Raw_TPS * (1 - Batch_Utilization_Loss) * (1 - Context_Attention_Overhead)，其中 Batch_Utilization_Loss 在 Batch Size=1 时为 0，Context_Attention_Overhead 随上下文长度 L 呈 O(L) 增长，在 32K 上下文下约为 10-15% [待核验]，此修正确保 ETPD 反映实际长上下文场景性能而非短文本峰值。

## Corrected Claim

ETPD 分子中 Tokens_per_second 的修正项：需使用有效吞吐 Effective_TPS = Raw_TPS * (1 - Batch_Utilization_Loss) * (1 - Context_Attention_Overhead)，其中 Batch_Utilization_Loss 在 Batch Size=1 时为 0，Context_Attention_Overhead 随上下文长度 L 增长（通常呈线性或超线性），具体数值取决于硬件与推理引擎实现，此修正确保 ETPD 反映实际长上下文场景性能而非短文本峰值。

## Evidence

[质询]Context_Attention_Overhead 的具体数值范围（10-15%）及 O(L) 增长模型属于特定硬件/软件栈下的经验观测值，并非普适物理定律或数学公理，且不同推理引擎（如 vLLM, TensorRT-LLM）和硬件架构下该开销差异巨大，缺乏通用性。 | source=knowledge，逻辑自洽（公式结构合理，量纲正确），但具体数值（10-15%）为经验事实，无外部来源支持，依据经验事实排除条款降级。
