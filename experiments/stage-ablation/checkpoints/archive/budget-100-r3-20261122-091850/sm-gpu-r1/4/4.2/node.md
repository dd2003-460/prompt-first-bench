# N20: 电力消耗成本（OPEX）：单卡方案与多卡方案的 TDP（热设计功耗）对比，例如 2× RTX 4090 (450W each) vs 1× A100 (400W

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N4

## Claim

电力消耗成本（OPEX）：单卡方案与多卡方案的 TDP（热设计功耗）对比，例如 2× RTX 4090 (450W each) vs 1× A100 (400W) vs 1× H100 (700W)；计算每小时电费 = (TDP * 1.2 [PSU效率] * 单位电价) * 小时数，假设电价 $0.10/kWh [待核验：需根据地区调整]。

## Corrected Claim

电力消耗成本（OPEX）估算需基于具体GPU型号及接口类型（SXM/PCIe）的TDP（如H100 SXM 700W, H100 PCIe 350W, A100 400W/650W, RTX 4090 450W），结合电源转换效率（通常80%-90%）及当地实际电价计算，公式为：电费 = (TDP / PSU效率 * 电价 * 小时数)。

## Evidence

[质询]TDP数值存在版本混淆风险（如H100 SXM为700W但PCIe为350W，A100也有400W/650W之分），且PSU效率系数1.2（即83%效率）为经验估算值，非固定物理常数，不同电源设计差异较大；电价$0.10/kWh为特定地区假设，不具备普适性。 | 来源[1]仅提及TCO包含电力消耗，未提供具体TDP数值、PSU效率系数或电价标准，无法直接支持具体参数；该节点为经验事实（具体硬件参数与成本假设），逻辑自洽但缺乏来源直接支持，依据经验事实排除条款降级。

## Search Query

RTX 4090 A100 H100 TDP power consumption watts electricity cost per hour

## Retrieval Sources

- {'url': 'https://cloud.baidu.com/article/3826301&rut=38dd17135be2a42e0550c5e6af98322ead4d220cdc4b4e4f36ce5c293a360ddb', 'type': 'ddg', 'title': '大模型一体机TCO全解析：千卡集群与单机方案成本矩阵对比'}
