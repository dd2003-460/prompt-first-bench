# N58: NVFP4/W4量化在MMLU基准上相比BF16的准确率损失通常为0.5%-1.5%，得益于NVFP4的块级缩放因子（Block-wise Scaling），其

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14

## Claim

NVFP4/W4量化在MMLU基准上相比BF16的准确率损失通常为0.5%-1.5%，得益于NVFP4的块级缩放因子（Block-wise Scaling），其精度损失接近INT8水平，显著优于传统W4A16 [待核验: Qwen3-27B NVFP4 MMLU score]

## Corrected Claim

NVFP4/W4量化在MMLU基准上相比BF16的准确率损失通常较小（具体数值因模型而异，常见报告在0.5%-1.5%区间），得益于NVFP4的块级缩放因子，其精度损失通常优于传统W4A16量化。

## Evidence

[质询]该陈述包含具体的经验性数值范围（0.5%-1.5%）和特定模型（Qwen3-27B）的基准测试结果，属于硬件/模型性能经验事实，无法从第一性原理推导。且‘NVFP4精度损失接近INT8水平’这一结论在不同模型规模和任务上可能存在显著差异，缺乏通用性保证。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值及Qwen3-27B的具体表现）

## Search Query

Qwen3-27B NVFP4 W4 MMLU benchmark accuracy loss BF16
