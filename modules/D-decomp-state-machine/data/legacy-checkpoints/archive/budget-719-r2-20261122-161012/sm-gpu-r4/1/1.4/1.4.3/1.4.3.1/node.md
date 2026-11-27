# N164: Apple M3 Ultra (Mac Studio 512GB) 在 Qwen3-27B 推理负载下的整机平均功耗约为 350W-400W（峰值 500W），

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N46

## Claim

Apple M3 Ultra (Mac Studio 512GB) 在 Qwen3-27B 推理负载下的整机平均功耗约为 350W-400W（峰值 500W），3 年 24/7 运行电费在 $0.15/kWh 电价下约为 $356-$416/年，与 RTX 4090 单卡相当但低于双卡方案。

## Corrected Claim

Apple M3 Ultra (Mac Studio 512GB) 在 Qwen3-27B 推理负载下的整机平均功耗可能高于典型值（200W），但具体数值（350W-400W）缺乏直接来源支持；3 年 24/7 运行电费在 $0.15/kWh 电价下需基于实际功耗重新计算。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 730)

## Search Query

Mac Studio M3 Ultra power consumption LLM inference benchmark watts

## Retrieval Sources

- {'url': 'https://support.apple.com/en-us/102027&rut=86bb1709a4af0c4d3d6127768b4842ac5d9635fa3dc1f18c44e9d5cf9b27c63d', 'type': 'ddg', 'title': 'Mac Studio power consumption and thermal output (BTU) information'}
- {'url': 'https://support.apple.com/en-gb/102027&rut=3a460d0f360559868f541eae67a1518b2e5025309e06c71645d5e2dd3df33ea2', 'type': 'ddg', 'title': 'Mac Studio power consumption and thermal output (BTU) information'}
- {'url': 'https://beatandwin.com/en/geraete/apple/mac-studio-m3-ultra&rut=4aba5f6e10036576d8d78e71c7db1cba5d783a6d7f7f764aac72befaa436d20b', 'type': 'ddg', 'title': 'Power consumption Apple Mac Studio (M3 Ultra): 318 kWh/year, €111 ...'}
