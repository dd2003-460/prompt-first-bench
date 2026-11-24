# N100: 安全工具链成本分解：Security_Cost = 10 × (WAF_Throughput_Cost + IDS_Sensor_License) + 1 × 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

安全工具链成本分解：Security_Cost = 10 × (WAF_Throughput_Cost + IDS_Sensor_License) + 1 × SOC_Integration_Fee，其中 WAF_Throughput_Cost 由单 POP 峰值 QPS 及规则复杂度决定，IDS_Sensor_License 由流量监控带宽决定。

## Corrected Claim

安全工具链成本分解：Security_Cost = 10 × (WAF_Throughput_Cost + IDS_Sensor_License) + 1 × SOC_Integration_Fee，其中 WAF_Throughput_Cost 由单 POP 峰值 QPS 及规则复杂度决定，IDS_Sensor_License 由流量监控带宽决定。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点公式中的三个独立变量（WAF、IDS、SOC），定义清晰且互不重叠，覆盖了所有关键成本项，且各自具有独立的计算逻辑和参数来源，不存在冗余。）

## Search Query

WAF cost per QPS IDS license per bandwidth SOC integration fee
