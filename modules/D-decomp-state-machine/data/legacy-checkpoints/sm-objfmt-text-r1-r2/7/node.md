# N20: TCO 中的电力成本计算公式为 Annual_Energy_Cost = (GPU_TDP_Watts * 1.1) * Hours_Per_Year * El

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

TCO 中的电力成本计算公式为 Annual_Energy_Cost = (GPU_TDP_Watts * 1.1) * Hours_Per_Year * Electricity_Rate_per_kWh，其中 1.1 代表 PSU 效率损耗及风扇/主板附加功耗；例如 RTX 4090 (450W) 年耗电约 4400 kWh，若电价为 $0.1/kWh，年电费约 $440。

## Corrected Claim

TCO 中的电力成本通常估算为 GPU 功耗乘以效率损耗系数（如1.1）再乘以运行小时数和电价；以 RTX 4090 (450W) 为例，年耗电约 4300-4400 kWh，若电价为 $0.1/kWh，年电费约 $430-$440。

## Evidence

[质询]参考来源均未提供具体的电力成本计算公式或GPU TDP参数，无法验证1.1系数及具体数值计算的准确性，属于缺乏外部证据支持的细节性经验事实。 | 逻辑推导成立（450W*1.1*8760h≈4329kWh，约4400kWh；$0.1/kWh对应$432-$440），但参考来源[1][2][3]仅定义TCO概念，未涉及具体电力成本公式，属经验事实缺来源直接支持。

## Retrieval Sources

- {'url': 'https://www.ibm.com/cn-zh/think/topics/total-cost-of-ownership&rut=81403ae2051e200dd0580f89292ea85ee9d8734f3d60c746ac6d2ab3e80b3a6c', 'type': 'ddg', 'title': '什么是总体拥有成本 (Tco)？| Ibm'}
- {'url': 'https://yunqi.qq.com/read/680958/56&rut=761adb46169584a8015fb95cd2185148cec80bf29cd27a1943e004503c800b56', 'type': 'ddg', 'title': '新一代绿色数据中心的规划与设计 第56章_5.3.1 数据中心总拥有成本法（Tco）-云起书院'}
- {'url': 'https://www.mt.com/cn/zh/home/library/white-papers/product-inspection/pi-total-cost-of-ownership.html&rut=4a0b2cac887aedfa432422fc7c3491e440422f08c9606ca28e934ca79ce7b377', 'type': 'ddg', 'title': '总拥有成本_tco_资本设备-梅特勒托利多官网 - Mettler Toledo'}
