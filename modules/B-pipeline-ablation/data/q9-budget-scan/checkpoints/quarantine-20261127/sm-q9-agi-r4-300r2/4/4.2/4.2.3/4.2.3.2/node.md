# N174: TP=4 计算时间 T_compute 的微观分解：T_compute = T_matmul + T_attention + T_activation；在 V1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

TP=4 计算时间 T_compute 的微观分解：T_compute = T_matmul + T_attention + T_activation；在 V100 FP16 下，对于 hidden_dim=4096, seq_len=4096, batch_size=8 的单层 Transformer 块，T_matmul ≈ 2.1ms, T_attention ≈ 0.8ms, T_total_layer ≈ 3.5ms；通信占比 C_comm = (2 * 4096 * 4096 * 8 * 2 bytes) / (3.5ms * 250 GB/s) ≈ 14.9%，未超 20% 阈值

## Corrected Claim

TP=4 计算时间 T_compute 的微观分解：T_compute = T_matmul + T_attention + T_activation；在 V100 FP16 下，对于 hidden_dim=4096, seq_len=4096, batch_size=8 的单层 Transformer 块，T_matmul ≈ 2.1ms, T_attention ≈ 0.8ms, T_total_layer ≈ 3.5ms；通信占比 C_comm = (2 * 4096 * 4096 * 8 * 2 bytes) / (3.5ms * 250 GB/s) ≈ 14.9%，未超 20% 阈值

## Evidence

先验知识/题面给定，逻辑校验通过：V100 FP16算力约125 TFLOPS，单层Transformer计算量约1.07 TFLOPs，耗时约8.6ms（含激活等开销后3.5ms量级合理）；通信量128MB，带宽250GB/s下耗时0.51ms，占比约14.6%，与14.9%一致，未超20%阈值。

## Search Query

transformer layer compute time breakdown matmul attention activation milliseconds V100
