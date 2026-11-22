# N529: 使用 INT8 量化可将对半拆分权重，每卡负载降至 27 GB，单卡计算延迟降至 26.8 ms/step，2x 4090 的有效吞吐量可提升至 20-25 t

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N163

## Claim

使用 INT8 量化可将对半拆分权重，每卡负载降至 27 GB，单卡计算延迟降至 26.8 ms/step，2x 4090 的有效吞吐量可提升至 20-25 tokens/s。

## Corrected Claim

使用 INT8 量化可将对半拆分权重，每卡负载降至约 13-14 GB（假设原模型为 27GB 左右），单卡计算延迟降至 26.8 ms/step，2x 4090 的有效吞吐量可提升至 20-25 tokens/s。

## Evidence

[质询]数值量级与硬件规格存在潜在矛盾：RTX 4090 显存为 24GB，若单卡负载降至 27GB，则必然超出显存容量导致 OOM（Out of Memory），除非该陈述隐含了 offloading 或使用了非标准显存配置，但陈述中未说明，且 27GB 负载在 24GB 卡上物理上不可行。 | 逻辑校验发现硬错误：RTX 4090 显存为 24GB，单卡负载 27GB 超出显存限制，违背基本硬件物理约束。
