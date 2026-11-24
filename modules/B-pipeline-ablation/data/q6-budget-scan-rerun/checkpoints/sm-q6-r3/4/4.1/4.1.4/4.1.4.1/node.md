# N244: 公有云 CDN 弹性伸缩的计费模式判定：阿里云/Cloudflare 按流量计费（GB）而非按带宽峰值（Mbps），因此不存在独立的'弹性伸缩成本'项，C_sc

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N76

## Claim

公有云 CDN 弹性伸缩的计费模式判定：阿里云/Cloudflare 按流量计费（GB）而非按带宽峰值（Mbps），因此不存在独立的'弹性伸缩成本'项，C_scale_pub 在按量计费模型下恒为 0，其影响已包含在基础带宽成本中。

## Corrected Claim

公有云 CDN 弹性伸缩的计费模式判定：阿里云/Cloudflare 按流量计费（GB）而非按带宽峰值（Mbps），因此不存在独立的'弹性伸缩成本'项，C_scale_pub 在按量计费模型下恒为 0，其影响已包含在基础带宽成本中。

## Evidence

先验知识/题面给定，逻辑校验通过：主流公有云CDN（如阿里云、Cloudflare）确实主要采用按流量计费模式，无独立的弹性伸缩成本项，C_scale_pub为0符合计费逻辑。

## Search Query

Alibaba Cloud CDN billing model traffic vs bandwidth peak cost
