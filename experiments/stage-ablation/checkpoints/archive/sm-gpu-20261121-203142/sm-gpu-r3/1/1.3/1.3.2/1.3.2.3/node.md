# N148: NVFP4量化质量损失与Group Size的关系：较小Group Size (16) 提供更精细的量化，MMLU准确率下降通常<0.5%；较大Group Si

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

NVFP4量化质量损失与Group Size的关系：较小Group Size (16) 提供更精细的量化，MMLU准确率下降通常<0.5%；较大Group Size (128) 可能导致准确率下降1-2% [待核验]，需在显存节省与质量损失间权衡

## Corrected Claim

NVFP4量化中，较小Group Size (16) 通常提供更精细的量化，准确率损失较小；较大Group Size (128) 可能导致更明显的准确率下降，需在显存节省与质量损失间权衡。

## Evidence

[质询]具体数值（<0.5% vs 1-2%）缺乏通用基准支持，不同模型架构（如LLaMA vs Mistral）和任务分布下，Group Size对MMLU的影响幅度差异显著，直接断言具体百分比区间可能以偏概全。 | 经验事实，逻辑自洽（小Group Size精度更高符合量化原理）但缺来源支持，且具体数值缺乏通用性，降级为定性表述。

## Search Query

NVFP4 quantization quality loss group size 16 64 128 MMLU benchmark
