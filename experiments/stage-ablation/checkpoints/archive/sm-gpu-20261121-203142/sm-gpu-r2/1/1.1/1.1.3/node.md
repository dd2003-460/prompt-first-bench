# N37: 基于确认参数的KV Cache显存精确值：8 heads * 128 head_dim * 2 bytes * 64 layers * 32768 tokens

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

基于确认参数的KV Cache显存精确值：8 heads * 128 head_dim * 2 bytes * 64 layers * 32768 tokens = 4.29 GB（替代N10中基于32层的4GB估算）

## Corrected Claim

基于确认参数的KV Cache显存精确值：8 heads * 128 head_dim * 2 bytes * 64 layers * 32768 tokens = 4.29 GB（替代N10中基于32层的4GB估算）

## Evidence

先验知识/题面给定，逻辑校验通过：8*128*2*64*32768 = 4,294,967,296 bytes，即 4.29 GB，计算准确且量级合理。
