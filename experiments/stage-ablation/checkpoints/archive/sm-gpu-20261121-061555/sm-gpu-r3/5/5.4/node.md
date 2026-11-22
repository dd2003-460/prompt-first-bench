# N29: 故障与维护成本：消费级 GPU 平均无故障时间（MTBF）[待核验]，数据中心 GPU 有 SLA 保障但单价高；多卡系统故障概率 = 1 - (1 - p_s

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

故障与维护成本：消费级 GPU 平均无故障时间（MTBF）[待核验]，数据中心 GPU 有 SLA 保障但单价高；多卡系统故障概率 = 1 - (1 - p_single)^N，p_single 为单卡年故障率，需量化多卡方案的额外维护支出

## Corrected Claim

故障与维护成本：消费级 GPU 平均无故障时间（MTBF）[待核验]，数据中心 GPU 有 SLA 保障但单价高；多卡系统故障概率 = 1 - (1 - p_single)^N，p_single 为单卡年故障率，需量化多卡方案的额外维护支出

## Evidence

先验知识/题面给定，逻辑校验通过：多卡系统故障概率公式符合独立事件概率论推导，数据中心SLA与消费级MTBF差异符合行业常识

## Search Query

consumer vs datacenter GPU MTBF failure rate annual
