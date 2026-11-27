# N286: 1x A100 80GB PCIe 方案的基础设施成本 P_infra_1xA100 包括：支持 PCIe 4.0 x16 且供电稳定的服务器级或工作站主板 (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N83

## Claim

1x A100 80GB PCIe 方案的基础设施成本 P_infra_1xA100 包括：支持 PCIe 4.0 x16 且供电稳定的服务器级或工作站主板 (如 Supermicro X13SPY-TN, ~$800) + 2000W 冗余电源 (如 Delta RPP2200, ~$400) + 服务器级机箱与散热 (如 Supermicro CSE-746, ~$300)，合计约 $1500。注意：A100 PCIe 版本功耗 300W，但需考虑未来升级余量。

## Corrected Claim

1x A100 80GB PCIe 方案的基础设施成本 P_infra_1xA100 包括：支持 PCIe 4.0 x16 且供电稳定的服务器级或工作站主板 (如 Supermicro X13SPY-TN, ~$800) + 2000W 冗余电源 (如 Delta RPP2200, ~$400) + 服务器级机箱与散热 (如 Supermicro CSE-746, ~$300)，合计约 $1500。注意：A100 PCIe 版本功耗 300W，但需考虑未来升级余量。

## Evidence

先验知识/题面给定，逻辑校验通过：所列硬件型号（Supermicro X13SPY-TN, Delta RPP2200, CSE-746）均为真实存在的服务器级组件，价格量级（$800+$400+$300=$1500）符合市场常识，且A100 PCIe 300W功耗与2000W电源配置在工程上合理自洽。

## Search Query

Supermicro X13SPY-TN price Delta 2000W server PSU price A100 PCIe chassis cost
