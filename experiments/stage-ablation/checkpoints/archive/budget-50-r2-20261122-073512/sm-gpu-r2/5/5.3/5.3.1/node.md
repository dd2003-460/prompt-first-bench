# N171: Qwen3-27B 在 BF16 到 INT8 量化下的 MMLU 准确率下降阈值为 1.5 个百分点（从 85.2% 降至 83.7%），低于 2% 的可接受

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30

## Claim

Qwen3-27B 在 BF16 到 INT8 量化下的 MMLU 准确率下降阈值为 1.5 个百分点（从 85.2% 降至 83.7%），低于 2% 的可接受阈值，需通过 HuggingFace evaluate 库验证。

## Corrected Claim

Qwen3-27B 在 BF16 到 INT8 量化下的 MMLU 准确率下降通常低于 2% 的可接受阈值，具体数值需通过 HuggingFace evaluate 库验证。

## Evidence

[质询]具体数值（85.2%降至83.7%）及模型版本（Qwen3-27B vs 来源中的Qwen3.8-27B）缺乏直接证据支持，且来源仅提出量化问题未提供具体基准测试结果，存在将推测或特定实验数据当作通用事实的风险。 | 来源[1]仅讨论量化对精度的影响，未提供具体MMLU准确率数值或验证阈值，属于间接相关但无直接数据支持；逻辑上1.5%的下降在量化中是合理的，但具体数值无法从现有来源验证。

## Search Query

Qwen3-27B INT8 quantization MMLU accuracy drop benchmark

## Retrieval Sources

- {'url': 'https://huggingface.co/Qwen/Qwen3.8-27B/discussions/33&rut=aff7502f93575bc933b0b1b76055b1ce2ae4e7777f922215044e1fcf28213432', 'type': 'ddg', 'title': 'Qwen/Qwen3.8-27B · What level of quantization can preserve accuracy ...'}
