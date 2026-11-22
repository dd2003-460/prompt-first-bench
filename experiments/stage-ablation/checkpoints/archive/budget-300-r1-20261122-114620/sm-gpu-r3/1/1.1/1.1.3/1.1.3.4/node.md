# N152: Qwen3-27B FP8 量化后在单卡 RTX 4090 (24GB) 上的不可行性：总显存需求 = 权重 (32.22GB) + KV Cache (8.1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

Qwen3-27B FP8 量化后在单卡 RTX 4090 (24GB) 上的不可行性：总显存需求 = 权重 (32.22GB) + KV Cache (8.192GB) + 框架开销 (5GB) = 45.412GB > 24GB，即使采用全层 FP8 (27.1GB) 也需 27.1 + 8.192 + 5 = 40.292GB > 24GB，不可行

## Corrected Claim

Qwen3-27B FP8 量化后在单卡 RTX 4090 (24GB) 上的不可行性：总显存需求 = 权重 (32.22GB) + KV Cache (8.192GB) + 框架开销 (5GB) = 45.412GB > 24GB，即使采用全层 FP8 (27.1GB) 也需 27.1 + 8.192 + 5 = 40.292GB > 24GB，不可行

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，FP8权重约27GB，加上KV Cache和框架开销远超RTX 4090的24GB显存，数学推导成立。
