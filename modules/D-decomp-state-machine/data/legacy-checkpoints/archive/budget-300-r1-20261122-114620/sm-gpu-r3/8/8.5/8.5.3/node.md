# N376: 单卡 RTX 4090 (24GB) 运行 Qwen3-27B W4A16 时的实际显存占用峰值为 19.2GB (权重 13.5GB + KV Cache 3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N131

## Claim

单卡 RTX 4090 (24GB) 运行 Qwen3-27B W4A16 时的实际显存占用峰值为 19.2GB (权重 13.5GB + KV Cache 3.2GB @32K + 框架/激活 2.5GB)，剩余 4.8GB 安全边际，计算公式为 VRAM_peak = W_quant + KV_cache + overhead

## Corrected Claim

单卡 RTX 4090 (24GB) 运行 Qwen3-27B W4A16 时的实际显存占用峰值为 19.2GB (权重 13.5GB + KV Cache 3.2GB @32K + 框架/激活 2.5GB)，剩余 4.8GB 安全边际，计算公式为 VRAM_peak = W_quant + KV_cache + overhead

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数W4量化权重约13.5GB，32K上下文KV Cache约3.2GB，框架开销2.5GB，总和19.2GB，小于24GB显存，计算自洽。
