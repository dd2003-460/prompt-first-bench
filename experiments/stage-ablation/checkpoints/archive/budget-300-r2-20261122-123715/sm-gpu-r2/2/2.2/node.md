# N12: 量化方法对质量损失的影响：GPTQ, AWQ, SmoothQuant 等后训练量化方法在 4-bit 下可保持 90-95% 的原始模型性能；需对比不同量化算

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

量化方法对质量损失的影响：GPTQ, AWQ, SmoothQuant 等后训练量化方法在 4-bit 下可保持 90-95% 的原始模型性能；需对比不同量化算法在 Qwen3-27B 上的实际困惑度增加量（Δperplexity）。

## Corrected Claim

GPTQ, AWQ, SmoothQuant 等后训练量化方法在 4-bit 下通常能显著降低模型精度损失，具体性能保持率（如 90-95%）取决于基准测试任务及模型规模，需针对 Qwen3-27B 实测困惑度增加量（Δperplexity）以评估实际影响。

## Evidence

[质询]陈述中关于“90-95% 原始模型性能”的具体数值范围属于经验事实，且未指定具体的基准测试（如 MMLU, GSM8K 等）或任务类型，不同任务下性能保持率差异巨大，该数值缺乏普适性且来源未提供具体数据支持。 | 来源[1]仅介绍了 SmoothQuant 的原理（解决激活值大值通道问题），未提供 GPTQ/AWQ/SmoothQuant 在 4-bit 下的具体性能保持率数值（90-95%）或 Qwen3-27B 的困惑度数据，属于经验事实缺来源直接支持。

## Search Query

GPTQ AWQ 4-bit quantization perplexity increase LLM

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1971154754953523608&rut=641fb2295f241042c352180a48a455276460bb005cbf8a370e48bf85b24ed21f', 'type': 'ddg', 'title': '大模型量化领域梳理（二）：SmoothQuant、GPTQ和AWQ'}
