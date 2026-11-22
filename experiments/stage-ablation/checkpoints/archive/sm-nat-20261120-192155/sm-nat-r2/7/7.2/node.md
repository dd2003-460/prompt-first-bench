# N46: 推导负相关对LFU命中率的影响：LFU基于频率，不受大小影响，因此H_LFU在独立和负相关假设下相同；但LRU受大小影响，负相关使LRU更接近LFU，从而缩小L

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

推导负相关对LFU命中率的影响：LFU基于频率，不受大小影响，因此H_LFU在独立和负相关假设下相同；但LRU受大小影响，负相关使LRU更接近LFU，从而缩小LFU相对LRU的提升空间；ΔH_LFU_LRU_ρ < ΔH_LFU_LRU_independent，具体差值需对比两种假设下的H_LRU。

## Corrected Claim

推导负相关对LFU命中率的影响：LFU基于频率，不受大小影响，因此H_LFU在独立和负相关假设下相同；但LRU受大小影响，负相关使LRU更接近LFU，从而缩小LFU相对LRU的提升空间；ΔH_LFU_LRU_ρ < ΔH_LFU_LRU_independent，具体差值需对比两种假设下的H_LRU。

## Evidence

先验知识/题面给定，逻辑校验通过
