# N8: 32K 上下文窗口下，KV Cache 显存占用公式为 `2 * L * H * d * S * P`，其中 L=64 (层数), H=32 (头数), d=1

- **status**: pending
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

父节点级核验未通过：不完备（子节点之间存在逻辑矛盾和事实错误。1. 矛盾：子节点1指出H_kv=8 (GQA)，子节点3公式正确使用了H_kv，但父节点中错误地使用了H=32（多头注意力）计算得出16.8GB，这与子节点提供的架构参数（GQA）直接冲突，导致父节点结论错误（实际KV Cache应为2.1GB左右）。2. 不完备：父节点提到“总显存下限为 权重+KV+激活缓冲”，但子节点中缺少“模型权重显存占用”这一关键子节点，无法支撑父节点关于总显存的结论。）

## Search Query

Qwen3 27B layers heads head_dim architecture parameters
