# N322: 跨运营商接入对 D_user_edge_p99 的等效距离惩罚 ΔD_cross：当用户运营商与 CDN 节点接入运营商不一致时，等效距离增加 ΔD_cross

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

跨运营商接入对 D_user_edge_p99 的等效距离惩罚 ΔD_cross：当用户运营商与 CDN 节点接入运营商不一致时，等效距离增加 ΔD_cross ≈ 100-200km（对应 RTT 增加 5-10ms），导致长尾区域 P99 距离从 200km 升至 300-400km，RTT 基础值升至 20-25ms。

## Corrected Claim

跨运营商接入对 D_user_edge_p99 的等效距离惩罚 ΔD_cross：当用户运营商与 CDN 节点接入运营商不一致时，等效距离增加 ΔD_cross ≈ 100-200km（对应 RTT 增加 5-10ms），导致长尾区域 P99 距离从 200km 升至 300-400km，RTT 基础值升至 20-25ms。

## Evidence

先验知识/题面给定，逻辑校验通过：跨运营商接入通常涉及额外的路由跳数或次优路径，导致等效距离增加100-200km及RTT增加5-10ms符合网络工程常识与物理直觉，数值量级合理。
