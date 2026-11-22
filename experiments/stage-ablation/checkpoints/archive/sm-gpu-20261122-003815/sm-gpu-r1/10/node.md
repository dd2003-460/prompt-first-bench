# N43: 精度损失可接受性的定量标准：对于通用对话助手，INT4量化导致的Perplexity增加 <5% 或 MMLU分数下降 <3 分 通常被视为可接受；对于专业推理

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

精度损失可接受性的定量标准：对于通用对话助手，INT4量化导致的Perplexity增加 <5% 或 MMLU分数下降 <3 分 通常被视为可接受；对于专业推理任务，INT8/FP8 是底线，INT4 仅在显存极度受限且用户容忍度高的情况下使用。

## Corrected Claim

对于通用对话助手，INT4量化通常被视为在显存受限下的可行方案，其精度损失（如Perplexity增加或MMLU下降）需根据具体模型和任务评估，通常要求保持在较低水平（如个位数百分比或分数点以内）以保证可用性；对于专业推理任务，INT8/FP8是更稳妥的底线，INT4仅在显存极度受限且用户容忍度高的情况下使用。

## Evidence

[质询]陈述中给出的具体数值阈值（Perplexity增加<5%、MMLU下降<3分）属于经验性工程标准，缺乏行业公认的硬性定义，且不同模型规模、量化算法（GPTQ/AWQ等）及任务类型下，可接受的精度损失范围差异巨大，该具体数值可能过于绝对或仅适用于特定小模型/特定基准，存在以偏概全的风险。 | 来源[1][2][3]均讨论了INT4量化的精度损失与平衡，但均未提供'Perplexity<5%'或'MMLU<3分'这一具体定量标准，仅定性提及精度损失不可避免及需控制，属于间接支持或无关，无法直接验证具体数值阈值。

## Retrieval Sources

- {'url': 'https://devpress.csdn.net/v1/article/detail/162357960&rut=40b082bc7cf3e80ea78fcb5bbb09a7f68d9f48e96433b104571b7f55cb6dcfc4', 'type': 'ddg', 'title': '模型量化实战：从 Fp16 到 Int4 的精度与性能平衡_人工智能_继续商行-ai硬件创业社区'}
- {'url': 'https://blog.csdn.net/iymei4986533030/article/details/162118827&rut=2097a23ab04625d1e44572f87dbca94e8d208c772bf2c33d497b54ef5348854b', 'type': 'ddg', 'title': '模型量化深度拆解：从 Fp16 到 Int4 的精度损失与推理加速实测'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/162118827&rut=14ea9a055f77b53a45c8428dcaec87a3701ebb5755a18454ff3bb7fc98e3a778', 'type': 'ddg', 'title': '模型量化深度拆解：从 Fp16 到 Int4 的精度损失与推理加速实测_人工智能_继续商行-amd开发者中国社区'}
