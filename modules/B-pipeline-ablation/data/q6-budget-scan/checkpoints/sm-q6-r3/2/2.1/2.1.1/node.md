# N75: C_server = N_servers_per_POP * P_server + C_storage，其中N_servers_per_POP≈2-4台（取决于

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

C_server = N_servers_per_POP * P_server + C_storage，其中N_servers_per_POP≈2-4台（取决于单点QPS需求），P_server≈¥50k-100k/台，C_storage≈¥10k-20k/点（SSD缓存盘）

## Corrected Claim

C_server = N_servers_per_POP * P_server + C_storage，其中N_servers_per_POP≈2-4台（取决于单点QPS需求），P_server≈¥50k-100k/台，C_storage≈¥10k-20k/点（SSD缓存盘）

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点公式中的三个独立变量（N_servers_per_POP, P_server, C_storage），彼此之间没有逻辑重叠或矛盾，且完整覆盖了成本构成的所有主要部分。每个子节点内部虽然包含多个参数和推导步骤，但这些都是为了确定该单一变量的具体数值，属于正常的详细化展开，不构成子节点间的冗余。）
