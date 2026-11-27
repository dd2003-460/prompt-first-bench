# N68: 曝光-成交弹性系数 ε_exposure = Δln(Q)/Δln(Exposure)，即曝光量每增加1%带来的成交量变化率；需量化该系数以验证高曝光是否足以抵

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

曝光-成交弹性系数 ε_exposure = Δln(Q)/Δln(Exposure)，即曝光量每增加1%带来的成交量变化率；需量化该系数以验证高曝光是否足以抵消高价格对需求Q的抑制，从而维持短周期成交。

## Corrected Claim

曝光-成交弹性系数 ε_exposure 定义为 Δln(Q)/Δln(Exposure)，用于量化曝光量变化对成交量的影响；该系数需通过具体市场数据回归分析确定，以验证高曝光能否抵消高价格对需求的抑制。

## Evidence

[质询]该陈述定义了一个特定的经济学/营销学弹性系数（曝光-成交弹性），属于经验事实或特定模型假设，无法从第一性原理直接推导其具体数值或普遍有效性；且参考来源均涉及摄影曝光技术，与商业曝光量无关，存在严重的领域混淆风险。 | 逻辑上定义自洽（弹性系数标准定义），但参考来源[1][2][3]均讨论摄影/图像处理中的曝光（Exposure），与商业语境下的曝光量（Impressions/Exposure）无关，无可用外部证据支持该特定商业系数的存在或数值，依据经验事实排除条款降级。

## Search Query

exposure conversion elasticity online marketplace second-hand goods

## Retrieval Sources

- {'url': 'https://blog.csdn.net/lz0499/article/details/168660308&rut=1454717133841d99fe8b718ad9f7f60a710f8dd633a6bc0c1ab6af777cd72042', 'type': 'ddg', 'title': '《Skin Dependent Exposure Correction》响应曲线图形、曝光偏移计算与像素亮度修正详解'}
- {'url': 'https://academy.fengniao.com/33/339579.html&rut=14e39c03cc06bee97a98ee7fe0191947fb144874ae791fa195fe1c2fca5cf6ff', 'type': 'ddg', 'title': '照相机构造原理（14）――曝光方程与apex系统_技法学院-蜂鸟网'}
- {'url': 'https://web.stanford.edu/class/cs231m/project-1/exposure-fusion.pdf&rut=b759fc68bd7382348076a314e3b717fecab7a2d338ec1e6d1b3f7a847adf381b', 'type': 'ddg', 'title': 'PDF Exposure Fusion - Stanford University'}
