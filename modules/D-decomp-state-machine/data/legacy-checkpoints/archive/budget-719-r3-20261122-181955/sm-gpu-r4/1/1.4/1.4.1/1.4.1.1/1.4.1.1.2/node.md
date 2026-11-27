# N542: Intel Arc A770 16GB 在 INT4 权重 (13.5GB) + 框架开销 (2.0GB) 下，若启用 INT8 KV Cache (128KB

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N188

## Claim

Intel Arc A770 16GB 在 INT4 权重 (13.5GB) + 框架开销 (2.0GB) 下，若启用 INT8 KV Cache (128KB/token)，最大支持上下文长度 = (16 - 13.5 - 2.0)GB / 128KB ≈ 4,096 tokens，远低于 32K 需求

## Corrected Claim

Intel Arc A770 16GB 在 INT4 权重 (13.5GB) + 框架开销 (2.0GB) 下，若启用 INT8 KV Cache (128KB/token)，最大支持上下文长度 = (16 - 13.5 - 2.0)GB / 128KB ≈ 4,096 tokens，远低于 32K 需求

## Evidence

先验知识/题面给定，逻辑校验通过：16GB - 13.5GB - 2.0GB = 0.5GB，0.5GB / 128KB = 4096 tokens，计算无误且符合显存分配逻辑。
