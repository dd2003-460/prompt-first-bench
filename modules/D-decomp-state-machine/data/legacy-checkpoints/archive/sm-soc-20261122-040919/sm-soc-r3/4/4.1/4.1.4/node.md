# N84: 先验概率 P(H2) 的校准修正项：若平台API文档或技术博客中明确提及'基于成交速度的推荐权重调整'（如k=0.6参数），则 P(H2) 应上调至0.5，因为

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

先验概率 P(H2) 的校准修正项：若平台API文档或技术博客中明确提及'基于成交速度的推荐权重调整'（如k=0.6参数），则 P(H2) 应上调至0.5，因为直接证据支持算法对信号机制的主动干预

## Corrected Claim

若平台API文档或技术博客中明确提及'基于成交速度的推荐权重调整'，则 P(H2) 应基于该直接证据进行上调，具体数值需依据文档提供的参数或实证数据确定，而非固定为0.5。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1定义了基础证据分级与线性修正公式，子节点2引入了参数一致性校验作为条件分支（调整gamma或无效化）。两者在逻辑上是正交的：一个处理证据来源等级，另一个处理证据内部参数的一致性验证。虽然子节点2修改了子节点1中的参数gamma，但这属于条件逻辑的细化，而非重复。完备性方面，父节点核心是‘基于文档/博客提及进行校准’，子节点覆盖了证据等级（来源）和证据有效性（参数一致性），基本覆盖了‘直接证据支持’这一概念的两个关键维度（来源可靠性与内容一致性）。无冗余，因为子节点2不是子节点1的简单参数替换，而是引入了新的校验逻辑（绝对差值判断）。）

## Search Query

second-hand marketplace API documentation recommendation algorithm pricing speed weight

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_40480526/article/details/149435478&rut=cf7e755a1f0baaa0703891c4b89d5d1d5d2eda226bfcb6df2af87556dde61a0f', 'type': 'ddg', 'title': '预测概率的先验校准 - Csdn博客'}
- {'url': 'https://www.cnblogs.com/zhb2000/p/18982246/prior-calibration&rut=63e878ab84a094f6e3a0576ddd080cb2aee52901a218bcb2952554270820ed9e', 'type': 'ddg', 'title': '预测概率的先验校准 - zhb2000 - 博客园'}
- {'url': 'https://blog.csdn.net/cmdos/article/details/149310088&rut=df52d852bd94e8b0dc134d68981430797d1345cd9913fd6a2d5bd8084b3a2d71', 'type': 'ddg', 'title': '预测概率的先验校准 - Csdn博客'}
