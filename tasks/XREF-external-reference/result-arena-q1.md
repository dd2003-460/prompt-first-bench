## 输出

**结论先行（条件化）**：单卡 H100 SXM5 相对 H100 PCIe 的 LLM 推理吞吐优势，主要由两个显存/算力比决定，NVLink 只在多卡张量并行时进入决定项。典型区间约为 **1.3x–1.7x**，不是「14 倍」。

**1. 「14 倍」误读的来源**
- 900 GB/s 是 SXM 的 NVLink 4 每卡总带宽（双向合计，18 条链路）；64 来自 PCIe Gen5 x16 单向 64 GB/s。两者既不是同一量纲（双向 vs 单向），也不是单卡吞吐。
- 按同为双向口径：900 / 128 ≈ 7x，仍是互联带宽比，不是推理吞吐比。
- 结论：「14 倍」是互联带宽比被误当成吞吐比，单卡推理不成立。

**2. 分解：推理按阶段拆，每个阶段受不同硬件指标约束**

| 阶段 / 场景 | 决定项 | 规格比 SXM/PCIe | 实测/可得数据 |
|---|---|---|---|
| Prefill（长 prompt，算力受限） | 稠密 FP16/BF16 Tensor 算力 | 989 / 756 ≈ **1.31x** | 未找到同口径的 Prefill 实测对比 |
| Decode，batch=1（访存受限） | HBM 带宽 | 3.35 / 2.0 ≈ **1.68x**（理论上限） | Dell 测试（经 usd.ai 转引）Llama 2 7B BF16：128 vs 98.8 tok/s ≈ **1.30x**；RunPod Qwen2.5-7B：165 vs 109 tok/s ≈ **1.51x** |
| Decode，大 batch | 先访存后算力，取决于 batch 落点 | 介于 1.31 与 1.68 之间（推导，非实测） | 未找到可靠的同条件实测 |
| 多卡张量并行（TP≥2） | NVLink 900 GB/s vs PCIe 128 GB/s（双向）+ 每层 all-reduce 延迟 | 带宽约 7x | 仅找到营销/二手数据，未采信为定量结论 |

**3. 条件化结论**
- **单卡、batch=1 的交互式 decode**：SXM 约快 1.3–1.5x（有实测支撑），理论上限 1.68x。模型越小、框架开销占比越高，差距越小（推导）。
- **以 prefill 为主（长输入、短输出）**：约 1.3x，接近稠密算力比。
- **单卡、大 batch 的高吞吐 decode**：通常落在 1.3–1.7x，具体取决于 batch 是否已进入算力受限区；本次未找到可靠实测，此项是推导。
- **多卡 TP、大模型**：SXM 优势随卡数和通信量上升，NVLink 成为决定项；但幅度本次无可靠定量来源，不给数字。
- **精度影响**：FP8/INT8 下稠密算力比仍约 1.31（3026 vs 3958 为稀疏口径，稠密为其一半，比例不变）；权重量化后 decode 仍由带宽比决定，比例不变（推导）。
- **功耗影响**：PCIe 版 350 W（部分配置 300–350 W 可调），持续负载下可能降频，实际比例可能低于峰值比；有文章给出 85–90% / 75–85% 的持续性能系数，但来源未核实，不采信为结论。
- **成本维度（需要价格输入，结论条件化）**：可查到的租用价差约 SXM 溢价 14%–30%（RunPod Secure 2.89 vs 3.29 $/h；GMI 2.00 vs 2.40 $/h；Lambda 1× 3.29 vs 4.29 $/h）。若 decode 比 ≈1.3–1.5x，且价差 ≈1.14–1.30x，则 SXM 每 token 成本接近持平或略优；价差更大或吞吐比更低时 PCIe 更划算。注意：RunPod 同一文章给出的 $/M output token（SXM 7.78、PCIe 6.52）与其自身吞吐和价格不一致，此数不采信。
- **多卡训练类数据**（如 SXM 训练快 1.8x）与本题的单卡推理不同口径，不用于本题结论。

