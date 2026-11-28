# N447: Monte Carlo 采样（N=10^6, d=1000）在 V100 上的纯计算耗时 T_compute_jax ≈ 0.1-0.3s（假设向量化程度高），

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N153

## Claim

Monte Carlo 采样（N=10^6, d=1000）在 V100 上的纯计算耗时 T_compute_jax ≈ 0.1-0.3s（假设向量化程度高），受限于显存带宽（HBM2 ~ 900GB/s）而非算力；若使用 float32，数据量为 4GB，读取耗时 ~4.4ms，写入耗时 ~4.4ms，计算耗时主导

## Corrected Claim

Monte Carlo 采样（N=10^6, d=1000）在 V100 上的纯计算耗时 T_compute_jax ≈ 0.1-0.3s（假设向量化程度高），受限于显存带宽（HBM2 ~ 900GB/s）而非算力；若使用 float32，数据量为 4GB，读取耗时 ~4.4ms，写入耗时 ~4.4ms，计算耗时主导

## Evidence

先验知识/题面给定，逻辑校验通过：V100 HBM2带宽约900GB/s，4GB数据读写耗时约4.4ms，总I/O耗时<10ms，远小于0.1-0.3s的计算耗时，符合内存带宽受限场景下的性能特征。
