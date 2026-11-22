# N222: 在 N_cache >= 100,000 的全量缓存场景下，LRU 的基础字节命中率 H_byte_LRU_base = 1.0，因为所有请求的对象均在内存中，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N79

## Claim

在 N_cache >= 100,000 的全量缓存场景下，LRU 的基础字节命中率 H_byte_LRU_base = 1.0，因为所有请求的对象均在内存中，不存在因容量不足导致的 Miss；该值不依赖于热度分布 β 或大小分布 α 的具体参数，仅取决于容量是否覆盖全集。

## Corrected Claim

在 N_cache >= 100,000 的全量缓存场景下，LRU 的基础字节命中率 H_byte_LRU_base = 1.0，因为所有请求的对象均在内存中，不存在因容量不足导致的 Miss；该值不依赖于热度分布 β 或大小分布 α 的具体参数，仅取决于容量是否覆盖全集。

## Evidence

先验知识/题面给定，逻辑校验通过：当缓存容量覆盖全集时，LRU 必然命中所有请求，命中率恒为 1.0，与分布参数无关。
