# N93: 2×RTX 4090 方案的显存容量验证：24GB × 2 = 48GB，Qwen3-27B FP8 权重 27GB + 32K 上下文 BF16 KV Cac

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

2×RTX 4090 方案的显存容量验证：24GB × 2 = 48GB，Qwen3-27B FP8 权重 27GB + 32K 上下文 BF16 KV Cache 16GB = 43GB，剩余 5GB 余量，满足容量需求；但若使用 BF16 权重（54GB）则不可行，必须限定为 FP8/INT8 精度。

## Corrected Claim

2×RTX 4090 方案的显存容量验证：24GB × 2 = 48GB，Qwen3-27B FP8 权重 27GB + 32K 上下文 BF16 KV Cache 16GB = 43GB，剩余 5GB 余量，满足容量需求；但若使用 BF16 权重（54GB）则不可行，必须限定为 FP8/INT8 精度。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点之间存在严重的逻辑矛盾和计算错误。子节点2中声称 INT8 权重支持 Batch=8 时总占用 59.24GB，但 27GB (权重) + 32.24GB (KV) = 59.24GB，这超过了 48GB 显存，结论正确但中间逻辑混乱（且 INT8 权重通常约 27GB，与 FP8 相近，此处未区分精度差异导致的 KV 大小变化或权重大小差异）；更严重的是，子节点3中 INT4 权重 Batch=12 时 KV 48.36GB 已超显存，却得出“实际 Batch=10”的结论，但 13.5GB (权重) + 40.3GB (KV) = 53.8GB 依然超过 48GB，计算完全错误。此外，子节点1和子节点3都重复计算了 FP8 权重下的 Batch 上限，存在冗余。）
