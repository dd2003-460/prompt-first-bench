# N257: 自建电力与机柜成本：单 POP 平均功耗 5kW（4 服务器 + 网络），电费 ¥0.8/kWh，月电费 = 5 * 24 * 30 * 0.8 = ¥2,88

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82, N83, N84

## Claim

自建电力与机柜成本：单 POP 平均功耗 5kW（4 服务器 + 网络），电费 ¥0.8/kWh，月电费 = 5 * 24 * 30 * 0.8 = ¥2,880；机柜租赁 ¥800/月/柜，单 POP 需 2 柜，机柜费 ¥1,600/月；合计单 POP 电力 + 机柜 = ¥4,480/月，N83 未包含此项。

## Corrected Claim

自建电力与机柜成本：单 POP 平均功耗 5kW（4 服务器 + 网络），电费 ¥0.8/kWh，月电费 = 5 * 24 * 30 * 0.8 = ¥2,880；机柜租赁 ¥800/月/柜，单 POP 需 2 柜，机柜费 ¥1,600/月；合计单 POP 电力 + 机柜 = ¥4,480/月，N83 未包含此项。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（5kW * 720h * 0.8元/kWh = 2880元；2柜 * 800元/柜 = 1600元；合计4480元），参数量级符合行业常识。

## Search Query

data center electricity cost per kW monthly China
