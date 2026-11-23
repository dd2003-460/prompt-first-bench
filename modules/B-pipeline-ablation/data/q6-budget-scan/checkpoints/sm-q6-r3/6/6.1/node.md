# N26: 工作点 A（高性低成）：全公有云 CDN 策略下，P99 延迟 ≤ 300ms 时的每千请求成本（¥/1000 req），含带宽+基础设施+运维。

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N6

## Claim

工作点 A（高性低成）：全公有云 CDN 策略下，P99 延迟 ≤ 300ms 时的每千请求成本（¥/1000 req），含带宽+基础设施+运维。

## Corrected Claim

工作点 A（高性低成）：全公有云 CDN 策略下，通常以 P99 延迟 ≤ 300ms 作为性能基准，需结合具体带宽、基础设施及运维开销计算每千请求成本（¥/1000 req）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应带宽、基础设施、运维三大成本组件及最终的聚合计算，符合MECE原则（相互独立、完全穷尽）。带宽成本内部虽区分了两种计费模式，但属于同一维度下的条件分支，不构成节点间的冗余或矛盾；其他组件无重叠。）

## Search Query

Cloudflare Alibaba CDN P99 latency cost per 1000 requests image video platform

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1907850060240257948&rut=f8568459f53c969be6c08e9ce6f128269cd34bc1378fc3538a037e0cd1594e62', 'type': 'ddg', 'title': '运维必懂：监控指标中的 P90、P95、P99，到底是个啥？'}
