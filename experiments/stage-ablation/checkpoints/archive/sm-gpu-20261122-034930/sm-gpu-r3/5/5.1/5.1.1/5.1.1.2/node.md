# N343: BF16精度下Qwen3-27B的权重显存需求约为54GB（27B参数 * 2 bytes），加上KV Cache（FP16, 32K ctx, Batch=1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N122, N123, N124

## Claim

BF16精度下Qwen3-27B的权重显存需求约为54GB（27B参数 * 2 bytes），加上KV Cache（FP16, 32K ctx, Batch=1 约10.7GB）及框架开销（约2.5-5GB），总显存需求约为67-70GB，超出单卡A100 40GB和单卡RTX 4090 24GB，需A100 80GB或2x RTX 4090 (48GB) + Offload。

## Corrected Claim

BF16精度下Qwen3-27B的权重显存需求约为54GB（27B参数 * 2 bytes），加上KV Cache（FP16, 32K ctx, Batch=1 约10.7GB）及框架开销（约2.5-5GB），总显存需求约为67-70GB，超出单卡A100 40GB和单卡RTX 4090 24GB，需A100 80GB或2x RTX 4090 (48GB) + Offload。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数BF16权重约54GB，加上KV Cache和框架开销后总显存需求约67-70GB，超出单卡A100 40GB和RTX 4090 24GB，需A100 80GB或2x RTX 4090+Offload，数值量级合理且逻辑自洽。

## Search Query

Qwen3-27B BF16 memory footprint KV cache size 32k context
