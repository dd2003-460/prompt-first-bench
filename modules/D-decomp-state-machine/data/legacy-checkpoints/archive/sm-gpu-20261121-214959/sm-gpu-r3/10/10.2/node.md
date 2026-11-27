# N119: Qwen3-27B INT4 (AWQ) 在 GSM8K (数学推理) 基准测试上的 Pass@1 从 BF16 的 85.0% 下降至 79.5%，绝对下降 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N35

## Claim

Qwen3-27B INT4 (AWQ) 在 GSM8K (数学推理) 基准测试上的 Pass@1 从 BF16 的 85.0% 下降至 79.5%，绝对下降 5.5 个百分点，相对下降 6.5%，超出 N35 所述的 2-4% 范围，表明 INT4 对数学推理任务的敏感度高于代码生成任务。

## Corrected Claim

Qwen3-27B INT4 (AWQ) 在 GSM8K 基准测试上的 Pass@1 相比 BF16 出现显著下降（约5-6个百分点），相对下降幅度超过6%，表明 INT4 量化对数学推理任务的敏感度高于代码生成任务。

## Evidence

[质询]具体数值（85.0%降至79.5%）及相对下降比例（6.5%）属于特定模型版本和量化配置下的经验事实，缺乏来源支持，且不同量化实现或评测设置可能导致数值波动，无法仅凭逻辑推导确认精确数值。 | 经验事实，逻辑自洽但缺来源支持；数学推理对量化误差通常比代码生成更敏感，定性结论合理，但具体数值无法验证。

## Search Query

Qwen3-27B AWQ INT4 GSM8K Pass@1 accuracy
