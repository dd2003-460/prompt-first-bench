# N154: 针对高熵科研任务，将 MTP 草稿长度从默认值（如 4）降低至 2，可将接受率从 0.45 提升至 0.65，尽管总 token 生成步数增加，但综合延迟降低约

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N53

## Claim

针对高熵科研任务，将 MTP 草稿长度从默认值（如 4）降低至 2，可将接受率从 0.45 提升至 0.65，尽管总 token 生成步数增加，但综合延迟降低约 12%。

## Corrected Claim

针对高熵科研任务，适当降低MTP草稿长度（如从4降至2）通常能提升token接受率并优化综合延迟，但具体提升幅度（如接受率升至0.65、延迟降低12%）需根据实际模型与负载实测确定。

## Evidence

[质询]具体数值（接受率0.45->0.65，延迟降低12%）缺乏来源支持，且不同模型/负载下MTP参数调优效果差异巨大，该特定量化结论可能源自特定实验而非通用规律。 | 来源[1]仅提及MTP配置及硬件适配，未提供高熵任务下草稿长度调整的具体接受率与延迟数据，属经验事实且缺直接来源支持。

## Search Query

speculative decoding draft length tuning high entropy tasks acceptance rate

## Retrieval Sources

- {'url': 'https://wenku.baidu.com/view/a51290f155e79b89680203d8ce2f0066f533649d.html&rut=40513086cd6a1b15becff9102232d5f80f4c7dcc0cc0dd9ff7fb0e79e253bb3d', 'type': 'ddg', 'title': 'Qwen3.8 27B MTP优化实操指南：推理速度提升2.69倍的配置方法'}
