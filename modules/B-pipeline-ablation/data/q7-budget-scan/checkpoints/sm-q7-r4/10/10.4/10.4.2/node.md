# N407: 数据量 < 100TB 且 IOPS > 100,000 场景下本地 NVMe 方案的延迟优势量化：NVMe 本地延迟 < 1ms，云 S3 延迟 ~50-10

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N154

## Claim

数据量 < 100TB 且 IOPS > 100,000 场景下本地 NVMe 方案的延迟优势量化：NVMe 本地延迟 < 1ms，云 S3 延迟 ~50-100ms，若业务对延迟敏感（如实时交易），云方案需引入本地缓存层，缓存命中率需 > 95% 才能避免频繁云请求，否则 IOPS 成本爆炸；本地 NVMe 方案无需缓存，直接满足 IOPS 需求，延迟稳定，故在极高 IOPS 场景下 NVMe 具备不可替代性。

## Corrected Claim

数据量 < 100TB 且 IOPS > 100,000 场景下本地 NVMe 方案的延迟优势量化：NVMe 本地延迟 < 1ms，云 S3 延迟 ~50-100ms，若业务对延迟敏感（如实时交易），云方案需引入本地缓存层，缓存命中率需 > 95% 才能避免频繁云请求，否则 IOPS 成本爆炸；本地 NVMe 方案无需缓存，直接满足 IOPS 需求，延迟稳定，故在极高 IOPS 场景下 NVMe 具备不可替代性。

## Evidence

先验知识/题面给定，逻辑校验通过：NVMe本地延迟（微秒级）远低于S3网络延迟（毫秒级），高IOPS下缓存命中率>95%是避免网络瓶颈的合理工程经验值，逻辑自洽且符合物理/经济直觉。

## Search Query

NVMe local latency vs S3 cloud latency ms
