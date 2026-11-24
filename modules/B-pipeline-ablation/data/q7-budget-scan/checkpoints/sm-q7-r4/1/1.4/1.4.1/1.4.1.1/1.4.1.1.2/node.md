# N471: 工作点C（极端小对象）：S_obj=100B, B_block=4KB，L_prealloc = 1 - (0.1/ceil(0.1/4)*4) = 1 - 0

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N174

## Claim

工作点C（极端小对象）：S_obj=100B, B_block=4KB，L_prealloc = 1 - (0.1/ceil(0.1/4)*4) = 1 - 0.025 = 97.5%，实际损耗率为97.5%

## Corrected Claim

工作点C（极端小对象）：S_obj=100B, B_block=4KB，L_prealloc = 1 - (0.1/ceil(0.1/4)*4) = 1 - 0.025 = 97.5%，实际损耗率为97.5%

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 1 - (0.1 % 4)/4 = 1 - 0.025 = 0.975 正确，符合预分配空间浪费率的定义。
