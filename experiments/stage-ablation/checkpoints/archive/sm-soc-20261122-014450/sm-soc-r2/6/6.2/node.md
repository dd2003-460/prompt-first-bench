# N113: 平台曝光权重超额效应量化：计算高挂价商品（P_list=1.2*P_mkt）相对于市场均价商品的曝光倍数 R_exposure = W(1.2*P_mkt)/W

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35

## Claim

平台曝光权重超额效应量化：计算高挂价商品（P_list=1.2*P_mkt）相对于市场均价商品的曝光倍数 R_exposure = W(1.2*P_mkt)/W(P_mkt)，假设CTR恒定，需证明R_exposure > 1.15以抵消需求损失。

## Corrected Claim

平台曝光权重超额效应量化：需计算高挂价商品（P_list=1.2*P_mkt）相对于市场均价商品的曝光倍数 R_exposure，并验证其是否足以抵消需求损失（具体阈值需根据实际平台数据或模型校准确定，而非固定为1.15）。

## Evidence

[质询]该陈述包含具体的量化阈值（R_exposure > 1.15）和特定的价格倍数关系（1.2*P_mkt），这属于经验性参数或特定模型假设，无法从第一性原理推导，且参考来源仅讨论权重影响因素，未提供具体的曝光倍数计算公式或阈值数据，存在来源不支持具体数值的风险。 | 逻辑上自洽（高挂价通常伴随高权重或特定策略下的曝光变化，需量化抵消需求损失），但参考来源[1]仅定性描述权重因素，未提供R_exposure的具体计算值或1.15阈值的依据，属于经验事实且缺乏直接来源支持。

## Search Query

platform algorithm exposure weight price bias marketplace study

## Retrieval Sources

- {'url': 'https://bk.taobao.com/k/wangdianSEO_19115/f5380b38236d8e98bb4880ec7a45e340.html&rut=7027c85b3659067863450a498c8f8394ae16fce4c733a8f4b20e58c39bdedff6', 'type': 'ddg', 'title': '网店权重到底怎么算？7大关键因素影响搜索排名，你中招了吗？'}
