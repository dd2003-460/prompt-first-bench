# N403: 马太效应系数 w_signal 的量化定义：w_signal 定义为平台算法赋予‘快速成交’标签商品的额外曝光权重，具体数值需通过平台流量分配日志数据计算，通常

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N123

## Claim

马太效应系数 w_signal 的量化定义：w_signal 定义为平台算法赋予‘快速成交’标签商品的额外曝光权重，具体数值需通过平台流量分配日志数据计算，通常 w_signal > 0.3 表示显著的马太效应。

## Corrected Claim

马太效应系数（如 w_signal）通常定义为平台算法赋予特定标签商品的额外曝光权重，其具体数值需通过平台流量分配日志数据计算；显著的马太效应通常表现为该系数显著大于零（具体阈值依模型而定）。

## Evidence

[质询]该陈述中的具体阈值（w_signal > 0.3）及特定变量名（w_signal）缺乏通用学术或行业标准支持，属于特定模型或内部定义的参数，参考来源未提供此具体数值定义，存在将特定案例参数泛化为通用标准的风险。 | 参考来源[1]讨论了马太效应的测度方法（如马太系数），但未提及'w_signal'这一特定变量或'0.3'这一具体阈值，属于经验事实且缺乏直接来源支持，逻辑上自洽但需降级为定性表述。

## Search Query

platform algorithm traffic allocation weight for fast-selling items

## Retrieval Sources

- {'url': 'https://xueshu.baidu.com/usercenter/paper/show?paperid=1r340850pe0408b0qb7p0au0uh754202&rut=7878e2f9ca21681b5e97f0e9176a08c8acf0fec84e2991c00313813dd1ab2279', 'type': 'ddg', 'title': '马太效应测度:一种新的方法与应用 - 百度 ... - 百度学术'}
