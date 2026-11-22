# N49: Apple 统一内存 (Unified Memory) 无 ECC 支持（部分数据中心级 M2 Ultra 可能例外，但消费级 Mac Studio 无 ECC

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

Apple 统一内存 (Unified Memory) 无 ECC 支持（部分数据中心级 M2 Ultra 可能例外，但消费级 Mac Studio 无 ECC），在 24/7 长期推理场景下，比特翻转 (Bit Flip) 风险导致的静默数据损坏 (Silent Data Corruption) 概率需量化，通常消费级 DRAM 的 FIT 率 (Failures In Time) 约为 10^6 小时 1-2 次，需评估对输出稳定性的影响。

## Corrected Claim

Apple 统一内存 (Unified Memory) 在消费级 Mac Studio 中通常无 ECC 支持（部分数据中心级 M2 Ultra 可能例外），在 24/7 长期推理场景下，比特翻转 (Bit Flip) 风险导致的静默数据损坏 (Silent Data Corruption) 概率需量化。通常消费级 DRAM 的比特错误率（BER）或相关可靠性指标需参考具体厂商数据，而非直接套用硬件 FIT 率（10^6 小时 1-2 次），需评估对输出稳定性的影响。

## Evidence

[质询]FIT率（Failures In Time）通常指硬件整体故障率，而非比特翻转率（Bit Error Rate, BER）。将硬件故障率直接等同于比特翻转风险在量纲和定义上存在混淆；此外，Apple Silicon的内存架构细节（如是否使用ECC）属于具体硬件规格，需确切来源支持，仅凭逻辑无法完全排除特定型号（如M2 Ultra）可能具备ECC支持的可能性。 | 经验事实，逻辑自洽但缺来源支持；FIT率与比特翻转率概念混淆，且无外部来源验证Apple Silicon ECC状态及具体FIT数值。

## Search Query

Apple Unified Memory ECC support Mac Studio data integrity LLM inference
