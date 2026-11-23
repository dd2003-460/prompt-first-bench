# N59: 下行带宽成本占比公式：C_down_ratio = (B_down * P_bw_down) / (B_down * P_bw_down + B_up * P_

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N19

## Claim

下行带宽成本占比公式：C_down_ratio = (B_down * P_bw_down) / (B_down * P_bw_down + B_up * P_bw_up)，其中 B_down = 2TB/day, B_up = 200GB/day, P_bw_down/up 为下行/上行带宽单价（通常 P_bw_down > P_bw_up，需查证具体厂商比例）

## Corrected Claim

下行带宽成本占比公式逻辑正确：C_down_ratio = (B_down * P_bw_down) / (B_down * P_bw_down + B_up * P_bw_up)。具体数值 B_down=2TB/day, B_up=200GB/day 及单价比例需根据具体业务场景和厂商报价确定，此处仅为示例假设。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式中的两个关键参数（下行单价、上行单价）、核心计算结果以及敏感性分析，逻辑清晰且互不重叠。虽然敏感性分析部分包含了上行单价的变体，但其目的是展示对最终占比的影响，属于独立的研究维度而非单纯参数罗列，因此不构成冗余。完备性方面，覆盖了参数确定、计算执行及结果解读/敏感性，满足父节点要求。）

## Search Query

CDN bandwidth pricing downlink vs uplink ratio aliyun cloudflare

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/706350338&rut=de20ecac59c16c6056856503b77d88165e7c74b7b0d9244563598f7797e85ead', 'type': 'ddg', 'title': '宽带薪酬设计的18个核心公式，Hr必看! - 知乎'}
