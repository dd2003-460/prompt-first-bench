# N56: 最终折损计算：f_update = 1 - 0.01 * 0.85 ≈ 0.9915，即有效命中率 H_effective = H_byte_LRU * 0.9

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

最终折损计算：f_update = 1 - 0.01 * 0.85 ≈ 0.9915，即有效命中率 H_effective = H_byte_LRU * 0.9915，折损约为 0.85 个百分点，可忽略不计但需记录在推导链中

## Corrected Claim

最终折损计算：f_update = 1 - 0.01 * 0.85 ≈ 0.9915，即有效命中率 H_effective = H_byte_LRU * 0.9915，折损约为 0.85 个百分点，可忽略不计但需记录在推导链中

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式 f_update = 1 - 0.01 * T_residence 在不同 T_residence 取值下的计算实例，属于参数化冗余而非正交维度；父节点强调“可忽略但需记录”，子节点未体现“记录”这一过程性要求，且未覆盖非标准负载或非线性折损的边界情况。）
