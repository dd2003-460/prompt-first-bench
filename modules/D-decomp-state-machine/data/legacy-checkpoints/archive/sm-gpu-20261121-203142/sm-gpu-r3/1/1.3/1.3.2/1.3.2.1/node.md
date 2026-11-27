# N146: NVFP4格式下Scale Factor的精确显存计算：每16个权重共享1个FP8 Scale (1 byte)，Scale Factor总大小 = (27.2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

NVFP4格式下Scale Factor的精确显存计算：每16个权重共享1个FP8 Scale (1 byte)，Scale Factor总大小 = (27.2e9 / 16) * 1 byte = 1.7 GB；相比权重本体 (13.6 GB)，开销比例为 1.7/13.6 = 12.5%（注：N43中6.25%的计算基于错误假设，此处修正）

## Corrected Claim

NVFP4格式下Scale Factor的精确显存计算：每16个权重共享1个FP8 Scale (1 byte)，Scale Factor总大小 = (27.2e9 / 16) * 1 byte = 1.7 GB；相比权重本体 (13.6 GB)，开销比例为 1.7/13.6 = 12.5%（注：N43中6.25%的计算基于错误假设，此处修正）

## Evidence

先验知识/题面给定，逻辑校验通过：NVFP4中每16个4-bit权重（共8字节）共享1个FP8 Scale（1字节），Scale开销为权重本体的1/8即12.5%，计算过程（1.7/13.6=12.5%）与逻辑推导一致。
