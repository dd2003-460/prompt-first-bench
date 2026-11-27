# N163: Qwen3-27B 使用 GPTQ 算法进行 INT8 量化（校准集大小 1024）后的 MMLU 分数需检索 HuggingFace AutoGPTQ 或 A

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N48

## Claim

Qwen3-27B 使用 GPTQ 算法进行 INT8 量化（校准集大小 1024）后的 MMLU 分数需检索 HuggingFace AutoGPTQ 或 AutoAWQ 社区发布的 Qwen3-27B-Int8 模型卡片，或查找 arXiv 上针对 Qwen3 的量化误差分析论文（如 'Quantization Error Analysis of Large Language Models'），以获取实测 MMLU 分数。

## Corrected Claim

Qwen3-27B 使用 GPTQ 算法进行 INT8 量化后的 MMLU 分数需通过实际量化并运行基准测试获取，或查阅最新发布的量化模型卡片及论文，目前公开渠道可能缺乏现成的标准实测数据。

## Evidence

[质询]该陈述是一个‘行动指令’而非‘事实结论’，且其隐含的前提（即存在现成的、可直接获取MMLU分数的Qwen3-27B-Int8模型卡片或特定论文）可能不成立。Qwen3-27B是较新的模型，社区可能尚未发布标准的GPTQ INT8量化版本及其对应的MMLU基准测试数据，或者该数据并未以陈述中描述的特定形式（如AutoGPTQ卡片）广泛存在。 | 来源未覆盖（检索失败）。该陈述逻辑上自洽（作为获取数据的建议是合理的），但属于经验事实范畴（具体模型是否存在、数据是否可得），且无外部来源支持其前提的真实性，故降级。

## Search Query

Qwen3-27B GPTQ INT8 quantization MMLU score huggingface
