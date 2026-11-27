# N99: A6000/L40S (48GB) 运行 Qwen3-27B 的可行性分析：BF16 总需求 ≈ 54 (Weights) + 8.6 (KV 32K) + 2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

A6000/L40S (48GB) 运行 Qwen3-27B 的可行性分析：BF16 总需求 ≈ 54 (Weights) + 8.6 (KV 32K) + 2 (Act) + 1 (Runtime) = 65.6 GB > 48 GB，不可行。FP8 总需求 ≈ 27 + 4.3 + 2 + 1 = 34.3 GB < 48 GB，可行且余量充足 (13.7 GB)，支持更大 Batch Size 或更长上下文 (如 64K-128K)。

## Corrected Claim

A6000/L40S (48GB) 运行 Qwen3-27B 的可行性分析：BF16 总需求 ≈ 54 (Weights) + 8.6 (KV 32K) + 2 (Act) + 1 (Runtime) = 65.6 GB > 48 GB，不可行。FP8 总需求 ≈ 27 + 4.3 + 2 + 1 = 34.3 GB < 48 GB，可行且余量充足 (13.7 GB)，支持更大 Batch Size 或更长上下文 (如 64K-128K)。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，BF16权重54GB、FP8权重27GB符合基本换算；KV Cache与激活值估算量级合理，总显存需求计算逻辑自洽且符合GPU显存管理常识。
