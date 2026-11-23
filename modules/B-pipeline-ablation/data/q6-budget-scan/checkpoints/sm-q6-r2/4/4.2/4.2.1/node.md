# N59: 下行带宽成本占比公式：C_down_ratio = (B_down * P_bw_down) / (B_down * P_bw_down + B_up * P_

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

下行带宽成本占比公式：C_down_ratio = (B_down * P_bw_down) / (B_down * P_bw_down + B_up * P_bw_up)，其中 B_down = 2TB/day, B_up = 200GB/day, P_bw_down/up 为下行/上行带宽单价（通常 P_bw_down > P_bw_up，需查证具体厂商比例）

## Corrected Claim

下行带宽成本占比公式逻辑正确：C_down_ratio = (B_down * P_bw_down) / (B_down * P_bw_down + B_up * P_bw_up)。具体数值 B_down=2TB/day, B_up=200GB/day 及单价比例需根据具体业务场景和厂商报价确定，此处仅为示例假设。

## Evidence

[质询]参考来源[1]主题为HR宽带薪酬设计，与网络带宽成本计算完全无关，无法提供外部支持；且具体数值（2TB/200GB）及单价比例属于特定场景假设或经验数据，缺乏通用性验证。 | 公式逻辑自洽（成本占比=下行成本/总成本），但参考来源[1]与主题无关，且具体参数为经验事实，无有效来源支持，故降级。

## Search Query

CDN bandwidth pricing downlink vs uplink ratio aliyun cloudflare

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/706350338&rut=de20ecac59c16c6056856503b77d88165e7c74b7b0d9244563598f7797e85ead', 'type': 'ddg', 'title': '宽带薪酬设计的18个核心公式，Hr必看! - 知乎'}
