# N60: Apple M3 Ultra Mac Studio (192GB) 的 5 年 TCO 约为 $4,500 (硬件 $3,999 + 5年电费 $500 @ 0

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14, N15, N16

## Claim

Apple M3 Ultra Mac Studio (192GB) 的 5 年 TCO 约为 $4,500 (硬件 $3,999 + 5年电费 $500 @ 0.15$/kWh, 平均负载 50W)，远低于同等性能的 NVIDIA 多卡方案，但其吞吐量仅为消费级 GPU 方案的 1/2 至 1/3，性价比指数 (TCO/Throughput) 仅在极端静音/低延迟容忍场景下占优

## Corrected Claim

Apple M3 Ultra Mac Studio (192GB) 的 5 年 TCO 约为 $4,500 (硬件 $3,999 + 5年电费 $500 @ 0.15$/kWh, 平均负载 50W)。其单位成本下的吞吐量通常低于同等价位的多卡 NVIDIA 方案，但在对静音、功耗和集成度有极高要求的场景下具有独特优势。

## Evidence

[质询]吞吐量对比基准模糊且缺乏实证：M3 Ultra 的 GPU 性能（约 30 TFLOPS FP32）通常高于单张高端消费级 GPU（如 RTX 4090 约 82 TFLOPS FP32，但受限于显存带宽和驱动优化，实际 AI 推理吞吐未必是 2-3 倍差距），且‘同等性能’的定义未明确（是峰值算力还是特定任务吞吐？），导致‘1/2 至 1/3’这一具体比例缺乏可靠数据支撑。 | 经验事实，逻辑自洽但缺来源支持；TCO 计算逻辑正确（3999 + 5*365*24*0.05*0.15 ≈ 4500），但吞吐量对比的具体倍数属于经验性断言，无外部来源验证，且‘同等性能’前提下的对比基准不明确。
