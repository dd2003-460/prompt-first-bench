# N47: 中国主要互联网骨干网（电信、联通、移动）之间的跨网延迟差异，典型 RTT 差值为 10-30ms，自建 POP 若未部署多线 BGP 接入，P99 延迟将受限于

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

中国主要互联网骨干网（电信、联通、移动）之间的跨网延迟差异，典型 RTT 差值为 10-30ms，自建 POP 若未部署多线 BGP 接入，P99 延迟将受限于跨网调度延迟。

## Corrected Claim

中国主要互联网骨干网（电信、联通、移动）之间存在跨网延迟差异，通常高于同网延迟；自建 POP 若未部署多线 BGP 接入，P99 延迟将受限于跨网调度及路由绕行带来的额外延迟。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点2（跨网RTT差异量化）与子节点4（无BGP接入时的跨网延迟惩罚）存在严重语义重叠和数值冗余。子节点2描述了跨网RTT比同网高10-30ms，子节点4描述无BGP时P99增加15-25ms，两者本质上是描述同一物理现象（跨网调度带来的额外延迟）的不同统计指标（RTT vs P99增量），且数值区间高度重合，缺乏正交性。此外，子节点1（同网跨省RTT）属于背景基线，虽有助于理解差异，但父节点核心关注的是“跨网”差异及BGP影响，子节点1并非父节点逻辑推导的必要组成部分，增加了冗余度。）

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_33686714/article/details/159840568&rut=dfa2a1482bb3d1f3894d2a36e4483838c4ccf8156ba802ce9f23ad926fc89dd5', 'type': 'ddg', 'title': '三大运营商骨干网技术对比：从架构设计到实际性能优化-csdn博客'}
- {'url': 'https://www.htstack.com/news/131446.shtml&rut=c0bb7a4feb6151b43d054f43253a6c210a813a6701f3e9264391a72dd73cbdb4', 'type': 'ddg', 'title': '不同运营商机房 跨网访问 延时多少？实测数据与优化方案全解析'}
- {'url': 'https://juejin.cn/post/7482208912467148838&rut=4109bff7f02c367c4798730251da8d40785c52e531210f6514948664a2b711a3', 'type': 'ddg', 'title': '三大运营商骨干网架构深度剖析：线路建设与用户体验详细分析了中国电信、中国联通、中国移动的互联网线路建设和运营，以及从稳定 - 掘金'}
