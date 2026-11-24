# N203: ΔL_per_pop 的边际递减函数形式：ΔL_per_pop(N) = ΔL_base * exp(-N / N_decay)，其中 N_decay ≈ 5-

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64, N65, N66

## Claim

ΔL_per_pop 的边际递减函数形式：ΔL_per_pop(N) = ΔL_base * exp(-N / N_decay)，其中 N_decay ≈ 5-8，反映新增 POP 对长尾用户覆盖效率的指数衰减

## Corrected Claim

ΔL_per_pop 的边际递减函数形式：ΔL_per_pop(N) = ΔL_base * exp(-N / N_decay)，其中 N_decay ≈ 5-8，反映新增 POP 对长尾用户覆盖效率的指数衰减

## Evidence

父节点级核验未通过：非正交（子节点1和子节点2存在逻辑依赖和重叠：子节点1主要阐述失效条件并引出修正项W_region，子节点2直接给出包含W_region的修正公式。两者并非完全正交，而是“问题诊断”与“解决方案”的紧密耦合，且子节点2的公式直接包含了子节点1中提到的修正逻辑，导致概念边界模糊。）
