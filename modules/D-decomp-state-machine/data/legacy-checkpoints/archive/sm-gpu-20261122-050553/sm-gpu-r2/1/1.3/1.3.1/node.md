# N43: NVIDIA A100 40GB 对 Qwen3-27B 的精度支持能力：40GB 显存可容纳 FP8 权重 (27GB) + KV Cache (13GB) 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

NVIDIA A100 40GB 对 Qwen3-27B 的精度支持能力：40GB 显存可容纳 FP8 权重 (27GB) + KV Cache (13GB) = 40GB，刚好满配；若需 BF16 (54GB) 则不可行。其 1555 GB/s HBM2e 带宽相比 4090 的 1008 GB/s 提升 54%，理论上 FP8 解码吞吐提升 54%，但需扣除 PCIe 接口瓶颈 (A100 PCIe 版本无 NVLink 高带宽互联，多卡时受限)。

## Corrected Claim

NVIDIA A100 40GB 对 Qwen3-27B 的精度支持能力：40GB 显存可容纳 FP8 权重 (27GB) + KV Cache (13GB) = 40GB，刚好满配；若需 BF16 (54GB) 则不可行。其 1555 GB/s HBM2e 带宽相比 4090 的 1008 GB/s 提升 54%，理论上 FP8 解码吞吐提升 54%，但需扣除 PCIe 接口瓶颈 (A100 PCIe 版本无 NVLink 高带宽互联，多卡时受限)。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 40GB显存容量与Qwen3-27B FP8权重(27GB)及KV Cache(13GB)之和匹配，带宽提升比例计算(1555/1008-1≈54%)正确，且符合硬件规格常识。

## Search Query

NVIDIA A100 40GB HBM2e bandwidth 1555 GB/s LLM inference FP8 Qwen3
