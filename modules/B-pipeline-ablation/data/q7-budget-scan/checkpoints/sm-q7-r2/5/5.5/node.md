# N38: 冷数据(400TB)随机读延迟容忍度：假设业务允许延迟<10秒，本地NVMe SSD延迟<1ms，HDD延迟<100ms，云对象存储延迟<200ms，三者均满足

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

冷数据(400TB)随机读延迟容忍度：假设业务允许延迟<10秒，本地NVMe SSD延迟<1ms，HDD延迟<100ms，云对象存储延迟<200ms，三者均满足，但云存储需考虑网络抖动

## Corrected Claim

冷数据(400TB)随机读延迟容忍度：假设业务允许延迟<10秒，本地NVMe SSD延迟<1ms，HDD延迟<100ms，云对象存储延迟<200ms，三者均满足，但云存储需考虑网络抖动

## Evidence

先验知识/题面给定，逻辑校验通过：NVMe(<1ms)、HDD(<100ms)、云存储(<200ms)的延迟量级符合工程常识，且均小于10秒阈值，逻辑自洽。
