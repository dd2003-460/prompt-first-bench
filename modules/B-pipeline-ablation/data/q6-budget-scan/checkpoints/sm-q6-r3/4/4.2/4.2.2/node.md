# N60: 上行带宽单价与下行带宽单价之比：r_bw = P_bw_up / P_bw_down，通常 r_bw ≈ 0.1-0.5（上行带宽远便宜于下行），需查证主流公有

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N19

## Claim

上行带宽单价与下行带宽单价之比：r_bw = P_bw_up / P_bw_down，通常 r_bw ≈ 0.1-0.5（上行带宽远便宜于下行），需查证主流公有云 CDN 的具体计费比例

## Corrected Claim

上行带宽单价通常高于或等于下行带宽单价，具体比例取决于运营商策略，但通常不存在上行远便宜于下行的情况（r_bw 通常 >= 1 或接近 1，而非 0.1-0.5）。

## Evidence

[质询]事实陈述与参考来源及普遍市场常识直接矛盾。参考来源[1]标题及内容明确指出“宽带上行价格比下行贵”，且解释了因业务模型不对称（下行需求大、上行稀缺或建设成本高）导致上行更贵。陈述中“上行带宽远便宜于下行”及“r_bw ≈ 0.1-0.5”的结论与来源信息完全相反。 | 来源[1]明确指向上行价格高于下行，与陈述中的比例关系（上行便宜）矛盾。

## Search Query

CDN uplink bandwidth price vs downlink price ratio

## Retrieval Sources

- {'url': 'https://www.toutiao.com/article/7324956592288350747/&rut=07bcfc9da594fd63275fbfe8cab9bd801fd8217039b14caf87f8257eeb98020e', 'type': 'ddg', 'title': '为什么你的宽带上行价格比下行贵？一文解答所有疑惑!'}
