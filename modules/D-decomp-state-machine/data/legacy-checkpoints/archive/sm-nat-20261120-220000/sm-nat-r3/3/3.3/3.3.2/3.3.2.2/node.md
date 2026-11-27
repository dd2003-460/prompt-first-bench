# N118: 重填充成本对带宽波动的敏感度：若带宽从 100MB/s 降至 50MB/s，cost_refill(10MB) 从 105ms 增至 205ms，增加 95.2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

重填充成本对带宽波动的敏感度：若带宽从 100MB/s 降至 50MB/s，cost_refill(10MB) 从 105ms 增至 205ms，增加 95.2%，表明大对象的重填充成本对带宽波动高度敏感，而小对象（1KB）仅从 5.01ms 增至 5.02ms，敏感度低。

## Corrected Claim

重填充成本对带宽波动的敏感度：若带宽从 100MB/s 降至 50MB/s，cost_refill(10MB) 从 105ms 增至 205ms，增加 95.2%，表明大对象的重填充成本对带宽波动高度敏感，而小对象（1KB）仅从 5.01ms 增至 5.02ms，敏感度低。

## Evidence

先验知识/题面给定，逻辑校验通过：带宽减半导致传输时间翻倍，10MB对象传输时间从100ms增至200ms，加上固定开销后总成本从105ms增至205ms，增幅约95.2%；1KB对象传输时间极短，固定开销主导，总成本变化微小，符合物理直觉与数学推导。
