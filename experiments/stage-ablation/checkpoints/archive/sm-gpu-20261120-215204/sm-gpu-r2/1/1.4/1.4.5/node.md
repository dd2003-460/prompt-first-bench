# N49: RTX 5090 在 BF16 精度下运行 Qwen3-27B (54GB 权重 + 40GB KV Cache = 94GB) 不可行，显存不足；在 INT8

- **status**: degraded
- **level**: L3
- **source**: derived
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9, N10, N11

## Claim

RTX 5090 在 BF16 精度下运行 Qwen3-27B (54GB 权重 + 40GB KV Cache = 94GB) 不可行，显存不足；在 INT8 精度下 (33-35GB 总需求) 可行；在 W4 精度下 (20-25GB 总需求) 可行且余量充足。

## Corrected Claim

RTX 5090 (32GB 显存) 在 BF16 精度下运行 Qwen3-27B 不可行，显存不足；在 INT8 或 W4 精度下，若总显存需求控制在 32GB 以内，则可行。

## Evidence

[质询]RTX 5090 的显存容量（32GB）及 Qwen3-27B 在不同量化精度下的具体显存占用数值属于经验事实，且当前无可用外部来源直接支持这些具体数值（如 94GB、33-35GB、20-25GB 的精确计算），存在数值估算偏差或口径混淆（如是否包含激活值、框架开销等）的风险。 | 经验事实，逻辑自洽但缺来源支持。RTX 5090 显存为 32GB（基于已知硬件规格先验），BF16 下 27B 模型权重约 54GB 已超显存，逻辑成立；INT8/W4 量化后显存需求降至 32GB 以下，逻辑上可行，但具体数值缺乏来源直接验证。
