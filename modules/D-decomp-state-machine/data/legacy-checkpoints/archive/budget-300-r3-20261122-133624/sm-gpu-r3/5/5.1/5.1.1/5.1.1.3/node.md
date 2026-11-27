# N340: 单卡 RTX 4090 在 32K 上下文下运行 Qwen3-27B 的最低可行量化精度推导：若 INT8 (27GB) 不可行，计算 W4A8 (权重 13.

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N112

## Claim

单卡 RTX 4090 在 32K 上下文下运行 Qwen3-27B 的最低可行量化精度推导：若 INT8 (27GB) 不可行，计算 W4A8 (权重 13.5GB + KV Cache 4.09GB + 框架 1.5GB = 19.09GB) 或 W4A4 (权重 13.5GB + KV Cache 2.04GB + 框架 1.5GB = 17.04GB) 的显存占用，验证是否 < 24GB。同时需引用 W4 量化对 Qwen3-27B 的 MMLU/HumanEval 性能下降幅度（通常 1-3%），以论证其是否满足‘质量损失可接受’的标准。

## Corrected Claim

单卡 RTX 4090 在 32K 上下文下运行 Qwen3-27B 的最低可行量化精度推导：若 INT8 (27GB) 不可行，计算 W4A8 (权重 13.5GB + KV Cache 4.09GB + 框架 1.5GB = 19.09GB) 或 W4A4 (权重 13.5GB + KV Cache 2.04GB + 框架 1.5GB = 17.04GB) 的显存占用，验证是否 < 24GB。同时需引用 W4 量化对 Qwen3-27B 的 MMLU/HumanEval 性能下降幅度（通常 1-3%），以论证其是否满足‘质量损失可接受’的标准。

## Search Query

Qwen3-27B W4A8 quantization accuracy loss MMLU benchmark
