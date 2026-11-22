# N11: 精度选择逻辑：BF16 为无损基准，FP8/INT8 量化损失通常 <1% 困惑度（perplexity），W4 量化损失可达 3-10% 困惑度；需根据任务类

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

精度选择逻辑：BF16 为无损基准，FP8/INT8 量化损失通常 <1% 困惑度（perplexity），W4 量化损失可达 3-10% 困惑度；需根据任务类型（代码生成 vs 通用对话）确定可接受的质量损失阈值。

## Corrected Claim

精度选择逻辑：BF16 为无损基准，FP8/INT8 量化损失通常 <1% 困惑度（perplexity），W4 量化损失可达 3-10% 困惑度；需根据任务类型（代码生成 vs 通用对话）确定可接受的质量损失阈值。

## Evidence

先验知识/题面给定，逻辑校验通过
