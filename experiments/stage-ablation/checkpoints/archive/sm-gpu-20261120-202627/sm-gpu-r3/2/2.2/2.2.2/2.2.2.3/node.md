# N215: FP8 量化中 Attention 层 Q/K/V 投影矩阵与 FFN 层权重在 E4M3 格式下的最大可表示值（6.0）与最小非零值（2^-9）对梯度/激活值

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N53

## Claim

FP8 量化中 Attention 层 Q/K/V 投影矩阵与 FFN 层权重在 E4M3 格式下的最大可表示值（6.0）与最小非零值（2^-9）对梯度/激活值截断的具体影响系数，需结合 Qwen3-27B 的 LayerNorm 后激活值分布统计（均值/标准差）计算截断比例

## Corrected Claim

FP8 E4M3格式的最大可表示值为6.0，最小非零值为2^-9。在Qwen3-27B模型中，Attention层Q/K/V投影矩阵与FFN层权重的梯度/激活值截断影响需结合LayerNorm后的实际激活值分布统计（如均值/标准差）进行具体计算，当前缺乏具体分布数据，无法给出确切截断比例系数。

## Evidence

[质询]该陈述试图将通用的FP8 E4M3格式参数（最大6.0，最小非零2^-9）与特定模型（Qwen3-27B）的具体激活值分布统计（均值/标准差）直接关联以计算“具体影响系数”，但缺乏该模型在LayerNorm后的实际分布数据支持，且“具体影响系数”的定义模糊，无法仅凭格式参数和未提供的统计量得出唯一确定的数值结论。 | 先验知识/题面给定，逻辑校验通过：FP8 E4M3格式的最大值确为6.0，最小正数为2^-9（0.001953125），这是IEEE 754子集的标准定义；但Qwen3-27B的具体激活值分布属于经验事实，且未提供具体统计数值，无法计算出具体的截断比例系数，故降级为定性描述。

## Search Query

FP8 E4M3 dynamic range impact on attention mechanism numerical stability LLM quantization
