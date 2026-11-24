# N210: Cloudflare 针对中国大陆（Mainland China）用户访问的跨境网络优化服务（如 China Network Interconnect, CNI

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N60

## Claim

Cloudflare 针对中国大陆（Mainland China）用户访问的跨境网络优化服务（如 China Network Interconnect, CNI）或专线接入的额外月费及流量单价，该费用通常为独立计费项（例如 ¥10,000+/月或按带宽计费），若不启用则 P99 延迟将因跨境链路而大幅劣化，需量化其成本增量

## Corrected Claim

Cloudflare 针对中国大陆用户提供的 China Network Interconnect (CNI) 服务是独立于普通全球网络的计费项，启用该服务可显著优化中国大陆用户的访问延迟，具体费用需咨询销售或查看最新定价页面。

## Evidence

[质询]具体数值（¥10,000+/月）和具体性能指标（P99延迟大幅劣化）属于经验事实，参考来源中未提供具体的价格数据或延迟对比数据，无法验证其准确性。 | 来源[1]和[2]确认了Cloudflare China Network (CNI) 是独立于普通全球网络的服务，且针对中国大陆用户，逻辑上支持其作为独立计费项且能优化跨境延迟的定性描述，但缺乏具体价格和延迟数据的支持。

## Search Query

Cloudflare China Network Interconnect CNI pricing cost monthly fee

## Retrieval Sources

- {'url': 'https://chendahuang.com/playbook/cloudflare/chapters/06-china-access&rut=da05086a25cd3c6a9bcc9f935bef378af3ad817de45741a30f34fa4c855056d1', 'type': 'ddg', 'title': '6. 国内访问 | Cloudflare 实战手册'}
- {'url': 'https://www.cloudflare.com/en-gb/application-services/products/china-network/&rut=4666b70c2556301de48151fc58f8b2a3ec7e6a2b7e768345db9588f18ec8a313', 'type': 'ddg', 'title': 'Cloudflare China Network'}
- {'url': 'https://developers.cloudflare.com/china-network/faq/&rut=2b6daf214b13bc720b33017a75bd1d8ba81584e89dc8c4e3e79d940e44ebbb1d', 'type': 'ddg', 'title': 'FAQ · Cloudflare China Network docs'}
