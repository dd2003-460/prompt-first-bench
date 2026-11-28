# N255: 端到端任务性能损失映射函数：ΔAccuracy_Task = f(ΔKL_Attention, Context_Length)，需通过在 GSM8K-CoT 或

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N79

## Claim

端到端任务性能损失映射函数：ΔAccuracy_Task = f(ΔKL_Attention, Context_Length)，需通过在 GSM8K-CoT 或 LongBench 上对比 FP16 与 NVFP4 的准确率差值来拟合该函数的斜率，确定每单位注意力偏移导致的任务性能下降系数。

## Corrected Claim

假设端到端任务性能损失与注意力KL散度及上下文长度存在映射关系，可通过在GSM8K-CoT或LongBench上对比FP16与NVFP4的准确率差值来探索该关系，但具体函数形式及斜率需实证验证。

## Evidence

[质询]该陈述描述了一个具体的实验方法论（在特定数据集上对比特定精度格式以拟合特定函数），属于经验性研究设计，无法从第一性原理推导。参考来源讨论的是ICML 2026关于无求解器训练算法的论文，与量化精度（NVFP4 vs FP16）对任务性能的影响完全无关，缺乏任何外部证据支持该具体映射函数的存在性或拟合方法的有效性。 | 逻辑上自洽（量化误差导致注意力分布变化进而影响任务性能是合理的因果链），但参考来源[1]主题为无求解器优化算法，与本事实涉及的量化精度性能评估完全无关，属于经验事实且无来源支持。

## Search Query

quantization accuracy drop mapping attention score divergence task performance long context

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2055981859935466133&rut=e172fb092c36782d2f543ce54e62f3c0e7b99106f9e19263b3e72e202cdb97c8', 'type': 'ddg', 'title': 'Icml 2026 爆款论文：训练速度飙升百倍!全新无求解器预测与优化算法，刷爆端到端学习效率'}
