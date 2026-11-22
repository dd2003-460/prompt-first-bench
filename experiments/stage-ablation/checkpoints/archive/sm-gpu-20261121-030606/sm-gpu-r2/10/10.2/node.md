# N159: RTX 5090的FP8推理吞吐量基于RTX 4090的FP8性能（约1.5x BF16）外推，但RTX 5090的FP8 Tensor Core架构改进可能带

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N78

## Claim

RTX 5090的FP8推理吞吐量基于RTX 4090的FP8性能（约1.5x BF16）外推，但RTX 5090的FP8 Tensor Core架构改进可能带来额外10-20%的性能提升，因此外推值存在±20%的不确定性区间，需等待官方基准测试确认。

## Corrected Claim

RTX 5090基于Blackwell架构，官方标称FP8 Tensor稀疏算力约为1,677 TFLOPS（稠密性能约为其一半，即约838 TFLOPS），相比RTX 4090有显著提升，具体推理吞吐量需结合实际模型负载测试确认。

## Evidence

[质询]该陈述将RTX 5090的FP8性能描述为基于RTX 4090的“外推”且存在±20%不确定性，但参考来源[1]提供了RTX 5090基于Blackwell架构的官方标称算力（FP8 Tensor sparse约1,677 TFLOPS，Dense约838 TFLOPS），这意味着性能数据已有官方基准或架构规格支持，并非单纯依赖上一代产品的模糊外推，且“±20%不确定性”这一具体量化区间缺乏来源支持，属于主观估计。 | 来源[1]直接提供了RTX 5090的FP8算力数据（Sparse 1677 TFLOPS / Dense ~838 TFLOPS），证实了性能量级，但并未支持“基于4090外推”或“±20%不确定性”这一特定推导逻辑和误差范围，属于间接支持性能存在但矛盾于“需等待官方基准”的表述（因来源已给出官方标称值）。

## Search Query

RTX 5090 FP8 inference throughput benchmark official NVIDIA

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2062928081980072755&rut=49bc8e8c89c7838d3642b90c83fe2489e9185702b221db690d43f108a0f13ce5', 'type': 'ddg', 'title': 'Rtx 5090算力到底多少？Fp16/Fp8/Int8算力实测与解读 - 知乎'}
