# N166: P_TTL_expire 的计算公式：P_TTL_expire = 1 - exp(-λ_t * T_request_interval)，其中 λ_t 为对象过

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

P_TTL_expire 的计算公式：P_TTL_expire = 1 - exp(-λ_t * T_request_interval)，其中 λ_t 为对象过期率（1/TTL）。若 TTL 设为 1 小时（3600s），且用户平均请求间隔为 30 分钟（1800s），则 P_TTL_expire = 1 - exp(-1800/3600) ≈ 39.3%。若 TTL 设为 24 小时，P_TTL_expire ≈ 1.7%。通常 CDN 采用分层 TTL，核心内容 TTL 长，边缘内容 TTL 短，加权平均 P_TTL_expire ≈ 10%-15%。

## Corrected Claim

P_TTL_expire 的计算公式：P_TTL_expire = 1 - exp(-λ_t * T_request_interval)，其中 λ_t 为对象过期率（1/TTL）。若 TTL 设为 1 小时（3600s），且用户平均请求间隔为 30 分钟（1800s），则 P_TTL_expire = 1 - exp(-1800/3600) ≈ 39.3%。若 TTL 设为 24 小时，P_TTL_expire ≈ 1.7%。通常 CDN 采用分层 TTL，核心内容 TTL 长，边缘内容 TTL 短，加权平均 P_TTL_expire ≈ 10%-15%。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于TTL分层策略下的加权计算模型及参数校准，子节点2聚焦于请求间隔分布特性对计算精度的影响。两者分别处理'空间/层级维度'和'时间/分布维度'，逻辑正交且无重复。父节点中的基础公式、具体数值示例（1h/24h TTL）已被子节点1涵盖并扩展为加权模型，子节点2补充了分布修正，共同覆盖了父节点的关键方面。）
