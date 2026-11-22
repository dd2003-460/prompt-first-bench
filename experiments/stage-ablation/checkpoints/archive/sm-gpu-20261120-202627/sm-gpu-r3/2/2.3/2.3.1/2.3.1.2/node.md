# N220: Qwen3-27B 使用 GPTQ 算法 (group_size=128, 校准集大小=512) 进行 INT8 量化后的 WikiText-2 或 C4 困惑

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N55

## Claim

Qwen3-27B 使用 GPTQ 算法 (group_size=128, 校准集大小=512) 进行 INT8 量化后的 WikiText-2 或 C4 困惑度具体数值（需引用 HuggingFace AutoGPTQ 或 GPTQModel 库的官方测试报告）

## Corrected Claim

Qwen3-27B 使用 GPTQ 算法 (group_size=128, 校准集大小=512) 进行 INT8 量化后的 WikiText-2 或 C4 困惑度具体数值未在 HuggingFace AutoGPTQ 或 GPTQModel 库的官方测试报告中公开，需通过自行运行量化评估获取。

## Evidence

[质询]该陈述要求提供特定模型（Qwen3-27B）在特定量化配置（GPTQ, INT8, group_size=128, calib=512）下的具体困惑度数值，并指定引用来源为 HuggingFace AutoGPTQ 或 GPTQModel 的官方测试报告。然而，Qwen3 系列模型（包括 27B 版本）在主流公开基准测试中通常以 FP16/BF16 或 AWQ/GPTQ INT4 形式发布，官方极少提供 INT8 GPTQ 量化后的具体困惑度数值，且 AutoGPTQ/GPTQModel 库本身不维护针对特定第三方大模型（如 Qwen3-27B）的官方量化后性能测试报告。因此，该具体数值极可能不存在于指定的官方来源中，属于无法验证的经验事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且指定来源通常不包含此类特定量化配置的具体数值）

## Search Query

Qwen3-27B GPTQ INT8 group_size 128 perplexity benchmark HuggingFace
