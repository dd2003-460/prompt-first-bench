# 02 信息调研 — Flash-Next 硬件

> origin: ai · 2026-11-03T23:15+08:00 · **v2 更新 2026-11-04**
> 通道：web_search（4+9 次）+ 本地已有 v3.1 数据
> 降级声明：ego-browser Perplexity 登录态失效，本次用 web_search 替代（conf 相应标注）
> **v2 变更**：补 M5 Ultra Flash-Next 实测（MacStories/Apple MLR/Reddit）、R9700 国内水货价（闲鱼/淘宝）、radiance 成熟度+第三方复现、RunPod 价格、M5U 定价结构修正。原"理论 ~400 t/s"结论被实测推翻，见 §关键结论 1。

## 检索记录

| # | 查询 | 来源 | 观察时间 | 关键发现 | conf |
|---|------|------|----------|----------|------|
| 1 | R9700 国内水货价 2026年11月 渠道报价 | Newegg/eBay/gpuprix/JP/IN 多源 | 2026-11-03 | US $1,699-2,730（MSRP $1,299 +31-110%），JP ¥379,800 (+103%)，IN ₹245,800 (+120%)，eBay 均价 $2,650。无直接中国水货报价 | 0.7（缺 CN 直报） |
| 2 | radiance StillDeadcode GitHub stars commits 2026 | Codeberg + HF | 2026-11-03 | Codeberg 项目（非 GitHub），RDNA4 gfx1200/1201 专用，C++/HIP，双卡默认 --tp 2 --tp-wire wht6，HF .rad 容器 113.6GiB，experts 4bit codebook GPTQ + trunk int8 W8A8，质量 92.85% top-1 vs bf16 95.13% | 0.8 |
| 3 | Strata Niko1221 latest release November 2026 | GitHub releases | 2026-11-03 | **v0.2.10 (Nov 2)**：DFlash2 默认 drafter，"one model across all your cards on Linux"，128K on 8GB cards，gfx12 chunked kernel 64-token start → prompt +3.5-6.1% | 0.9 |
| 4 | Mac M5 Ultra Mac Studio 2026 release specs | Apple + 媒体 | 2026-11-03 | **Aug 25 发布，Sep 22 出货**。M5 Ultra：36-core CPU / 80-core GPU / **1.2TB/s BW** / 最高 512GB unified。$5,499 起（edu $5,099）。512GB 配置延期至 ~1 月底。4.3x AI vs M3 Ultra。TB5 4-node cluster 3x | 0.9 |
| 5 | MacStudio M5 Ultra Flash-Next tokens per second benchmark | MacStories + Apple ML Research + Reddit r/LocalLLM + llmcheck/presenc | 2026-11-04 | **M5 Ultra 跑 Qwen3.8-Flash-Next 实测**：短 prompt >100 t/s；64K-256K ctx 下 60-85 t/s（MacStories，oMLX oQ4e）；128K 处 ~61 t/s（YouTube 引述 MacStories）；256K ctx 写速 74.7 t/s vs M3 Ultra 38.6（voltgridnews 转述 MacStories 表）；prefill 16K@2,887 t/s。**~400 t/s 理论值严重高估**（KV cache 读写+routing 开销吃掉大部分带宽） | 0.85（多个独立来源一致区间） |
| 6 | M5 Ultra 512GB price configuration | MacRumors/CNET/voltgridnews/progressiverobot | 2026-11-04 | **定价结构修正**：$5,499 = 30-core/64-core/96GB 基础款；256GB 需 36-core/80-core 顶配芯片（+$4,000 级）；**512GB 最低 $22,299**（MacRumors 2026-10-28：$6,799 顶配芯片 + $15,500 内存升级）；512GB 配置 10 月底-12 月初到货（各源不一，取"已可订购"）。Engadget 测 256GB/2TB 配置 $11,299 | 0.85（MacRumors 有具体日期） |
| 7 | R9700 国内价格 闲鱼 淘宝 | vramglass.com(闲鱼聚合) + 淘宝商品页 + pconline + smzdm | 2026-11-04 | **CN 水货价补齐**：闲鱼当前 ¥16,900（区间 ¥15,000-18,000，16 件在售，30 天 +43%，7 天 -3.4%）；淘宝行货 ¥16,099-17,800（华硕/技嘉涡轮版），瀚铠盒装 ¥16,500，XFX 海外版 ¥29,999；pconline 行货参考价 ¥10,999-12,999（京东/讯景，未见实际成交）。折合 $2,300-2,600，与 US eBay 均价相当 | 0.75（闲鱼为二手聚合价，非一手） |
| 8 | radiance maturity third-party benchmarks | Codeberg repo + Level1Techs forum + Reddit r/LocalLLaMA + Docker Hub + Patreon | 2026-11-04 | **成熟度确认**：Codeberg 86 stars / 47 forks（对比：同作者 vllm-radiance 20/5）；release cadence 极高（1.9.0→1.16.0 在 ~3 周内，Nov 2 最新）；贡献者 ≥4 人（RikshaDriver/keptn42/mici81/gostar）；CI 每 push 跑全套测试；**第三方复现**：Level1Techs 2×ASUS R9700 实测 Flash-Next MoE 单流 137 tok/s（medium reasoning）/ 162 tok/s（regular），峰值聚合 1103 @ conc16；Reddit 个人 bench（Threadripper P620 + 128GB DDR4）radiance 147.2 gen t/s vs Strata 79.1 vs llama.cpp 17.6；radiance issue #161 显示社区在做 fp8 attention 优化（PR #162 merged，v1.10.0） | 0.85 |
| 9 | RunPod A100 price November 2026 | runpod.io 官方 + computeprices.com | 2026-11-04 | **cloud 价格落地**：RunPod A100 PCIe 80GB $1.19/hr（Community）/ $1.79/hr（Secure）；A100 SXM 80GB $1.39/$1.79；H100 PCIe $2.89/hr（dev.to 引）；GCP/AWS 按需 A100 40GB ~$3.28/GPU-hr。原报告 "$1.2-2/hr" 基本准确（PCIe Community 档） | 0.9（官方页面） |

