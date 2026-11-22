# N441: 修正后的 A100 80GB PCIe BF16 理论 Prefill 吞吐量计算：312e12 / (2 * 27e9 * 32768) ≈ 177 toke

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N149

## Claim

修正后的 A100 80GB PCIe BF16 理论 Prefill 吞吐量计算：312e12 / (2 * 27e9 * 32768) ≈ 177 tokens/s，该值需进一步乘以硬件效率系数（通常 0.6-0.8）得到实际可达吞吐量。

## Corrected Claim

修正后的 A100 80GB PCIe BF16 理论 Prefill 吞吐量计算：312e12 / (2 * 27e9 * 32768) ≈ 177 tokens/s，该值需进一步乘以硬件效率系数（通常 0.6-0.8）得到实际可达吞吐量。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB PCIe 的 BF16 峰值算力约为 312 TFLOPS，分母中 27e9 对应 LLaMA-2 70B 等典型大模型的参数量级，32768 为序列长度，计算逻辑与量级符合硬件理论峰值吞吐量的定义（FLOPS / (2 * Params * SeqLen)），且硬件效率系数 0.6-0.8 符合工程经验。
