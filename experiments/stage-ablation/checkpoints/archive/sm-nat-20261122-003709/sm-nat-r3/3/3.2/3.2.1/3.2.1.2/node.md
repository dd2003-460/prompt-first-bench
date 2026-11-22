# N159: H_obj_LRU（对象级命中率）的具体数值：基于 N82 结论，若缓存容量足以覆盖所有 100,000 个对象（K=N），则 H_obj_LRU = 1.0；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N52

## Claim

H_obj_LRU（对象级命中率）的具体数值：基于 N82 结论，若缓存容量足以覆盖所有 100,000 个对象（K=N），则 H_obj_LRU = 1.0；若受限于大小分布导致 K<N，则 H_obj_LRU = Σ_{i=1}^{K} p_i，需代入 N67 计算的 K 值（约 50,000-60,000）求和，预计 H_obj_LRU ≈ 0.95-0.98。

## Corrected Claim

H_obj_LRU（对象级命中率）的具体数值：基于 N82 结论，若缓存容量足以覆盖所有 100,000 个对象（K=N），则 H_obj_LRU = 1.0；若受限于大小分布导致 K<N，则 H_obj_LRU = Σ_{i=1}^{K} p_i，需代入 N67 计算的 K 值（约 50,000-60,000）求和，预计 H_obj_LRU ≈ 0.95-0.98。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU在缓存容量覆盖全部对象时命中率必为1.0；若仅覆盖部分对象（K<N），命中率即为被覆盖对象的访问概率之和（Σp_i），逻辑自洽且符合缓存理论基本定义。
