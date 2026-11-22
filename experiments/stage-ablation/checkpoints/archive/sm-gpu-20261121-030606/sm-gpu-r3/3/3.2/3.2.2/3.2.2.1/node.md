# N257: Qwen3-27B在BF16精度下的GSM8K基准得分需从Hugging Face官方模型卡或Qwen3技术报告中获取确切数值（当前假设为82.0%，标记为[待

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N112

## Claim

Qwen3-27B在BF16精度下的GSM8K基准得分需从Hugging Face官方模型卡或Qwen3技术报告中获取确切数值（当前假设为82.0%，标记为[待核验]），该数值是计算FP8质量损失绝对值及判断是否满足业务阈值的基准锚点。

## Corrected Claim

Qwen3-27B在BF16精度下的GSM8K基准得分需从Hugging Face官方模型卡或Qwen3技术报告中获取确切数值（当前假设为82.0%，标记为[待核验]），该数值是计算FP8质量损失绝对值及判断是否满足业务阈值的基准锚点。

## Evidence

[质询]参考来源[1]仅涉及Qwen3-8B模型，与Qwen3-27B无关，无法提供GSM8K基准得分的直接证据；且82.0%为假设值，缺乏权威来源（如Hugging Face官方模型卡或技术报告）的直接支持。 | 经验事实，逻辑自洽但缺来源支持（来源[1]不相关）

## Search Query

Qwen3-27B GSM8K benchmark score BF16 official technical report

## Retrieval Sources

- {'url': 'https://huggingface.co/Qwen/Qwen3-8B&rut=1ce670a2e9c4b69e3e7b523a812604aebf772a5bc377db7e620e9ebca234040a', 'type': 'ddg', 'title': 'Qwen/Qwen3-8B · Hugging Face'}
