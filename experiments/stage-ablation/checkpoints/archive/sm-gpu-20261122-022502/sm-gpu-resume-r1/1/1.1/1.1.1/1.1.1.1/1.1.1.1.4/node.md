# N369: Qwen3-27B 的 intermediate_size 确切值为 11008，依据 HuggingFace 官方仓库 Qwen/Qwen3-27B 的 co

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N130, N131, N132

## Claim

Qwen3-27B 的 intermediate_size 确切值为 11008，依据 HuggingFace 官方仓库 Qwen/Qwen3-27B 的 config.json 文件。

## Corrected Claim

Qwen3-27B 的 intermediate_size 确切值为 11008（需查阅 HuggingFace 官方仓库 Qwen/Qwen3-27B 的 config.json 确认，当前参考来源未覆盖该具体模型）。

## Evidence

[质询]参考来源均针对 Qwen3-30B-A3B 模型，未提供 Qwen3-27B 的具体配置数据，无法直接验证 11008 这一数值；且 27B 与 30B-A3B 架构不同，不能直接类比。 | 经验事实，逻辑自洽但缺来源支持（来源[1][3]讨论的是Qwen3-30B-A3B，与Qwen3-27B无关）

## Search Query

Qwen3-27B config.json intermediate_size

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00897/article/details/151735347&rut=bdb3cb8fc30287c0e39d606be7fe3fd60593d6a66a399112523470d6a5f3bbe6', 'type': 'ddg', 'title': 'Qwen3-30B-A3B参数配置指南：hidden_size与intermediate_size最佳实践-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_30694389/article/details/171149906&rut=c4b577297602702dbd6b6067c596c86ffd505b92fd3a5fad4dc08119fcb37ba5', 'type': 'ddg', 'title': 'Apple Silicon本地部署Qwen3.8四大翻车原因与MLX绕行方案-CSDN博客'}
- {'url': 'https://adg.csdn.net/69523cc05b9f5f31781b4004.html&rut=2999d46c3d0d0af37dfe17f581a5757d2c8add351cde1cefa9823c16e7a1f129', 'type': 'ddg', 'title': 'Qwen3-30B-A3B参数配置指南：hidden_size与intermediate_size最佳实践'}
