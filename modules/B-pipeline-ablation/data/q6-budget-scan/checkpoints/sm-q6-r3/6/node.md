# N26: 公有云CDN带宽计费单价：阿里云/Cloudflare 下行流量单价 P_bw_cloud 约为 ¥0.2-0.5/GB 或 $0.05-0.12/GB，需根据

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

公有云CDN带宽计费单价：阿里云/Cloudflare 下行流量单价 P_bw_cloud 约为 ¥0.2-0.5/GB 或 $0.05-0.12/GB，需根据承诺带宽（Committed Bandwidth）阶梯计价，日均下载2TB对应月成本 ≈ 2TB * 30 * P_bw_cloud

## Corrected Claim

公有云CDN（如阿里云）支持按下行流量或带宽峰值计费，并采用阶梯计价模式；具体单价需参考各厂商最新价目表，日均2TB流量月成本约为60TB乘以对应单价。

## Evidence

[质询]来源仅提供了阿里云的计费模式（按流量/带宽）和阶梯计价逻辑，但未提供具体的单价数值（¥0.2-0.5/GB 或 $0.05-0.12/GB），且未包含 Cloudflare 的价格信息，无法直接验证具体数值范围。 | 来源[1][2][3]确认了阿里云CDN存在按流量和按带宽的计费方式及阶梯计价逻辑，支持了计费模式的描述，但缺乏具体单价数值的直接证据，属于经验事实缺来源支持。

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
