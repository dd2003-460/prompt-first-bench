# N22: 电力成本差异：2×消费级 GPU（如 RTX 4090，单卡 TDP 450W）总功耗约为 900W + 主板/内存/存储约 200W = 1100W；1×数据

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

电力成本差异：2×消费级 GPU（如 RTX 4090，单卡 TDP 450W）总功耗约为 900W + 主板/内存/存储约 200W = 1100W；1×数据中心卡（如 H100 SXM，TDP 700W）总功耗约为 700W + 服务器开销 300W = 1000W；假设电价 0.1 元/kWh，年运行 8760 小时，2×消费卡年电费约为 966 元，1×数据中心卡约为 876 元，差异约为 90 元/年

## Corrected Claim

电力成本差异：2×消费级 GPU（如 RTX 4090，单卡 TDP 450W）总功耗约为 900W + 主板/内存/存储约 200W = 1100W；1×数据中心卡（如 H100 SXM，TDP 700W）总功耗约为 700W + 服务器开销 300W = 1000W；假设电价 0.1 元/kWh，年运行 8760 小时，2×消费卡年电费约为 966 元，1×数据中心卡约为 876 元，差异约为 90 元/年

## Evidence

先验知识/题面给定，逻辑校验通过：功耗估算符合硬件规格常识（RTX 4090 TDP 450W, H100 SXM TDP 700W），电费计算公式（功率×时间×电价）及数值计算（1.1kW×8760h×0.1元/kWh=966.6元, 1.0kW×8760h×0.1元/kWh=876元）准确无误，差异约90元/年符合逻辑。

## Search Query

RTX 4090 H100 TDP power consumption watts
