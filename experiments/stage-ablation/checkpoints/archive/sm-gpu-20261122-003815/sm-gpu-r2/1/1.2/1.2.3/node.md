# N50: L40S 48GB 运行 Qwen3-27B 的可行性：BF16 总需求 71.2GB > 48GB，不可行；FP8 总需求 35.6GB (KV-FP8) <

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

L40S 48GB 运行 Qwen3-27B 的可行性：BF16 总需求 71.2GB > 48GB，不可行；FP8 总需求 35.6GB (KV-FP8) < 48GB，可行，但需验证 L40S 对 FP8 推理的硬件加速支持及软件栈兼容性。

## Corrected Claim

L40S 48GB 运行 Qwen3-27B 的可行性：BF16 总需求 71.2GB > 48GB，不可行；FP8 总需求 35.6GB (KV-FP8) < 48GB，可行，但需验证 L40S 对 FP8 推理的硬件加速支持及软件栈兼容性。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，BF16权重约54GB，加上KV Cache及激活值，总显存需求71.2GB超过L40S 48GB显存，故不可行；FP8权重约27GB，加上KV Cache等开销，总需求35.6GB小于48GB，故可行。L40S基于Ada Lovelace架构，支持FP8硬件加速，软件栈兼容性需验证但逻辑上成立。

## Search Query

L40S FP8 inference support Qwen3-27B
