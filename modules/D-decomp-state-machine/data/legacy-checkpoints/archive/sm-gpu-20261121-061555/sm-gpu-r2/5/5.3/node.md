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

父节点级核验未通过：不完备, 有冗余（1. 正交性：子节点分别对应不同硬件架构（消费级NVIDIA、数据中心NVIDIA、消费级AMD），场景互斥，无逻辑重叠，正交性合格。2. 完备性：父节点强调‘需结合当地电价’，但子节点仅覆盖了单一电价（0.6-0.8元/kWh）下的计算结果，未体现电价波动对成本结构的敏感性分析，且未涵盖父节点提到的TDP范围全貌（如低负载场景或不同地域电价差异），覆盖不全。3. 冗余：三个子节点本质上是同一公式在不同硬件参数下的实例化，属于‘同构数据’。在知识图谱或学术分解中，若未提炼出通用的计算模型或对比维度，仅罗列具体数值案例显得冗余，应抽象为‘硬件能效对比’或‘不同TDP/电价组合下的成本敏感性’。）

## Search Query

GPU power consumption annual electricity cost LLM inference server
