# N267: Apple M3 Ultra 在持续高负载推理下的典型功耗（Watt）及能效比，需修正 N103 中 '0.1kW' 的假设；Mac Studio M3 Ult

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

Apple M3 Ultra 在持续高负载推理下的典型功耗（Watt）及能效比，需修正 N103 中 '0.1kW' 的假设；Mac Studio M3 Ultra 在满载 GPU 推理时功耗通常在 150W-250W 区间（取决于散热和负载），需实测确认以准确计算 5 年电力成本（公式：Power_W * 8760h * 5 * Price_$per_kWh / 1000）。

## Corrected Claim

Apple M3 Ultra 在持续高负载推理下的典型功耗（Watt）及能效比，需修正 N103 中 '0.1kW' 的假设；Mac Studio M3 Ultra 在满载 GPU 推理时功耗通常在 150W-250W 区间（取决于散热和负载），需实测确认以准确计算 5 年电力成本（公式：Power_W * 8760h * 5 * Price_$per_kWh / 1000）。

## Evidence

[质询]来源仅提供了特定模型（DeepSeek-R1）下的系统总功耗数据，未明确区分是纯GPU功耗还是整机功耗，且未覆盖所有可能的负载场景，可能存在以偏概全的风险。 | 来源[1]和[2]均指出M3 Ultra在运行高负载AI模型时系统功耗约为200W，该数值落在陈述所述的150W-250W区间内，且两个独立来源数据一致，支持了该功耗区间的合理性。

## Search Query

Mac Studio M3 Ultra GPU inference power consumption watts benchmark

## Retrieval Sources

- {'url': 'https://www.sohu.com/a/870665862_121924584&rut=3e378cc34fccd9a1c97fa34617a16cbdbc27f7a79253d0530fb441b92d7608d0', 'type': 'ddg', 'title': '苹果M3 Ultra深度解析：200W耗能运行6710亿参数AI模型 - 搜狐'}
- {'url': 'https://www.sohu.com/a/870645436_121924584&rut=07baf00c68eaab1c40905f007883146bbc42cc3dbcf9651df540e7949c612c99', 'type': 'ddg', 'title': '揭密苹果M3 Ultra处理器：200W功耗与DeepSeek-R1运行实测'}
