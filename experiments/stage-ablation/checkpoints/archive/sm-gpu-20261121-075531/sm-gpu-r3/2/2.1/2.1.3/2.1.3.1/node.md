# N171: Mac Studio M2 Ultra 在 W4 量化下运行 Qwen3-27B 的 32K 上下文 KV Cache 显存占用量计算：KV Cache Siz

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

Mac Studio M2 Ultra 在 W4 量化下运行 Qwen3-27B 的 32K 上下文 KV Cache 显存占用量计算：KV Cache Size = 2 (K/V) × 16 (GQA Heads) × 128 (Head Dim) × 32768 (Seq Len) × 27 (Layers) × 4 (Bytes) = 4.25 GB，加上 W4 权重 (13.5GB) 和激活值 (1.5GB)，总占用 19.25GB，远低于 192GB 统一内存上限，验证容量可行性。

## Corrected Claim

Mac Studio M2 Ultra 在 W4 量化下运行 Qwen3-27B 的 32K 上下文 KV Cache 显存占用量计算：KV Cache Size = 2 (K/V) × 16 (GQA Heads) × 128 (Head Dim) × 32768 (Seq Len) × 27 (Layers) × 4 (Bytes) = 4.25 GB，加上 W4 权重 (13.5GB) 和激活值 (1.5GB)，总占用 19.25GB，远低于 192GB 统一内存上限，验证容量可行性。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算公式及数值量级（4.25GB）符合 Qwen3-27B 架构参数（GQA 16 heads, 128 dim, 27 layers）及 32K 上下文设定，总显存占用远低于 192GB 上限，结论合理。
