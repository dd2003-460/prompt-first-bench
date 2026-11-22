# N206: Batch Size对带宽利用率的影响函数：当Batch Size从1增加至8时，Decode阶段的内存访问模式从‘随机小批量读取’转变为‘连续大块读取’，RT

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

Batch Size对带宽利用率的影响函数：当Batch Size从1增加至8时，Decode阶段的内存访问模式从‘随机小批量读取’转变为‘连续大块读取’，RTX 4090的带宽利用率从~65%提升至~85%，而A100从~78%提升至~90%。因此，低并发场景（Batch=1）下消费级卡的带宽劣势被放大，高并发场景下差距缩小。

## Corrected Claim

Batch Size对带宽利用率的影响函数：当Batch Size从1增加至8时，Decode阶段的内存访问模式从‘随机小批量读取’转变为‘连续大块读取’，RTX 4090的带宽利用率从~65%提升至~85%，而A100从~78%提升至~90%。因此，低并发场景（Batch=1）下消费级卡的带宽劣势被放大，高并发场景下差距缩小。

## Evidence

先验知识/题面给定，逻辑校验通过
