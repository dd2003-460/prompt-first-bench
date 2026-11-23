# N309: 多运营商BGP接入带宽成本溢价：若需接入电信+联通+移动三家，带宽单价需乘以 k_multi_carrier = 1.3-1.5，10Gbps多线月租 = 10

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N98

## Claim

多运营商BGP接入带宽成本溢价：若需接入电信+联通+移动三家，带宽单价需乘以 k_multi_carrier = 1.3-1.5，10Gbps多线月租 = 10 * P_single * 1.4 ≈ ¥21000-35000/月（一线城市）

## Corrected Claim

多运营商BGP接入带宽成本溢价：若需接入电信+联通+移动三家，带宽单价需乘以 k_multi_carrier > 1（具体系数视带宽大小和地区而定，通常随带宽增大而降低）。根据来源[1]示例，100M BGP多线月租约为11000元，10Gbps多线月租成本远高于2-3.5万元，具体需参考最新市场报价。

## Evidence

[质询]数值量级与来源数据存在显著偏差：来源[1]显示100M BGP多线月租约11000元（即10Gbps约为110万元/月），而陈述中10Gbps仅为2.1-3.5万元/月，两者相差约30-50倍。陈述中的单价（约2100-3500元/Gbps/月）远低于来源提供的市场参考值（约11000元/100M=110000元/Gbps/月），且未说明是共享带宽、静态IP还是特定促销价格，存在口径混淆或数据过时/错误风险。 | 来源[1]和[3]确认了BGP多线需接入多家运营商且成本独立累加的逻辑（支持k>1的定性结论），但来源[1]的具体报价（100M=11000元）与陈述中的10Gbps总价（2.1-3.5万元）在量级上严重不符，无法直接支持陈述中的具体数值范围，故降级。

## Search Query

China multi-carrier BGP bandwidth cost premium factor telecom unicom mobile

## Retrieval Sources

- {'url': 'https://www.iisidc.cn/archives/62650&rut=01a3bb663d3b525691f738d2c41ff7efcb6df53f125d3ed9d07a22a1ce1f8b18', 'type': 'ddg', 'title': '单线路与bgp多线的报价分别包含哪些内容，服务器带宽价格怎么算 - 简米科技'}
- {'url': 'https://www.htstack.com/news/118856.shtml&rut=9b3ce97eec557fe79a1ca8c65e378c730e47754d5341bc104a80ddc68b83287f', 'type': 'ddg', 'title': 'BGP带宽多少钱一兆？影响价格的关键因素与市场行情解析'}
- {'url': 'https://www.iisidc.cn/archives/38327&rut=e8608adac5e18886c6fd71717c05ec7d8a9ca9b419caf0fc974c5094d3cd8dae', 'type': 'ddg', 'title': 'Bgp多线机房带宽租用费用怎么构成，一年多少钱？ - 简米科技'}