**4. 不确定点清单（黑盒表）**

| # | 不确定点 | 为什么影响结论 | 当前状态 |
|---|---|---|---|
| U1 | workload 未定（输入/输出长度、batch、并发） | 决定落在 prefill / decode 哪一段，直接决定 1.31x 还是 1.68x | 未定，给出分段结论 |
| U2 | 推理框架与版本未定（vLLM / TensorRT-LLM / 自研内核，融合算子程度） | 框架优化程度改变有效带宽利用率，实测比例可偏离理论比 | 未知 |
| U3 | 模型规模与精度未定 | 小模型易受框架开销限制，比例被压缩 | 仅引用 7B、8B、32B 的零散数据 |
| U4 | 并行度（单卡 / TP 卡数）未定 | NVLink 是否成为决定项取决于此 | 多卡量化数据不可靠 |
| U5 | 实测数据缺失 | 目前只有 1–2 组同类 batch=1 数据，且 Dell 数据为二手转引，未核对原文 | 不确定 |
| U6 | 价格维度缺失（日期、区域、折扣、预留/按需） | 成本结论完全依赖价格 | 只有若干供应商的零散报价，口径不一 |
| U7 | 功耗/散热设置（350 W 或 300 W 档、机箱风道）未知 | 持续降频会压低 PCIe 实际性能 | 未找到可靠的持续性能测量 |
| U8 | 「H100 PCIe」具体是哪种版本未知（标准 PCIe、NVL 桥接对） | NVL 双卡桥接的 600 GB/s 与标准 PCIe 不同，显存带宽也不同（NVL 为 3.9 TB/s/板） | 需用户确认 |
| U9 | 部分来源数值冲突 | 例：clusterbid 称 FP16 峰值两者均为 989、io.net 称 PCIe 带宽 3.35 TB/s，均与 NVIDIA 规格不符，已排除 | 以 Colfax 规格表为准 |

## 来源

逐条为本次实际打开或检索到且用于结论的 URL：

