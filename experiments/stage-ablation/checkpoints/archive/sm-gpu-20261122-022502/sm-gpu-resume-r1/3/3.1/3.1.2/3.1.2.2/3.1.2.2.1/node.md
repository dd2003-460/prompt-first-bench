# N659: RTX 5090 的 32GB GDDR7 显存带宽 1792 GB/s 是由 512-bit 位宽乘以 28 Gbps 等效速率计算得出的 (512/8 * 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N203, N204, N205

## Claim

RTX 5090 的 32GB GDDR7 显存带宽 1792 GB/s 是由 512-bit 位宽乘以 28 Gbps 等效速率计算得出的 (512/8 * 28 = 1792)，该带宽为理论峰值，实际推理吞吐受内存控制器效率限制，通常有效带宽为峰值的 85-90%。

## Corrected Claim

RTX 5090 的 32GB GDDR7 显存带宽 1792 GB/s 是由 512-bit 位宽乘以 28 Gbps 等效速率计算得出的 (512/8 * 28 = 1792)，该带宽为理论峰值，实际推理吞吐受内存控制器效率限制，通常有效带宽为峰值的 85-90%。

## Evidence

先验知识/题面给定，逻辑校验通过：512-bit位宽除以8等于64字节，乘以28Gbps等于1792GB/s，计算无误；85-90%的有效带宽效率符合GPU内存控制器的一般工程经验。

## Search Query

RTX 5090 memory bandwidth 1792 GB/s 512-bit 28Gbps
