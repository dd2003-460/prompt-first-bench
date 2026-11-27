# N441: W4 (NVFP4/INT4) 量化下 Qwen3-27B 在 HumanEval (或 LiveCodeBench) 代码生成基准测试上的 Pass@1 准确

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N143

## Claim

W4 (NVFP4/INT4) 量化下 Qwen3-27B 在 HumanEval (或 LiveCodeBench) 代码生成基准测试上的 Pass@1 准确率绝对值及相对于 BF16 基线的下降幅度，用于计算代码生成场景下的 QF_Code = Acc_W4 / Acc_BF16，以验证短上下文/细节敏感任务的质量波动。

## Corrected Claim

W4 (NVFP4/INT4) 量化下 Qwen3-27B 在 HumanEval 或 LiveCodeBench 上的 Pass@1 准确率通常低于 BF16 基线，具体下降幅度取决于量化算法及校准策略，需查阅特定实验报告获取精确数值。

## Evidence

[质询]该陈述要求提供具体的绝对值（Pass@1）和相对下降幅度，属于具体的经验性实验数据。由于缺乏检索来源，无法验证具体数值是否准确，且不同量化实现（如GPTQ, AWQ, SmoothQuant）及校准集的选择会导致结果显著差异，单一数值不具备普适性。 | 经验事实，逻辑自洽但缺来源支持。W4量化通常会导致代码生成能力下降，但具体数值需依赖特定实验报告，当前无可用外部证据。

## Search Query

Qwen3-27B W4 NVFP4 INT4 HumanEval LiveCodeBench accuracy benchmark comparison BF16
