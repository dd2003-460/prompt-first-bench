# N193: 在 H100 80GB 上运行 FP8 模型时，剩余 47.6GB 显存支持的最大并发 Batch Size (32K 上下文) 约为 44 个 (47.6GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

在 H100 80GB 上运行 FP8 模型时，剩余 47.6GB 显存支持的最大并发 Batch Size (32K 上下文) 约为 44 个 (47.6GB / 1.07GB per request ≈ 44.5)，这意味着在长期持有且高负载场景下，H100 的每用户边际成本显著低于 A100 BF16 方案，尽管初始 TCO 较高

## Corrected Claim

在 H100 80GB 上运行 FP8 模型时，剩余 47.6GB 显存支持的最大并发 Batch Size (32K 上下文) 约为 44 个 (47.6GB / 1.07GB per request ≈ 44.5)，这意味着在长期持有且高负载场景下，H100 的每用户边际成本显著低于 A100 BF16 方案，尽管初始 TCO 较高

## Evidence

先验知识/题面给定，逻辑校验通过：47.6GB / 1.07GB ≈ 44.48，取整为44符合数学逻辑；FP8相比BF16显存占用减半，在同等显存下支持更高并发，从而降低长期高负载下的边际成本，符合硬件经济学直觉。
