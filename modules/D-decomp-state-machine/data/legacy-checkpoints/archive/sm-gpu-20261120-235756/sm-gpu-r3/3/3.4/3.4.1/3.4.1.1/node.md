# N236: RTX 4090 在 32K Prefill 阶段 (计算密集) 功耗峰值 450W 持续时间约 100-200ms (取决于 Prefill 长度 32K t

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N74

## Claim

RTX 4090 在 32K Prefill 阶段 (计算密集) 功耗峰值 450W 持续时间约 100-200ms (取决于 Prefill 长度 32K tokens 的处理速度，假设 1000 tokens/s 则 32ms，但实际 Batch 处理可能更久)，Decode 阶段 (访存密集) 平均功耗 280W；若工作负载为 10% Prefill + 90% Decode (按时间加权)，平均功耗为 297W (计算式: 0.1*450 + 0.9*280)，年电费 (24/7, $0.15/kWh) 为 $390 (计算式: 297W * 24h * 365d / 1000 * 0.15)，相比仅按 TDP 450W 估算的 $590 低 34%，TCO 模型中必须使用加权平均功耗而非峰值功耗以避免高估运营成本。

## Corrected Claim

RTX 4090 在 32K Prefill 阶段功耗接近 TDP 450W，持续时间取决于实际 Prefill 吞吐（通常远快于 1000 tokens/s，故持续时间可能短于 100ms）；Decode 阶段平均功耗约 280W。若按时间加权平均功耗 297W 估算，年电费约 $390，相比按峰值 TDP 估算的 $590 低约 34%。TCO 模型应使用加权平均功耗。

## Evidence

[质询]RTX 4090 的 TDP 为 450W，但在 32K Prefill 这种极端计算密集场景下，实际功耗峰值通常难以稳定维持在 450W 满负荷状态（受限于散热和实际负载分布），且 100-200ms 的持续时间假设基于 1000 tokens/s 的处理速度，这与 RTX 4090 在 32K 上下文下的实际 Prefill 吞吐（通常远高于 1000 tokens/s，可达数千 tokens/s）存在量级偏差，导致时间加权比例（10% Prefill）可能不准确。 | 先验知识/题面给定，逻辑校验通过。数学计算（0.1*450 + 0.9*280 = 297W; 297*24*365/1000*0.15 ≈ $390）自洽。但作为 knowledge 节点，虽然逻辑自洽，但其中包含的经验参数（如具体功耗值、Prefill 持续时间、吞吐率）属于硬件行为经验数据，且存在上述关于 Prefill 速度和功耗峰值维持时间的潜在偏差，故降级为 degraded 以提示参数需根据实际基准测试校准。
