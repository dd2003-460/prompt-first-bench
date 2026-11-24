# N637: 万兆网卡备件单价 P_NIC 的取值：基于 2024-2025 年主流品牌（如 Intel/Mellanox）10GbE SFP+ 或 25GbE 网卡的市场均

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N218

## Claim

万兆网卡备件单价 P_NIC 的取值：基于 2024-2025 年主流品牌（如 Intel/Mellanox）10GbE SFP+ 或 25GbE 网卡的市场均价，P_NIC 典型区间为 ¥500-¥2,000/张，取决于速率（10G vs 25G）及接口类型（SFP+ vs QSFP），需匹配 N15 中 10Gbps 上行带宽配置。

## Corrected Claim

万兆网卡备件单价 P_NIC 的取值：基于 2024-2025 年市场均价，10GbE 单口/双口网卡典型区间约为 ¥500-¥4,000/张（视品牌、端口数及是否含 RDMA 功能而定），25GbE 网卡价格通常更高，需根据具体速率和接口类型（SFP+/QSFP28）匹配 N15 配置。

## Evidence

[质询]来源[1]显示企业级双口万兆网卡预算为2000-4000元，高于陈述中的上限2000元；且陈述将25GbE（通常需QSFP28接口，价格更高）与10GbE SFP+混同，未区分导致价格区间可能偏低或混淆。 | 来源[1]提供部分支持（工作站800-1500元，二手300-600元），但企业级价格超出陈述上限；来源[2]仅定义概念无价格数据。作为经验事实，缺乏直接覆盖全区间且无矛盾的多源一致证据，故降级。

## Search Query

10GbE 25GbE network interface card price 2024

## Retrieval Sources

- {'url': 'https://b2bwiki.baidu.com/article/740318715988082689&rut=2390e6fc3911889eebf81c62cf41d408652805906e901d87146fde78e565c2d8', 'type': 'ddg', 'title': '万兆网卡价格 - b2bwiki.baidu.com'}
- {'url': 'https://wenku.baidu.com/view/e6b0e156c1da50e2524de518964bcf84b8d52d7e.html&rut=61d3444676480f88d315d2e83b3dcd2ed28cd92779da2f7e471a5f6037eb0d56', 'type': 'ddg', 'title': '2025年中国万兆网卡行业市场全景分析及前景机遇研判报告'}
