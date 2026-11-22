# N212: Qwen3-27B 在 BF16 精度下 GSM8K 评测的具体配置参数：max_new_tokens（通常设为 512 或 1024 以容纳思维链）、temp

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

Qwen3-27B 在 BF16 精度下 GSM8K 评测的具体配置参数：max_new_tokens（通常设为 512 或 1024 以容纳思维链）、temperature（通常 0 或 0.7，需确认官方基准是否使用 greedy decoding）、top_p（1.0 或 0.95），这些参数直接决定分数可比性

## Corrected Claim

Qwen3-27B 在 BF16 精度下 GSM8K 评测的具体配置参数（如 max_new_tokens、temperature、top_p）需参照官方技术报告或基准测试代码确认，不同解码策略（greedy vs sampling）及思维链提示词的使用会直接影响分数可比性，不宜仅凭通用默认值断定。

## Evidence

[质询]该陈述将具体的超参数（如 max_new_tokens=512/1024, temperature=0/0.7）描述为‘通常’或‘需确认’的固定配置，但 Qwen3 系列（特别是 27B 级别）在 GSM8K 等数学基准上的官方评测往往依赖于特定的推理框架（如 vLLM 或 SGLang）及特定的解码策略（如 greedy 或 beam search），且不同版本（Instruct vs Base）及是否启用思维链（CoT）提示词会显著改变这些参数的实际取值。将‘通常’值断定为决定分数可比性的唯一具体配置，忽略了官方基准测试中可能存在的特定采样参数（如 top_k）或动态长度限制，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体超参数属于经验事实，无法从第一性原理严格推出，故降级）

## Search Query

Qwen3 GSM8K evaluation config max_new_tokens temperature
