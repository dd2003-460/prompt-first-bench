# N45: 字节覆盖率计算：缓存集合的字节覆盖率 = Σ_{i∈Cache} (r_i * s_i) / Σ_{j=1}^N (r_j * s_j)，在 LRU 策略下，由

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

字节覆盖率计算：缓存集合的字节覆盖率 = Σ_{i∈Cache} (r_i * s_i) / Σ_{j=1}^N (r_j * s_j)，在 LRU 策略下，由于保留高热度小对象，字节覆盖率通常低于对象数量覆盖率，需量化两者差距。

## Corrected Claim

字节覆盖率计算：缓存集合的字节覆盖率 = Σ_{i∈Cache} (r_i * s_i) / Σ_{j=1}^N (r_j * s_j)，在 LRU 策略下，由于保留高热度小对象，字节覆盖率通常低于对象数量覆盖率，需量化两者差距。

## Evidence

父节点级核验未通过：非正交（子节点1（差距量化）与子节点2、3（分别计算H_byte和H_obj）存在逻辑包含与重复。子节点1的公式 ΔCov = H_byte - H_obj 依赖于子节点2和3的结果，且其描述中再次详细阐述了H_byte低于H_obj的原因及计算需求，这与子节点2和3的内容高度重叠。子节点1应仅作为最终结果的合成步骤，而非重复阐述分量。）

## Search Query

cache byte coverage vs object coverage LRU
