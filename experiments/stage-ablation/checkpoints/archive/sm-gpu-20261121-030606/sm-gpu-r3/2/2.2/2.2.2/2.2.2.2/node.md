# N227: W4A16精度下Qwen3-27B在MMLU基准上的准确率下降幅度通常小于1.5%，具体数值依赖于量化算法（如AWQ/GPTQ）及校准数据集大小，需与FP8的<

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N103, N104, N105

## Claim

W4A16精度下Qwen3-27B在MMLU基准上的准确率下降幅度通常小于1.5%，具体数值依赖于量化算法（如AWQ/GPTQ）及校准数据集大小，需与FP8的<0.5%损失进行对比以评估通用对话场景的质量容忍度。

## Corrected Claim

W4A16精度下Qwen3-27B在MMLU基准上的准确率下降幅度通常较小（具体数值依赖于量化算法及校准数据集大小），需与FP8的<0.5%损失进行对比以评估通用对话场景的质量容忍度。

## Evidence

[质询]具体数值（<1.5%）属于经验事实，缺乏通用性保证，不同量化算法和校准集大小可能导致显著差异，且未提供具体实验数据支撑该上限。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B W4A16 quantization MMLU accuracy loss
