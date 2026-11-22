# N474: Qwen3-27B BF16 基线在 HumanEval 上的 Pass@1 准确率为 60.1% (来源：Qwen3 官方技术报告或 CodeLlama 对比

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N147

## Claim

Qwen3-27B BF16 基线在 HumanEval 上的 Pass@1 准确率为 60.1% (来源：Qwen3 官方技术报告或 CodeLlama 对比基准，需核验)。

## Corrected Claim

Qwen3-27B BF16 基线在 HumanEval 上的 Pass@1 准确率约为 60% 左右（具体数值需依据官方技术报告确认，参考来源显示 Qwen 3.6/3.8 27B 版本在该基准上有相关评测数据）。

## Evidence

[质询]参考来源均指向 Qwen 3.6 或 3.8 版本，未直接提供 Qwen3-27B（通常指 Qwen3 系列首发或特定版本）在 HumanEval 上 60.1% 这一具体数值的直接证据，存在版本混淆或数据缺失风险。 | 来源 [1] 和 [3] 涉及 Qwen 27B 系列在 HumanEval 上的评测，但分别针对 Qwen 3.6 和 3.8 版本，未直接证实 Qwen3-27B 基线为 60.1%；该数值属于经验事实，逻辑上合理（27B 模型在 HumanEval 上通常表现优于 70B 以下小模型，60% 左右符合量级），但缺乏直接来源支持，故降级。

## Search Query

Qwen3-27B HumanEval Pass@1 BF16 accuracy

## Retrieval Sources

- {'url': 'https://www.heyneo.com/blog/evaluating-qwen-3-6-27b-benchmarking-case-study&rut=571a544cb81258e236fa2b0edcef46fd8229258b797ad38077042d55b58b7306', 'type': 'ddg', 'title': 'Evaluating Qwen 3.6 27B: A Complete Benchmarking Case Study'}
- {'url': 'https://blog.csdn.net/liangjinhu/article/details/164183862&rut=8d101b892bffb46b87003cdc8ef3a4d74fd9cad312ea5acd751e7c426bb2b5fe', 'type': 'ddg', 'title': 'Qwen3.8-27B GSQ-RCO 量化部署实测：9.3GB 跑出超 BF16 精度，消费级显卡落地 27B 多模态'}
- {'url': 'https://blog.csdn.net/gitblog_00989/article/details/170458404&rut=e04bb905daebdfb20f06bc7b9447fc485dd20902c182d3614a0133ce584f4182', 'type': 'ddg', 'title': '量化真的零损失吗？Qwen3.8-27B-W4A16-AutoRound 的 GSM8K/HumanEval/MMLU-Pro 评测数据深度 ...'}
