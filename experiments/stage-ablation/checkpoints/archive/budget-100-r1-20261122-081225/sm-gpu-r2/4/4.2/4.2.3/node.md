# N129: 工作点 B（低成本/高吞吐）：1× RTX 4090 24GB 运行 W4A8 Qwen3-27B (32K ctx)，若 KV Cache 量化至 FP8（总

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N41

## Claim

工作点 B（低成本/高吞吐）：1× RTX 4090 24GB 运行 W4A8 Qwen3-27B (32K ctx)，若 KV Cache 量化至 FP8（总显存 ~20.41 GB），可原生运行无需 Offload，单卡 TCO 约 $1.6k-$2k + $643/年电力，是消费级性价比最优解。

## Corrected Claim

工作点 B（低成本/高吞吐）：1× RTX 4090 24GB 运行 W4A8 Qwen3-27B (32K ctx)，若 KV Cache 量化至 FP8（总显存 ~20.41 GB），可原生运行无需 Offload。单卡 TCO 估算约 $1.6k-$2k + $643/年电力，是消费级高性价比方案之一（具体价格需根据实时市场调整）。

## Evidence

[质询]该陈述包含具体的硬件价格（$1.6k-$2k）、电力成本（$643/年）以及特定的模型量化配置（W4A8 Qwen3-27B），属于经验事实。由于检索失败，无法验证这些具体数值是否准确或是否为当前市场/技术条件下的最优解，存在数据过时或估算偏差的风险。 | 经验事实，逻辑自洽但缺来源支持。显存计算（27B参数W4A8约13.5GB + 32K ctx FP8 KV Cache约6-7GB ≈ 20.41GB）在量级上合理，未超过24GB显存限制，但具体价格和电力成本无法通过现有来源验证。

## Search Query

RTX 4090 24GB Qwen3-27B W4A8 KV FP8 32k context native run
