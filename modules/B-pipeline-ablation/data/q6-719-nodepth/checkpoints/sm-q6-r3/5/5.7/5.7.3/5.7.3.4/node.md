# N344: 公有云CDN服务中断概率 P_outage 的独立估算：区别于SLA中的月度不可用时长（N117），此处需考虑“导致显著P99延迟劣化”的事件概率。基于阿里云/

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N119

## Claim

公有云CDN服务中断概率 P_outage 的独立估算：区别于SLA中的月度不可用时长（N117），此处需考虑“导致显著P99延迟劣化”的事件概率。基于阿里云/Cloudflare历史SLA报告，月均发生P99延迟超过阈值（如>500ms）且持续>5分钟的频率约为 1-3 次/年，即 P_outage_annual = 0.08-0.25，月均 P_outage_monthly ≈ 0.007-0.02。

## Corrected Claim

公有云CDN服务中，导致显著P99延迟劣化（如>500ms且持续>5分钟）的事件频率因监控口径和阈值定义而异，通常高于传统SLA定义的“服务中断”频率；具体数值（如1-3次/年）需基于特定服务商的历史监控数据估算，非通用公开标准。

## Evidence

[质询]该陈述将“P99延迟劣化”等同于“服务中断（Outage）”，且引用的具体频率（1-3次/年）缺乏公开权威数据支持。阿里云和Cloudflare的SLA通常定义“不可用”为完全无法访问或严重错误，而非P99延迟超过500ms；延迟劣化在CDN中极为常见（受网络抖动、源站响应影响），其发生频率远高于“服务中断”，且不同阈值（500ms）下的具体统计值属于高度依赖特定监控口径的经验数据，非通用公开事实。 | 参考来源[1]仅讨论云主机SLA赔偿规则，未涉及CDN延迟劣化频率或P99阈值统计，与该事实主题不匹配，无可用外部证据支持具体数值；该数值属于经验事实，逻辑上量级合理（0.08-0.25/年对应约1-3次），但缺乏来源直接支持，故降级。

## Search Query

cloud CDN monthly probability of significant latency degradation events SLA report

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2084274840274466495&rut=968668ea9d2e3c9a12eccf09576bd36a02b15cba81953e770ab64835cea9b82e', 'type': 'ddg', 'title': '海外云主机 Sla 对比：可用性承诺、赔偿规则和故障恢复能力'}
