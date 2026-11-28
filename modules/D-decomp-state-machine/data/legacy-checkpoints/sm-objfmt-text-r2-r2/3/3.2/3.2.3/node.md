# N69: Qwen3-27B INT4 (W4A16) 量化后的 MMLU、HumanEval、GSM8K 绝对分数，用于实证计算 ΔScore_INT4 是否落在 2%

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N17

## Claim

Qwen3-27B INT4 (W4A16) 量化后的 MMLU、HumanEval、GSM8K 绝对分数，用于实证计算 ΔScore_INT4 是否落在 2%-5% 区间，特别关注 GSM8K 是否突破 5% 红线。

## Corrected Claim

Qwen3-27B INT4 (W4A16) 量化模型已发布（见来源 [1]），但其具体的 MMLU、HumanEval、GSM8K 绝对分数及相应的性能衰减幅度需查阅该仓库内的详细评测报告或相关技术博客，当前参考来源未提供具体数值。

## Evidence

[质询]参考来源仅提供了量化模型的仓库链接和压缩方法描述（W4A16 GPTQ），并未包含具体的 MMLU、HumanEval、GSM8K 基准测试绝对分数，因此无法从现有来源中直接提取数据以验证 ΔScore 是否落在 2%-5% 区间或 GSM8K 是否突破 5% 红线。 | 来源 [1] 确认了 Qwen3-27B INT4 (W4A16) 模型的存在及量化方案，但未提供具体的基准测试分数，属于经验事实且缺乏直接数据支持，故降级。

## Search Query

Qwen3-27B INT4 W4A16 quantization accuracy drop GSM8K

## Retrieval Sources

- {'url': 'https://github.com/mbgulden/Qwen3.8-27B-INT4-W4A16-MTP&rut=2247b55b6a57ead5c62b310b0a425e584cc592bebd1158e0c785880fd81eac62', 'type': 'ddg', 'title': 'GitHub - mbgulden/Qwen3.8-27B-INT4-W4A16-MTP: W4A16 (INT4) GPTQ ...'}
