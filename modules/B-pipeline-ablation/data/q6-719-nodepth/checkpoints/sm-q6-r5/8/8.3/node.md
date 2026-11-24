# N123: Cloudflare 计费模式对比：Cloudflare 主要采用按流量计费（无严格带宽阶梯，但有公平使用政策），单价约为 $0.08/GB（≈¥0.58/GB

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30

## Claim

Cloudflare 计费模式对比：Cloudflare 主要采用按流量计费（无严格带宽阶梯，但有公平使用政策），单价约为 $0.08/GB（≈¥0.58/GB），与阿里云阶梯计费模式不同，需单独建模。

## Corrected Claim

Cloudflare 主要采用按量计费模式（无严格带宽阶梯，但有公平使用政策），具体单价因产品而异（如R2存储、Workers等），需根据具体服务单独建模，与阿里云阶梯计费模式不同。

## Evidence

[质询]具体单价数值（$0.08/GB）缺乏来源支持，且Cloudflare不同产品（如CDN、Workers、R2）计费模式差异巨大，笼统概括为单一单价存在口径混淆风险。 | 来源[1]仅提及'按量计费'模式，未提供具体单价数值，无法直接支持$0.08/GB这一具体经验参数；逻辑上按流量计费与阶梯计费对比合理，但具体数值缺据。

## Search Query

Cloudflare CDN pricing per GB traffic 2024

## Retrieval Sources

- {'url': 'https://wenku.baidu.com/view/bbedf45cbad5b9f3f90f76c66137ee06eef94e02.html&rut=5f9b851b653d67a1ae65e0506a8ca1cca29a29e428f3aca94ecde1709ca6f36d', 'type': 'ddg', 'title': 'Cloudflare付费套餐全解析：价格、功能对比及升级指南'}
