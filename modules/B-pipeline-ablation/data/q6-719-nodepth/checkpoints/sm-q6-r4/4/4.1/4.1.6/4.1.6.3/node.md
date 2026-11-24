# N253: 公有云CDN扩容边际成本：若从基础版（100Gbps）升级至企业版（500Gbps），月度费用增量 ΔC_cloud_upgrade = C_enterpris

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N82, N83, N84

## Claim

公有云CDN扩容边际成本：若从基础版（100Gbps）升级至企业版（500Gbps），月度费用增量 ΔC_cloud_upgrade = C_enterprise - C_basic；假设基础版 ¥12,690/月，企业版按量计费单价降低 20% 但固定费用增加 ¥5,000/月，则 ΔC ≈ ¥2,500/月，需对比自建扩容成本。

## Corrected Claim

公有云CDN扩容边际成本取决于具体厂商的计费模式（如按带宽峰值、按流量或95计费）。从基础版升级至企业版通常涉及固定费用增加与单位流量/带宽单价降低的权衡，具体月度费用增量需依据所选云服务商的官方价格表及实际业务量进行测算，不能简单套用固定数值。

## Evidence

[质询]该陈述中的具体数值（基础版¥12,690/月、企业版固定费用增加¥5,000/月、单价降低20%）属于特定厂商或特定场景下的经验性假设，并非公有云CDN的通用标准或第一性原理可推导的数学事实。参考来源中未包含任何支持这些具体金额或计费结构变化的数据，且不同云厂商（如阿里云、腾讯云、Google Cloud）的计费模式差异巨大，无法从现有来源验证该特定计算模型的真实性。 | 逻辑上算术自洽（若假设成立，增量计算无误），但作为经验事实，缺乏来源直接支持具体数值，且来源[1][2][3]仅展示通用计费模式或不同厂商价格，未覆盖该特定升级场景的成本结构，故降级为定性表述。

## Search Query

Alibaba Cloud CDN enterprise vs basic pricing difference upgrade cost

## Retrieval Sources

- {'url': 'https://cloud.google.com/cdn/pricing?hl=zh-cn&rut=74fac12a2c12ad0f3ff9712259e6fb7f4eb556c23cf368ae2dd79e79f2660348', 'type': 'ddg', 'title': 'Cloud CDN 价格 | Google Cloud'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://cloud.tencent.com/developer/article/2790741&rut=679370241cca038cfe310fd96a9d33db5c91893e3b9551253a2eaa8256441c10', 'type': 'ddg', 'title': '网站要不要上 Cdn：17 元 100gb 流量包与服务器带宽的成本分界点-腾讯云开发者社区-腾讯云'}
