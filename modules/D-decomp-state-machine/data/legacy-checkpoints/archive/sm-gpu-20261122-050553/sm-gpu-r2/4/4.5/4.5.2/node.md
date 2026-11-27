# N93: 2×RTX 4090 方案的显存容量验证：24GB × 2 = 48GB，Qwen3-27B FP8 权重 27GB + 32K 上下文 BF16 KV Cac

- **status**: verified
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

先验知识/题面给定，逻辑校验通过：24GB*2=48GB，27GB(FP8权重)+16GB(KV Cache)=43GB，48-43=5GB，计算自洽且符合硬件规格常识。
