# N147: P_cooling_hardware（散热硬件成本）的量化分解：消费级风冷散热器（2× Noctua NH-D15）= $100-$200；液冷冷板/分水器（2

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N23

## Claim

P_cooling_hardware（散热硬件成本）的量化分解：消费级风冷散热器（2× Noctua NH-D15）= $100-$200；液冷冷板/分水器（2× GPU）= $500-$1,500；数据中心风冷/液冷集成系统 = $0（已包含在机架 PUE 中，但独立液冷系统需额外 $2,000-$5,000）；Mac Studio 被动散热，P_cooling = $0。

## Corrected Claim

消费级风冷散热器（如2× Noctua NH-D15）成本约为$100-$200；双GPU液冷组件（冷板/分水器）成本约为$500-$1,500；数据中心独立液冷系统额外成本约为$2,000-$5,000（基础风冷通常包含在机架PUE/基础设施成本中）；Mac Studio采用被动散热，无额外散热硬件成本。

## Evidence

[质询]参考来源仅涉及笔记本压风散热器测评，与陈述中涉及的数据中心液冷、Mac Studio及具体高端硬件（Noctua NH-D15）成本完全无关，无法提供外部证据支持；且数据中心散热成本通常计入基础设施CAPEX而非单台设备PUE，表述存在口径混淆风险。 | 逻辑自洽（消费级风冷$100-200、液冷$500-1500符合市场常识，Mac Studio被动散热$0符合事实），但参考来源[1]主题不相关，无可用外部证据支持具体数值，属经验事实缺来源支持。

## Search Query

GPU cooling hardware cost liquid cooling loop dual GPU water block price

## Retrieval Sources

- {'url': 'https://www.toutiao.com/article/7651942949990777390/&rut=2e919c42b251cc9d30228dba446afe6eaa02f9bceca151f4f020c38572242144', 'type': 'ddg', 'title': '2026压风式散热器深度测评：涡轮压风制冷，破解游戏本高温痛点 - 今日头条'}
