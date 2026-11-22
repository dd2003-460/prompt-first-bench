# N106: Qwen3-27B的GQA（Grouped Query Attention）配置：若头数（Head）为40，KV头数（KV Head）通常小于Query头数（如

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

Qwen3-27B的GQA（Grouped Query Attention）配置：若头数（Head）为40，KV头数（KV Head）通常小于Query头数（如10或16），则KV Cache计算中的'头数'应替换为'KV Head数'；若KV Head=10，则KV Cache显存 = 2 * 64 * 10 * 128 * 32768 * 2 bytes ≈ 2.68 GB，远低于非GQA的40GB。

## Corrected Claim

Qwen3-27B采用GQA机制，其KV Cache显存占用取决于具体的KV Head数配置（通常小于Query头数），相比非GQA（MHA）方案显存占用显著降低，具体数值需依据官方模型配置确认。

## Evidence

[质询]该陈述包含具体的硬件/模型配置参数（如Head=40, KV Head=10, 序列长度32768等），属于经验事实。参考来源[1]仅确认Qwen3系列（具体为30B-A3B）采用GQA机制，但未提供Qwen3-27B的具体头数配置或KV Cache显存计算数值，无法直接支持该具体数值结论。 | 逻辑推导自洽（GQA下KV Cache确实随KV Head数线性减少，量级估算合理），但来源[1]仅间接支持GQA机制的存在，未覆盖具体数值参数，符合经验事实降级条件。

## Search Query

Qwen3-27B architecture GQA kv head count specification config.json

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1905664754569185060&rut=996eead263dea3540db5dd80d1c2d089ec97a6079e18ef49b1c485c5cace2d64', 'type': 'ddg', 'title': '图解Qwen3混合专家模型推理过程--GQA和MoE - 知乎'}
