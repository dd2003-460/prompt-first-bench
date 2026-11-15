# 任务书：27B 本地部署硬件选型 — 阶段 02 资料搜集

【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00-common-review.md + 02-information-research.md + 02.5-cross-check.md（仓库内）。
2. 每阶段产出落盘 loop-artifacts/stages/<N>/，阶段判定 pass 才进下一阶段。
3. 完成后 commit + push（含全部 loop-artifacts/）。
4. 通道故障（403/沙箱）→ 报告 Lead，由 Lead 降级本地执行，不得静默跳过 loop。

---

## 调研问题
为本地部署 27B 级模型（以 Qwen3.8-27B 为基准）选出 2026 年 10 月中国大陆市场性价比最高的硬件系统。

## 已知背景（阶段 01 结论）
- 阶段 01 工件：`loop-artifacts/stages/01/01-factor-decomposition.md`（7 因素 F1-F7 正交分解，G1-G12 空缺清单）
- 用户现状：已有 Mac 跑 MLX 27B ~30 tok/s；负载 = 长上下文 30K-226K + solo + 中并发 ≤8
- 初版报告（仅线索，全部数值待核验）：workspace `projects/知识/D1-knowledge-base/notes/27b-local-hardware-costperf-2026-10.md`

## 候选范围
- C1 NVIDIA 消费级（RTX 5090/5080/5070Ti/5060Ti 及特供版 5090D）
- C2 NVIDIA 专业/数据中心（RTX PRO 5000/6000、二手 A100/H100/A6000/L40S）
- C3 Apple Silicon（Mac Studio M5 Max/Ultra、Mac mini M5/M6）
- C4 AMD（RX 7000/8000/9000 系 24G+）
- C5 二手/多卡（二手 3090/4090 24G、2-4 卡工作站）
- C6 国产/其他（昇腾/摩尔线程，生态不成熟则记录排除理由）
- C7 云/租赁（仅边界参照，不作主选）

## 量化口径
- 显存需求 = 权重(B/param×quant) + KV(2×layers×kv_heads×head_dim×ctx×batch×bytes) + 激活 + 10% 余量
- decode 理论上限 = 显存带宽(GB/s) / 权重占用(GB)
- 性价比主指标 = 系统总价(元) / 实测 decode tok/s（同量化同上下文口径）
- 价格必须带快照时间戳（周级波动）；每条证据记录 来源URL/日期/conf

## 分工（两线并行）

### 线 A：价格与市场 → 产出 `loop-artifacts/stages/02/research-pricing.md`
1. **G3 市场异常核验**：GDDR7 涨价 + RTX 5090 停产传闻 + 渠道炒价的真实性与幅度（多源：新闻/渠道商/官方回应，注意区分传闻与事实）
2. **G2 价格快照**（2026-10 中国大陆到手价，多平台 + 时间戳）：
   - NVIDIA 消费：RTX 5090 32G（官方 vs 水货）、5090D v2 24G、5080 16G、5070Ti 16G、5060Ti 16G
   - 二手：RTX 3090 24G、RTX 4090 24G（闲鱼/淘宝二手价区间）
   - 专业卡：RTX PRO 5000 48G、RTX PRO 6000 96G（国行渠道价）
   - Apple：Mac Studio M5 Max 36/48/64/128G 国行价 + 教育价、M5 Ultra 96G 起售价
   - AMD：RX 9070/9070XT 16G、RX 7900 XTX 24G 等 24G+ 型号
3. **G4 Apple 规格落地**：M5 Max（40核GPU/128GB/614GB/s）与 M5 Ultra（80核GPU/512GB/1.2TB/s）国行配置与发售状态
4. **G9 渠道风险**：水货无保/走私风险、二手卡质量风险、专业卡渠道溢价

### 线 B：性能与生态 → 产出 `loop-artifacts/stages/02/research-performance.md`
1. **G1 模型架构**：Qwen3.8-27B 的 config（层数/隐藏维/注意力头/KV heads/GQA/上下文上限）— 从 HuggingFace model card 或本地模型文件获取
2. **G5 实测性能搜集**（各候选跑 27B 级模型的 decode/prefill 实测，分上下文/量化/引擎）：
   - RTX 4090/5090/3090 跑 Qwen3.8-27B 或同级 27B 的 llama.cpp/vLLM 实测（GitHub/bilibili/论坛）
   - RTX PRO 5000/6000 实测（workspace KB 笔记 gpu-inference-hardware.md 有数据可引用）
   - Mac M3 Ultra/M4 Max/M5 跑 27B 的 MLX 实测（注意 M3 Ultra 512G 实测仅 30+ tok/s 的数据点）
   - 长上下文（64K/128K/200K+）下的速度衰减数据
3. **G6 软件生态门禁**：
   - Apple：MLX/LM Studio 对 27B 长ctx+并发≤8 的支持成熟度
   - NVIDIA：CUDA/llama.cpp/vLLM 无疑问，确认即可
   - AMD：ROCm 跑 27B 的成熟度与实测（不成熟则记录排除理由）
   - 国产卡：CANN 等生态成熟度（不成熟则记录排除理由）
4. **G11 候选补全**：是否有遗漏的重要候选（如 Threadripper+双卡、工作站整机方案）

## 研究纪律
- 所有网页访问优先用 web_search/web_extract（本环境可用）；需要登录态的页面标注"需人工"
- 每条证据：来源 URL + 抓取日期 + conf（0-1）；价格类额外标快照时间
- 传闻与事实严格区分：停产/涨价传闻标"传闻，未官方证实"
- 找不到数据的候选：标"无现货数据" + 给区间估计 + 保守假设，不得编造

## 产出要求
- 线 A：`loop-artifacts/stages/02/research-pricing.md`（价格表 + 市场核验结论 + 渠道风险）
- 线 B：`loop-artifacts/stages/02/research-performance.md`（架构参数 + 性能表 + 生态门禁结论）
- 两线各自完成后 commit + push 到 prompt-first-bench 仓库
- 最后各返回 ≤300 字总结：关键发现 TOP5 + 数据缺口

## 失败降级
- 某候选价格查不到 → 标"无现货数据" + 区间估计
- 实测数据只有单一来源 → conf 降 0.3 并标注
- web 工具不可用 → 报告 Lead，不得静默跳过
