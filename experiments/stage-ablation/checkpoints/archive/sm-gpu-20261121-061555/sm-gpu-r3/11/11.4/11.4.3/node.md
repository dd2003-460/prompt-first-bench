# N378: W4A4 量化导致 MMLU 准确率下降的机制归因：区分是权重截断误差（Weight Quantization Error）主导还是激活值动态范围溢出（Acti

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N133

## Claim

W4A4 量化导致 MMLU 准确率下降的机制归因：区分是权重截断误差（Weight Quantization Error）主导还是激活值动态范围溢出（Activation Overflow/Clipping）主导，通过对比 W4A16（仅权重量化）与 W4A4（权值+激活量化）的 MMLU 差值来量化激活量化的额外损失贡献率。

## Corrected Claim

通过对比 W4A16 与 W4A4 的 MMLU 差值，可以量化激活量化相对于仅权重量化带来的额外性能损失，从而分析激活值动态范围溢出对准确率的贡献率。

## Evidence

[质询]该陈述描述了一种方法论（通过对比W4A16与W4A4来量化激活量化的额外损失），而非一个已证实的单一事实结论。虽然逻辑上对比实验是归因的标准手段，但缺乏具体实验数据支持‘激活量化主导’或‘权重截断主导’的具体结论，且不同模型/数据集下主导因素可能不同，直接断言该机制归因结果可能过于绝对。 | 逻辑自洽：对比W4A16（仅权重量化）和W4A4（权值+激活量化）确实可以分离出激活量化带来的额外性能损失，这是量化误差分析的标准控制变量法。但作为经验事实（具体哪种误差主导），缺乏来源支持，且不同场景下结论可能不同，故降级。

## Search Query

W4A4 vs W4A16 quantization accuracy loss decomposition LLM
