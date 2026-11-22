# N122: 第 t 期转化率 p_conv_t 受信用评分 SCS 影响，公式为 p_conv_t = p_base × (1 + α_scs × (SCS - 500)/

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37, N40, N41

## Claim

第 t 期转化率 p_conv_t 受信用评分 SCS 影响，公式为 p_conv_t = p_base × (1 + α_scs × (SCS - 500)/100)，其中 p_base 为基准转化率（如 5%），α_scs 为敏感度系数（如 0.1）。

## Corrected Claim

第 t 期转化率 p_conv_t 可能受信用评分 SCS 影响，一种可能的建模方式为 p_conv_t = p_base × (1 + α_scs × (SCS - 500)/100)，其中 p_base 和 α_scs 需根据具体业务数据校准。

## Evidence

[质询]该公式为特定业务场景下的经验性参数化模型，并非通用的数学或物理定律。参考来源仅定义了通用的转化率计算概念（如访客转化、债券转换比例），未包含任何关于信用评分（SCS）影响转化率的特定公式、系数（α_scs）或基准值（p_base）。因此，该具体公式缺乏外部来源支持，属于未经验证的经验假设。 | 逻辑上公式结构自洽（线性调整模型），但参考来源[1][2][3]仅涉及通用转化率定义或金融转换比率，与信用评分影响转化率的特定业务逻辑无关，无法提供直接支持。

## Search Query

conversion rate p_conv formula credit score SCS sensitivity coefficient alpha

## Retrieval Sources

- {'url': 'https://wisernotify.com/blog/how-to-calculate-conversion-rate/&rut=d60e868bd25e29920b3bdf10f55d63b4dd46ac336a53978f93caf3a5f96cb863', 'type': 'ddg', 'title': 'How to Calculate Conversion Rate (Formula + Examples)'}
- {'url': 'https://www.waterfalls.app/learn/conversion-ratio-definition-calculation-methods/&rut=89b3788ec26369ddbee5bc18443d622c2c3093238db2cd11ec08238b8ed26ff2', 'type': 'ddg', 'title': 'Conversion Ratio: How to Calculate It (With Worked Examples)'}
- {'url': 'https://www.wallstreetprep.com/knowledge/conversion-rate/&rut=f2514acbc918fcc7e27edf2ca6b19df5733ae8095377e9ec93420027b9570679', 'type': 'ddg', 'title': 'Conversion Rate | Formula + Calculator - Wall Street Prep'}
