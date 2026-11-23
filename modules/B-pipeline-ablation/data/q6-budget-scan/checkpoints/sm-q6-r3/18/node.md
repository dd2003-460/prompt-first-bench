# N225: 日均请求频率推导公式：QPS_avg = (DAU * Avg_Requests_Per_User) / 86400；假设 DAU=500万，人均日均浏览 20

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

日均请求频率推导公式：QPS_avg = (DAU * Avg_Requests_Per_User) / 86400；假设 DAU=500万，人均日均浏览 20 个对象，则 QPS_avg = 5,000,000 * 20 / 86400 ≈ 1157 QPS；结合峰值系数 1.5，峰值 QPS ≈ 1736 QPS。

## Corrected Claim

日均请求频率推导公式：QPS_avg = (DAU * Avg_Requests_Per_User) / 86400；假设 DAU=500万，人均日均浏览 20 个对象，则 QPS_avg = 5,000,000 * 20 / 86400 ≈ 1157 QPS；结合峰值系数 1.5，峰值 QPS ≈ 1736 QPS。

## Evidence

逻辑推导成立（5,000,000 * 20 / 86400 ≈ 1157.4，1157.4 * 1.5 ≈ 1736.1），且来源[2]提供了基于DAU估算QPS的通用方法论及类似量级的参考案例（DAU 1000万对应均值QPS 1160，与本题DAU 500万对应均值QPS 1157在数量级和逻辑上兼容），来源[3]支持峰值系数1.5-3倍的设计惯例。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/vxzhg/article/details/118548270&rut=a71580f70e826aec1edd976cb328d6219b4137bb270d1e9233827718e929370d', 'type': 'ddg', 'title': 'Qps和并发数和平均耗时的关系以及压测思路 - Csdn博客'}
- {'url': 'https://blog.csdn.net/weixin_34452850/article/details/118929761&rut=bbe737dbc6e60fceef53af326f48b9429a2cd2f3b59659535683228b76669547', 'type': 'ddg', 'title': '根据 DAU 估算 QPS 的一般思路_1万日活大概多少qps-CSDN博客'}
- {'url': 'https://cloud.tencent.com/developer/article/2701516&rut=f7ed684cd5d2aa84f8d3d61f3fd987b9238c6364d07121639aea7bc9aaaec659', 'type': 'ddg', 'title': '【架构】如何预估一个系统的qps？-腾讯云开发者社区-腾讯云'}
