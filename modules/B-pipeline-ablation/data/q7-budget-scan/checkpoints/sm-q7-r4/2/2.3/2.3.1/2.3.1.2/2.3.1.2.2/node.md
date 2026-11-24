# N554: OSS 公网流出流量单价查证：需核实阿里云 OSS 公网流出流量单价，通常约为 ¥0.5 / GB（具体以官网实时定价为准）。

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N182

## Claim

OSS 公网流出流量单价查证：需核实阿里云 OSS 公网流出流量单价，通常约为 ¥0.5 / GB（具体以官网实时定价为准）。

## Corrected Claim

阿里云 OSS 公网流出流量单价需以官网实时定价为准，通常量级在 ¥0.5/GB 左右（具体因地域和优惠策略而异）。

## Evidence

[质询]具体数值 ¥0.5/GB 属于经验事实（价格参数），参考来源仅提供了计费项定义和链接，未直接提供该具体数值，且阿里云 OSS 公网流出流量价格随地域、资源包及时间变化，可能存在偏差。 | 来源 [1][2][3] 确认了 OSS 存在公网流出流量计费项，但未直接列出 ¥0.5/GB 的具体单价；该数值符合行业常见量级，逻辑自洽，但因缺乏直接来源支持具体数值，依据经验事实排除条款降级。

## Search Query

Alibaba Cloud OSS public network data transfer out price per GB

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/oss/traffic-fees&rut=c2fe1ce0123449071f15817310ba52a8b5688d93d41bd2fe07f2789403b93fd9', 'type': 'ddg', 'title': '流量费用-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://help.aliyun.com/zh/oss/billing-overview&rut=20a4e60b70be8973e18cefcd6f2fb100293e26b95f3592f62bb8694d97cde4f2', 'type': 'ddg', 'title': 'Oss的计费组成、付费方式和定价-对象存储 (Oss)-阿里云帮助中心'}
- {'url': 'https://www.alibabacloud.com/help/zh/oss/traffic-fees&rut=885913b8a739f992a64441e8d8da6088b539e63f22106c45220446d0c024e7b1', 'type': 'ddg', 'title': '流量费用 - 对象存储 OSS - 阿里云 - Alibaba Cloud'}
