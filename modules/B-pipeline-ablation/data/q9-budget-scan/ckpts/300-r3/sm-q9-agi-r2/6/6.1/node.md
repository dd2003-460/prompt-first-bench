# N28: 长上下文实际有效窗口（EAW）的实证验证协议：设计一组长度为 [8k, 32k, 128k, 256k] 的针在草堆（Needle-in-a-Haystack）

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

长上下文实际有效窗口（EAW）的实证验证协议：设计一组长度为 [8k, 32k, 128k, 256k] 的针在草堆（Needle-in-a-Haystack）测试集，嵌入关键科学事实于不同位置，测量 Qwen3.8-27b 的召回率。记录召回率降至 90% 时的最大上下文长度，作为该模型的 EAW 硬边界

## Corrected Claim

一种用于评估长上下文实际有效窗口（EAW）的潜在协议是：设计长度为 [8k, 32k, 128k, 256k] 的针在草堆测试集，测量模型在不同位置的召回率，并将召回率降至特定阈值（如90%）时的最大上下文长度视为该模型在该测试条件下的有效边界。

## Evidence

父节点级核验未通过：不完备（子节点分别定义了测试集规模与长度（节点1）、针的位置分布（节点2）、评估指标公式（节点3）以及数据内容构造（节点4），各维度互不重叠且无逻辑矛盾，正交性良好；无冗余，每个子节点代表独立的实验配置维度。然而，完备性不足：父节点明确指出了具体的模型 'Qwen3.8-27b' 和特定的长度区间 [8k, 32k, 128k, 256k]，但子节点1引入了未在父节点中定义的硬件约束（4×V100-16GB）并擅自修改了长度阶梯（增加了65k，跳过了128k直接到256k，且未说明为何改变父节点设定的特定长度点），导致子节点未能忠实覆盖父节点指定的核心参数，反而引入了外部变量。）

## Search Query

Needle in a haystack test Qwen long context recall rate 256k

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29046611/article/details/168581991&rut=1c4742d2fe4e7c8ad8449e5c144bf3e85eb7b9d2ac6291abc147d505d6b41bb1', 'type': 'ddg', 'title': '标称128k实际只有32k？长上下文有效窗口的实测与工程优化-csdn博客'}
- {'url': 'https://blog.csdn.net/weixin_32238157/article/details/168709396&rut=a2e97c67860431b0e63c5df5dcaf56f6b36ef571cebdbb308651d99324e8dadb', 'type': 'ddg', 'title': '大模型长上下文有效窗口实测：标称128k为何实际用不满-csdn博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/159480523&rut=72293ce57d5938d0cf44563c2c0d10db60edd6c98504c6acd00dc693a2fc0943', 'type': 'ddg', 'title': '百川2-13B上下文长度实测：OpenClaw处理长文档任务表现_宁柳跨越-龙虾开发者社区'}
