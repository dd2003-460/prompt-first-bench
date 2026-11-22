# N522: 若使用 FP8 精度进行推理，单次 All-Reduce 数据量减半为 4 KB，总通信数据量 D_total_comm_FP8 = 128 * 4 KB = 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N214

## Claim

若使用 FP8 精度进行推理，单次 All-Reduce 数据量减半为 4 KB，总通信数据量 D_total_comm_FP8 = 128 * 4 KB = 512 KB = 0.5 MB，通信开销占解码总数据量（权重+KV）的比例需重新计算。

## Corrected Claim

若使用 FP8 精度进行推理，单次 All-Reduce 数据量减半为 4 KB，总通信数据量 D_total_comm_FP8 = 128 * 4 KB = 512 KB = 0.5 MB，通信开销占解码总数据量（权重+KV）的比例需重新计算。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8为8位精度，相比FP16（16位）数据量减半，128*4KB=512KB=0.5MB计算正确，符合基本算术与精度定义。
