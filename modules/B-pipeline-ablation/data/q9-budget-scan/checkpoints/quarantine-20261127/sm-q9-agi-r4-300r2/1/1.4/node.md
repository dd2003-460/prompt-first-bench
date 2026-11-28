# N9: MTP×4 投机解码加速比受接受率限制：在复杂科研推理任务中，草稿模型与主模型分布差异大，接受率 η 预计降至 0.4-0.6 (低于代码补全场景的 0.8+)

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N1

## Claim

MTP×4 投机解码加速比受接受率限制：在复杂科研推理任务中，草稿模型与主模型分布差异大，接受率 η 预计降至 0.4-0.6 (低于代码补全场景的 0.8+)。有效加速比 S = 1 + η * k，其中 k=4，故 S ∈ [2.6, 3.4]。若接受率 < 0.3，MTP 反而因验证开销降低吞吐，需动态禁用机制。

## Corrected Claim

MTP×4 投机解码加速比受接受率限制，理论上 S = 1 + η * 4。在复杂科研推理任务中，由于分布差异，接受率通常低于代码补全场景，导致实际加速比受限；若接受率过低（如 < 0.3），验证开销可能抵消收益，需动态调整。

## Evidence

[质询]接受率 η 的具体数值范围（0.4-0.6 vs 0.8+）及加速比区间属于特定实验条件下的经验数据，缺乏通用性，且参考来源摘要未提供具体数值支持，存在将特定场景数据泛化的风险。 | 逻辑推导自洽（S=1+ηk 计算正确），但参考来源 [1] 仅介绍 MTP 方法，未提供具体接受率数值或加速比实证数据，属于经验事实且缺乏直接来源支持。

## Search Query

multi-token prediction speculative decoding acceptance rate complex reasoning tasks vLLM

## Retrieval Sources

- {'url': 'https://arxiv.org/abs/2611.25813&rut=3d906509c1e3f49c86c5924b72485f52f3df6a2fc68928d6d6f1ebe3eab4e3f5', 'type': 'ddg', 'title': 'Efficient and Robust Drafting with Multi-Token Prediction'}
