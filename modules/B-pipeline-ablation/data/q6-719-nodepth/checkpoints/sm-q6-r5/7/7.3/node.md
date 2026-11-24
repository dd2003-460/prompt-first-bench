# N119: 写请求（上传）流量占比 5%，对应日均上传量 200GB（题面给定），验证一致性：200GB / (2TB * 0.05) = 200GB / 100GB = 

- **status**: pending
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

写请求（上传）流量占比 5%，对应日均上传量 200GB（题面给定），验证一致性：200GB / (2TB * 0.05) = 200GB / 100GB = 2，说明上传对象平均大小或压缩比需进一步澄清，此处仅用于流量分离。

## Corrected Claim

写请求（上传）流量占比 5%，对应日均上传量 200GB（题面给定），验证一致性：200GB / (2TB * 0.05) = 200GB / 100GB = 2，说明上传对象平均大小或压缩比需进一步澄清，此处仅用于流量分离。

## Evidence

父节点级核验失败（LLM 错误）：Expecting ',' delimiter: line 9 column 126 (char 769)
