# N185: RTX 4080 Super 在 W4 精度下的实测 TPS 约为 50-60 tokens/s (基于 717 GB/s 带宽及 4-bit 解码效率)，相比

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

RTX 4080 Super 在 W4 精度下的实测 TPS 约为 50-60 tokens/s (基于 717 GB/s 带宽及 4-bit 解码效率)，相比 RTX 5090 INT8 (60-70 TPS) 仅低 10-20%，但其价格 ($1050) 比 RTX 5090 ($1999) 低 47%，需计算 Cost_Per_Token 并评估 W4 精度损失是否可接受。

## Corrected Claim

RTX 4080 Super 在 W4 精度下的实测 TPS 受多种因素影响，需具体测试验证；其价格优势明显，但性能对比需结合具体模型和场景评估。

## Evidence

[质询]RTX 4080 Super 的显存带宽为 717 GB/s，但 RTX 5090 的显存带宽通常远高于此（如 GDDR7 可能达到 1.5-2 TB/s 或更高），且 INT8 与 W4 的解码效率差异并非简单的线性关系，仅凭带宽和精度粗略估算 TPS 存在较大误差，且具体 TPS 数值高度依赖模型大小、上下文长度及软件优化，缺乏实测数据支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 4080 Super Qwen 27B W4 inference tokens per second benchmark
