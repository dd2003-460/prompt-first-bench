# N26: 多卡互联硬件（如 NVLink 桥接器）及高带宽内存的附加成本需计入多卡方案的初始购置成本中，NVLink 桥接器单价约 $500 [待核验]

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

多卡互联硬件（如 NVLink 桥接器）及高带宽内存的附加成本需计入多卡方案的初始购置成本中，NVLink 桥接器单价约 $500 [待核验]

## Corrected Claim

多卡互联硬件（如 NVLink 桥接器）及高带宽内存的附加成本需计入多卡方案的初始购置成本中，NVLink 相关互联组件的具体单价需根据实际型号和市场行情确定，通常显著高于普通 PCIe 配件。

## Evidence

[质询]参考来源仅讨论GPU互联技术的概念和瓶颈，完全未提及NVLink桥接器的具体价格或任何硬件成本数据，无法验证'$500'这一具体数值。此外，NVLink桥接器（如用于A100/H100的NVSwitch或专用桥接模块）的实际市场价格通常远高于$500（往往在数千美元级别，取决于具体型号和数量），$500的量级可能存在严重低估或混淆了普通PCIe转接卡的价格。 | 来源[1]与事实主题（GPU互联）相关，但仅涉及技术原理，未提供成本数据，属于间接支持或无关；该事实为经验性价格数据，缺乏直接来源支持且数值量级存疑，故降级。

## Search Query

NVLink bridge price cost

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1942166741070386153&rut=c7da1086102d9d43d5db4894cae5e3d33f5a052f7fafb0e82a6f47abbead7d16', 'type': 'ddg', 'title': 'AI芯片重要参数详解（中）GPU互联：Nvlink和其他厂商互联技术'}
