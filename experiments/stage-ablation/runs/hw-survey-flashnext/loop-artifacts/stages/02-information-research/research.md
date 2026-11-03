# 02 信息调研 — Flash-Next 硬件

> origin: ai · 2026-11-03T23:15+08:00
> 通道：web_search（4 次）+ 本地已有 v3.1 数据
> 降级声明：ego-browser Perplexity 登录态失效，本次用 web_search 替代（conf 相应标注）

## 检索记录

| # | 查询 | 来源 | 观察时间 | 关键发现 | conf |
|---|------|------|----------|----------|------|
| 1 | R9700 国内水货价 2026年11月 渠道报价 | Newegg/eBay/gpuprix/JP/IN 多源 | 2026-11-03 | US $1,699-2,730（MSRP $1,299 +31-110%），JP ¥379,800 (+103%)，IN ₹245,800 (+120%)，eBay 均价 $2,650。无直接中国水货报价 | 0.7（缺 CN 直报） |
| 2 | radiance StillDeadcode GitHub stars commits 2026 | Codeberg + HF | 2026-11-03 | Codeberg 项目（非 GitHub），RDNA4 gfx1200/1201 专用，C++/HIP，双卡默认 --tp 2 --tp-wire wht6，HF .rad 容器 113.6GiB，experts 4bit codebook GPTQ + trunk int8 W8A8，质量 92.85% top-1 vs bf16 95.13% | 0.8 |
| 3 | Strata Niko1221 latest release November 2026 | GitHub releases | 2026-11-03 | **v0.2.10 (Nov 2)**：DFlash2 默认 drafter，"one model across all your cards on Linux"，128K on 8GB cards，gfx12 chunked kernel 64-token start → prompt +3.5-6.1% | 0.9 |
| 4 | Mac M5 Ultra Mac Studio 2026 release specs | Apple + 媒体 | 2026-11-03 | **Aug 25 发布，Sep 22 出货**。M5 Ultra：36-core CPU / 80-core GPU / **1.2TB/s BW** / 最高 512GB unified。$5,499 起（edu $5,099）。512GB 配置延期至 ~1 月底。4.3x AI vs M3 Ultra。TB5 4-node cluster 3x | 0.9 |

## 关键结论（带来源）

1. **M5 Ultra 是当前最强单卡 LLM 推理平台**：1.2TB/s 带宽 + 512GB 统一内存 = 无 PCIe 瓶颈 + 装下完整模型 + KV cache + 裁判模型。理论 decode ~400 t/s @ 6B active 4bit（1.2TB/s ÷ 3GB/token）。[来源: Apple spec + 带宽公式推导] conf 0.7（理论值，无实测）

2. **R9700 全球性短缺，溢价 31-110%**：不是中国特例。US/EU/JP/IN 全线溢价，eBay 均价 $2,650。采购决策需考虑"等降价"vs"现在买"的时间成本。[来源: Newegg/eBay/gpuprix] conf 0.8

3. **radiance 是 RDNA4 专用引擎，质量损失可控**：92.85% top-1 agreement（全 token）/ 94.57%（assistant turns）vs bf16 95.13%。对 autoresearch 场景（不需要逐 token 精确复现）可接受。但成熟度待验（Codeberg 非 GitHub，社区规模未知）。[来源: Codeberg + HF] conf 0.7

4. **Strata 0.2.10 的 DFlash2 默认 drafter 可能改变速度预期**：spec decoding 加速比取决于 acceptance rate，Flash-Next 的 MoE 结构是否适合 DFlash2 未验证。所有基于 Strata 的速度数字需标注"待 DFlash2 实测"。[来源: GitHub release notes] conf 0.6

5. **MoE 部署瓶颈 = 内存容量 + swap 效率，不是显存容量**：Flash-Next 176B total / 6B active，4bit ≈ 88GB 权重。需要 ≥96GB 可用内存。PCIe Gen4 x16 (~25GB/s) 是 offload 瓶颈；统一内存架构（Mac）完全消除此问题。[来源: 模型 config + PCIe spec] conf 0.9

## [待核验] 清单（→ 02.5 交叉核对）

- [ ] M5 Ultra 512GB 配置跑 Flash-Next 的实测 t/s（目前只有理论 ~400）
- [ ] radiance 引擎成熟度（star 数/commit 频率/issue 活跃度/user reports）
- [ ] Strata 0.2.10 DFlash2 对 Flash-Next MoE 的实际加速比
- [ ] R9700 国内水货实际成交价（目前只有海外渠道）
- [ ] 本机 27B baseline 200 t/s 的机型 + 测量方法（物理红旗）
- [ ] 是否有新消费级卡（RTX 5080 / RX 9060 XT）值得纳入候选
- [ ] cloud GPU 租赁（RunPod/Vast.ai）价格 + 延迟作为替代选项
