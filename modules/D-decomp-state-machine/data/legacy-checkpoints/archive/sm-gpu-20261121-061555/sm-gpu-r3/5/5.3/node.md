# N28: 电力成本（OpEx 主要项）：年电费 = TDP_watts * 24h * 365d * Electricity_Rate_per_kWh * Duty_Cy

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

电力成本（OpEx 主要项）：年电费 = TDP_watts * 24h * 365d * Electricity_Rate_per_kWh * Duty_Cycle，消费级 GPU TDP 通常 250-450W，数据中心 GPU TDP 可达 400-1000W，需结合当地电价（如中国 0.5-1.5 元/kWh）计算

## Corrected Claim

电力成本（OpEx 主要项）：年电费 = TDP_watts * 24h * 365d * Electricity_Rate_per_kWh * Duty_Cycle，消费级 GPU TDP 通常 250-450W，数据中心 GPU TDP 可达 400-1000W，需结合当地电价（如中国 0.5-1.5 元/kWh）计算

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点在硬件选型上是正交的（消费级 vs 数据中心 vs 竞品），但在结构上存在严重冗余：三个子节点本质上是同一公式（年电费 = TDP * 时间 * 电价 * 效率）针对不同硬件参数的实例化计算，而非对‘电力成本’这一父节点概念的不同维度分解。此外，完备性不足，父节点明确提到的‘Duty_Cycle’（负载率）在子节点计算中均被假设为 100%（满载），未体现负载波动对成本的实际影响，且缺少对电价地域差异或动态电价的讨论。）

## Search Query

GPU power consumption annual electricity cost LLM inference server
