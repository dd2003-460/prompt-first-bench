# N121: 驱动均衡的核心利益相关方识别指标：定义‘均衡驱动力指数’ $D_{driver}$，用于量化买家、卖家、平台三方对当前均衡的贡献度。$D_{driver} = 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

驱动均衡的核心利益相关方识别指标：定义‘均衡驱动力指数’ $D_{driver}$，用于量化买家、卖家、平台三方对当前均衡的贡献度。$D_{driver} = w_s * S_{seller} + w_b * S_{buyer} + w_p * S_{platform}$，其中 $S_{seller}$ 为卖家策略偏离度（如挂价溢价率），$S_{buyer}$ 为买家容忍度（如接受溢价的概率），$S_{platform}$ 为平台激励强度（如流量倾斜系数）。实证数据显示，在二手平台中 $S_{platform}$ 的变异系数 $CV_{platform}$ 通常高于 $S_{seller}$ 和 $S_{buyer}$，表明平台是主要驱动方。

## Corrected Claim

驱动均衡的核心利益相关方识别指标：定义‘均衡驱动力指数’ $D_{driver}$，用于量化买家、卖家、平台三方对当前均衡的贡献度。$D_{driver} = w_s * S_{seller} + w_b * S_{buyer} + w_p * S_{platform}$，其中 $S_{seller}$ 为卖家策略偏离度，$S_{buyer}$ 为买家容忍度，$S_{platform}$ 为平台激励强度。在二手平台中，平台往往通过流量倾斜等机制对均衡产生显著影响，但其变异系数是否通常高于买卖双方需具体实证数据支持。

## Evidence

[质询]陈述中关于二手平台实证数据的具体结论（S_platform 的变异系数通常高于其他方）属于特定领域的经验事实，且参考来源仅提供了通用的驱动因子分析方法论，未包含任何关于二手平台或该特定指标变异性比较的实证数据支持，存在‘无据断言’的风险。 | 逻辑上公式定义自洽，但参考来源[1][2]仅涉及驱动性指标的一般步骤和KDA方法论，与二手平台具体实证数据无关，无法提供外部支持；作为经验事实，缺乏直接来源支持，故降级。

## Retrieval Sources

- {'url': 'https://cp.baidu.com/landing/tscp_doc/97971477709bfd557d89b5918fc00270&rut=21e25cdfbb5579ddf61e4bebf84de10777ca18ef8d5c13fec01769c9015a5ef5', 'type': 'ddg', 'title': '探寻驱动性指标的步骤 - cp.baidu.com'}
- {'url': 'https://zhuanlan.zhihu.com/p/668984453&rut=215ed34cbf9534b6890a1f44fb552c1ee016f97db586cba3db017a87be359671', 'type': 'ddg', 'title': '谷雨知识库：驱动因子分析 (Key Driver Analysis, KDA)'}
