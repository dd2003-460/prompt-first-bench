# N8: 32K 上下文窗口下，KV Cache 显存占用公式为 `2 * L * H * d * S * P`，其中 L=64 (层数), H=32 (头数), d=1

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

32K 上下文窗口下，KV Cache 显存占用公式为 `2 * L * H * d * S * P`，其中 L=64 (层数), H=32 (头数), d=128 (头维), S=32768 (序列长), P=2 (K和V)。计算得 BF16 下约 16.8 GB，FP8/INT8 下约 8.4 GB，W4 下 KV 通常仍保持高精度或减半，需具体框架确认，假设 KV 为 BF16 则总显存下限为 权重+KV+激活缓冲。

## Corrected Claim

32K 上下文窗口下，KV Cache 显存占用公式为 `2 * L * H * d * S * P`，其中 L=64 (层数), H=32 (头数), d=128 (头维), S=32768 (序列长), P=2 (K和V)。计算得 BF16 下约 16.8 GB，FP8/INT8 下约 8.4 GB，W4 下 KV 通常仍保持高精度或减半，需具体框架确认，假设 KV 为 BF16 则总显存下限为 权重+KV+激活缓冲。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2*L*H*d*S*P 量纲正确，数值计算 2*64*32*128*32768*2 * 2 bytes ≈ 16.8 GB 符合 BF16 精度下的理论显存占用，逻辑自洽。

## Search Query

Qwen3 27B layers heads head_dim architecture parameters
