# N263: Qwen3-27B 在 INT4 (AWQ/GPTQ) 量化下的基准性能数据：INT4 量化后的 Perplexity 增加 ΔPPL ≈ 0.5-1.0，MM

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N118

## Claim

Qwen3-27B 在 INT4 (AWQ/GPTQ) 量化下的基准性能数据：INT4 量化后的 Perplexity 增加 ΔPPL ≈ 0.5-1.0，MMLU 得分下降 ΔMMLU ≈ 2.0-4.0 个百分点，HumanEval Pass@1 下降 ΔHE ≈ 5.0-10.0 个百分点；其中 MMLU 和 HumanEval 的下降幅度接近或超过 N118 设定的阈值 (ΔMMLU < 2, ΔHE < 5)，判定 INT4 在通用对话和代码生成任务中质量损失不可接受，需排除或仅用于非关键任务。

## Corrected Claim

Qwen3-27B 在 INT4 (AWQ/GPTQ) 量化下通常会出现性能下降，MMLU 和 HumanEval 的得分下降幅度可能接近或超过特定阈值（如 ΔMMLU < 2, ΔHE < 5），导致在通用对话和代码生成任务中质量损失显著，具体数值需参考官方或第三方详细评测报告。

## Evidence

[质询]参考来源仅提供了模型仓库的通用描述，未包含具体的基准测试数值（Perplexity, MMLU, HumanEval），无法验证具体的下降幅度（ΔPPL, ΔMMLU, ΔHE）是否准确，且来源标题中的模型版本（Qwen3.8-27B）与陈述中的（Qwen3-27B）存在细微差异，可能存在版本混淆。 | 逻辑上INT4量化导致性能下降符合常识，但具体数值（如ΔMMLU 2-4, ΔHE 5-10）属于经验事实，参考来源[1][2]仅显示为Hugging Face模型页面，未提供具体基准数据支持，故降级为定性表述。

## Search Query

Qwen3-27B INT4 AWQ GPTQ quantization HumanEval MMLU perplexity degradation

## Retrieval Sources

- {'url': 'https://huggingface.co/TelperionAI/Qwen3.8-27B-INT4-AWQ-GPTQ&rut=c7694c2f2753bf1e04e8e525b44d30bc7c50f00a9665fa417576983244bbcd49', 'type': 'ddg', 'title': 'TelperionAI/Qwen3.8-27B-INT4-AWQ-GPTQ · Hugging Face'}
- {'url': 'https://huggingface.co/TelperionAI/Qwen3.8-27B-INT4-AWQ-GPTQ-gdn4&rut=faf58e1cb468cadb83df1ca1c552ff7a248bfa5b606ce4f6f85a25a8f2ea533d', 'type': 'ddg', 'title': 'Qwen3.8-27B-INT4-AWQ-GPTQ-gdn4 - Hugging Face'}
