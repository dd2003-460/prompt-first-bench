# N40: Qwen3-27B 的参数量分布：总参数量 27B，其中 Dense 层参数量占比约 95% (25.65B)，Embedding 层参数量占比约 5% (1.

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

Qwen3-27B 的参数量分布：总参数量 27B，其中 Dense 层参数量占比约 95% (25.65B)，Embedding 层参数量占比约 5% (1.35B)，用于验证权重显存计算中是否包含 Embedding 矩阵

## Corrected Claim

Qwen3.8-27B（或 Qwen3-27B，视具体版本而定）的总参数量为 27B，其中 Dense 层约占 95%，Embedding 层约占 5%。具体拆分数值（25.65B/1.35B）需依据该特定版本的官方配置确认。

## Evidence

[质询]参考来源均指向 'Qwen3.8-27B'（或 Qwen3.8 系列），而事实节点声称的是 'Qwen3-27B'。虽然参数量 27B 一致，但不同版本（3.0 vs 3.8）的架构细节（如 Embedding 与 Dense 层的具体参数量分布）可能存在差异，且来源中未提供具体的 25.65B/1.35B 拆分数据，存在版本混淆或数据无直接来源支持的风险。 | 来源 [1][2][3] 确认存在 27B 参数的 Dense 模型，但均指代 Qwen3.8 版本，且未提供具体的层参数量拆分（25.65B/1.35B）；逻辑上 25.65+1.35=27 自洽，但作为经验事实缺乏直接来源支持具体数值，且存在版本名称不匹配（Qwen3 vs Qwen3.8）的潜在歧义。

## Search Query

Qwen3-27B parameter distribution dense embedding layers

## Retrieval Sources

- {'url': 'https://www.pongo.com.tw/qwen3-8-27b-hands-on/&rut=95074ced42951b0e21f3a0ae411357b678e9d7f4fb630633322b39255b6ef374', 'type': 'ddg', 'title': 'Qwen3.8 27B 開源模型一次看懂：規格、跑分到本地實測'}
- {'url': 'https://help.aliyun.com/zh/model-studio/qwen3-8-27b&rut=e255e88f541dd7e98ba29bb3128b9db57653b47bdddbe91b654467996d229204', 'type': 'ddg', 'title': 'qwen3.8-27b 模型信息-大模型服务平台百炼 (Model Studio)-阿里云帮助中心'}
- {'url': 'https://www.cnblogs.com/sing1ee/p/22498000&rut=e1a4a75338ea7b8dd9906f6fd7993bdcd78532cfd255bfc4583f3ebbf527f720', 'type': 'ddg', 'title': 'Qwen3.8-27B（2026）：Qwen 新 27B 视觉语言模型完整指南 - 见路非道 - 博客园'}
