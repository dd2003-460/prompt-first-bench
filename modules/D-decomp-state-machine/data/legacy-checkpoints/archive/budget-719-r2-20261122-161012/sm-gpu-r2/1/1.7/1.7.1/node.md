# N92: Qwen3-27B 在 FP8 (E4M3) 精度下的权重文件大小为 27 GB (27B * 1 byte)，相比 BF16 (54 GB) 节省 50% 权

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的权重文件大小为 27 GB (27B * 1 byte)，相比 BF16 (54 GB) 节省 50% 权重显存，但需注意 KV Cache 若保持 BF16 则总显存节省比例低于 50%。

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的权重文件大小为 27 GB (27B * 1 byte)，相比 BF16 (54 GB) 节省 50% 权重显存，但需注意 KV Cache 若保持 BF16 则总显存节省比例低于 50%。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8(1字节/参数)下权重约为27GB，BF16(2字节/参数)下约为54GB，节省50%权重显存符合数学推导；KV Cache通常独立于权重精度或保持高精度，因此总显存节省比例低于50%的逻辑自洽。
