# N113: 公有云CDN因地缘政策导致的服务中断/降级概率 P_cloud_outage 极低（<0.01%），且通常包含在SLA赔付条款内，无额外显性风险溢价成本

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30, N31, N32

## Claim

公有云CDN因地缘政策导致的服务中断/降级概率 P_cloud_outage 极低（<0.01%），且通常包含在SLA赔付条款内，无额外显性风险溢价成本

## Corrected Claim

公有云CDN因地缘政策导致的服务中断/降级概率通常极低，且此类风险通常包含在SLA赔付条款内，一般不产生额外的显性风险溢价成本。

## Evidence

父节点级核验未通过：不完备（子节点1聚焦于概率/频率推导，子节点2聚焦于赔付覆盖/成本计算，两者维度正交且无冗余。但父节点明确提到了“因地缘政策”这一特定风险源，而子节点仅基于通用SLO可用性下限推导概率，未涵盖地缘政治导致的服务中断（如制裁、封锁）这一关键方面，导致完备性不足。）

## Search Query

cloud CDN SLA geopolitical risk compensation clause
