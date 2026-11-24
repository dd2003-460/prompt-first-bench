# N90: 混合策略公有云部分峰值带宽预留成本 C_peak_pub_tail：C_peak_pub_tail = B_peak_pub_tail × unit_cost_

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N22

## Claim

混合策略公有云部分峰值带宽预留成本 C_peak_pub_tail：C_peak_pub_tail = B_peak_pub_tail × unit_cost_pub_per_Mbps_month × 12 / (Total_Annual_Requests / 1000)，其中 B_peak_pub_tail = B_avg_total × R_pg × w_tail = 26.4 Mbps × 3.0 × 0.4 ≈ 31.7 Mbps，unit_cost_pub_per_Mbps_month 需根据阿里云/Cloudflare 按量计费阶梯确定 [时效待核]

## Corrected Claim

混合策略公有云部分峰值带宽预留成本 C_peak_pub_tail 的计算逻辑为：C_peak_pub_tail = B_peak_pub_tail × unit_cost_pub_per_Mbps_month × 12 / (Total_Annual_Requests / 1000)，其中 B_peak_pub_tail 由平均带宽、峰值系数及尾部权重决定，具体数值需依据实际业务流量数据及云厂商当期按量计费阶梯确定。

## Evidence

[质询]该陈述包含具体的经验参数（如 B_avg_total=26.4 Mbps, R_pg=3.0, w_tail=0.4）以及未确定的单位成本（unit_cost_pub_per_Mbps_month），这些属于特定业务场景下的经验事实或需实时查询的市场价格，无法从第一性原理推导，且参考来源中未提供这些具体数值或阿里云/Cloudflare 的精确阶梯价格，导致无法验证其数值准确性。 | 逻辑推导自洽（公式结构合理，量纲一致），但属于经验事实，参考来源 [1][2][3] 仅涉及 CDN 计费模式原理或混合架构通用优化，未提供该特定场景下的具体带宽数值或精确单价，缺乏直接来源支持。

## Search Query

Alibaba Cloud CDN pay-as-you-go bandwidth cost per Mbps per month China 2024

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29235525/article/details/162773768&rut=21a2552a91ccc7af375859c686443a87323b495bd83c77008df658787c235e69', 'type': 'ddg', 'title': 'Cdn 节点成本优化：包端口、95计费、流量计费 3种模式下的配置策略-csdn博客'}
- {'url': 'https://blog.csdn.net/FuncTide/article/details/156679155&rut=030829522b0fda5d95bfd678477c33d545cd534374b279973083831a5c4ea5a3', 'type': 'ddg', 'title': '【Mcp混合架构成本与性能平衡术】：降本40%仍保障高可用的优化逻辑-csdn博客'}
- {'url': 'https://www.ctyun.cn/developer/article/678947566956613&rut=2562919c314d1cd5c2e5ddae652da4c57032340914560c65683c4805981a2e05', 'type': 'ddg', 'title': '弹性伸缩与混合计费模式的成本优化模型-天翼云开发者社区 - 天翼云'}
