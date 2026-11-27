# N353: 混合精度回退策略的成本量化：若 INT4 损失超标，采用 'Attention Layers BF16 + FFN Layers INT4' 的混合精度策略，显

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N119

## Claim

混合精度回退策略的成本量化：若 INT4 损失超标，采用 'Attention Layers BF16 + FFN Layers INT4' 的混合精度策略，显存占用从 13.5GB 增加至约 18.5GB (假设 Attention 占权重 20%)，但仍可容纳于 24GB 显存，性能损失预计降至 < 1.5% (HumanEval) 和 < 0.8% (MMLU) [待核验: 需实测验证]。

## Corrected Claim

混合精度回退策略的成本量化：若 INT4 损失超标，采用 'Attention Layers BF16 + FFN Layers INT4' 的混合精度策略。假设 Attention 占权重 20%，显存占用将显著增加（具体数值取决于基线模型精度和架构细节，例如若基线为纯 INT4，显存可能从 13.5GB 增至约 21.6GB），需确保总显存不超过 24GB。性能损失预计降低，但具体数值（如 HumanEval < 1.5% 和 MMLU < 0.8%）需实测验证。

## Evidence

[质询]显存占用从13.5GB增加至18.5GB的数值推导存在逻辑瑕疵：若INT4全量模型为13.5GB，且Attention占权重20%，则Attention权重约为2.7GB。将其从INT4转为BF16（4倍精度），显存增加量应为2.7GB * 3 = 8.1GB，总显存应为13.5 + 8.1 = 21.6GB，而非18.5GB。18.5GB的数值可能基于不同的基线假设（如基线并非纯INT4，或Attention占比/权重分布不同），但陈述中未明确说明基线构成，导致数值与假设条件（Attention占20%）在简单线性推导下不匹配。此外，性能损失<1.5%和<0.8%为经验预测值，缺乏实测数据支持。 | 先验知识/题面给定，逻辑校验发现显存增量计算与假设条件存在不一致（13.5GB基线+20% Attention转BF16应增至约21.6GB，而非18.5GB），且性能损失为未验证的经验预测，故降级。

## Search Query

mixed precision quantization LLM attention BF16 FFN INT4 memory footprint accuracy tradeoff
