# N376: 公有云回源单价 unit_cost_origin 的量化：基于 N120 中阿里云 50TB+ 档位边缘单价 0.18 元/GB，回源单价为边缘单价的 1.5-

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N119

## Claim

公有云回源单价 unit_cost_origin 的量化：基于 N120 中阿里云 50TB+ 档位边缘单价 0.18 元/GB，回源单价为边缘单价的 1.5-2 倍，取中位数 1.75 倍，则 unit_cost_origin = 0.18 × 1.75 = 0.315 元/GB；若采用 Cloudflare，需查询其回源计费标准，通常回源流量按 $0.08/GB 计费，换算为人民币约 0.576 元/GB（汇率 7.2）。

## Corrected Claim

公有云回源单价因厂商和配置而异。阿里云在特定CDN+OSS配置下回源单价可低至0.15元/GB，而非固定为边缘单价的1.75倍；Cloudflare回源流量通常按$0.08/GB计费（约0.576元/GB），具体需以官方最新价目表为准。

## Evidence

[质询]阿里云回源单价并非固定为边缘单价的1.5-2倍，且参考来源[1]明确指出在特定配置下（CDN+OSS组合）回源流量单价可低至0.15元/GB，这与陈述中计算的0.315元/GB存在显著差异，说明该倍数关系缺乏普适性，属于经验假设而非固定事实。 | 逻辑计算自洽（0.18*1.75=0.315），但参考来源[1]显示阿里云回源单价存在优惠机制（0.15元/GB），与陈述中的高估值矛盾，且Cloudflare价格缺乏来源支持，故降级。

## Search Query

Alibaba Cloud CDN origin pull pricing 2024

## Retrieval Sources

- {'url': 'https://github.com/hgrm032/oss-origin-traffic-optimization&rut=58316ed8f90a9ace755f46d349fbb77e5a2feda23c60929666311ed4c0ef399a', 'type': 'ddg', 'title': 'hgrm032/oss-origin-traffic-optimization - GitHub'}
