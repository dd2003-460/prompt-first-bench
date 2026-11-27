# N191: 单卡 RTX 4090 (24GB) 运行 FP8/INT8 Qwen3-27B 的显存可行性量化：需求 27GB(权重) + 6.4GB(KV Cache@3

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

单卡 RTX 4090 (24GB) 运行 FP8/INT8 Qwen3-27B 的显存可行性量化：需求 27GB(权重) + 6.4GB(KV Cache@32K, FP8) + 2GB(Overhead) = 35.4GB > 24GB，缺口 11.4GB，单卡不可行；若采用 4-bit KV Cache 可将 KV 降至 ~3.2GB，总需求 32.2GB，仍超出 24GB 8.2GB，需 Offload 或进一步量化权重。

## Corrected Claim

单卡 RTX 4090 (24GB) 运行 FP8/INT8 Qwen3-27B 的显存可行性量化：需求 27GB(权重) + 6.4GB(KV Cache@32K, FP8) + 2GB(Overhead) = 35.4GB > 24GB，缺口 11.4GB，单卡不可行；若采用 4-bit KV Cache 可将 KV 降至 ~3.2GB，总需求 32.2GB，仍超出 24GB 8.2GB，需 Offload 或进一步量化权重。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型FP8/INT8权重约27GB，32K上下文KV Cache在FP8下约6.4GB，加上2GB开销总计35.4GB，确实超过24GB显存；4-bit KV Cache降至3.2GB后总需求32.2GB仍超24GB，结论合理。
