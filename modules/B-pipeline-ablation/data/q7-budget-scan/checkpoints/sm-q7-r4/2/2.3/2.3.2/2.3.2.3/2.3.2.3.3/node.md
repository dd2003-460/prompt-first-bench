# N575: 阿里云OSS归档存储GET请求单价为¥0.01/万次（同N73），若冷数据年访问率为10%（40TB），每次访问平均对象大小128KB，则年请求次数 = 40 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N207, N208, N209

## Claim

阿里云OSS归档存储GET请求单价为¥0.01/万次（同N73），若冷数据年访问率为10%（40TB），每次访问平均对象大小128KB，则年请求次数 = 40 * 1024 * 1024 / 128 * 10,000 = 3.2e9 次，年请求成本 = 3.2e9 / 10,000 * 0.01 = ¥3,200，折合每TB年成本 = ¥6.4/TB/年。

## Corrected Claim

基于假设的GET请求单价¥0.01/万次（需核实具体地域及存储类型最新定价，并考虑可能的数据取回费用），若冷数据年访问率为10%（40TB），每次访问平均对象大小128KB，则年请求次数约为3.2e9次，年请求成本约为¥3,200，折合每TB年请求成本约为¥6.4。

## Evidence

[质询]阿里云OSS归档存储（Archive）的GET请求单价并非固定的¥0.01/万次，该价格通常对应于“冷归档”或特定地域/时期的促销价，且归档存储通常涉及数据取回费（Retrieval Fee），仅计算GET请求费会低估总成本；此外，参考来源中未提供具体的单价数值，无法直接验证该经验参数。 | 逻辑推导过程（40TB*10%*1024^2/128KB*10000次/GB换算等）数学上自洽，但参考来源[1][2][3]仅涉及计费模式和存储类型对比，未包含具体的GET请求单价数值，属于经验事实且缺乏直接来源支持。

## Search Query

Alibaba Cloud OSS Archive Storage GET request cost per 10000

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/oss/user-guide/deep-cold-archive-storage-usage-best-practices&rut=ff05bb1049f1f8ca16616c616f530efde79cb96aeef587900ddbdcfbc765b551', 'type': 'ddg', 'title': '使用深度冷归档存储的最佳实践-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://help.aliyun.com/zh/oss/billing-overview&rut=20a4e60b70be8973e18cefcd6f2fb100293e26b95f3592f62bb8694d97cde4f2', 'type': 'ddg', 'title': 'Oss的计费组成、付费方式和定价-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1727772&rut=591bcff50d0edb0cdb0d0b032e619cca4fb8e912bfb8a059b2597bc179282787', 'type': 'ddg', 'title': '阿里云oss储类型对比：标准 / 低频 / 归档 / 冷归档 / 深度冷归档全解析，一文看懂-阿里云开发者社区'}
