# N54: INT8 与 FP8 在 Qwen3-27B 上的关键差异在于梯度消失风险：INT8 在反向传播中可能因量化噪声导致训练不稳定，但推理时 FP8 的动态范围优势

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

INT8 与 FP8 在 Qwen3-27B 上的关键差异在于梯度消失风险：INT8 在反向传播中可能因量化噪声导致训练不稳定，但推理时 FP8 的动态范围优势使其在处理异常值（outliers）时更鲁棒，推荐在存在大量 outlier 的层使用 FP8。

## Corrected Claim

INT8 与 FP8 在 Qwen3-27B 上的关键差异在于数值表示特性：INT8 在反向传播中可能因量化噪声导致训练震荡或不稳定，而 FP8 在推理时因具有更大的动态范围，在处理异常值（outliers）时通常表现出更好的数值鲁棒性，因此在特定存在大量 outlier 的层中，FP8 可能是更优的量化选择。

## Evidence

[质询]将INT8与FP8在训练中的稳定性差异归因于'梯度消失风险'存在概念混淆。INT8量化噪声主要导致梯度方差增大或训练震荡（instability），而非典型的梯度消失（vanishing gradients，通常由激活函数饱和或网络深度引起）；此外，FP8在推理中对outliers的鲁棒性主要源于其较大的动态范围（相比INT8的固定8位整数范围），但'推荐在存在大量outlier的层使用FP8'这一具体工程建议缺乏通用理论支持，因为INT8通常通过per-channel或per-tensor scaling也能处理outliers，且FP8训练/推理的硬件支持普及度低于INT8，该建议可能过于绝对。 | 先验知识/题面给定，逻辑校验通过但存在概念不严谨（梯度消失 vs 训练不稳定）及工程建议的绝对化问题，降级为定性表述。

## Search Query

INT8 vs FP8 outlier handling LLM inference robustness
