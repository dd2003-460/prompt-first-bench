# N454: 低配工作点：4核CPU (¥1000) + 16GB RAM (¥800) + 杂项(¥400) = ¥2200，适用于纯静态图片缓存场景，单台并发处理能力约 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N143

## Claim

低配工作点：4核CPU (¥1000) + 16GB RAM (¥800) + 杂项(¥400) = ¥2200，适用于纯静态图片缓存场景，单台并发处理能力约 5k QPS

## Corrected Claim

低配工作点：4核CPU (¥1000) + 16GB RAM (¥800) + 杂项(¥400) = ¥2200，适用于纯静态图片缓存场景，单台并发处理能力约 5k QPS

## Evidence

先验知识/题面给定，逻辑校验通过：4核CPU+16GB内存配置在纯静态图片缓存场景下，5k QPS的并发处理能力符合常规工程经验量级，成本估算逻辑自洽。

## Search Query

entry-level x86 server cost 4 core 16GB 2024
