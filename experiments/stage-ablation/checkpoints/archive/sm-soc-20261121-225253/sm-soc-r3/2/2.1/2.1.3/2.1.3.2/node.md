# N73: '降价事件'权重系数 $\omega_{discount}$ 的零假设检验：构建事件研究法（Event Study），以降价事件为断点，对比降价前后72小时内的

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27

## Claim

'降价事件'权重系数 $\omega_{discount}$ 的零假设检验：构建事件研究法（Event Study），以降价事件为断点，对比降价前后72小时内的曝光量变化 $\Delta E_{discount}$；若 $\omega_{discount} \approx 0$，则 $\Delta E_{discount}$ 应落在随机波动范围内（$|\Delta E_{discount}| < 2\sigma_{noise}$），需计算 $\sigma_{noise}$ 基于历史无降价商品的曝光波动率。

## Corrected Claim

在缺乏具体业务数据验证的情况下，该陈述应视为一种合理的方法论假设而非已验证的事实结论：若采用事件研究法检验降价对曝光量的影响，理论上应在零假设下对比降价前后窗口期的曝光量变化与基于历史无降价商品计算的噪声波动范围（如2σ）。

## Evidence

[质询]该陈述属于特定业务场景下的方法论设计（Event Study在电商曝光量上的应用），参考来源均为通用计量经济学教材或习题，未覆盖具体的“降价事件”、“72小时窗口”或“曝光量”等经验性参数，无法提供直接支持。 | 逻辑自洽：事件研究法（Event Study）是检验断点效应的标准方法，零假设下观测值应落在噪声范围内（通常以2σ为界），且噪声标准差需基于无事件期数据估计，符合统计学第一性原理。但参考来源[1][2][3]仅涉及通用回归与假设检验理论，未涉及具体业务场景，属于间接支持/无关，故降级。

## Search Query

event study price discount exposure impact zero weight hypothesis test noise variance

## Retrieval Sources

- {'url': 'https://wenku.baidu.com/view/0ef62b1284c24028915f804d2b160b4e767f81cd.html&rut=99b5441c61c992dbd815820918ec333328f7aed9d9d4ea5f0aca6b53d80079e8', 'type': 'ddg', 'title': '伍德里奇---计量经济学第4章部分计算机习题详解（Matlab）'}
- {'url': 'https://wenku.baidu.com/view/a452b0247fd184254b35eefdc8d376eeaeaa1721.html&rut=a13db74c32996c51e3a23efb17bf523e2e19e9f9e344641a0750568b9c227dc8', 'type': 'ddg', 'title': '伍德里奇---计量经济学第4章部分计算机习题详解（Matlab）'}
- {'url': 'https://zhuanlan.zhihu.com/p/551242484&rut=2de6dce47d6907132b0c6d6af4e5874573e6a079ab9d2e14998bde1c0fcae391', 'type': 'ddg', 'title': '计量经济学：假设检验 - 知乎专栏'}
