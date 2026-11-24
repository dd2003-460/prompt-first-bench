# N156: L_queue_wait 的负载敏感公式：L_queue_wait = L_base × (1 + (L_util - 0.8)^2 × 100)，其中 L_u

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

L_queue_wait 的负载敏感公式：L_queue_wait = L_base × (1 + (L_util - 0.8)^2 × 100)，其中 L_util 为节点负载率，L_base = 1ms；当 L_util = 90% 时，L_queue_wait ≈ 1 + (0.1)^2 × 100 = 2ms；当 L_util = 95% 时，L_queue_wait ≈ 1 + (0.15)^2 × 100 = 3.25ms，需结合 N108 的故障重分配模型验证极端情况。

## Corrected Claim

L_queue_wait 的负载敏感公式：L_queue_wait = L_base × (1 + (L_util - 0.8)^2 × 100)，其中 L_util 为节点负载率，L_base = 1ms；当 L_util = 90% 时，L_queue_wait ≈ 1 + (0.1)^2 × 100 = 2ms；当 L_util = 95% 时，L_queue_wait ≈ 1 + (0.15)^2 × 100 = 3.25ms，需结合 N108 的故障重分配模型验证极端情况。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的输入变量（L_util）、模型修正（排队论替代）以及外部扰动（故障重分配），逻辑上正交且无重叠。父节点明确提到的‘需结合 N108 的故障重分配模型验证极端情况’由子节点3覆盖，‘负载率’定义由子节点1覆盖，‘公式有效性/极端情况’由子节点2覆盖，整体完备。）
