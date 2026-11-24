# N740: 混合云管理场景中，云原生存储管理工具（如 AWS Storage Gateway 或 Azure Blob Sync）的基础实例订阅费为 ¥10,000/年，主

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N277

## Claim

混合云管理场景中，云原生存储管理工具（如 AWS Storage Gateway 或 Azure Blob Sync）的基础实例订阅费为 ¥10,000/年，主要成本构成包括：管理面实例费（t3.small 级别，¥0.1/hour × 8760h ≈ ¥876/年）+ 数据传输 API 调用费（假设月均 10,000 次 API 调用 × $0.0001/次 × 12 月 × 7.2 ≈ ¥864/年）+ 存储网关本地缓存磁盘摊销（200GB SSD，¥2,000/5年 ≈ ¥400/年），其余为服务溢价与支持费。

## Corrected Claim

混合云管理场景中，云原生存储管理工具（如 AWS Storage Gateway）的成本通常由计算实例费、数据传输/API调用费及本地硬件摊销组成。具体金额取决于所选实例规格、数据吞吐量及存储容量，需根据实时官方定价计算，此处提供的¥10,000/年仅为基于特定假设（t3.small, 1万次/月API调用, 200GB SSD）的估算示例。

## Evidence

[质询]该陈述包含具体的经验性价格数据（如基础订阅费¥10,000/年、t3.small实例单价¥0.1/hour、API调用费率$0.0001/次等），这些并非第一性原理可推导的数学或物理事实，而是随时间、地区和市场波动的商业定价信息。参考来源仅介绍了AWS Storage Gateway的功能和应用场景，未提供任何具体的计费标准或价格明细，因此无法验证这些具体数值的准确性。 | 逻辑上各项成本相加（876+864+400=2140）小于总额10000，剩余部分归为服务溢价，算术自洽；但所有具体单价和总价均为经验事实，参考来源[1][2][3]均未提供价格支持，属于缺乏来源支持的估算。

## Search Query

AWS Storage Gateway pricing instance hours API request cost annual

## Retrieval Sources

- {'url': 'https://aws.amazon.com/cn/storagegateway/&rut=90822dfb0b665e638cc29c2699aa90772a751ce1783b590ae4b9f777dac2185a', 'type': 'ddg', 'title': 'AWS Storage Gateway 云存储网关 - AWS云服务'}
- {'url': 'https://blog.csdn.net/awscloud/article/details/145873532&rut=b1de989743fd159e74e0880b4479effe29ae20bf8457b16bbaca291c375c0df4', 'type': 'ddg', 'title': 'Storage Gateway：解锁企业混合云存储的智能钥匙_aws storage gateway应用场景-CSDN博客'}
- {'url': 'https://en.wangsu.com/wp-content/uploads/cloudmanagement/20200225_1.pdf&rut=b0b5c38055e3a9fcb22b1405138718991f505a751c7cb7b4c4ae9924942f7c3b', 'type': 'ddg', 'title': 'PDF AWS Storage Gateway 使用手册'}
