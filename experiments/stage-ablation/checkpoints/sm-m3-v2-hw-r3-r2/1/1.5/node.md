# N11: Qwen3.8-27B 在 HumanEval (代码生成) 和 MMLU-Pro (综合知识) 基准测试上的零样本准确率分别约为 78% 和 72%，但其在“

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

Qwen3.8-27B 在 HumanEval (代码生成) 和 MMLU-Pro (综合知识) 基准测试上的零样本准确率分别约为 78% 和 72%，但其在“多步逻辑推理链”任务（如 GSM8K 变体或 ARC-AGI 简化版）中的 CoT 成功率仅为 45-55%，显著低于前沿模型 (如 o1-preview) 的 85%+，这一差距构成了自主科研循环中“假设验证”步骤的硬性能力天花板，需通过外部工具补偿。

## Corrected Claim

Qwen3.8-27B 在 HumanEval 上的准确率约为 92.1%，MMLU 约为 84.1%，GSM8K 约为 96.1%。其性能表现优异，并未显示出陈述中所描述的‘显著低于前沿模型’的能力短板。

## Evidence

[质询]数值严重不符：参考来源显示 Qwen3.8-27B 系列模型在 HumanEval 上的得分约为 92.1%，MMLU 约为 84.1%，远高于陈述中的 78% 和 72%；此外，来源 [1] 指出 GSM8K 得分高达 96.1%，这与陈述中声称的 CoT 成功率仅 45-55% 存在巨大矛盾。 | 来源 [1] 和 [3] 直接提供数据表明 HumanEval 为 92.1%，MMLU 为 84.1%，GSM8K 为 96.1%，与陈述中的低分（78%/72%/45-55%）明确矛盾。

## Search Query

Qwen2.5 72B HumanEval MMLU accuracy multi-step reasoning failure rate

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00194/article/details/171189400&rut=aaa2e18dce2a9e640b43f1ac95adbc0a24312b16049ec1ebd1829c58765919f0', 'type': 'ddg', 'title': 'Qwen3.8-27B-pi-adapted-OptiQ-4bit基准测试报告解读：MMLU 84.1%与HumanEval 92.1%意味着 ...'}
- {'url': 'https://blog.csdn.net/gitblog_00989/article/details/170458404&rut=5759ae499e270ba978b576ac5ad4f7f2845f149932cdafa8f21482511ea23247', 'type': 'ddg', 'title': '量化真的零损失吗？Qwen3.8-27B-W4A16-AutoRound 的 GSM8K/HumanEval/MMLU-Pro 评测数据深度 ...'}
- {'url': 'https://blog.gitcode.com/bed0acc86146baeaac09b183394cd3a0.html&rut=2fb746cc73b035eb3687321f65d3fb7c73361ea394f76fbf4b65fc9b16b24f78', 'type': 'ddg', 'title': 'Qwen3.8-27B-pi-adapted-OptiQ-4bit基准测试报告解读：MMLU 84.1%与HumanEval 92.1%意味着 ...'}
