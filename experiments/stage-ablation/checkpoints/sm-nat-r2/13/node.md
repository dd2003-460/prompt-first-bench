# N84: 对象更新率 u=1%/day 导致的额外未命中率增量 ΔH_update 近似为 u * T_res * (1 - H_base)，其中 T_res 为缓存内对

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

对象更新率 u=1%/day 导致的额外未命中率增量 ΔH_update 近似为 u * T_res * (1 - H_base)，其中 T_res 为缓存内对象平均驻留时间，H_base 为无更新时的命中率；当 u*T_res < 0.01 时，该折损可忽略。

## Corrected Claim

对象更新率 u=1%/day 导致的额外未命中率增量 ΔH_update 近似为 u * T_res * (1 - H_base)，其中 T_res 为缓存内对象平均驻留时间，H_base 为无更新时的命中率；当 u*T_res < 0.01 时，该折损可忽略。

## Evidence

公式/推导类，逻辑校验通过，来源未直接覆盖

## Retrieval Sources

- {'url': 'https://www.cnblogs.com/kion/p/17917964.html&rut=22e0f69532e7358f05aa8480ab2372edf2e68af45b9aaa25b77873d8d3a4c0f9', 'type': 'ddg', 'title': 'C++ Thread - miyasaka - 博客园'}
- {'url': 'https://docs.pingcode.com/insights/u8foz7sn3j66r5ijbcac8lk6&rut=a72dd3e4774880f19b340af445a775ed8d37b91c75259993216facf4cb8649fb', 'type': 'ddg', 'title': '缓存命中率低怎么优化 - docs.pingcode.com'}
- {'url': 'https://blog.csdn.net/u012864553/article/details/121307373&rut=e66ac14e1fc119bb26425ed82c87e4b46cb79b2c13fd46383906aa1b53c444d5', 'type': 'ddg', 'title': '缓存管理：Mrc模型与算法解析-csdn博客'}
- {'url': 'https://summerplaceal.com/', 'type': 'bing', 'title': 'Summer Place Apartment Homes | Summer Place'}
