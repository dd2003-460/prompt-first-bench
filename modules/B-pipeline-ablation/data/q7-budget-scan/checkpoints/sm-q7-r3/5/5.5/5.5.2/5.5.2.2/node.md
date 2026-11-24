# N317: 工作点B（中成本/低风险）：采用MD5哈希+多线程并行（8核），有效吞吐提升至4GB/s，总耗时T=500TB/4GB/s≈347h，机会成本C_opex=34

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

工作点B（中成本/低风险）：采用MD5哈希+多线程并行（8核），有效吞吐提升至4GB/s，总耗时T=500TB/4GB/s≈347h，机会成本C_opex=347h×10%×¥5000/h≈¥173,500，误检率（False Negative）约1e-32，工程上视为安全。

## Corrected Claim

工作点B（中成本/低风险）：采用MD5哈希+多线程并行（8核），有效吞吐提升至4GB/s，总耗时T=500TB/4GB/s≈347h，机会成本C_opex=347h×10%×¥5000/h≈¥173,500，误检率（False Negative）约1e-32，工程上视为安全。

## Evidence

先验知识/题面给定，逻辑校验通过：MD5碰撞概率极低（~1e-32符合安全假设），8核并行达到4GB/s吞吐在工程上合理，时间计算（500TB/4GB/s ≈ 347h）及成本估算（347*0.1*5000 ≈ 173,500）数学自洽。
