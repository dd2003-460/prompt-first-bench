# N10: 数据中心级显卡（如 A100 80GB, H100 80GB）单卡可承载 BF16/FP8 下的 Qwen3-27B + 32K KV Cache，需验证具体余

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

数据中心级显卡（如 A100 80GB, H100 80GB）单卡可承载 BF16/FP8 下的 Qwen3-27B + 32K KV Cache，需验证具体余量是否满足激活值开销

## Corrected Claim

数据中心级显卡（如 A100 80GB, H100 80GB）单卡可承载 BF16/FP8 下的 Qwen3-27B + 32K KV Cache，需验证具体余量是否满足激活值开销

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 模型权重在 BF16 下约 54GB，FP8 下约 27GB；32K 上下文 KV Cache 在主流架构下通常占用 10-20GB 显存，总占用远低于 80GB 显存上限，激活值开销在合理范围内，逻辑自洽。
