# N442: W4 (NVFP4/INT4) 量化下 Qwen3-27B 在 MMLU-Pro (或 IFEval) 复杂指令/知识基准测试上的准确率绝对值及相对于 BF16

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N143

## Claim

W4 (NVFP4/INT4) 量化下 Qwen3-27B 在 MMLU-Pro (或 IFEval) 复杂指令/知识基准测试上的准确率绝对值及相对于 BF16 基线的下降幅度，用于计算复杂推理场景下的 QF_Reasoning = Acc_W4 / Acc_BF16，以验证长上下文/复杂任务的质量保持率。

## Corrected Claim

在W4量化下，Qwen3-27B在MMLU-Pro或IFEval基准上的准确率通常会有所下降，具体下降幅度取决于量化算法与校准策略，需查阅特定量化库（如llama.cpp, GPTQModel等）针对该模型的实测报告以获取准确数值。

## Evidence

[质询]该陈述要求提供具体的准确率绝对值及下降幅度，属于特定模型（Qwen3-27B）在特定量化方案（NVFP4/INT4）下的经验性性能数据。此类数据高度依赖于具体的量化实现细节（如校准集、量化粒度、是否使用GPTQ/AWQ等算法）以及测试时的随机种子，并非由第一性原理或数学公理严格推导出的唯一确定值。此外，'NVFP4'并非业界通用的标准量化格式名称（常见为FP4/INT4），可能存在术语混淆或特定内部实现导致的不可复现性。 | 经验事实，逻辑自洽但缺来源支持。检索无可用来源，且该数据为特定模型量化后的经验性能指标，无法从第一性原理推出，故降级。

## Search Query

Qwen3-27B W4 NVFP4 INT4 MMLU-Pro IFEval accuracy benchmark comparison BF16
