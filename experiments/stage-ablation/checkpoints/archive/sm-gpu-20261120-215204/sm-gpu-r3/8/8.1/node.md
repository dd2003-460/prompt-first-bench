# N143: RTX 4090 在 W4 精度下运行 Qwen3-27B 的实际生成速度约为 37-40 Tokens/s (基于 1008 GB/s 带宽 / 13.5 G

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N36

## Claim

RTX 4090 在 W4 精度下运行 Qwen3-27B 的实际生成速度约为 37-40 Tokens/s (基于 1008 GB/s 带宽 / 13.5 GB 权重)，而非 N36 中估算的 20 Tokens/s，导致其每美元吞吐量修正为 ~0.023 Tokens/s/$

## Corrected Claim

RTX 4090 在 W4 精度下运行 Qwen3-27B 的实际生成速度约为 37-40 Tokens/s (基于 1008 GB/s 带宽 / 13.5 GB 权重)，而非 N36 中估算的 20 Tokens/s，导致其每美元吞吐量修正为 ~0.023 Tokens/s/$

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一物理模型（Tokens/s = 带宽 * 效率因子 / 权重大小）在不同效率参数下的取值，存在高度冗余；同时，父节点核心结论包含“每美元吞吐量修正为 ~0.023”，但子节点B仅提供了速度基准，未明确展示该速度如何推导出 0.023 的每美元吞吐量（缺少成本/价格维度的显式分解或计算步骤），导致在覆盖“性价比修正”这一关键方面时不够完备。）

## Search Query

RTX 4090 W4 quantization tokens per second 27B model benchmark
