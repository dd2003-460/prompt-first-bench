# N664: OSS IA 层最小存储时长约束：IA 层数据若存储时间 < 30 天即被删除，将额外产生最小存储费用（按 30 天计费），若冷数据中存在短期临时文件（寿命 <

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N240, N241, N242

## Claim

OSS IA 层最小存储时长约束：IA 层数据若存储时间 < 30 天即被删除，将额外产生最小存储费用（按 30 天计费），若冷数据中存在短期临时文件（寿命 < 30 天），需将其排除在 IA 层外或计入额外成本，否则 ¥1,364/年 的估算将低估实际支出。

## Corrected Claim

OSS IA 层数据若存储时间 < 30 天即被删除，将额外产生最小存储费用（按 30 天计费）。若冷数据中存在短期临时文件（寿命 < 30 天），需将其排除在 IA 层外或计入额外成本，否则基于长期存储假设的成本估算将低估实际支出。

## Evidence

[质询]来源仅确认了IA层适用于30天以上数据及存在最小存储时长概念，但未直接提供“¥1,364/年”这一具体估算值的上下文或验证其计算逻辑，且未明确说明“排除在IA层外”是唯一解决方案（也可选择接受额外成本），存在将特定场景估算泛化为通用约束的风险。 | 来源[2]和[3]间接支持IA层有30天最小存储时长约束的逻辑（逻辑自洽），但所有来源均未提及“¥1,364/年”的具体数值，属于经验事实且缺乏直接来源支持。

## Search Query

Alibaba Cloud OSS IA minimum storage duration 30 days fee

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/oss/user-guide/configuration-examples&rut=36e7555a3c0861e28f17e9d9815650ed1385b3536330f7851e1cb55e1c926d00', 'type': 'ddg', 'title': '常见的生命周期配置示例-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://promotion.aliyun.com/ntms/act/ossia.html&rut=c5565e6978fea9d098cca4e9eb6ccdd3ec8754481640eea199320593cbaaac19', 'type': 'ddg', 'title': 'OSS IA全新上线 - 阿里云 - aliyun.com'}
- {'url': 'https://help.aliyun.com/zh/oss/user-guide/overview-54/&rut=5d672e3120595c0c498d342cddf4c250f5e0d77fb94f783febc9e30eb4fb7826', 'type': 'ddg', 'title': '什么是oss生命周期-对象存储 (Oss)-阿里云帮助中心'}
