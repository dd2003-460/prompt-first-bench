# N319: 判定'厂商标称峰值算力'的具体数值：RTX 5090 标称 FP8 峰值算力为 250 TOPS (含稀疏)，RTX 4090 标称 INT8 峰值算力为 33

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N104

## Claim

判定'厂商标称峰值算力'的具体数值：RTX 5090 标称 FP8 峰值算力为 250 TOPS (含稀疏)，RTX 4090 标称 INT8 峰值算力为 330 TOPS (含稀疏)；若数据源仅引用此类 TOPS 数值而未提供特定模型 (如 Qwen3-27B) 的实测 Tokens/s，则视为无效性能数据。

## Corrected Claim

判定'厂商标称峰值算力'的具体数值：RTX 5090 标称 FP8 峰值算力远高于 250 TOPS (含稀疏，具体数值需核实最新官方数据，通常 >1000 TOPS)，RTX 4090 标称 INT8 峰值算力约为 330 TOPS (含稀疏)；若数据源仅引用此类 TOPS 数值而未提供特定模型 (如 Qwen3-27B) 的实测 Tokens/s，则视为无效性能数据。

## Evidence

[质询]RTX 4090 的 INT8 峰值算力标称值存在争议，部分官方或第三方数据源可能标注为 330 TOPS (稀疏) 或 165 TOPS (稠密)，但更常见的对比中，RTX 4090 的 INT8 稀疏算力常被引用为 330 TOPS 左右，然而 RTX 5090 的 FP8 稀疏算力标称值通常远高于 250 TOPS（例如 NVIDIA 官方或泄露数据显示 RTX 5090 FP8 稀疏算力可能在 1000+ TOPS 量级，或者至少是 RTX 4090 的数倍）。250 TOPS 对于 RTX 5090 的 FP8 稀疏算力而言量级偏低，疑似混淆了稠密算力或特定精度下的数值，或者引用了错误的早期泄露数据。 | 先验知识/题面给定，逻辑校验通过，但数值量级存疑（RTX 5090 FP8 稀疏算力通常远高于 250 TOPS），且无外部来源支持，故降级。

## Search Query

NVIDIA RTX 5090 4090 peak TOPS specifications
