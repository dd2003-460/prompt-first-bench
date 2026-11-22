# N124: 量化损失工作点2（平衡/中显存）：INT8精度（GPTQ/AWQ）下Qwen3-27B的MMLU准确率损失约1-2% [待核验]，Perplexity增加约0.

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

量化损失工作点2（平衡/中显存）：INT8精度（GPTQ/AWQ）下Qwen3-27B的MMLU准确率损失约1-2% [待核验]，Perplexity增加约0.3-0.5%，显存需求27GB（权重），单卡RTX 4090 (24GB) 不足，需双卡或A100 40GB，质量损失在可接受范围内，适合通用对话任务。

## Corrected Claim

量化损失工作点2（平衡/中显存）：INT8精度（GPTQ/AWQ）下Qwen3-27B的MMLU准确率损失约1-2% [待核验]，Perplexity增加约0.3-0.5% [待核验]，权重显存需求约27GB，加上KV Cache和激活值后总显存需求超过24GB，单卡RTX 4090 (24GB) 不足，需双卡或A100 40GB，质量损失在可接受范围内，适合通用对话任务。

## Evidence

[质询]显存需求数值存在量级错误：Qwen3-27B在INT8精度下权重体积约为27GB，加上KV Cache和激活值，实际运行显存远超24GB，但陈述中称'显存需求27GB（权重）'暗示总需求接近27GB，这与单卡24GB不足、需双卡或A100 40GB的结论在逻辑上虽自洽（27>24），但'27GB'仅指权重，未包含运行时开销，易误导用户认为27GB是总需求；此外，MMLU损失1-2%和Perplexity增加0.3-0.5%为经验数据，缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持；显存计算基本合理（27B INT8权重≈27GB，单卡24GB不足），但具体精度损失数值无来源佐证，且'27GB'仅指权重，未明确总显存需求，存在表述不严谨风险。

## Search Query

Qwen3-27B INT8 GPTQ AWQ MMLU accuracy loss perplexity degradation
