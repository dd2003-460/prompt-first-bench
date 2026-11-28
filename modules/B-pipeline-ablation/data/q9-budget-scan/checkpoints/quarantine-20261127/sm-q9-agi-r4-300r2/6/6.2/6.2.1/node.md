# N190: NVFP4 量化在 GPQA/AIME 上的准确率衰减 Δ_acc 并非均匀分布：在涉及大量数字比较或高精度小数运算的子集中，衰减可达 8-10 个百分点；而在

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N74

## Claim

NVFP4 量化在 GPQA/AIME 上的准确率衰减 Δ_acc 并非均匀分布：在涉及大量数字比较或高精度小数运算的子集中，衰减可达 8-10 个百分点；而在定性逻辑推理子集中，衰减仅为 1-2 个百分点。因此，全局平均 39-42% 的估计掩盖了关键数值推理环节的严重缺陷，需对数值敏感任务单独监控。

## Corrected Claim

NVFP4 量化在 GPQA/AIME 上的准确率衰减呈现非均匀分布特征：涉及大量数字比较或高精度小数运算的子集衰减显著高于定性逻辑推理子集。全局平均准确率估计可能掩盖数值推理环节的性能损失，建议对数值敏感任务进行单独监控。

## Evidence

[质询]具体数值（8-10个百分点 vs 1-2个百分点）及全局平均范围（39-42%）缺乏公开基准数据支持，属于高度具体的经验观测值，可能存在过拟合特定测试集或夸大差异的风险。 | 逻辑自洽：低精度量化（NVFP4）确实会显著影响数值计算精度，导致数值敏感任务性能下降大于定性推理任务，符合量化误差传播的基本原理；但具体衰减幅度为经验事实，无来源支持，故降级。

## Search Query

low-bit quantization impact on numerical reasoning accuracy variance by task type
