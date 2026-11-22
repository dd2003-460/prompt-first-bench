# N61: Qwen3-27B 在 INT8 精度下的 MMLU 基准测试分数及相对于 BF16 的下降幅度（需检索或根据 GPTQ/AWQ 量化误差估算）

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14

## Claim

Qwen3-27B 在 INT8 精度下的 MMLU 基准测试分数及相对于 BF16 的下降幅度（需检索或根据 GPTQ/AWQ 量化误差估算）

## Corrected Claim

Qwen3-27B 在 INT8 精度下的 MMLU 分数通常接近 BF16 水平，下降幅度极小（通常 <1-2%），但具体数值需参考官方技术报告或特定量化库（如 GPTQ/AWQ）的实测数据，现有来源仅提供了 Qwen3.8 变体在 GGUF 量化下的性能参考。

## Evidence

[质询]参考来源均指向 'Qwen3.8-27B' 或 'Qwopus3.8-27B' 等特定微调/衍生版本，且主要讨论 GGUF 量化（如 Q4_K_M, Q8_0）或 MMLU-Pro 分数，未提供标准 'Qwen3-27B' 在 INT8 精度下的 MMLU 原始分数及相对于 BF16 的具体下降幅度数据，存在模型版本混淆和量化格式不匹配的风险。 | 来源 [1][2][3] 均涉及 Qwen3 系列 27B 模型的基准测试，但具体指向 Qwen3.8 或 Qwopus 变体及 GGUF 量化，未直接提供标准 Qwen3-27B INT8 的 MMLU 分数及 BF16 对比数据，属于间接相关但无法直接支持具体数值，故降级。

## Search Query

Qwen3-27B INT8 GPTQ AWQ MMLU benchmark score

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00688/article/details/152594884&rut=2ea9d2926423814f0c72df18929bb87fe87fd51d21ec45624adbbec869aadb02', 'type': 'ddg', 'title': '数据说话：Qwen3.8-27B-Uncensored-GGUF 基准评测全解读（MMLU、GSM8K 与安全测试）'}
- {'url': 'https://blog.csdn.net/gitblog_00965/article/details/168436283&rut=282fd1dabda0000c440f22cf523759f23adf269358a71c8d64b86de9dd41c976', 'type': 'ddg', 'title': 'Qwopus3.8-27B-Flash基准测试深度解读：MMLU-Pro 91.28%与Agent编程93%通过率'}
- {'url': 'https://yololab.net/archives/jonathancoletti-qwen3-8-27b-uncensored-gguf-%E6%B7%B1%E5%BA%A6%E8%A9%95%E6%B8%AC%EF%BC%9A27b-dense%E3%80%81mtp%E3%80%81%E9%87%8F%E5%8C%96%E8%88%87-speculative-decoding%EF%BD%9C2026%E6%9B%B4%E6%96%B0&rut=86c39b1fbe4bdc1f88c7c953a14c992c242af1da64f1a34f5327ea7caaf27fd4', 'type': 'ddg', 'title': 'JonathanColetti Qwen3.8-27B Uncensored GGUF 深度評測：27B dense、MTP、量化與 spe ...'}
