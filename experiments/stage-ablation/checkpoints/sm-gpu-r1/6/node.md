# N27: 量化质量损失量化基准：针对Qwen3-27B，需使用MMLU-Pro或GSM8K数据集，对比BF16基准模型与INT4/FP8量化模型的准确率差异；若INT4导

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

量化质量损失量化基准：针对Qwen3-27B，需使用MMLU-Pro或GSM8K数据集，对比BF16基准模型与INT4/FP8量化模型的准确率差异；若INT4导致GSM8K准确率下降超过5%或MMLU-Pro下降超过3%，则判定质量损失不可接受，必须升级至FP8/INT8精度。

## Corrected Claim

针对Qwen3-27B，需使用MMLU-Pro或GSM8K数据集，对比BF16基准模型与INT4/FP8量化模型的准确率差异；若INT4导致GSM8K或MMLU-Pro准确率出现显著下降（具体阈值需根据业务容忍度设定，通常参考行业经验值），则需评估是否升级至FP8/INT8精度。

## Evidence

[质询]该陈述中的具体阈值（GSM8K下降>5%或MMLU-Pro下降>3%即判定不可接受）属于经验性工程规范，并非行业通用的绝对标准，且参考来源仅提供了特定量化模型（W4A16 AutoRound, GGUF）的评测数据，并未提供该特定阈值作为通用判定标准的直接依据或行业共识证明。 | 来源[1]和[2]证实了使用MMLU-Pro和GSM8K评估Qwen3-27B系列量化模型是合理的实践（间接支持方法论），但未直接支持具体的5%/3%阈值标准，属于经验事实且缺乏直接来源支持。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00989/article/details/170458404&rut=306b11aff0fb16a744af9e06a32e141331d86b3faacd7d26de2e66c51daad6f0', 'type': 'ddg', 'title': '量化真的零损失吗？Qwen3.8-27B-W4A16-AutoRound 的 GSM8K/HumanEval/MMLU-Pro 评测数据深度 ...'}
- {'url': 'https://blog.csdn.net/gitblog_00688/article/details/152594884&rut=1db48303b05c71547dfa18e7e1c16b29c221f8ce934e51a239e5cffefb92d074', 'type': 'ddg', 'title': '数据说话：Qwen3.8-27B-Uncensored-GGUF 基准评测全解读（MMLU、GSM8K 与安全测试）'}
