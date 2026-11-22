# N30: 决策敏感性分析维度 2（精度容忍度）：若应用对幻觉率敏感（如医疗/法律），则必须使用 BF16/FP8，排除 INT4/W4；若为创意写作/代码补全，INT4/

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

决策敏感性分析维度 2（精度容忍度）：若应用对幻觉率敏感（如医疗/法律），则必须使用 BF16/FP8，排除 INT4/W4；若为创意写作/代码补全，INT4/W4 的质量损失（Perplexity 增加 5-15% [待核验]）可接受，此时低精度方案的性价比显著上升。

## Corrected Claim

决策敏感性分析维度 2（精度容忍度）：若应用对幻觉率敏感（如医疗/法律），通常建议优先使用 BF16/FP8 或高精度量化（如 INT8），以最小化质量损失；若为创意写作/代码补全，INT4/W4 的质量损失（Perplexity 增加幅度视模型与算法而定，通常在可接受范围内）可接受，此时低精度方案的性价比显著上升。

## Evidence

[质询]数值量级存疑：INT4/W4 量化导致的 Perplexity 增加 5-15% 并非普适常数，高度依赖模型规模、量化算法（如 GPTQ/AWQ）及数据集，小模型或激进量化下 PPL 增幅可能远超 15%，大模型或高精度量化下可能低于 5%；此外，'必须使用 BF16/FP8' 的绝对化表述忽略了 INT8 在部分医疗/法律场景下可能作为折中方案的存在。 | 先验知识/题面给定，逻辑校验通过；但具体数值区间（5-15%）缺乏统一标准且受多种变量影响，属于经验性估计而非严格推导，故降级为定性表述。

## Search Query

quantization quality loss perplexity increase INT4 vs BF16 LLM task dependent
