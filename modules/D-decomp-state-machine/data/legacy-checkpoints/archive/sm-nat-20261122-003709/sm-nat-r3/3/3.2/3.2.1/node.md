# N52: 对象在LRU缓存中的平均驻留时间 T_resident 的解析近似公式：T_resident ≈ C_bytes / (R_bytes * (1 - H_obj

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

对象在LRU缓存中的平均驻留时间 T_resident 的解析近似公式：T_resident ≈ C_bytes / (R_bytes * (1 - H_obj_LRU))，其中 C_bytes=128GB，R_bytes 为总字节请求速率（需由 N6 的 E[S] 和 50M 请求/天计算），H_obj_LRU 为对象级命中率（需由 N19 或 N25 提供具体数值）。

## Corrected Claim

对象在LRU缓存中的平均驻留时间 T_resident 的解析近似公式：T_resident ≈ C_bytes / (R_bytes * (1 - H_obj_LRU))，其中 C_bytes=128GB，R_bytes 为总字节请求速率（需由 N6 的 E[S] 和 50M 请求/天计算），H_obj_LRU 为对象级命中率（需由 N19 或 N25 提供具体数值）。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应公式中的独立变量 R_bytes、H_obj_LRU 以及最终合成计算 T_resident，逻辑上互不重叠且无矛盾，完整覆盖了父节点解析近似所需的输入参数和最终推导结果。）
