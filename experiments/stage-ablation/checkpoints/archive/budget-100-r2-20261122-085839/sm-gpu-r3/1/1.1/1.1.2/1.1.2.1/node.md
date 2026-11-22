# N125: W4 量化方案中，权重矩阵的 Group Size（分组大小）通常设为 128 或 256，即每 128 或 256 个权重共享一组量化参数，该参数直接影响缩放

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

W4 量化方案中，权重矩阵的 Group Size（分组大小）通常设为 128 或 256，即每 128 或 256 个权重共享一组量化参数，该参数直接影响缩放因子（Scale）和零点（Zero）的数量。

## Corrected Claim

W4 量化方案中，权重矩阵的 Group Size（分组大小）通常设为 128 或 256，即每 128 或 256 个权重共享一组量化参数，该参数直接影响缩放因子（Scale）和零点（Zero）的数量。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

W4A16 quantization group size 128 256 standard