1. https://www.colfax-intl.com/nvidia/nvidia-h100 （已打开全文）— 用于：SXM/PCIe 规格对照（TF32/FP16/FP8 稠密与稀疏口径标注、显存带宽 3.35 TB/s vs 2 TB/s、TDP 700 W vs 300–350 W、NVLink 900 GB/s、PCIe Gen5 128 GB/s）。结论中的 989/756 稠密 FP16 比值由此表推出（表中 1979/1513 为稀疏口径，稠密为其一半）。
2. https://www.nvidia.com/content/dam/en-zz/Solutions/gtcs22/data-center/h100/PB-11133-001_v01.pdf （检索摘要）— 用于：PCIe 版 350 W 默认 / 200 W 下限、功耗档位说明。
3. https://millionminer.com/news/nvidia-h100-specs-price-guide （检索摘要）— 用于：规格交叉核对（3.35 TB/s、2 TB/s、NVLink 900 GB/s）。
4. https://yobitel.com/knowledge-base/nvidia-h100 （检索摘要）— 用于：规格交叉核对（PCIe 稀疏 FP16 1513、稠密口径推导）。
5. https://www.thundercompute.com/blog/nvidia-h100-specs-full-guide （检索摘要）— 用于：TF32/FP16 稠密与稀疏比值交叉核对。
6. https://www.runpod.io/articles/guides/best-gpu-for-llm-inference （检索摘要）— 用于：Qwen2.5-7B-Instruct 单请求场景 SXM 165 tok/s vs PCIe 109 tok/s（decode 实测比例 ≈1.51x）；其 $/M output token 数据因与自身吞吐和价格不一致，未采信。
7. https://usd.ai/blog/sxm-vs-pcie （检索摘要）— 用于：转引 Dell InfoHub（2024-09）Llama 2 7B BF16、batch=1：SXM 128 tok/s vs PCIe 98.8 tok/s（≈1.30x）；RunPod Secure Cloud 价格 $3.99 / $2.89。Dell 原文未打开核对。
8. https://vdf.ai/llm-tokens-per-second-calculator/ （检索摘要）— 用于：decode 访存受限的理论公式（每 token 读取权重与 KV cache），以及 Qwen3-32B FP8 单卡 SXM batch=1 理论上限约 60 tok/s 的量级参考。
9. https://www.spheron.network/blog/heterogeneous-gpu-inference-cost-optimization/ （检索摘要）— 用于：prefill 偏算力受限、decode 偏带宽受限的定性框架。数值未采用。
10. https://tutorsbot.com/blog/h100-gpu-rental-cost-per-hour-2026 （检索摘要）— 用于：Lambda 2026-08 报价 H100 PCIe 1× $3.29/GPU-h，SXM 1× $4.29/GPU-h；RunPod Secure PCIe $2.89 / SXM $3.29。
11. https://www.gmicloud.ai/en/blog/2026-cost-of-renting-or-uying-nvidia-h100-gpus-for-data-centers （检索摘要）— 用于：GMI PCIe $2.00 vs SXM $2.40 /GPU-h（2026-04）。
12. https://hardware.co/blog/nvlink-sxm-vs-pcie-inference （检索摘要）— 用于：PCIe x16 约 128 GB/s 双向、NVLink 桥 600 GB/s 的互联层级说明；未采信其中无来源的性能陈述。
13. https://clusterbid.com/blog/h100-sxm-vs-pcie-form-factor-guide （检索摘要）— 用于：仅作为「营销/非权威来源」参照（称训练多卡 SXM 约 1.8x、PCIe 单卡 batch 推理损失 25–30%、持续性能系数 85–90%）。以上数值均未经独立核实，未作为结论依据；其中 FP16 峰值两者 989 的写法与 NVIDIA 规格不符，已排除。
14. https://io.net/p/h100-sxm-vs-pcie-which-gpu-configuration-for-ai-training （检索摘要）— 仅作参照：称 batch-64 推理 SXM 2850 vs PCIe 2780 tok/s（差 2.5%）。其文内把 PCIe 带宽写为 3.35 TB/s，与 NVIDIA 规格矛盾，未采信。

未查到、未给出 URL 的内容：Prefill 同口径实测对比；大 batch decode 的可靠实测；多卡 TP 下 PCIe 与 SXM 的推理吞吐实测比例；PCIe 版持续功耗下的降频幅度实测。

## 自述缺口

- **U1–U8 详见上文黑盒表**，核心是 workload、框架、模型与精度、并行度、功耗设置、价格日期均未给定，所以结论只能写成条件化区间。
- **实测样本少**：单卡 batch=1 decode 仅有两组数据（1.30x 与 1.51x），且 Dell 数据为二手转引、未打开原文；无 prefill 实测、无大 batch 实测、无多卡 TP 实测。
- **1.3–1.7x 区间中，1.68x 是理论上限，不是实测**；1.31x 是稠密算力比，实际 prefill 受 kernel 效率和功耗影响，未实测。
- **功耗降频幅度未核实**：仅找到非权威文章的系数，未采信为结论。
- **价格**：各供应商报价日期、区域与计费方式不一；同一来源的 $/token 与其吞吐、单价不自洽，未采用。
- **多卡 NVLink 影响**未给出可靠定量值，只给出定性方向（SXM 优势随 TP 卡数增加）。
- **来源可靠性**：大部分引用来自检索摘要而非原始页面全文（仅 Colfax 页面已完整打开）；NVIDIA 原始 datasheet 仅以检索摘要形式核对。
- 本题的「快多少」只能以单卡推理吞吐比计，不包含训练、不包含 NVLink 之外的系统级差异（机箱、CPU、网络、存储）。
