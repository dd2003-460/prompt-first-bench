# N29: 自建POP的缓存层级为单级或两级（视硬件配置），若为单级则回源路径为 POP Miss -> 源站，若为两级则 POP-L1 Miss -> POP-L2 ->

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

自建POP的缓存层级为单级或两级（视硬件配置），若为单级则回源路径为 POP Miss -> 源站，若为两级则 POP-L1 Miss -> POP-L2 -> 源站，自建缓存命中率 H_self 受限于POP总存储容量 C_pop 与内容工作集大小 W。

## Corrected Claim

自建POP的缓存层级为单级或两级（视硬件配置），若为单级则回源路径为 POP Miss -> 源站，若为两级则 POP-L1 Miss -> POP-L2 -> 源站，自建缓存命中率 H_self 受限于POP总存储容量 C_pop 与内容工作集大小 W。

## Evidence

先验知识/题面给定，逻辑校验通过
