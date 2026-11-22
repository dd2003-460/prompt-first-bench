# N123: FP8 量化对长尾/高难度任务的敏感性阈值：在 HumanEval (代码生成) 和 GSM8K (数学推理) 上，FP8 的 Pass@1 下降通常 <1% 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

FP8 量化对长尾/高难度任务的敏感性阈值：在 HumanEval (代码生成) 和 GSM8K (数学推理) 上，FP8 的 Pass@1 下降通常 <1% (即 <1 个测试用例失败)，显著低于 INT4 的 2-5% 下降，表明 FP8 在逻辑推理链上的质量损失可忽略。

## Corrected Claim

FP8 量化在 HumanEval 和 GSM8K 等任务上的 Pass@1 下降通常显著低于 INT4 量化，表明 FP8 在逻辑推理链上的质量损失相对较小，但具体下降幅度取决于模型架构与量化策略。

## Evidence

[质询]该陈述包含具体的经验性数值阈值（FP8下降<1%，INT4下降2-5%），属于硬件/模型量化性能的经验事实，无法从第一性原理推导。且不同模型架构、量化实现（如SmoothQuant, FP8 E4M3 vs E5M2）及任务难度分布下，具体下降幅度存在显著方差，'通常<1%'的绝对化表述缺乏普适性证据支持。 | 经验事实，逻辑自洽（FP8精度高于INT4，损失理应更小）但缺来源支持（本轮检索无可用来源），无法验证具体数值阈值。

## Search Query

Qwen3-27B FP8 vs INT4 quantization HumanEval GSM8K Pass@1 accuracy comparison
