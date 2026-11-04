# Q1 · GPU 硬件规格（沿用 r1）

> 题面：`projects/decomp/experiments/autoresearch-r1/run/prompt-decomp.txt` 的任务段（原样，不改一个字——保持与 r1 可比）
> gold 锚点：`projects/decomp/experiments/autoresearch-r1/run/gold-facts.md`（含隐藏矛盾清单 + 应识别缺口 D2 锚点）

## 题面

任务：H100 PCIe 版 vs SXM 版跑 LLM 推理的实际吞吐差异。请按上面方法拆解，判断什么场景下 SXM 优势大、什么场景下小，并给出"快多少"的条件化结论。把你「不确定、需要进一步查证」的点收进黑盒表。

注：S0 臂只注入任务段本身（无方法论前缀）；S1+ 臂按 DESIGN §2 规则拼接阶段 prompt。

## gold 要点（判分用，不进 prompt）

- 隐藏矛盾：「SXM 快 14 倍」误读（900/64 是互联带宽比，非单卡吞吐比）
- decode 差距 ≈ 显存带宽比 3.35/2.0≈1.68x；prefill 才是算力比 ~1.31x
- NVLink 只在多卡 TP 场景成为决定项
- 应识别缺口：workload 未定 / 框架优化程度未知 / 价格维度缺失 / 实测数据缺失 → conf 降级