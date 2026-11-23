# N27: 工作点 B（中性价比最优）：混合策略（5 个核心区域自建 POP + 长尾走公有云）下，P99 延迟 ≤ 200ms 时的每千请求成本（¥/1000 req）。

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N6

## Claim

工作点 B（中性价比最优）：混合策略（5 个核心区域自建 POP + 长尾走公有云）下，P99 延迟 ≤ 200ms 时的每千请求成本（¥/1000 req）。

## Corrected Claim

工作点 B（中性价比最优）：混合策略（5 个核心区域自建 POP + 长尾走公有云）下，P99 延迟 ≤ 200ms 时的每千请求成本（¥/1000 req）需根据具体云厂商报价及流量分布模型计算，当前缺乏具体数值支持。

## Evidence

父节点级核验未通过：不完备（子节点涵盖了带宽、基础设施和运维三大主要成本项，分类清晰且互不重叠（正交性良好），无冗余。但存在关键遗漏：1. 缺少计算/服务器运行时的直接资源成本（如CPU/内存占用费，虽然折旧已算，但通常需区分折旧与运行资源，或确认是否包含在 Colo 中，此处 Colo 仅算了电力，未算机柜租金或云主机费用，若自建则需明确硬件采购外的其他费用）；2. 最重要的是，父节点要求计算“每千请求成本”，而子节点仅提供了“月度总成本”，缺少将月总成本转换为“每千请求”所必需的“月请求总量”或“日均请求量”这一关键参数，导致无法直接得出父节点定义的指标。）

## Search Query

hybrid CDN self-built edge node core region cost optimization P99 latency

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/640171988&rut=63c4a50511aeafec2cf4538098dbec6c8c7211039a7e5fa3896ba2b50a1cb26a', 'type': 'ddg', 'title': '第五章 博弈论（2）：混合策略纳什均衡 - 知乎'}
