# N297: Qwen3-27B 在无校准 (Calibration-free) INT8 量化策略下，由于缺乏分布自适应缩放因子，MMLU 数学子集准确率相比 BF16 下

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N94

## Claim

Qwen3-27B 在无校准 (Calibration-free) INT8 量化策略下，由于缺乏分布自适应缩放因子，MMLU 数学子集准确率相比 BF16 下降幅度通常 >5 个百分点（例如从 70% 降至 <65%），远超 N99 定义的 3% 相对或 2% 绝对阈值。

## Corrected Claim

Qwen3-27B 在无校准 (Calibration-free) INT8 量化策略下，由于缺乏分布自适应缩放因子，MMLU 数学子集准确率相比 BF16 可能出现显著下降，具体幅度需依据实际基准测试结果确定，但通常预期会超过常见的 3% 相对或 2% 绝对阈值。

## Evidence

[质询]该陈述包含具体的经验性数值断言（MMLU数学子集准确率下降>5个百分点，从70%降至<65%），这属于特定模型在特定量化策略下的经验事实，无法从第一性原理推导。此外，'通常'一词暗示了普遍性，但缺乏大规模基准测试数据支持这一具体量级的下降幅度，且不同量化实现（如SmoothQuant, GPTQ等）的效果可能存在差异，单一数值断言可能过于绝对。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且该具体数值断言无法从第一性原理推出，符合经验事实排除条款，故降级为degraded）

## Search Query

Qwen3-27B calibration-free INT8 quantization MMLU math subset accuracy drop
