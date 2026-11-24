# N90: 混合策略公有云部分峰值带宽预留成本 C_peak_pub_tail：C_peak_pub_tail = B_peak_pub_tail × unit_cost_

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N22

## Claim

混合策略公有云部分峰值带宽预留成本 C_peak_pub_tail：C_peak_pub_tail = B_peak_pub_tail × unit_cost_pub_per_Mbps_month × 12 / (Total_Annual_Requests / 1000)，其中 B_peak_pub_tail = B_avg_total × R_pg × w_tail = 26.4 Mbps × 3.0 × 0.4 ≈ 31.7 Mbps，unit_cost_pub_per_Mbps_month 需根据阿里云/Cloudflare 按量计费阶梯确定 [时效待核]

## Corrected Claim

混合策略公有云部分峰值带宽预留成本 C_peak_pub_tail 的计算逻辑为：C_peak_pub_tail = B_peak_pub_tail × unit_cost_pub_per_Mbps_month × 12 / (Total_Annual_Requests / 1000)，其中 B_peak_pub_tail 由平均带宽、峰值系数及尾部权重决定，具体数值需依据实际业务流量数据及云厂商当期按量计费阶梯确定。

## Evidence

父节点级核验未通过：有冗余（子节点A和B代表了同一成本函数在两种不同计费策略（按量 vs 预留）下的具体实例。虽然它们在策略上是正交的（互斥的选择），但从知识分解的角度看，它们本质上是同一个变量 `C_peak_pub_tail` 在不同参数配置下的取值，而非两个独立的、不可合并的子概念。父节点已经定义了通用公式，子节点仅提供了两个特定工作点的参数代入，存在结构上的冗余。）

## Search Query

Alibaba Cloud CDN pay-as-you-go bandwidth cost per Mbps per month China 2024

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29235525/article/details/162773768&rut=21a2552a91ccc7af375859c686443a87323b495bd83c77008df658787c235e69', 'type': 'ddg', 'title': 'Cdn 节点成本优化：包端口、95计费、流量计费 3种模式下的配置策略-csdn博客'}
- {'url': 'https://blog.csdn.net/FuncTide/article/details/156679155&rut=030829522b0fda5d95bfd678477c33d545cd534374b279973083831a5c4ea5a3', 'type': 'ddg', 'title': '【Mcp混合架构成本与性能平衡术】：降本40%仍保障高可用的优化逻辑-csdn博客'}
- {'url': 'https://www.ctyun.cn/developer/article/678947566956613&rut=2562919c314d1cd5c2e5ddae652da4c57032340914560c65683c4805981a2e05', 'type': 'ddg', 'title': '弹性伸缩与混合计费模式的成本优化模型-天翼云开发者社区 - 天翼云'}
