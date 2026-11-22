# N95: 数学推理任务（GSM8K/MATH）的质量损失阈值：Qwen3-27B 从 BF16 降至 FP8 时，准确率下降通常 < 0.5%；降至 INT4 时，准确率

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14

## Claim

数学推理任务（GSM8K/MATH）的质量损失阈值：Qwen3-27B 从 BF16 降至 FP8 时，准确率下降通常 < 0.5%；降至 INT4 时，准确率下降通常在 2-4% 之间 [待核验]，若业务要求 GSM8K 准确率不低于 90%，则 INT4 需实测验证是否跌破底线。

## Corrected Claim

Qwen3-27B 从 BF16 降至 FP8 时，准确率下降通常较小；降至 INT4 时，准确率下降可能显著。若业务要求 GSM8K 准确率不低于 90%，INT4 需实测验证是否跌破底线。

## Evidence

[质询]参考来源均未涉及量化（FP8/INT4）对Qwen3-27B数学推理准确率的具体影响数值，且来源[1]评测的是Qwen3-30B-A3B而非27B，来源[2]是1.7B模型，无法直接支持该特定模型在特定量化下的具体损失阈值（<0.5%和2-4%）。 | 逻辑上量化精度降低导致性能下降符合直觉，但具体数值（<0.5%, 2-4%）属于经验事实，参考来源[1][2][3]均未提供Qwen3-27B在FP8/INT4下的GSM8K/MATH具体准确率对比数据，缺乏直接外部证据支持。

## Search Query

Qwen3-27B FP8 INT4 GSM8K MATH accuracy degradation

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00188/article/details/151731924&rut=d93487ec49ea823a36c6180dc146de8223d20832bddd3877dd499fb38a490c01', 'type': 'ddg', 'title': 'Qwen3-30B-A3B数学推理能力评测：GSM8K与MATH数据集表现分析-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_33773084/article/details/157501369&rut=432a2a32e32e71dc3e0ff20f5e187d29fa2609d36c7b02b24e72aaa5fbe6a4ad', 'type': 'ddg', 'title': 'Qwen3-1.7B数学推理测试，GSM8K表现亮眼 - CSDN博客'}
- {'url': 'https://www.cnblogs.com/tlnshuju/p/19138181&rut=3abe3e6387eba73f1b351b30c297f5c594eb8920e683a8c880a3fd28cb4c41ef', 'type': 'ddg', 'title': '完整教程：GSM8K：评估大模型数学推理能力的关键数据集 - tlnshuju - 博客园'}
