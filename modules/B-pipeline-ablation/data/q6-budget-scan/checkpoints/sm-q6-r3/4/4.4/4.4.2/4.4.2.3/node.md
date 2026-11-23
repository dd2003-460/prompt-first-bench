# N219: 在自建边缘节点场景下，10Gbps静态IP带宽月租单价约为¥8,000-15,000/POP（一线城市），10个POP点总带宽预留成本约为¥80,000-150

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N69, N70, N71

## Claim

在自建边缘节点场景下，10Gbps静态IP带宽月租单价约为¥8,000-15,000/POP（一线城市），10个POP点总带宽预留成本约为¥80,000-150,000/月，高于公有云按流量计费但低于公有云峰值计费

## Corrected Claim

在自建边缘节点场景下，10Gbps静态IP带宽月租单价因运营商和具体POP位置而异，通常高于公有云按流量计费（针对低利用率场景）但低于公有云峰值带宽预留计费（针对高利用率场景）。

## Evidence

[质询]具体数值（¥8,000-15,000/POP）属于经验市场数据，参考来源仅提供了计费模式说明，未提供具体的单价数值，无法直接验证该价格区间的准确性；且不同运营商、具体POP位置及带宽质量（静态IP vs BGP）会导致价格巨大差异，单一区间可能具有误导性。 | 来源[1][2][3]确认了边缘节点和公有云存在带宽计费模式（如固定带宽、按流量），支持了成本结构对比的逻辑框架，但未提供具体单价数值，属于经验事实缺来源直接支持。

## Search Query

China dedicated line 10Gbps monthly rent cost tier-1 city POP point

## Retrieval Sources

- {'url': 'https://cloud.tencent.com/document/product/213/113026&rut=a501ecba2dabcf5954cbd1ff80294dcea4a0d783652de2fc5e517e5e7a9e6f82', 'type': 'ddg', 'title': '云服务器 公网网络费用_腾讯云'}
- {'url': 'https://help.aliyun.com/zh/ens/product-overview/billing-for-bandwidth&rut=ceedc0175b009370a4259435a086d9ed5540d45fbe1d6b7f28d1353c80c3876d', 'type': 'ddg', 'title': '边缘计算服务带宽如何计费及计费项-边缘节点服务 Ens (Ens)-阿里云帮助中心'}
- {'url': 'https://www.alibabacloud.com/help/zh/ens/product-overview/billing-for-bandwidth&rut=192c581dc88cac96e0c634a3e36b9b15716eac2f18db012095f500d2f056b3db', 'type': 'ddg', 'title': '边缘计算服务带宽如何计费及计费项 - 边缘节点服务ens - 阿里云'}
