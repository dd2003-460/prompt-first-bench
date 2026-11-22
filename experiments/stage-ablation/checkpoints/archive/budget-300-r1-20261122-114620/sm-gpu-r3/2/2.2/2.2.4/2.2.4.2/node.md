# N199: AMD MI250X 的 HBM3 显存带宽为 3.276 TB/s (3276 GB/s)，其理论最大推理吞吐上限 T_max ≈ Bandwidth / M

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

AMD MI250X 的 HBM3 显存带宽为 3.276 TB/s (3276 GB/s)，其理论最大推理吞吐上限 T_max ≈ Bandwidth / Model_Size = 3276 / 54 ≈ 60.6 tokens/s，实测 45 tokens/s 达到了理论上限的 74%，表明计算单元或内存访问模式存在瓶颈

## Corrected Claim

AMD MI250X 的 HBM3 显存带宽为 3.276 TB/s (3276 GB/s)，其理论最大推理吞吐上限 T_max ≈ Bandwidth / Model_Size = 3276 / 54 ≈ 60.6 tokens/s，实测 45 tokens/s 达到了理论上限的 74%，表明计算单元或内存访问模式存在瓶颈

## Evidence

先验知识/题面给定，逻辑校验通过：MI250X HBM3带宽3.276TB/s符合官方规格，算术推导3276/54≈60.6及45/60.6≈74%均正确，符合Roofline模型分析逻辑。
