# N166: Qwen3-27B 在 GSM8K 数学推理基准上，INT8 (W8A8) 精度相比 BF16 基线的准确率下降幅度约为 1.5% - 3.0%（基于 Llam

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N48

## Claim

Qwen3-27B 在 GSM8K 数学推理基准上，INT8 (W8A8) 精度相比 BF16 基线的准确率下降幅度约为 1.5% - 3.0%（基于 Llama-3-70B 和 Qwen2-72B 的公开量化基准外推，具体需针对 Qwen3-27B 复测验证）

## Corrected Claim

Qwen3-27B 在 GSM8K 数学推理基准上，INT8 (W8A8) 精度相比 BF16 基线的准确率下降幅度预计约为 1.5% - 3.0%（参考 Llama-3-70B 和 Qwen2-72B 的量化表现外推，具体数值需针对 Qwen3-27B 实测验证）

## Evidence

[质询]该陈述明确标注为基于其他模型（Llama-3-70B, Qwen2-72B）的“外推”，且承认需针对 Qwen3-27B 复测。不同模型架构、参数量及训练数据分布对量化敏感度的影响存在显著差异，直接外推缺乏严谨性，属于经验事实而非第一性原理可推导结论。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且为跨模型外推的经验性估计，非数学/物理定律推论）

## Search Query

Qwen3-27B INT8 quantization GSM8K accuracy drop benchmark
