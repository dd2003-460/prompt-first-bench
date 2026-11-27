# N225: 显存占用计算：2×RTX 4090 INT8 权重 (27GB) + 32K KV Cache (FP16/INT8) 占用量，需确认是否超过 48GB 总显存

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

显存占用计算：2×RTX 4090 INT8 权重 (27GB) + 32K KV Cache (FP16/INT8) 占用量，需确认是否超过 48GB 总显存或触发 Offload 阈值。

## Corrected Claim

显存占用计算：2×RTX 4090 INT8 权重 (27GB) + 32K KV Cache (FP16/INT8) 占用量，需确认是否超过 48GB 总显存或触发 Offload 阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：27GB权重 + 32K KV Cache（FP16约10-20GB，INT8约5-10GB）总和在37-47GB之间，未超过48GB显存，逻辑自洽且符合硬件常识。
