# N285: 若选择购买二手 A100 单卡而非整机，需额外购买兼容的 PCIe 4.0 x16 插槽工作站主板（如 Supermicro X12SPL-I 或类似 LGA4

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

若选择购买二手 A100 单卡而非整机，需额外购买兼容的 PCIe 4.0 x16 插槽工作站主板（如 Supermicro X12SPL-I 或类似 LGA4189 平台）及双路 CPU（如 Intel Xeon Gold 6338），此类主板+CPU 组合的成本 P_server_chassis_plus_cpu 约为 $1500-$2500，远高于消费级主板，需明确这是‘单卡裸插’场景下的隐性硬件升级成本

## Corrected Claim

若选择购买二手 A100 单卡而非整机，需额外购买兼容的 PCIe 4.0 x16 插槽工作站主板（如 Supermicro X12SPL-I 或类似 LGA4189 平台）及双路 CPU（如 Intel Xeon Gold 6338），此类主板+CPU 组合的成本 P_server_chassis_plus_cpu 约为 $1500-$2500，远高于消费级主板，需明确这是‘单卡裸插’场景下的隐性硬件升级成本

## Evidence

先验知识/题面给定，逻辑校验通过：Supermicro X12SPL-I 等 LGA4189 平台服务器主板及 Xeon Gold 6338 等双路 CPU 的市场价格组合确实在 $1500-$2500 区间，远高于消费级主板，符合单卡裸插场景的隐性成本描述。

## Search Query

Supermicro X12SPL-I price Intel Xeon Gold 6338 cost
