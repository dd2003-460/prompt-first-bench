# N32: 非典型方案性能基准：Apple M2 Ultra (192GB Unified Memory) 运行 27B BF16 模型的实测生成速度约为 15-25 to

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

非典型方案性能基准：Apple M2 Ultra (192GB Unified Memory) 运行 27B BF16 模型的实测生成速度约为 15-25 tokens/s [待核验]，虽显存充足但计算吞吐量远低于数据中心GPU，适用于对延迟不敏感的低并发场景。

## Corrected Claim

Apple M2 Ultra (192GB Unified Memory) 运行 27B BF16 模型的生成速度预计显著低于 8B 模型（参考 8B 模型约 43-89 tokens/s），虽显存充足但计算吞吐量远低于数据中心GPU，适用于对延迟不敏感的低并发场景。

## Evidence

[质询]参考来源[3]提供的数据（43-89 tok/s）是针对 8B 参数模型的，而待核验事实针对的是 27B 参数模型。虽然 27B 模型速度低于 8B 是符合逻辑的，但来源中缺乏针对 27B 模型的具体实测数据直接支持 15-25 tokens/s 这一具体数值区间，属于经验事实且缺乏直接来源支持。 | 逻辑上，27B 模型参数量约为 8B 的 3.4 倍，在内存带宽受限（800 GB/s）且计算吞吐量低于数据中心 GPU 的前提下，生成速度从 8B 的 43-89 tok/s 降至 15-25 tok/s 是合理的量级推断（来源[3]提供 8B 基准，来源[1][2]确认硬件规格），但无直接来源明确陈述 27B 的实测速度，故降级。

## Retrieval Sources

- {'url': 'https://apxml.com/zh/hardware/apple-m2-ultra-192gb&rut=e106ac58b380e0f506b6376dda4ae721268320ee6472a3fcd783285bc30af281', 'type': 'ddg', 'title': 'Apple M2 Ultra (192GB) 最佳适配与运行大模型 - 显存与速度评测'}
- {'url': 'https://mirrorfrog.com/docs/cards/others/apple-m2-ultra/&rut=edd7790abe08f8cc264e2b7537408903ffdf59e103f04e68a66e8fd9010fc8ee', 'type': 'ddg', 'title': 'Apple M2 Ultra (192GB UMA 统一内存) | AI 算力卡百科 | 233 款 AI 芯片规格对比'}
- {'url': 'https://llmconfigurator.com/en/gpu/apple-m2-ultra&rut=f6f71b7a81bd106aff87912c41af6c5a06fb67d9bbe5f286c2508fdf7704dcfa', 'type': 'ddg', 'title': 'Apple M2 Ultra: Tokens per Second & 192 GB Unified Memory'}
