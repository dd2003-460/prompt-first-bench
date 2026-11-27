# N366: Qwen3-27B 的 num_key_value_heads 确切值为 8，依据 HuggingFace 官方仓库 Qwen/Qwen3-27B 的 conf

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N130, N131, N132

## Claim

Qwen3-27B 的 num_key_value_heads 确切值为 8，依据 HuggingFace 官方仓库 Qwen/Qwen3-27B 的 config.json 文件。

## Corrected Claim

Qwen3-27B 的 num_key_value_heads 值为 8（基于 HuggingFace 官方配置，参考来源未直接提供该数值，需进一步核实具体版本配置）。

## Evidence

[质询]参考来源均指向 'Qwen3.8-27B' 而非 'Qwen3-27B'，存在模型版本混淆风险；且来源摘要未直接展示 config.json 中 num_key_value_heads 的具体数值，无法直接证实该特定参数值。 | 来源 [1][2][3] 均涉及 Qwen3.8-27B 的部署与配置，虽未直接列出 num_key_value_heads=8，但主题相关且无矛盾；鉴于 source=search 且缺乏直接数值证据，依据经验事实排除条款降级。

## Search Query

Qwen3-27B config.json num_key_value_heads

## Retrieval Sources

- {'url': 'https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.8-27B&rut=c3f65cdc4d8b2b3a2f100da1b3b0502ad17e9b0f929ce4ff7d2559344f8fe050', 'type': 'ddg', 'title': 'Qwen3.8-27B - SGLang Documentation'}
- {'url': 'https://blog.csdn.net/gitblog_00238/article/details/151043054&rut=a8a2abdc0d7f502937225041f83418c16854877c83377a7107677b067d58ae25', 'type': 'ddg', 'title': 'Qwen3.8-27B-FP8 推理性能调优 10 个技巧：采样参数、输出长度与 KV Cache 优化-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_42588555/article/details/167075500&rut=4ed961b01de1de2df52c337158c8c5522a5fd17630b24670eab0466cab43a84f', 'type': 'ddg', 'title': 'Qwen3.8-27B 源码拆解 + 保姆级本地部署 + 模型横评：270 亿参数如何用混合线性注意力打穿长序列天花板-CSDN博客'}
