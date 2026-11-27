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

父节点级核验未通过：非正交, 有冗余（子节点1和子节点3存在逻辑冗余（均为电力成本计算，仅硬件配置不同，可合并为通用公式）；子节点1与子节点2存在轻微重叠（子节点2隐含了单卡基础功耗，未完全正交）；子节点4依赖前两者的计算结果，属于分析层而非独立量化层，导致结构层级不统一。）

## Search Query

RTX 4090 TDP watts A100 H100 power consumption cost per year
