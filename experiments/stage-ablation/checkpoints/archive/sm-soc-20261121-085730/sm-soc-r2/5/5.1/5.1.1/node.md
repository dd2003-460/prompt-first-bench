# N105: 数据质量 q_data 的量化指标：q_data = 1 - (σ_error / σ_signal)，其中σ_error为数据噪声标准差，σ_signal为信

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

数据质量 q_data 的量化指标：q_data = 1 - (σ_error / σ_signal)，其中σ_error为数据噪声标准差，σ_signal为信号标准差，通常二手平台数据质量q_data在0.7-0.9之间[待核验]

## Corrected Claim

数据质量 q_data 可定义为 1 - (σ_error / σ_signal)（其中 σ_error 为噪声标准差，σ_signal 为信号标准差），但二手平台数据质量的具体数值范围因数据源和评估维度而异，通常需通过具体样本计算得出，不宜直接断定为 0.7-0.9。

## Evidence

[质询]该公式 q_data = 1 - (σ_error / σ_signal) 并非数据质量评估领域的通用标准定义（通常使用信噪比 SNR 或相关系数），且“二手平台数据质量在 0.7-0.9 之间”属于缺乏广泛共识的经验性断言，不同平台、不同数据维度（如价格、描述、图片）的质量差异巨大，该数值范围缺乏普适性依据。 | 参考来源 [1][2][3] 仅泛泛提及数据质量评估指标（如准确率、RMSE），未提供该特定公式或二手平台数据质量的具体数值范围，属于经验事实且缺乏直接来源支持。

## Search Query

data quality metric signal to noise ratio e-commerce transaction data

## Retrieval Sources

- {'url': 'https://blog.csdn.net/universsky2015/article/details/137296952&rut=aeb33202d180ee4c79df5d2a1e996e721d551cd5603dfbbf597f4f82bd1bba47', 'type': 'ddg', 'title': '数据质量评估：标准与指标 - Csdn博客'}
- {'url': 'https://blog.csdn.net/weixin_43156294/article/details/147795979&rut=2f8ea48a9ed27ccf0686db6bbf52325fe0cf737fa403ad6db37961486037f0f6', 'type': 'ddg', 'title': '数据质量评估标准与指标_数据质量评估模型-csdn博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/135786091&rut=1d290f0c07e548b7959f6d21d39708ad43642f9b72264f538763a27680f1c724', 'type': 'ddg', 'title': '数据分析中的数据质量评估与数据质量控制技巧_数据分析_禅与计算机程序设计艺术-腾讯云开发者社区'}
