# N196: INT8 量化相比 BF16 在 GPQA 上的准确率绝对下降值 (ΔGPQA_INT8)，用于与 NVFP4 进行同口径对比，预期范围 0.5%-1.5% [

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N59

## Claim

INT8 量化相比 BF16 在 GPQA 上的准确率绝对下降值 (ΔGPQA_INT8)，用于与 NVFP4 进行同口径对比，预期范围 0.5%-1.5% [待核验]

## Corrected Claim

在主流大语言模型（如Llama-3系列）的INT8量化实践中，GPQA准确率相比BF16通常呈现小幅下降，具体数值取决于模型规模与量化方法，常见范围约为0.5%-1.5%，需结合具体模型基准测试确认。

## Evidence

[质询]该数值属于特定模型（如Llama-3-70B等）在特定量化方案下的经验测量值，不同模型架构、参数量及量化算法（如GPTQ, AWQ, SmoothQuant）会导致INT8与BF16的精度差异波动较大，0.5%-1.5%并非普适的物理或数学常数，且缺乏具体模型上下文，存在以偏概全的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数值为特定硬件/模型配置下的经验数据，不适用第一性原理推导条款）

## Search Query

Qwen3-27B INT8 quantization GPQA accuracy drop comparison BF16
