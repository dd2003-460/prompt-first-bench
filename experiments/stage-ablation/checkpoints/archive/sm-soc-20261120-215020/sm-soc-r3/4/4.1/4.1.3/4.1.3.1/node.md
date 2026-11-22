# N151: 高质量商品（$q > q^*$）的基准成交周期 $T_{quality}^{base}$ 与低质量商品的差异量化：假设高质量商品因信号效应，其基准成交周期 $T

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

高质量商品（$q > q^*$）的基准成交周期 $T_{quality}^{base}$ 与低质量商品的差异量化：假设高质量商品因信号效应，其基准成交周期 $T_{quality}^{base} = k_{quality} \times T_{avg}^{base}$，其中 $k_{quality} < 1$。需通过数据确定 $k_{quality}$ 的具体值（例如 0.7 或 0.8），以作为计算 $\Delta T_{quality}$ 的基线。

## Corrected Claim

高质量商品（q > q*）的基准成交周期 T_quality^base 可能低于低质量商品，即 T_quality^base = k_quality × T_avg^base 且 k_quality < 1，但 k_quality 的具体数值需通过特定数据集实证确定，无通用固定值。

## Evidence

[质询]该陈述属于特定市场或模型下的经验性参数设定，缺乏通用的理论推导基础或公开数据支持，且参考来源完全无关，无法验证 k_quality 的具体数值或存在性。 | 参考来源[1][2][3]分别涉及托宾Q理论、博世质量原则和制造业QCD概念，均与商品成交周期及质量信号效应无关，无可用外部证据；该事实为经验性假设，逻辑自洽但缺来源支持。

## Search Query

high quality signal effect on transaction time used goods platform

## Retrieval Sources

- {'url': 'https://baike.baidu.com/item/%E6%89%98%E5%AE%BEQ%E7%90%86%E8%AE%BA/5058380&rut=0ec2608869e501297c2fcef5618a2aa312c9c00c4d2664dc16eb35dc1aa8e2e3', 'type': 'ddg', 'title': '托宾q理论 - 百度百科'}
- {'url': 'https://www.zhihu.com/pin/1928701230156353801&rut=01e3e85c54b5eb28646f55332544fd216385e2ee74ba284614698d68e05976f8', 'type': 'ddg', 'title': '博世14个质量原则（14Q-Basics Value Steam） | 博世十四个质量管理原则描述了实现最优质量的基本标准。…'}
- {'url': 'https://zhuanlan.zhihu.com/p/1945879512106645405&rut=59abf5c5fd5b54334237e6fd3130f90313a59241bd2895735fc69ad09f6f7e23', 'type': 'ddg', 'title': '制造业里常说的 Qcd 是什么？一文讲清质量、成本、交付的平衡逻辑'}
