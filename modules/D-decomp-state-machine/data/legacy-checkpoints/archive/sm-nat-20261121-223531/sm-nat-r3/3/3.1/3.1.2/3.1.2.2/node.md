# N138: LFU通过频率过滤避免缓存低频更新对象，其相对LRU_stale的增益 ΔH_stale = H_LFU - H_LRU_stale 主要来源于对脏数据的规避。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

LFU通过频率过滤避免缓存低频更新对象，其相对LRU_stale的增益 ΔH_stale = H_LFU - H_LRU_stale 主要来源于对脏数据的规避。若LRU_stale的有效容量降至99%，则 H_LRU_stale ≈ 0.99 * H_LRU，LFU增益 ΔH_stale ≈ 0.01 * H_LRU，在H_LRU=100%时增益约为1个百分点，但此增益非来自频率排序本身，而是容量恢复效应。

## Corrected Claim

LFU通过频率过滤避免缓存低频更新对象，其相对LRU_stale的增益 ΔH_stale = H_LFU - H_LRU_stale 主要来源于对脏数据的规避。若LRU_stale的有效容量降至99%，则 H_LRU_stale ≈ 0.99 * H_LRU，LFU增益 ΔH_stale ≈ 0.01 * H_LRU，在H_LRU=100%时增益约为1个百分点，但此增益非来自频率排序本身，而是容量恢复效应。

## Evidence

先验知识/题面给定，逻辑校验通过：LFU通过频率过滤减少脏数据写入，若LRU_stale因脏数据占用导致有效容量降至99%，则其命中率近似为0.99*H_LRU，LFU的增益主要源于容量恢复效应而非频率排序本身，逻辑自洽且数值量级合理。
