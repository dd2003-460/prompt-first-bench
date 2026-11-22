# N32: 非典型方案性能基准：Apple M2 Ultra (192GB Unified Memory) 运行 27B BF16 模型的实测生成速度约为 15-25 to

- **status**: verified
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

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了物理极限推导（理论vs实测）、全生命周期成本（TCO）、长上下文性能瓶颈（Prefill延迟）以及成本计算模型（公式），四个维度（性能物理基础、经济性、特定场景性能、方法论）相互独立且无重复，共同支撑了父节点关于‘非典型方案性能基准’及‘适用场景’的结论。）

## Retrieval Sources

- {'url': 'https://apxml.com/zh/hardware/apple-m2-ultra-192gb&rut=e106ac58b380e0f506b6376dda4ae721268320ee6472a3fcd783285bc30af281', 'type': 'ddg', 'title': 'Apple M2 Ultra (192GB) 最佳适配与运行大模型 - 显存与速度评测'}
- {'url': 'https://mirrorfrog.com/docs/cards/others/apple-m2-ultra/&rut=edd7790abe08f8cc264e2b7537408903ffdf59e103f04e68a66e8fd9010fc8ee', 'type': 'ddg', 'title': 'Apple M2 Ultra (192GB UMA 统一内存) | AI 算力卡百科 | 233 款 AI 芯片规格对比'}
- {'url': 'https://llmconfigurator.com/en/gpu/apple-m2-ultra&rut=f6f71b7a81bd106aff87912c41af6c5a06fb67d9bbe5f286c2508fdf7704dcfa', 'type': 'ddg', 'title': 'Apple M2 Ultra: Tokens per Second & 192 GB Unified Memory'}
