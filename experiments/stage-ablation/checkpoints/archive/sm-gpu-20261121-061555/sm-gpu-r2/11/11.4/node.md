# N133: W4A4 (权重和激活均为4位) 量化下 Qwen3-27B 的 MMLU 准确率具体数值及相对于 BF16 的下降幅度，验证是否超过 3-5% 且是否导致任务

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N38

## Claim

W4A4 (权重和激活均为4位) 量化下 Qwen3-27B 的 MMLU 准确率具体数值及相对于 BF16 的下降幅度，验证是否超过 3-5% 且是否导致任务不可用。

## Corrected Claim

W4A4量化下Qwen3-27B的MMLU准确率具体数值及相对于BF16的下降幅度需查阅特定量化方案（如GPTQ/AWQ）的官方报告或基准测试数据；通常W4A4量化会导致一定精度损失，但是否超过3-5%及是否导致任务不可用取决于具体实现和任务敏感度。

## Evidence

[质询]具体数值（MMLU准确率及下降幅度）属于经验事实，且不同量化实现（如GPTQ, AWQ, SmoothQuant等）和校准数据集会导致结果差异，无法仅凭逻辑推导得出唯一确定值；此外，'任务不可用'是主观判断，缺乏统一标准。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值及是否超过3-5%的阈值）

## Search Query

Qwen3-27B W4A4 quantization MMLU accuracy drop performance degradation
