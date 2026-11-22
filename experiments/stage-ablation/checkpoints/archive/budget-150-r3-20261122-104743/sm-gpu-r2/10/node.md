# N37: 推荐方案边界条件 1（显存容量）：若选择 BF16 精度，单卡 RTX 4090 (24GB) 不可行（需 62GB+），必须采用 2×RTX 4090 (48

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

推荐方案边界条件 1（显存容量）：若选择 BF16 精度，单卡 RTX 4090 (24GB) 不可行（需 62GB+），必须采用 2×RTX 4090 (48GB, 仍不足 62GB，需启用 KV Cache 量化或 offload) 或 1×H100 (80GB)；若选择 FP8/INT8，单卡 RTX 4090 (24GB) 可行（需 35GB，仍不足，需 2×4090 或 H100）；若选择 4-bit，单卡 RTX 4090 可行（需 22GB，24GB 足够）

## Corrected Claim

若选择 BF16 精度，单卡 RTX 4090 (24GB) 在标准配置下通常不可行（需 62GB+ 显存），需采用多卡或 H100；若启用激进量化或 Offload 技术，单卡 4090 可能通过牺牲性能或速度实现运行，但非标准推荐方案。

## Evidence

[质询]陈述中关于BF16精度下模型显存需求的具体数值（62GB+）以及FP8/INT8下的需求（35GB）属于特定模型的经验参数，参考来源仅涉及Qwen-Turbo在4090上的部署优化，未提供该特定模型在BF16下需62GB的直接证据，且来源[1]标题暗示Qwen-Turbo BF16可在单卡4090运行（可能通过量化或offload），与陈述中‘单卡不可行’的绝对化表述存在潜在冲突或口径差异（是否包含KV Cache及具体上下文长度）。 | 逻辑上显存计算自洽（BF16权重+KV Cache通常远超24GB），但参考来源[1][2][3]主要讨论Qwen-Turbo在4090上的优化实践，未直接证实‘需62GB’这一具体数值，且来源[1]暗示单卡可行（通过优化），与陈述的‘不可行’结论存在间接矛盾或需特定条件限定，故降级。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_33557333/article/details/157996745&rut=54f93b0fc0e96f8de1973d4ec8f2ca73b81df9afd7f5dd5b5035dc0aa47e7572', 'type': 'ddg', 'title': 'Qwen-Turbo-BF16算力适配教程：如何在单卡4090上稳定运行多任务图像生成-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_34413326/article/details/159744499&rut=59927c34a67e9ca9a2bf6bf4cdfa190c779cbe59271dbe75690455aba3f89b88', 'type': 'ddg', 'title': 'RTX 4090专属优化：造相-Z-Image防爆显存+BF16高精度实战解析-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/158477687&rut=f6c6c7b3940d839d311579a107068d2a8bdfd3eab82398606f6086d98a46c86d', 'type': 'ddg', 'title': 'Qwen-Turbo-BF16 GPU算力适配教程：RTX 4090显存深度优化参数详解'}
