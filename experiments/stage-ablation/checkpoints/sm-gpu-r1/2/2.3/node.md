# N12: 量化质量损失边界：BF16为基准（Loss=0）。FP8/INT8在长上下文（>8K）下的困惑度（Perplexity）增加通常<1%，但在极长链推理中可能累积

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

量化质量损失边界：BF16为基准（Loss=0）。FP8/INT8在长上下文（>8K）下的困惑度（Perplexity）增加通常<1%，但在极长链推理中可能累积至3-5% [待核验]。INT4 (4-bit) 困惑度增加通常在5-10%，且对数学/代码任务影响更大（准确率下降5-15%）。若业务容忍度为PPL增加<2%，则必须选FP8/INT8，排除INT4。

## Corrected Claim

量化质量损失边界：BF16为基准。FP8/INT8在长上下文下的困惑度增加通常较小（通常<1%），但在极长链推理中可能累积；INT4困惑度增加通常显著高于INT8/FP8（常见范围5-10%），且对数学/代码任务影响更大。若业务容忍度为PPL增加<2%，通常建议选FP8/INT8，排除INT4。

## Evidence

[质询]具体数值区间（如FP8/INT8 PPL增加<1%，INT4增加5-10%）属于经验事实，且高度依赖于具体模型架构、校准数据集及任务类型，缺乏通用性；参考来源仅涵盖量化原理与格式对比，未提供具体的困惑度（Perplexity）或准确率下降的量化统计数据，无法直接支持这些精确数值。 | 逻辑自洽（精度越低误差通常越大，INT4误差大于INT8/FP8），但参考来源[1][2][3]仅介绍量化原理与格式特性，未提供具体的PPL或准确率下降数值，属于经验事实且缺来源直接支持。

## Search Query

Qwen3-27B quantization perplexity degradation FP8 INT8 INT4 long context benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_02936/article/details/149627108&rut=3776e66959c1bd6695b9798e3c2c5872abe36e543625cb00774ef2a796575f5f', 'type': 'ddg', 'title': 'oneDNN量化计算权威指南：INT8、FP16、BF16精度优化策略-CSDN博客'}
- {'url': 'https://blog.csdn.net/qq_48379015/article/details/155849573&rut=785c5594b0a6f710bf30325fd05d3d596288c68fb4ab3ba9d90d4dfdc8d4d817', 'type': 'ddg', 'title': 'Fp8 / Fp16 / Bf16 / Int8 / Int4 / 量化 —— 从原理到工程实战（面向部署的大模型）'}
- {'url': 'https://amoursec.github.io/aikg/06-accelerators-architecture/precision-formats-low-bit-compute/&rut=ceb7c1e3122e475faa32f2fe31b91976358efdde00a20ee1350404d3672ac3e3', 'type': 'ddg', 'title': '精度格式：FP16、BF16、FP8 与量化计算 - AI Knowledge Graph'}
