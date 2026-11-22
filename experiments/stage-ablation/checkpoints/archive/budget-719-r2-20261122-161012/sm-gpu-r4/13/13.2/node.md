# N315: Qwen3-27B 在 INT4 (AWQ) 量化后的 HumanEval Pass@1 实测得分为 [待核验: 需查量化模型卡或第三方评测]，计算其相对 BF

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N136

## Claim

Qwen3-27B 在 INT4 (AWQ) 量化后的 HumanEval Pass@1 实测得分为 [待核验: 需查量化模型卡或第三方评测]，计算其相对 BF16 的绝对下降量 ΔPass@1；若 ΔPass@1 > 5%，则判定代码生成任务中 INT4 不可接受，必须排除 INT4 硬件方案 (如仅靠 INT4 才能跑下的单卡 4090)。

## Corrected Claim

Qwen3-27B 在 INT4 (AWQ) 量化后的 HumanEval Pass@1 实测得分需查阅具体模型卡或第三方评测报告以获取确切数值，进而计算相对 BF16 的绝对下降量 ΔPass@1；若 ΔPass@1 > 5%，则判定代码生成任务中 INT4 不可接受。

## Evidence

[质询]参考来源[1]仅提供了模型仓库链接，未包含具体的HumanEval Pass@1实测数值，无法直接验证ΔPass@1是否大于5%这一具体经验事实；且模型名称存在版本混淆风险（Qwen3 vs Qwen3.6）。 | 逻辑自洽，但参考来源[1]仅指向模型卡，未提供具体评测数据，属于经验事实且缺乏直接数值支持，故降级。

## Search Query

Qwen3-27B AWQ INT4 HumanEval Pass@1 drop evaluation

## Retrieval Sources

- {'url': 'https://huggingface.co/drawais/Qwen3.6-27B-AWQ-INT4&rut=c56e77d74a9087f6e6e5b25bd74ca49d12d1debc5cd4d783d04b81935ff5307a', 'type': 'ddg', 'title': 'drawais/Qwen3.6-27B-AWQ-INT4 · Hugging Face'}
