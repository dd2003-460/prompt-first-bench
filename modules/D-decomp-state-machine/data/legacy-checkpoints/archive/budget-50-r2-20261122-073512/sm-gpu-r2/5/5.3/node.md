# N30: 量化质量损失量化指标：‘质量损失可接受’需定义为具体基准测试分数下降阈值（如 MMLU 或 GSM8K 准确率下降 < 2%）；需检索 Qwen3-27B 在 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

量化质量损失量化指标：‘质量损失可接受’需定义为具体基准测试分数下降阈值（如 MMLU 或 GSM8K 准确率下降 < 2%）；需检索 Qwen3-27B 在 BF16 到 INT4/FP8 量化下的官方或社区评测数据（[待核验]：Qwen3 官方是否发布量化精度对比报告），若无数据，则引用同类 MoE/Dense 模型（如 Llama-3-70B）的量化退化曲线作为代理指标。

## Corrected Claim

量化质量损失需定义具体基准测试分数下降阈值（如MMLU或GSM8K准确率下降<2%）；需检索Qwen3-27B在BF16到INT4/FP8量化下的官方或社区评测数据，若无数据，则引用同类MoE/Dense模型（如Llama-3-70B）的量化退化曲线作为代理指标。

## Evidence

[质询]该陈述包含具体的经验性阈值（如MMLU/GSM8K下降<2%）和特定模型（Qwen3-27B）的量化数据需求，属于经验事实而非第一性原理可推导内容；且参考来源仅讨论通用评估方法论，未提供Qwen3-27B的具体量化精度对比数据或官方报告存在性证明，无法直接支持该具体事实节点。 | 逻辑自洽，但参考来源[1]仅涉及量化精度评估的通用方法论，未覆盖Qwen3-27B具体量化数据或官方报告情况，属于经验事实缺来源直接支持。

## Search Query

Qwen3-27B quantization accuracy loss MMLU GSM8K INT4 FP8 benchmark

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1995649267013018246&rut=b5b080612239b158466ceb63792e363943864715fcd6f2dece5c31aedcdfd188', 'type': 'ddg', 'title': '如何科学评估量化模型的精度 - 知乎'}
