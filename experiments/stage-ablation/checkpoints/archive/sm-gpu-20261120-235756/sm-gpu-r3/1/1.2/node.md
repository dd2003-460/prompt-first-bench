# N8: Qwen3-27B的KV Cache每token显存占用公式为：2 × n_layers × n_kv_heads × head_dim × dtype_siz

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B的KV Cache每token显存占用公式为：2 × n_layers × n_kv_heads × head_dim × dtype_size，需结合具体层数与头数计算32K上下文下的峰值显存。

## Corrected Claim

Qwen3-27B的KV Cache每token显存占用公式为：2 × n_layers × n_kv_heads × head_dim × dtype_size，需结合具体层数与头数计算32K上下文下的峰值显存。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于每token显存占用的推导与计算，子节点2聚焦于32K上下文下的总峰值显存及与权重显存的叠加关系。两者在逻辑上是递进关系（单位量 -> 总量），内容不重叠、不矛盾，且共同覆盖了父节点中'公式'、'参数代入'、'32K峰值计算'及'结合具体参数'的所有关键要求。不存在冗余，因为二者分别解决了不同层级的计算问题。）

## Search Query

Qwen3-27B n_layers n_kv_heads head_dim architecture details
