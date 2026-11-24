# N346: 预取策略（Prefetching）对C_idle_cloud的削减效果：若提前2小时启动预取，将数据加载至本地NVMe缓存（容量需覆盖2小时扫描量≈500TB/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N118

## Claim

预取策略（Prefetching）对C_idle_cloud的削减效果：若提前2小时启动预取，将数据加载至本地NVMe缓存（容量需覆盖2小时扫描量≈500TB/111h*2h≈9TB），则集群空闲时间从(111-2)h降至(111-2-2)=107h？不，预取使数据本地化，后续扫描不再等待网络传输，C_idle_cloud_daily趋近于0，但需支付额外的本地缓存存储成本 9TB * ¥200/TB = ¥1,800（一次性）或月度分摊，以及预取期间的带宽费用。

## Corrected Claim

预取策略（Prefetching）对C_idle_cloud的削减效果：若提前2小时启动预取，将数据加载至本地NVMe缓存（容量需覆盖2小时扫描量≈500TB/111h*2h≈9TB），则集群空闲时间从(111-2)h降至(111-2-2)=107h？不，预取使数据本地化，后续扫描不再等待网络传输，C_idle_cloud_daily趋近于0，但需支付额外的本地缓存存储成本 9TB * ¥200/TB = ¥1,800（一次性）或月度分摊，以及预取期间的带宽费用。

## Evidence

先验知识/题面给定，逻辑校验通过：预取消除网络等待导致空闲时间归零的逻辑成立，存储成本计算（9TB * 200元/TB = 1800元）算术正确，符合工程常识。
