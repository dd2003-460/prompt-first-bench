# N246: 机柜租赁单价 P_rack 的地理分布差异：一线城市（北京/上海）P_rack_high ≈ ¥8k-10k/rack/月，二三线城市 P_rack_low ≈

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N77

## Claim

机柜租赁单价 P_rack 的地理分布差异：一线城市（北京/上海）P_rack_high ≈ ¥8k-10k/rack/月，二三线城市 P_rack_low ≈ ¥3k-5k/rack/月，需根据10个POP的具体选址加权计算

## Corrected Claim

机柜租赁单价 P_rack 存在显著地理分布差异：一线城市（如上海）价格通常高于二三线及偏远地区（如内蒙），具体单价受机柜功率、带宽及服务商影响，市场区间约为 ¥2k-20k/rack/月，一线城市常见报价可能在 ¥4k-10k+ 区间，需根据具体POP选址及配置加权计算。

## Evidence

[质询]数值量级偏高且口径可能混淆：来源[1]显示上海浦东20A机柜约4000元/月，来源[2]显示全国范围2000-20000元/月，而陈述中一线城市8k-10k/rack/月处于高位区间，可能混淆了标准机柜与高功率/托管服务价格，或仅适用于特定高端场景，缺乏普遍性直接支持。 | 来源[1]和[2]证实了地域价格差异的存在（上海高于内蒙，全国区间2k-20k），但具体数值8k-10k仅落在来源[2]的宽泛区间内，且来源[1]的具体案例（4k）低于该值，属于间接支持，无法排除其他定价可能性。

## Search Query

China data center rack rental cost by city 2023 2024

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/665496676&rut=3bf14b8cb8dc7e8e6524b3412331e9ce53261eda603bfabb3370c7b505425e87', 'type': 'ddg', 'title': '数据中心机柜租赁价格表，收费标准如何？ - 知乎'}
- {'url': 'https://www.sohu.com/a/954382417_121961969&rut=384c2ae1c45fefcd35ce00dd39c55aa75b1c2c87295a40bde10afa40c6538cb5', 'type': 'ddg', 'title': 'IDC机房机柜租赁一个多少钱？999吗_成本_创云_Mbps - 搜狐'}
