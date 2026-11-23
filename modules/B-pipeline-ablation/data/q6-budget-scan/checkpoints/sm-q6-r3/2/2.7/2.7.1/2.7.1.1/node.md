# N285: 高可用性工作点（7x24三班倒）：N_engineers = 6，配置为3个班次x2人（1主1备），确保任意时刻有2名工程师在线响应，故障响应时间SLA < 5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

高可用性工作点（7x24三班倒）：N_engineers = 6，配置为3个班次x2人（1主1备），确保任意时刻有2名工程师在线响应，故障响应时间SLA < 5分钟，适用于P99延迟敏感型业务，人力成本最高但运维风险最低

## Corrected Claim

高可用性工作点（7x24三班倒）：N_engineers = 6，配置为3个班次x2人（1主1备），确保任意时刻有2名工程师在线响应，故障响应时间SLA < 5分钟，适用于P99延迟敏感型业务，人力成本最高但运维风险最低

## Evidence

先验知识/题面给定，逻辑校验通过：6人配置3班次x2人（1主1备）符合7x24高可用标准运维模型，确保任意时刻2人在线，逻辑自洽且量级合理。

## Search Query

SRE team staffing model 7x24 3-shift
