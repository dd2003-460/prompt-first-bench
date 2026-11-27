# N165: Qwen3-27B 使用 SmoothQuant 算法进行 INT8 量化后的 MMLU 分数需检索 NVIDIA TensorRT-LLM 或 SmoothQ

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N49

## Claim

Qwen3-27B 使用 SmoothQuant 算法进行 INT8 量化后的 MMLU 分数需检索 NVIDIA TensorRT-LLM 或 SmoothQuant 官方 GitHub 仓库的 Issue 讨论区，或查找针对 Qwen 系列模型 SmoothQuant 适配的社区博客（如 HuggingFace Blog 或 Medium 文章），以获取实测 MMLU 分数。

## Corrected Claim

Qwen3-27B 使用 SmoothQuant 算法进行 INT8 量化后的 MMLU 分数需查阅 NVIDIA TensorRT-LLM 或 SmoothQuant 官方文档及社区实测报告以获取具体数值。

## Evidence

[质询]该陈述是一个‘行动建议’而非‘事实结论’，且未提供具体的MMLU分数数值。作为事实节点，它缺乏可验证的具体数据支撑，仅指出了检索路径，属于经验性操作指南而非客观事实陈述。 | 来源未覆盖（检索失败）。该陈述逻辑自洽（SmoothQuant确实常用于LLM量化，MMLU是标准评测集），但作为经验事实/操作建议，缺乏具体数值或来源直接支持其‘需检索...以获取实测分数’这一特定路径的唯一性或准确性，且未给出实际分数，故降级。

## Search Query

Qwen3-27B SmoothQuant INT8 MMLU score tensorrt-llm
