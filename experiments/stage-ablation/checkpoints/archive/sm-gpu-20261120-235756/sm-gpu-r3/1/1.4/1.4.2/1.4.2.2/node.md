# N158: FP8 (E4M3) 权重在 GSM8K 数学推理基准测试中的准确率下降幅度：由于数学推理对数值精度敏感，FP8 量化可能导致 GSM8K 准确率下降 0.5%

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N45

## Claim

FP8 (E4M3) 权重在 GSM8K 数学推理基准测试中的准确率下降幅度：由于数学推理对数值精度敏感，FP8 量化可能导致 GSM8K 准确率下降 0.5% - 1.0%（例如 BF16: 85.0% -> FP8: 84.2%），需验证 Qwen3-27B 在 FP8 下的具体 GSM8K 得分及与 BF16 基线的差值。

## Corrected Claim

FP8 (E4M3) 量化通常会导致 GSM8K 等数学推理基准测试的准确率出现轻微下降，具体幅度取决于模型架构、量化校准方法及数据集分布，需针对 Qwen3-27B 进行实测以获取 BF16 与 FP8 的具体得分差值。

## Evidence

[质询]该陈述包含具体的经验性数值（0.5%-1.0% 的下降幅度及具体分数示例），属于硬件/模型性能的经验事实，无法从第一性原理推导。且不同模型架构、量化实现（如是否使用 SmoothQuant 等校准技术）对 GSM8K 的影响差异巨大，0.5%-1.0% 并非普适常数，存在以偏概全的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数值为特定模型/配置下的经验观测值，非通用物理/数学定律）。

## Search Query

Qwen3-27B FP8 GSM8K math reasoning accuracy drop vs BF16
