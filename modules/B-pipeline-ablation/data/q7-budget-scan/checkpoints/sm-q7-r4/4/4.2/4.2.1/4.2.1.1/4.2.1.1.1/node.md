# N676: 阿里云 OSS LRS 持久性 11个9（99.999999999%）对应的年化数据丢失字节数 EBL：EBL = (1 - 0.99999999999) * 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N234

## Claim

阿里云 OSS LRS 持久性 11个9（99.999999999%）对应的年化数据丢失字节数 EBL：EBL = (1 - 0.99999999999) * Total_Data_Size = 10^-11 * 500TB = 5KB/年，该数值远低于任何业务可感知阈值，确证持久性成本项在 TCO 中可忽略。

## Corrected Claim

阿里云 OSS LRS 持久性 11个9（99.999999999%）对应的年化数据丢失字节数 EBL：EBL = (1 - 0.99999999999) * Total_Data_Size = 10^-11 * 500TB = 5KB/年，该数值远低于任何业务可感知阈值，确证持久性成本项在 TCO 中可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：11个9持久性对应 $10^{-11}$ 的年丢失率，500TB ($5 	imes 10^{14}$ bytes) 乘以 $10^{-11}$ 等于 $5 	imes 10^3$ bytes (5KB)，计算无误且符合物理直觉。
