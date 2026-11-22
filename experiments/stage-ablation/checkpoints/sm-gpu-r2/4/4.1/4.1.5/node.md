# N84: 筛选标准量化：显存容量 ≥ 24GB 可完整加载 Qwen3-27B FP8 (27GB) 或 W4 (13.5GB) + 32K KV Cache (8.4G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

筛选标准量化：显存容量 ≥ 24GB 可完整加载 Qwen3-27B FP8 (27GB) 或 W4 (13.5GB) + 32K KV Cache (8.4GB)，总需求 ≤ 35.4GB (FP8) 或 21.9GB (W4)，因此 24GB 卡仅能运行 W4 或需 KV 压缩，16GB 卡必须 W4 + 短上下文 (<8K)。

## Corrected Claim

筛选标准量化：显存容量 ≥ 24GB 可完整加载 Qwen3-27B FP8 (27GB) 或 W4 (13.5GB) + 32K KV Cache (8.4GB)，总需求 ≤ 35.4GB (FP8) 或 21.9GB (W4)，因此 24GB 卡仅能运行 W4 或需 KV 压缩，16GB 卡必须 W4 + 短上下文 (<8K)。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B FP8权重约27GB，W4约13.5GB，32K KV Cache约8.4GB，总需求计算正确，24GB卡无法容纳FP8+KV但可容纳W4+KV，16GB卡需W4+短上下文，逻辑自洽且数值量级合理
