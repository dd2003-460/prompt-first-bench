# N26: 摩擦系数不确定性：当前数值模式（如 HWRF, WRF）中使用的地表摩擦参数化方案（如 Monin-Obukhov 相似理论）在气旋尺度下的适用性存疑，不同模式

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

摩擦系数不确定性：当前数值模式（如 HWRF, WRF）中使用的地表摩擦参数化方案（如 Monin-Obukhov 相似理论）在气旋尺度下的适用性存疑，不同模式间模拟的登陆后风速偏差可达 ±10-20%，源于 z_0 取值和对流混合层高度的参数化差异

## Corrected Claim

当前数值模式（如 HWRF, WRF）中使用的地表摩擦参数化方案在气旋尺度下的适用性存在不确定性，不同模式间模拟的登陆后风速存在显著偏差，主要源于地表粗糙度长度（z_0）及边界层参数化方案的差异。

## Evidence

[质询]具体数值偏差范围（±10-20%）及特定归因（z_0取值和对流混合层高度）缺乏来源直接支持，属于经验事实，现有来源仅泛泛提及参数化不确定性，未提供该特定量级数据。 | 来源[1][2]确认WRF等模式中物理参数化方案（包括边界层/摩擦相关）存在显著不确定性且是误差主要来源，间接支持了‘适用性存疑’和‘存在偏差’的逻辑，但未提供具体的±10-20%数值或特定参数归因，故降级。

## Search Query

uncertainty in surface drag coefficient parameterization for tropical cyclones landfalling numerical models

## Retrieval Sources

- {'url': 'https://blog.csdn.net/islandowner2017/article/details/120804936&rut=2288f3330a265540b4b6cefc8bc3587263cd3ccbe6a273f1cedc8327944e303a', 'type': 'ddg', 'title': 'Wrf系列教程2：物理参数化方案 - Csdn博客'}
- {'url': 'https://faculty.nuist.edu.cn/huangqian/zh_CN/article/53088/content/1354.htm&rut=761f313d7dc466b64860d7af40ef0a2a2351f72e490ceee6de950dc8234d779b', 'type': 'ddg', 'title': '南京信息工程大学主页平台管理系统 黄乾--中文主页--wrf系列教程2：物理参数化方案'}
- {'url': 'https://blog.csdn.net/weixin_43750300/article/details/131325690&rut=7c29e4f1c012c050a477f275645d65a17635ad5f956302895a13fc349d2eb6c7', 'type': 'ddg', 'title': 'WRF进阶：如何增加/耦合新参数化方案至WRF中？WRF如何添加新输入变量_增加wrf便来你高输出-CSDN博客'}
