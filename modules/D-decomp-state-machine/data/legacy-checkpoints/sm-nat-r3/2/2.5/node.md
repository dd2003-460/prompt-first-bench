# N14: 工作点 2（中命中率中容量）：当前 128GB 容量下，LRU 命中率下界为 H_byte_LRU_mid，需计算保留对象集合的字节覆盖率和访问概率覆盖率。

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

工作点 2（中命中率中容量）：当前 128GB 容量下，LRU 命中率下界为 H_byte_LRU_mid，需计算保留对象集合的字节覆盖率和访问概率覆盖率。

## Corrected Claim

工作点 2（中命中率中容量）：当前 128GB 容量下，LRU 命中率下界为 H_byte_LRU_mid，需计算保留对象集合的字节覆盖率和访问概率覆盖率。

## Evidence

父节点级核验未通过：不完备（子节点1和2分别计算字节覆盖率和概率覆盖率，正交且无冗余。子节点3是计算子节点2所需的映射函数，属于前置条件，逻辑上独立。但父节点明确提到“LRU命中率下界为 H_byte_LRU_mid，需计算...”，子节点仅计算了覆盖率指标，未给出如何从这些覆盖率推导出 H_byte_LRU_mid 的具体公式或步骤，导致对父节点目标（计算命中率下界）的覆盖不完备。）
