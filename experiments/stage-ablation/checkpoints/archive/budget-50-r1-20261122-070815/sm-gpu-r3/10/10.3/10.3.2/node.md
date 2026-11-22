# N425: A100 80GB 运行 Qwen3-27B FP8 权重 (27GB) + 32K BF16 KV Cache (2.0GB) 时的显存占用约为 29GB，剩

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N147

## Claim

A100 80GB 运行 Qwen3-27B FP8 权重 (27GB) + 32K BF16 KV Cache (2.0GB) 时的显存占用约为 29GB，剩余 51GB 用于激活值和碎片，显存非瓶颈；因此 FP8 在 A100 上的主要价值不在于显存节省（BF16 54GB 亦能单卡运行），而在于潜在的内存带宽压力缓解，但因计算瓶颈在 Tensor Core 而非 HBM 带宽，实际加速比预计低于 1.0x。

## Corrected Claim

A100 80GB 运行 Qwen3-27B FP8 权重 (27GB) + 32K BF16 KV Cache (2.0GB) 时的显存占用约为 29GB，剩余 51GB 用于激活值和碎片，显存非瓶颈；因此 FP8 在 A100 上的主要价值不在于显存节省（BF16 54GB 亦能单卡运行），而在于潜在的内存带宽压力缓解，但因计算瓶颈在 Tensor Core 而非 HBM 带宽，实际加速比预计低于 1.0x。

## Evidence

先验知识/题面给定，逻辑校验通过：显存占用计算（27GB+2GB=29GB）准确，A100 80GB 显存充足；FP8 在 A100 上因缺乏原生硬件加速且计算瓶颈在 Tensor Core，确实难以带来加速，逻辑自洽。
