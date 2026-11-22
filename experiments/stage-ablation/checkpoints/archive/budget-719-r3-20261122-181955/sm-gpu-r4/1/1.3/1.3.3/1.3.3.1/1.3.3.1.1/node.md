# N520: RX 7800 XT (16GB) 在 INT4 量化下，权重 13.5GB + 框架 2GB = 15.5GB，剩余显存仅 0.5GB，无法容纳 32K 上下

- **status**: verified
- **level**: L5
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N181

## Claim

RX 7800 XT (16GB) 在 INT4 量化下，权重 13.5GB + 框架 2GB = 15.5GB，剩余显存仅 0.5GB，无法容纳 32K 上下文所需的 8GB (BF16) 或 4GB (INT8) KV Cache，判定为完全不可行。

## Corrected Claim

RX 7800 XT (16GB) 在 INT4 量化下，权重 13.5GB + 框架 2GB = 15.5GB，剩余显存仅 0.5GB，无法容纳 32K 上下文所需的 8GB (BF16) 或 4GB (INT8) KV Cache，判定为完全不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：16GB - 15.5GB = 0.5GB，确实小于 32K 上下文所需的 KV Cache 最小值（4GB），算术与逻辑自洽。
