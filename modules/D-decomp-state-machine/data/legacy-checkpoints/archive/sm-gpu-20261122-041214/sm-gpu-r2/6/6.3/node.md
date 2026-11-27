# N153: 量化质量损失的非线性边界：当模型规模从 7B 增加到 27B 时，INT8 量化损失从 ~1.5% 降至 ~0.7%，而 W4A16 损失从 ~5% 降至 ~3

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N44

## Claim

量化质量损失的非线性边界：当模型规模从 7B 增加到 27B 时，INT8 量化损失从 ~1.5% 降至 ~0.7%，而 W4A16 损失从 ~5% 降至 ~3.3%；这表明 27B 规模已处于量化鲁棒性的“安全区”，但若上下文长度超过 32K，长序列累积误差可能导致实际任务表现比短序列基准测试再下降 0.5-1%，需在实际长文本任务中验证。

## Corrected Claim

量化质量损失通常随模型规模增大而降低，大模型（如27B+）在INT8和W4A16量化下通常表现出更高的鲁棒性；但在超长上下文（>32K）场景下，量化误差可能累积，导致实际任务表现低于短序列基准测试，具体损失幅度需根据特定模型和任务进行实测验证。

## Evidence

[质询]具体数值（如7B INT8损失~1.5%、27B W4A16损失~3.3%）属于特定实验条件下的经验数据，不同模型架构、数据集及量化算法（如GPTQ, AWQ, SmoothQuant）会导致结果显著差异，缺乏通用性；此外，长序列累积误差导致额外下降0.5-1%的断言缺乏普遍适用的理论或广泛共识支持，可能过度泛化。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

LLM quantization error accumulation long context length 32K tokens impact accuracy
