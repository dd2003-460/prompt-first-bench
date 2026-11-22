# N404: Qwen3-27B INT8量化版本的GSM8K准确率Acc_INT8，需对比INT8与BF16在数学推理任务上的差异；INT8通常对数学推理影响较小，但需确认

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N133

## Claim

Qwen3-27B INT8量化版本的GSM8K准确率Acc_INT8，需对比INT8与BF16在数学推理任务上的差异；INT8通常对数学推理影响较小，但需确认量化校准数据集是否包含数学推理样本，若校准集缺乏数学数据，可能导致数学特定token的量化误差增大。

## Corrected Claim

Qwen3-27B INT8量化版本在GSM8K上的准确率需通过实际测试确认；理论上INT8量化对数学推理的影响取决于校准数据集是否包含数学样本，若校准集缺乏数学数据，可能导致数学特定token的量化误差增大，进而影响准确率。

## Evidence

[质询]该陈述包含具体的经验性结论（INT8对数学推理影响较小）和特定模型（Qwen3-27B）的性能预期，属于经验事实，无法仅凭逻辑推导得出，且缺乏具体量化数据支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B INT8 GSM8K math reasoning accuracy
