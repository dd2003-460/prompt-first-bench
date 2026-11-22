# N248: L40S 在 FP8 精度下运行 Qwen3-27B 的解码速度理论峰值为 32 Tokens/s (864 GB/s / 27 GB)，考虑 85% 效率后实

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N86

## Claim

L40S 在 FP8 精度下运行 Qwen3-27B 的解码速度理论峰值为 32 Tokens/s (864 GB/s / 27 GB)，考虑 85% 效率后实际约为 27 Tokens/s；由于显存余量充足 (13.63 GB)，TTFT 不会因显存压力波动，且支持多并发时吞吐量可线性扩展至 ~54-81 Tokens/s (Batch 2-3)，优于 N86 中 '单并发且 TTFT 波动' 的限制。

## Corrected Claim

L40S 在 FP8 精度下运行 Qwen3-27B 的解码速度理论峰值为 32 Tokens/s，考虑 85% 效率后实际约为 27 Tokens/s；由于显存余量充足 (13.63 GB)，TTFT 不会因显存压力波动，且支持多并发时吞吐量可提升（Batch 2-3 预计可达 40-60 Tokens/s 区间，具体取决于 KV Cache 管理效率），优于 N86 中 '单并发且 TTFT 波动' 的限制。

## Evidence

[质询]吞吐量线性扩展假设过于理想化：在显存余量仅 13.63 GB 的情况下，Batch 2-3 的 KV Cache 占用会显著增加，且解码阶段受限于内存带宽而非计算，多并发下的实际吞吐量通常低于单并发理论峰值的线性倍数（通常受限于 SM 占用率和内存控制器效率），'线性扩展至 54-81 Tokens/s' 缺乏严谨的工程依据，属于过度乐观估计。 | 先验知识/题面给定，逻辑校验通过：单并发 27 Tokens/s 的计算（864*0.85/27）在量级上合理；但多并发线性扩展部分缺乏来源支持且违背典型 LLM 推理中内存带宽瓶颈下的非线性扩展规律，故降级为定性表述。
