# N55: 修正矛盾：N10 与 N16 的差异源于 N16 仅计算权重+KV Cache (37.7GB) 而 N10 包含了 4GB 框架开销 (41.7GB)。在 v

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10, N11, N12

## Claim

修正矛盾：N10 与 N16 的差异源于 N16 仅计算权重+KV Cache (37.7GB) 而 N10 包含了 4GB 框架开销 (41.7GB)。在 vLLM/PyTorch 环境中，4GB 框架开销是保守下限，实际 CUDA Context + Activation Buffers 在 32K 上下文下可能更高，需按 5GB 预留以确保护边际。

## Corrected Claim

修正矛盾：N10 与 N16 的差异源于 N16 仅计算权重+KV Cache (37.7GB) 而 N10 包含了 4GB 框架开销 (41.7GB)。在 vLLM/PyTorch 环境中，4GB 框架开销是保守下限，实际 CUDA Context + Activation Buffers 在 32K 上下文下可能更高，需按 5GB 预留以确保护边际。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别拆解了框架开销的三个主要组成部分（KV Cache元数据、激活值缓冲、CUDA Context），三者互不重叠且逻辑独立。覆盖方面，子节点详细解释了父节点中提到的'4GB保守下限'的具体构成及'32K上下文'下的具体影响，并回应了'需按5GB预留'的合理性（通过指出各部分的实际可能值及多卡场景的翻倍效应）。无冗余，因为每个子节点描述的是不同性质的内存开销（元数据、计算中间态、系统固定开销），而非同一参数的不同取值。）
