# N72: L_P99_core = max_j (RTT_P99(j) + T_proc_P99(j) + T_queue_P99(j)) * (1 + ε_core)，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

L_P99_core = max_j (RTT_P99(j) + T_proc_P99(j) + T_queue_P99(j)) * (1 + ε_core)，其中j遍历核心区域自建POP（如Top 5省对应节点），ε_core≈2-3%

## Corrected Claim

L_P99_core = max_j (RTT_P99(j) + T_proc_P99(j) + T_queue_P99(j)) * (1 + ε_core)，其中j遍历核心区域自建POP（如Top 5省对应节点），ε_core≈2-3%

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点公式中的 RTT、T_proc 和 T_queue 三个独立加项，逻辑上互不重叠（正交）。父节点公式由这三项相加及常数系数构成，子节点完整覆盖了所有关键组成部分（完备）。虽然 RTT 在 T_proc 中作为 TLS 握手的一部分被提及，但这是协议栈依赖关系的正常描述，并非数值计算上的冗余或矛盾。）