## 关键结论（带来源）

1. **~~M5 Ultra 理论 ~400 t/s~~ → 实测 60-100+ t/s（ctx 相关）**：MacStories 实测 Flash-Next 4-bit 在 M5 Ultra 上短 prompt >100 t/s，128K ctx 衰减到 ~61，256K 后仍 74.7（oQ4e/oMLX）。Apple ML Research 官方 MLX benchmark 给的是 dense 27B（19.69 t/s @8K）和 Muse Spark Open（24.99 t/s），**没有 Flash-Next 的官方数字**。~400 t/s 是纯权重带宽上限，MoE decode 的实际瓶颈还包括 KV cache 读写（262K ctx 时 KV 很大）、routing、引擎调度——实测只有理论值的 15-25%。**报告中 ~400 必须改为实测区间 60-100+ [实测]**。[来源: MacStories review + voltgridnews + llmcheck + YouTube 引述] conf 0.85

2. **M5 Ultra 512GB 真实价格 = $22,299 起，不是 $5,499**：$5,499 是 96GB 基础款（30-core/64-core）。要 512GB 必须顶配 36-core/80-core 芯片 + $15,500 内存升级。256GB 配置约 $9,500-11,300（视存储）。这大幅改变性价比叙事：**M5U 512GB 不再是"$5,499+"，而是 $22k+ 的机器**。[来源: MacRumors 2026-10-28 + CNET + progressiverobot] conf 0.85

3. **R9700 全球性短缺，溢价 31-110%（含 CN）**：US $1,699-2,730 / JP ¥369,000-399,800 / DE €2,261 / **CN 闲鱼 ¥15,000-18,000（中位 ¥16,900，30 天 +43%）/ 淘宝行货 ¥16,099-17,800**。CN 一手行货参考价 ¥10,999-12,999 但无实际成交记录。采购决策需考虑"等降价"vs"现在买"的时间成本。[来源: Newegg/eBay/gpuprix/ツクモ/heise/vramglass/淘宝/pconline] conf 0.8

4. **radiance 是 RDNA4 专用引擎，成熟度比预想高**：Codeberg 86 stars/47 forks，3 周 7 个 minor release，≥4 外部贡献者，CI 全量测试，Docker Hub 镜像日更。**两个独立第三方复现了 Flash-Next 速度**：Level1Techs 2×R9700 单流 137-162 t/s；Reddit P620 用户 147.2 t/s（DDR4 128GB 主机！）。质量 92.85% top-1（全 token）/ 94.57%（assistant turns）vs bf16 95.13%。对 autoresearch 场景可接受。[来源: Codeberg + Level1Techs + Reddit + Docker Hub] conf 0.85

5. **Strata 0.2.10 的 DFlash2 默认 drafter 可能改变速度预期**：spec decoding 加速比取决于 acceptance rate，Flash-Next 的 MoE 结构是否适合 DFlash2 未验证。所有基于 Strata 的速度数字需标注"待 DFlash2 实测"。注意 Reddit 个人 bench 里 Strata 0.1.42 只有 79.1 t/s（radiance 的 54%），DFlash2 能否翻盘是关键变量。[来源: GitHub release notes + Reddit bench] conf 0.6

6. **MoE 部署瓶颈 = 内存容量 + swap 效率，不是显存容量**：Flash-Next 176B total / 6B active，4bit ≈ 88GB 权重（radiance .rad 容器 113.6GiB，含 MTP head + vision tower）。需要 ≥96GB 可用内存。PCIe Gen4 x16 (~25GB/s) 是 offload 瓶颈；统一内存架构（Mac）完全消除此问题。radiance 方案：热 expert 留 VRAM + 冷 expert 从 pinned host pool 流式加载（host 需 ~32GB 空闲 RAM）。[来源: 模型 config + PCIe spec + HF model card] conf 0.9

7. **新候选浮现：Intel Arc Pro B70 32GB**：US 售价从 $949 涨到 $2,399（+58%），日本 ¥274,980（无货）。同为 32GB 专业卡，若 AMD 生态不可用时的备选。暂不纳入主表（软件生态未验证），列入观察。[来源: gaming-st.com 2026-10] conf 0.6

## [待核验] 清单（→ 02.5 交叉核对）

- [x] M5 Ultra 跑 Flash-Next 的实测 t/s → **已补**（§检索 5：60-100+ t/s ctx 相关）
- [x] radiance 引擎成熟度 → **已补**（§检索 8：86 stars/47 forks/4 贡献者/2 个第三方复现）
- [ ] Strata 0.2.10 DFlash2 对 Flash-Next MoE 的实际加速比（P1，仍未解）
- [x] R9700 国内水货实际成交价 → **已补**（§检索 7：闲鱼 ¥15-18k）
- [ ] 本机 27B baseline 200 t/s 的机型 + 测量方法（物理红旗，待成璐确认）
- [ ] 是否有新消费级卡（RTX 5080 / RX 9060 XT）值得纳入候选（P2）
- [x] cloud GPU 租赁价格 → **已补**（§检索 9：RunPod A100 80GB $1.19-1.79/hr）
- [ ] M5U 512GB 配置的 Flash-Next 实测（现有实测来自 256GB 单元，512GB 只影响容量不影响带宽，速度应相近但需确认）