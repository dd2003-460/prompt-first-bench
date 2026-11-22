# N147: Qwen3-27B 在 GSM8K 数学推理任务中，AWQ-INT4 量化后的 Pass@1 准确率相比 BF16 基线下降幅度具体为 1.8%（基于 7B-7

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54

## Claim

Qwen3-27B 在 GSM8K 数学推理任务中，AWQ-INT4 量化后的 Pass@1 准确率相比 BF16 基线下降幅度具体为 1.8%（基于 7B-70B 模型量化敏感性曲线外推，需实测核验）

## Corrected Claim

Qwen3-27B 在 GSM8K 数学推理任务中，AWQ-INT4 量化后的 Pass@1 准确率相比 BF16 基线下降幅度约为 2.3%（基于来源[2]实测恢复率97.7%推算）。

## Evidence

[质询]陈述声称下降幅度为1.8%，但参考来源[2]显示AWQ-INT4量化后的GSM8K恢复率为97.7%，意味着下降幅度约为2.3%（100% - 97.7%），与1.8%存在显著数值差异；且来源[1]和[3]分别涉及AutoRound和NVFP4量化，与AWQ-INT4不完全一致，无法直接支持1.8%这一具体数值。 | 来源[2]直接测试了Qwen3.8-27B AWQ-INT4在GSM8K上的表现，恢复率为97.7%（即损失约2.3%），与陈述中的1.8%下降幅度矛盾；其他来源涉及不同量化方法，无法支持该具体数值。

## Search Query

Qwen3-27B INT4 GSM8K Pass@1 accuracy degradation

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00989/article/details/170458404&rut=f06d326da382b9eb44829c84ba46726f32fbe2f7ffe91362b18793edad016c5b', 'type': 'ddg', 'title': '量化真的零损失吗？Qwen3.8-27B-W4A16-AutoRound 的 GSM8K/HumanEval/MMLU-Pro 评测数据深度 ...'}
- {'url': 'https://blog.csdn.net/gitblog_00887/article/details/168443952&rut=c3b7b31e370c638c409246611c2c6dd79951dd8acab18a707e840823b6d8b7b5', 'type': 'ddg', 'title': 'Qwen3.8-27B-Quark-AWQ-INT4-W4A16基准实测：GSM8K恢复率97.7%，INT4量化真实损失有多大？'}
- {'url': 'https://blog.gitcode.com/1a111ab8e09a688e2827a5b1ce93ebf9.html&rut=c7f6e7424980384ab77a353f77a62b1f2d6c48777ec4e52ce1cacc7009a74d8b', 'type': 'ddg', 'title': 'Qwen3.8-27B-NVFP4基准测试全解析：量化后GSM8K 97.27%的准确率从何而来？'}
