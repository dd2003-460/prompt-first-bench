# N155: Qwen3-27B 在 32K 上下文长度下，INT8 (W8A8) 量化与 BF16 基线相比的 Perplexity (困惑度) 增加具体数值（例如：+1.

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N45

## Claim

Qwen3-27B 在 32K 上下文长度下，INT8 (W8A8) 量化与 BF16 基线相比的 Perplexity (困惑度) 增加具体数值（例如：+1.5% 或 +2.0%），需引用同一来源以控制变量对比。

## Corrected Claim

Qwen3-27B 在 32K 上下文长度下，INT8 (W8A8) 量化相比 BF16 基线会导致 Perplexity 增加，但具体数值需查阅官方技术报告或特定基准测试数据，当前参考来源未提供确切数值。

## Evidence

[质询]参考来源中未包含 Qwen3-27B 在 32K 上下文下 INT8 (W8A8) 量化与 BF16 基线的具体 Perplexity 对比数值，且来源 [1] 和 [3] 提及的是 Qwen3.8-27B（可能为不同版本或笔误），来源 [2] 是 Qwen3-8B，均无法直接支持该特定数值事实。 | 经验事实，逻辑自洽但缺来源支持（来源 [1][2][3] 均未提供 Qwen3-27B 32K 上下文下 W8A8 vs BF16 的具体 PPL 增量数值）

## Search Query

Qwen3-27B INT8 W8A8 quantization perplexity 32k context evaluation benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/liu8485/article/details/164338425&rut=02ff81f583a68c8c292e5c57e8dfe792713585af4c396aa0d38b3238af6d81c3', 'type': 'ddg', 'title': 'Qwen3.8-27B 长上下文部署实战：一条 vLLM 命令吃下 75 万 token（含 NUMA 拓扑实测）'}
- {'url': 'https://blog.csdn.net/weixin_42300144/article/details/155326631&rut=b8272c504613f079183ebc49c407c3c82505f16a5689d2a8584ff67cfa93d999', 'type': 'ddg', 'title': 'Qwen3-8B长上下文处理能力实测：32K到底有多强？-CSDN博客'}
- {'url': 'https://www.cnblogs.com/sing1ee/p/22498000&rut=e1a4a75338ea7b8dd9906f6fd7993bdcd78532cfd255bfc4583f3ebbf527f720', 'type': 'ddg', 'title': 'Qwen3.8-27B（2026）：Qwen 新 27B 视觉语言模型完整指南 - 见路非道 - 博客园'}
