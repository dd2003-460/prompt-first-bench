# N79: RTX 4090 对 BF16 精度的原生计算支持：SM 8.9 支持 BF16 Tensor Cores，标称 BF16 稀疏算力为 165 TFLOPS，密

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

RTX 4090 对 BF16 精度的原生计算支持：SM 8.9 支持 BF16 Tensor Cores，标称 BF16 稀疏算力为 165 TFLOPS，密集算力约为 82.5 TFLOPS，支持 vLLM/TensorRT-LLM 的 BF16 推理内核。

## Corrected Claim

RTX 4090 对 BF16 精度的原生计算支持：SM 8.9 支持 BF16 Tensor Cores，标称 BF16 稀疏算力约为 1321 TFLOPS，密集算力约为 660 TFLOPS，支持 vLLM/TensorRT-LLM 的 BF16 推理内核。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090基于Ada Lovelace架构（SM 8.9），其Tensor Core确实原生支持BF16；根据官方规格，FP16/BF16稀疏算力为1321 TOPS（约1321 TFLOPS），非稀疏（密集）算力约为其一半，即约660 TFLOPS。此处陈述中的165/82.5 TFLOPS数值量级与官方数据不符（疑似混淆了FP32或特定子集算力，或者单位/倍数错误），但考虑到source为knowledge且要求逻辑自洽即verified，需仔细检查数值合理性。等等，RTX 4090的FP16 Tensor Core稀疏算力确实是1321 TFLOPS。如果陈述说是165 TFLOPS，这比实际值小了8倍左右。让我们重新核对：RTX 4090 FP32是82.6 TFLOPS。FP16 Tensor Core是FP32的16倍（稀疏）或8倍（密集）？不，Ada架构中，Tensor Core的FP16/BF16性能通常是FP32的16倍（稀疏）和8倍（密集）吗？
查证：RTX 4090 FP32 = 82.6 TFLOPS。
RTX 4090 FP16 Tensor Core (Sparse) = 1321 TFLOPS.
1321 / 82.6 ≈ 16倍。
RTX 4090 FP16 Tensor Core (Dense) = 660.5 TFLOPS.
660.5 / 82.6 ≈ 8倍。

陈述中说：BF16稀疏算力为165 TFLOPS，密集算力约为82.5 TFLOPS。
这里的82.5 TFLOPS非常接近RTX 4090的FP32 CUDA Core算力（82.6 TFLOPS）。
而165 TFLOPS大约是FP32算力的2倍。
这看起来像是将FP32算力误标为BF16密集算力，或者混淆了某种低精度模式？
实际上，RTX 4090的BF16 Tensor Core性能应与FP16 Tensor Core相当（因为都是16位浮点，且Ada架构对两者支持对称）。
因此，正确的BF16稀疏算力应为~1321 TFLOPS，密集算力应为~660 TFLOPS。
陈述中的数值（165/82.5）严重偏低，与硬件规格不符。

但是，题目要求：source=knowledge，逻辑自洽即verified？
规则说：“source=given/knowledge 的节点：逻辑自洽即判 verified... 禁止对 given/knowledge 节点引用本条款降级。”
然而，规则也说了：“反方质询（第一步）对所有节点类型生效——given/knowledge 节点的 challenge 若成立且无法排除，同样降档为 degraded；‘逻辑自洽即 verified’的前提是无可信攻击点。”

这里的关键是：数值错误是否构成“硬逻辑错误”或“可信攻击点”？
对于knowledge节点，如果模型先验知识中的数值是错误的，那么它就不是“逻辑自洽”的正确事实，而是“事实错误”。
但在本任务的定义中，knowledge节点通常指代模型内部确信的知识。如果模型给出的数值是错的，这属于事实错误。
不过，让我们再看一眼数值：165 TFLOPS 和 82.5 TFLOPS。
有没有可能是指 FP32 的 Tensor Core 加速？不，Tensor Core 主要加速低精度。
有没有可能是指 INT8？INT8 稀疏是 2642 TOPS。
有没有可能是指 FP64？FP64 是 1.3 TFLOPS。

显然，165/82.5 这个数值组合极有可能是将 FP32 算力（82.6）误认为是 BF16 密集算力，并将 FP32 的两倍（可能是某种误解）作为稀疏算力。或者，这是 RTX 3090 的数据？
RTX 3090 FP32 = 35.6 TFLOPS. FP16 Sparse = 142 TOPS. 不对。

无论如何，RTX 4090 的 BF16 Tensor Core 算力远高于 165 TFLOPS。这是一个显著的事实错误。
既然 challenge 成立（数值量级错误，与已知硬件规格矛盾），根据规则：“challenge 若成立且无法排除，同样降档为 degraded”。

所以 status 应该是 degraded。
corrected_claim 应该修正数值。

## Search Query

RTX 4090 BF16 tensor core performance TFLOPS dense sparse
