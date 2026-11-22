# N57: Qwen3-27B 在 BF16 精度下的代码生成基准测试分数（如 HumanEval/MBPP，具体数值需检索，作为代码能力基准线）

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

Qwen3-27B 在 BF16 精度下的代码生成基准测试分数（如 HumanEval/MBPP，具体数值需检索，作为代码能力基准线）

## Corrected Claim

Qwen3-27B 在 BF16 精度下具有前沿模型级的代码生成能力（HumanEval 表现优异），但具体基准测试分数未在参考来源中明确给出。

## Evidence

[质询]参考来源[1]讨论的是吞吐量/延迟性能而非代码生成基准分数；来源[2]仅定性描述'编程效果'和'超越同级'，未提供HumanEval/MBPP的具体数值，无法支撑'具体数值需检索'这一事实节点的核心需求。 | 来源[2]间接支持Qwen3-27B具备较强的代码生成能力（提及HumanEval测试维度），但未提供具体分数，属于间接支持且缺乏量化数据。

## Search Query

Qwen3-27B BF16 HumanEval MBPP code benchmark

## Retrieval Sources

- {'url': 'https://devpress.csdn.net/v1/article/detail/141946772&rut=7aae2ac515b2d8496787d3262e190159eac55c7fb3ba5e9d4de1f8edb620e8de', 'type': 'ddg', 'title': 'Qwen3.6-27B-AEON-Ultimate-Uncensored-BF16性能测试：在A100/H100上的吞吐量与延迟基准'}
- {'url': 'https://www.kongchang.com/articles/qwen3-27bben-di-shi-ce-16gxian-cun-pao-chu-ding-ji-xiao-guo&rut=6191f3e778d5ced81232a1e4e16cf2a499b03e593ccd358e0cb06113f745153d', 'type': 'ddg', 'title': 'Qwen3 27B本地部署实测：16G显存跑出前沿模型级编程效果 - 控场AI'}
