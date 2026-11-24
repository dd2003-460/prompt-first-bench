# N658: OSS IA 层数据取回（Retrieval）费用单价为 ¥0.03/GB（标准取回）或 ¥0.01/GB（高优先级），若冷数据年访问率为 10%（40TB），

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N238

## Claim

OSS IA 层数据取回（Retrieval）费用单价为 ¥0.03/GB（标准取回）或 ¥0.01/GB（高优先级），若冷数据年访问率为 10%（40TB），则年取回成本 = 40 * 1024 * 0.03 = ¥1,228.8/年（标准）或 ¥409.6/年（高优），此费用独立于存储费。

## Corrected Claim

OSS IA 层数据取回费用单价需查阅最新官方定价页（通常为 ¥0.03/GB 左右），若按此估算，40TB 数据年访问率 10% 的年取回成本约为 ¥1,228.8。注意：高优先级取回通常适用于归档存储而非 IA 层。

## Evidence

[质询]具体单价数值（¥0.03/GB 和 ¥0.01/GB）属于经验事实，参考来源仅提及存在取回费用但未提供具体价格表，无法验证数值准确性；此外，阿里云OSS通常将“高优先级”取回用于归档存储（Archive），而IA（低频访问）通常只有标准取回，此处可能存在存储类型与取回优先级的概念混淆。 | 来源[1]确认OSS收取数据取回费用，但未提供具体单价；计算逻辑（40*1024*0.03=1228.8）正确，但具体价格缺乏直接来源支持，且IA层是否存在“高优先级”取回选项存疑。

## Search Query

Aliyun OSS Infrequent Access retrieval fee per GB

## Retrieval Sources

- {'url': 'https://www.alibabacloud.com/help/zh/oss/data-processing-fees&rut=e38d89eb046a353bd4e9a55687abdf1399762c59d4a426202d26b617b45e19d8', 'type': 'ddg', 'title': 'OSS数据处理费用说明 - 对象存储 OSS - 阿里云 - Alibaba Cloud'}
- {'url': 'https://help.aliyun.com/zh/oss/data-processing-fees&rut=b15fc372b173424fa68a60215fcb09f768069127a2cdba9742a8c1222e9ea8c8', 'type': 'ddg', 'title': 'Oss数据处理费用说明-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1704273&rut=14db771f48c3da8f08d6609f407704c9a549a94f0391bc553853f3e5822bfbcf', 'type': 'ddg', 'title': '2026年阿里云对象存储OSS最新收费标准价格表：'}
