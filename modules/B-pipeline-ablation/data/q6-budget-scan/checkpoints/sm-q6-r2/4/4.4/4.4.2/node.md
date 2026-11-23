# N69: 带宽预留成本 C_bw_reserve = (Q_peak * s_avg) * P_bw_peak * 24h，其中 P_bw_peak 为峰值带宽单价（通常

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N21

## Claim

带宽预留成本 C_bw_reserve = (Q_peak * s_avg) * P_bw_peak * 24h，其中 P_bw_peak 为峰值带宽单价（通常高于均值带宽单价，需查证厂商阶梯计价），该值决定带宽预留成本

## Corrected Claim

带宽预留成本 C_bw_reserve 通常基于峰值带宽或总流量计算，具体公式取决于厂商计费模式（如按峰值带宽包月或按流量计费），通用估算可表示为 C_bw_reserve ≈ Q_peak * s_avg * P_bw * T，其中 T 为计费周期，P_bw 为对应计费模式的单价。

## Evidence

[质询]公式中的时间单位 '24h' 存在量纲和逻辑疑点：带宽单价通常按 '元/GB' 或 '元/Mbps/月' 计费，若按流量计费，乘以 '24h' 无物理意义；若按峰值带宽包月计费，通常直接乘以月数或天数，而非简单的 '24h' 线性累加，且 '峰值带宽单价' 与 '均值带宽单价' 的对比及阶梯计价细节在通用公式中未体现，属于特定厂商经验参数。 | 来源[1]主题相关（CDN带宽费用计算），但摘要未提供具体公式细节，无法直接支持该特定公式；该公式属于经验性工程估算模型，逻辑上自洽（成本=用量*单价），但缺乏来源直接验证具体系数 '24h' 的合理性，符合经验事实排除条款，判为 degraded。

## Search Query

CDN peak bandwidth pricing tiered model aliyun cloudflare

## Retrieval Sources

- {'url': 'https://developer.baidu.com/article/detail.html?id=5133010&rut=952430d01cc7df48f01763e79ca32ea625e87b615b4e25237d7926f3ad6e37c8', 'type': 'ddg', 'title': '流媒体cdn带宽费用计算全解析：成本优化与策略选择-百度开发者中心'}
