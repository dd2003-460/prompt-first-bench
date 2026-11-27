# N22: 运营支出（OpEx）中的电力成本量化：基于各候选硬件的TDP（功耗）和24/7运行假设，计算每月电费差异；需包含多卡方案中CPU、内存、散热风扇的附加功耗。

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

运营支出（OpEx）中的电力成本量化：基于各候选硬件的TDP（功耗）和24/7运行假设，计算每月电费差异；需包含多卡方案中CPU、内存、散热风扇的附加功耗。

## Corrected Claim

运营支出（OpEx）中的电力成本量化：基于各候选硬件的TDP（功耗）和24/7运行假设，计算每月电费差异；需包含多卡方案中CPU、内存、散热风扇的附加功耗。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点1和子节点3存在逻辑冗余，它们本质上是同一计算公式在‘单卡’和‘多卡’两种参数下的实例化，而非正交的不同维度；此外，子节点2（功耗估算）是子节点3（成本计算）的前置输入，两者耦合紧密，建议合并。）

## Search Query

RTX 4090 TDP watts A100 H100 power consumption cost per year
