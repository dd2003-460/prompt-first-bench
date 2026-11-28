# N40: Apple M3 Ultra (Mac Studio) 的统一内存带宽为 819 GB/s，显存容量最高 512 GB，该带宽参数决定了其在 BF16 精度下的

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

Apple M3 Ultra (Mac Studio) 的统一内存带宽为 819 GB/s，显存容量最高 512 GB，该带宽参数决定了其在 BF16 精度下的理论 Decode 吞吐率上限约为 15.1 Tokens/s。

## Corrected Claim

Apple M3 Ultra (Mac Studio) 支持最高 512 GB 统一内存，其内存带宽（约 819 GB/s）是决定本地 LLM 推理速度的关键瓶颈，但具体理论 Decode 吞吐率取决于模型参数量，15.1 Tokens/s 并非通用上限。

## Evidence

[质询]数值量级与计算逻辑存疑：819 GB/s 带宽在 BF16 下通常对应更高的理论吞吐（例如对于 70B 模型，理论上限约为 5.8 tokens/s，对于 7B 模型则高达 58 tokens/s），15.1 tokens/s 这一特定数值缺乏明确的模型规模前提，且参考来源中未提供该具体计算结果，疑似混淆了不同模型规模或引入了未说明的效率损耗系数。 | 来源 [1] 和 [2] 确认了 M3 Ultra 512GB 的存在及本地推理能力，但未提及 819 GB/s 的具体带宽数值或 15.1 Tokens/s 的理论上限计算，属于经验事实且缺乏直接来源支持。

## Search Query

Apple M3 Ultra unified memory bandwidth GB/s

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1928856739001927267&rut=2d141ae0a02bb09271fba85164b01ddcc928b15dd445cba7d16fa473ae1bd0e3', 'type': 'ddg', 'title': 'Apple M3 Ultra（512GB统一内存）本地LLM推理全面分析'}
- {'url': 'https://zhuanlan.zhihu.com/p/2025875529602020659&rut=2bd6e886abfac2e531da05074e455259db096759bfc17ab15959f2c88f7f41e9', 'type': 'ddg', 'title': 'Mac Studio 跑本地大模型：苹果的统一内存，可能是你最容易上手的方案'}
