# N18: 高性低成工作点：单张高端消费卡（如 RTX 5090 32GB）在 BF16 或 FP8 下的推理吞吐量与 TCO 比值，作为性价比基准线

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N3

## Claim

高性低成工作点：单张高端消费卡（如 RTX 5090 32GB）在 BF16 或 FP8 下的推理吞吐量与 TCO 比值，作为性价比基准线

## Corrected Claim

单张高端消费卡（如 RTX 5090 32GB）凭借Blackwell架构在算力与显存带宽上的提升，在BF16或FP8推理场景下具备较高的性价比潜力，可作为消费级硬件的性价比参考基准。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了吞吐量理论推导（BF16/FP8）、TCO成本构成、以及最终的性价比比值计算。虽然BF16和FP8的吞吐量计算结构相似，但它们是不同精度下的独立性能基准，且父节点明确要求作为'性价比基准线'，因此需要分别列出以支撑最终对比。子节点之间逻辑递进清晰，无重复或矛盾。）

## Search Query

RTX 5090 32GB Qwen3-27B inference throughput tokens/s

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2040766374843245011&rut=e502f40dbaf3bf97cf5277ec2f318a0f47173457ccf470aa5f402bd5a0400fe9', 'type': 'ddg', 'title': 'Nvidia计算卡算力及详细参数综合报告（2026年5月版） - 知乎'}
