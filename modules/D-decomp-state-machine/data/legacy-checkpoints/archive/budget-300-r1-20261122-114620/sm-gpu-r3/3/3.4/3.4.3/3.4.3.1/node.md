# N302: 4-bit 量化下 KV Cache 的精度损失量化：当 KV Cache 采用 INT8 存储时，长上下文 (>8K tokens) 场景下注意力机制的累积误

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N97

## Claim

4-bit 量化下 KV Cache 的精度损失量化：当 KV Cache 采用 INT8 存储时，长上下文 (>8K tokens) 场景下注意力机制的累积误差导致最终生成序列的 Bit Error Rate (BER) 或困惑度增加通常比短上下文 (<2K tokens) 高 2-5 倍，具体系数取决于序列长度与头数的乘积。

## Corrected Claim

4-bit 量化下 KV Cache 的精度损失：当 KV Cache 采用低精度（如 INT8 或 INT4）存储时，长上下文场景下注意力机制的累积误差通常会导致最终生成序列的困惑度（Perplexity）或任务准确率下降幅度大于短上下文场景，具体影响程度取决于序列长度、头数及量化算法。

## Evidence

[质询]该陈述包含具体的经验性数值范围（2-5倍）和特定的因果机制（累积误差导致BER/困惑度增加），这属于经验事实而非第一性原理可推导的数学或物理定律。此外，'Bit Error Rate'通常用于通信信道或存储介质，用于描述生成序列的语义错误（通常用困惑度或任务准确率衡量）在术语使用上存在混淆，且具体倍数缺乏通用理论支持，高度依赖于模型架构、量化算法（如SmoothQuant, GPTQ）及具体数据集。 | 经验事实，逻辑自洽但缺来源支持；术语'BER'用于生成序列略显不当，且具体倍数无通用理论依据，故降级。
