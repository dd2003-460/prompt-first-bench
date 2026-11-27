# N272: RTX 4090 (24GB) 在 32K 上下文下支持的最大 batch_size 计算：假设使用 INT4 权重 (13.5GB) + FP8 KV Cac

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98, N99, N100

## Claim

RTX 4090 (24GB) 在 32K 上下文下支持的最大 batch_size 计算：假设使用 INT4 权重 (13.5GB) + FP8 KV Cache (6.29GB/req)，剩余显存 = 24GB - 13.5GB - 1GB (激活/缓冲) = 9.5GB。最大 batch_size = floor(9.5GB / 6.29GB) = 1。因此，在 32K 上下文下，单卡 4090 仅支持 batch_size=1 (若使用 BF16 KV 则完全不可行，需双卡)。

## Corrected Claim

RTX 4090 (24GB) 在 32K 上下文下支持的最大 batch_size 计算：假设使用 INT4 权重 (13.5GB) + FP8 KV Cache (6.29GB/req)，剩余显存 = 24GB - 13.5GB - 1GB (激活/缓冲) = 9.5GB。最大 batch_size = floor(9.5GB / 6.29GB) = 1。因此，在 32K 上下文下，单卡 4090 仅支持 batch_size=1 (若使用 BF16 KV 则完全不可行，需双卡)。

## Evidence

先验知识/题面给定，逻辑校验通过：24GB总显存减去13.5GB权重和1GB激活/缓冲后剩余9.5GB，9.5GB除以6.29GB/req的KV Cache需求，向下取整确实为1，数学推导自洽且符合显存管理基本逻辑。

## Search Query

RTX 4090 24GB max batch size 32k context Qwen3-27B
