# T48 双 Gold 构建回执

- 日期：2026-11-06（Asia/Shanghai）
- Repository：<https://github.com/dd2003-460/prompt-first-bench>
- Branch：`arena/2858680a-prompt-first-bench`
- `commit_sha`（研究开始时的基线 HEAD）：`dfc1ea3`（包含已合并的最新 `origin/main`；交付提交另见最终 git HEAD）
- 交付树：[`gold-tree-independent.md`](./gold-tree-independent.md)
- 搜索方法：按题面推导并分别搜索 a/b/c/d 四个硬件分区，合并后显式计默认先验/外先验；只使用可访问 GitHub 源。价格报价不可复核处用黑盒估计区间，不伪装为当日报价。

## 阶段执行记录（01→02→02.5→03→04→04.5）

1. **01 目标分解：** 根节点定义为满足每并发流 ≥20 token/s 与质量约束的候选中，最小化 `[(K/N)+E+O]/p`。把可行性、单次成本、返工乘数和候选集分开；标明题面缺少的测量输入。
2. **02 信息研究：** 搜索四个候选分区和 27B/长上下文公开实测；采集硬件、后端、模型量化、上下文、并发、通过率和采购价格证据。外部连接只验证 GitHub 源；价格与部分候选的 64K 数据诚实标为黑盒/open。
3. **02.5 交叉核查：** 比较 RTX 5090 基线/PCIe 修正报告与 RTX 4090 MTP 日志；确认差异来自模型量化、运行时、speculative decoding 和测量上下文等不可比项，不把它们混成同一性能值。M3 Ultra 同一报告内比较单流、批处理和多个独立进程。关键矛盾和较可信来源理由已写入树。
4. **03 行动拆解：** 定义复现实验：固定模型与量化、64K 活跃上下文、暖稳定前缀、并发扫描、逐流 400-token 解码重复 5 次；同时记电表、报价、通过率和返工成本。
5. **04 执行/验证：** 完成四分区各 2 候选（共 8），预先口径下默认先验 3、外先验 5；每个候选记录来源日期、数值/范围及成本估计；5 个外先验候选逐一回答生态、相对获取成本、实测瓶颈。
6. **04.5 最终复核：** 确认树含根、≥3 层、≥8 叶、超过 50 行；每个设备叶包含来源日期及实测值或诚实黑盒范围；记录瓶颈和矛盾；未计算与既有 gold 的节点重叠率，留给 Lead；未打分。

## 搜索来源（GitHub，页面日期）

- NVIDIA H100 80GB / Qwen3.6-27B-FP8 / prefix caching / MTP 长上下文问题：<https://github.com/vllm-project/vllm/issues/40756>（2026-04-23 开题；2026-04-29 评论含 H100 复现信息）。
- Strix Halo HIP/Vulkan 7B Q4 基准及实现瓶颈：<https://github.com/ggml-org/llama.cpp/issues/13565>（2025-05-15）。
- Strix Halo ROCm 120B MoE 多深度基准/后端回归讨论：<https://github.com/ggml-org/llama.cpp/issues/17917>（2025-12-10）。
- RTX 4090 双卡设备与 Qwen 27B 应用记录：<https://github.com/ggml-org/llama.cpp/issues/20733>（2026-03-18；用于候选检索，不当作速度基准）。
- RTX 4090 上 Qwen3.6-27B IQ4_XS 的长会话/MTP运行日志：<https://github.com/ggml-org/llama.cpp/issues/23577>（2026-05-23）。
- 8×AMD MI300X、32K 长上下文 ROCm/llama.cpp 实测及构建回归：<https://github.com/ggml-org/llama.cpp/issues/26445>（2026-08-02）。
- 双 Arc Pro B70、Qwen 27B 8-bit、SYCL tensor split 崩溃与 P2P 测量：<https://github.com/ggml-org/llama.cpp/issues/27198>（2026-08-16）。
- RTX 5090 / RTX 4090、Qwen3.5-27B Q4_K_M 基准和 PCIe 修正数据：<https://github.com/ggml-org/llama.cpp/issues/28196>（2026-09-01 起，含后续更正评论）。
- 单 Arc Pro B70、Qwen3.8-27B-Q4_K_M、约 1K→64K 深上下文 decode 对照：<https://github.com/ggml-org/llama.cpp/issues/28721>（2026-09-10）。
- Apple M3 Ultra 512GB、长上下文单流与多流实测：<https://github.com/ggml-org/llama.cpp/issues/29335>（2026-09-23）。
- vLLM 基准套件/基准方法文档：<https://github.com/vllm-project/vllm/tree/main/docs/benchmarking>（页面于 2026-11-06 检索；文档目录中的 README 最新更新 2026-08-11）。
- vLLM 性能仪表板方法与 TTFT/TPOT/吞吐比较：<https://github.com/vllm-project/vllm/blob/main/docs/benchmarking/dashboard.md>（2026-09-17）。

## 限定和交接

- 没有把短上下文、不同模型、不同量化或 MTP speculative token 统计直接当成题面要求的 27B×64K 每流吞吐。
- 本任务未访问 `gold-tree.md` 的数值内容、未访问 `calc.py`，未打分；交付树独立于既有 gold。Lead 后续负责节点重叠率及双 gold 对照。
- 需要任务方补充固定任务验收集、当前通过率、并发流数、目标 27B 模型配置和每年任务量；需要采购方补充现时报价/电价。未补前，“最低成本”只能给出上述可行性筛选与代入公式，不能可靠地产生唯一赢家。
