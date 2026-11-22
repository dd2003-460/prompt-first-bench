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

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于单位token的显存计算（基础参数代入），子节点2聚焦于总峰值显存计算及上下文关联（应用结果）。两者逻辑递进，无重复或矛盾，且共同覆盖了父节点要求的'公式'与'32K峰值计算'。）

## Search Query

Qwen3-27B n_layers n_kv_heads head_dim architecture details
