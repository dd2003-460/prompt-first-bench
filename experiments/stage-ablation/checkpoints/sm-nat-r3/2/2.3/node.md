# N12: 特定参数修正：考虑 Pareto(α=1.1) 的长尾特性，LRU 命中率下界需修正为 H_byte_LRU_corrected = H_byte_LRU_ba

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

特定参数修正：考虑 Pareto(α=1.1) 的长尾特性，LRU 命中率下界需修正为 H_byte_LRU_corrected = H_byte_LRU_base × (1 - ε_tail)，其中 ε_tail 为长尾对象未被缓存导致的额外损失，需通过数值积分估算。

## Corrected Claim

特定参数修正：考虑 Pareto(α=1.1) 的长尾特性，LRU 命中率下界需修正为 H_byte_LRU_corrected = H_byte_LRU_base × (1 - ε_tail)，其中 ε_tail 为长尾对象未被缓存导致的额外损失，需通过数值积分估算。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1定义了核心修正因子 ε_tail 的计算逻辑（涉及积分与截断点），子节点2定义了该公式中关键参数 S_cache 的具体求解方法。两者分别对应‘公式主体’和‘参数确定’，逻辑上层层递进且互不重叠，完整覆盖了父节点中关于‘修正公式’及‘数值估算所需的具体参数’的要求。）
