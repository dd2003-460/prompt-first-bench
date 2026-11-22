# N368: Qwen3-27B 的 hidden_size 确切值为 4096，依据 HuggingFace 官方仓库 Qwen/Qwen3-27B 的 config.js

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N130, N131, N132

## Claim

Qwen3-27B 的 hidden_size 确切值为 4096，依据 HuggingFace 官方仓库 Qwen/Qwen3-27B 的 config.json 文件。

## Corrected Claim

Qwen3-27B 的 hidden_size 确切值为 4096，依据 HuggingFace 官方仓库 Qwen/Qwen3-27B 的 config.json 文件（需进一步核实具体数值）

## Evidence

[质询]参考来源[1]讨论的是 Qwen3.6-27B 而非 Qwen3-27B，且未直接提供 config.json 中 hidden_size 的具体数值，仅凭该来源无法直接证实 Qwen3-27B 的 hidden_size 为 4096。 | 经验事实，逻辑自洽但缺来源支持（来源[1]主题相关但未直接提供 hidden_size 数值，且模型版本存在差异）

## Search Query

Qwen3-27B config.json hidden_size

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2071169496807650145&rut=8521ff63c2644888afeeb65b991dce4ce32450ffb032f96c2145a8e87320cc5f', 'type': 'ddg', 'title': 'Qwen 3.8 前夕最后一测：27B 稠密模型 MTP 推测解码在 4090 上的完整数据'}
