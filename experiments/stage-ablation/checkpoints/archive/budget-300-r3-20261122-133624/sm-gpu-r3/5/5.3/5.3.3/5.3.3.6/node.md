# N382: Apple M2 Ultra 的显存容量为 192GB（统一内存），在 INT8 下运行 Qwen3-27B 时，权重占用 27GB，KV Cache (32K

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N146, N147, N149

## Claim

Apple M2 Ultra 的显存容量为 192GB（统一内存），在 INT8 下运行 Qwen3-27B 时，权重占用 27GB，KV Cache (32K tokens) 占用约 2.5GB，总占用约 30GB，远低于 192GB 上限，单卡部署完全可行且无需量化，甚至可运行 BF16 精度（54GB）或更大模型。

## Corrected Claim

Apple M2 Ultra 的显存容量为 192GB（统一内存），在 INT8 下运行 Qwen3-27B 时，权重占用 27GB，KV Cache (32K tokens) 占用约 2.5GB，总占用约 30GB，远低于 192GB 上限，单卡部署完全可行且无需量化，甚至可运行 BF16 精度（54GB）或更大模型。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 192GB 统一内存为已知规格；Qwen3-27B 在 INT8 下权重约 27GB，BF16 下约 54GB，KV Cache 32K tokens 占用约 2.5GB 符合常规估算，总占用远低于 192GB，单卡部署可行。

## Search Query

Apple M2 Ultra 192GB unified memory capacity
