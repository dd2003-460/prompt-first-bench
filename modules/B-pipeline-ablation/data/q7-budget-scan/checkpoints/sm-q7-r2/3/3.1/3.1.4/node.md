# N89: 云对象存储低频/归档层冷数据取回延迟约束：S3 IA取回延迟 < 毫秒级（与标准层相同），S3 Glacier Instant Retrieval取回延迟 < 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

云对象存储低频/归档层冷数据取回延迟约束：S3 IA取回延迟 < 毫秒级（与标准层相同），S3 Glacier Instant Retrieval取回延迟 < 毫秒级，S3 Glacier Flexible Retrieval取回延迟 < 5分钟，需根据业务对冷数据取回的实时性要求选择具体层级，若要求实时取回则排除Flexible Retrieval

## Corrected Claim

云对象存储低频/归档层冷数据取回延迟约束：S3 IA取回延迟 < 毫秒级（与标准层相同），S3 Glacier Instant Retrieval取回延迟 < 毫秒级，S3 Glacier Flexible Retrieval取回延迟 < 5分钟，需根据业务对冷数据取回的实时性要求选择具体层级，若要求实时取回则排除Flexible Retrieval

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

AWS S3 Glacier retrieval latency milliseconds flexible instant
