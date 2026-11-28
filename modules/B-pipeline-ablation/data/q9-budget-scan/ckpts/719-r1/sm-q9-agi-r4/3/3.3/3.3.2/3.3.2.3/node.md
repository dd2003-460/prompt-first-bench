# N197: 长上下文下 MTP 失效阈值：当生成长度 > 8k tokens 且 MTP 加速比 < 1.2x 时，系统自动禁用 MTP，回退至标准自回归模式，以避免验证开

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

长上下文下 MTP 失效阈值：当生成长度 > 8k tokens 且 MTP 加速比 < 1.2x 时，系统自动禁用 MTP，回退至标准自回归模式，以避免验证开销抵消草稿收益，确保整体延迟可控。

## Corrected Claim

长上下文下 MTP 失效阈值：当生成长度 > 8k tokens 且 MTP 加速比 < 1.2x 时，系统自动禁用 MTP，回退至标准自回归模式，以避免验证开销抵消草稿收益，确保整体延迟可控。

## Evidence

先验知识/题面给定，逻辑校验通过
