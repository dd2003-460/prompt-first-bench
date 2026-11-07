# Q9 Gold Tree — VLM 四路线对比（CLIP / SAM / GPT-4V / Gemini）：任务-架构匹配判据

> 题面：`bench/questions/Q9-vlm-arch.txt`｜域：AI/ML — multimodal architecture（B 面域内新题）
> **独立调研声明：本树全部数值来自 T50 任务期间的独立调研（arXiv 一手 abstract + 公开技术页/数据集卡，观察日 2026-11-07），未引用 `gold-tree.md`（Q1）及任何 Q1-Q5 gold 内容。**
> 节点计数：**34 节点 / 主干深度 4 / 叶子 27 个**（含 4 个黑盒叶子）。

## 结论先行

- **四个对象不是同一类模型，横向"跑分对比"本身是范畴错误**：CLIP 输出 embedding（判别式双塔）、SAM 输出 mask（提示驱动解码器）、GPT-4V/Gemini 输出文本（自回归生成）。正确的根节点是**任务-架构匹配矩阵**：先按输出空间分组，再在组内比规格。
- **量化锚点（本树的硬事实层）**：CLIP 400M 图文对 / ViT-L/14 768-dim 共享嵌入 / zero-shot ImageNet 76.2%；SAM 11M 图像 / 1.1B masks / ViT-H 636M 编码器；GPT-4V 动态 tiling 每图 85–1,445 tokens；Gemini 1.5 跨模态 >99% recall 直至 ≥10M tokens 上下文。
- **最容易被漏掉的判断（★）**：分辨率处理是**成本与能力的隐藏轴**——同一张 1024×1024 图，low detail 85 tokens、high detail 765 tokens，差 **9×**；上限样例 1,445 tokens 时差 **17×**。对比 VLM 而不谈图像 token 成本的，结论不可用于选型。

---

## 全树

```
N-0  任务-架构匹配判据  M(task, model)                     SHARE 1.00   split
│    四维匹配：输出空间 × 视觉接入 × 训练信号 × 上下文/提示形态
│    每维落到可查证的量化锚点（数据规模/参数量/token 成本/精度）
│
├─ N-1  视觉接入方式与表征（眼睛怎么长）                      .35   split  ★F-A
│  ├─ N-1.1  CLIP 双塔对比：图像/文本编码器各自独立 → 投影到共享
│  │         embedding 空间；ViT-L/14 维度 768                  leaf S-a
│  ├─ N-1.2  CLIP 训练数据：WIT 400M 网络图文对（从零训练）      leaf S-a
│  ├─ N-1.3  SAM：MAE 预训练 ViT-H 编码器 ~636M 参数；输入
│  │         1024×1024 → 64×64×256 embedding；每图只编码一次，
│  │         prompt 复用（交互成本被摊销）                       leaf S-a
│  ├─ N-1.4  GPT-4V：动态分辨率 tiling——先缩放进 2048×2048、
│  │         短边至 768，再切 512×512 tiles；token 成本 =
│  │         85 base + 170×tiles（high）/ flat 85（low）        leaf S-b
│  │  │      （官方文档口径，三个独立社区源逐项一致，conf 0.8）
│  │  └─ N-1.4.1  算例锚点：1024×1024 → 2×2 tiles → 85+4×170 =
│  │              765 tokens；上限样例 8 tiles → 1,445 tokens   leaf S-b
│  ├─ N-1.5  Gemini：原生多模态（natively multimodal，文本/图像/
│  │         音频/视频联合训练谱系；1.0 报告具体数值本次未复核，
│  │         只采 abstract 级主张）                              leaf S-a
│  └─ N-1.6  连接层谱系（参照架构，冻结集内登记的显式扩展）      split
│     ├─ N-1.6.1  Flamingo：冻结视觉塔+冻结 LLM 之间插 Perceiver
│     │           Resampler + gated cross-attention，任意交错
│     │           图文，few-shot ICL 达 SOTA                     leaf S-a
│     └─ N-1.6.2  LLaVA：冻结 CLIP ViT-L/14 → 可训练线性投影
│                 (1024→5120) → Vicuna；1.5 版升级 336px +
│                 2 层 MLP + 558K LAION-CC-SBU 对齐数据          leaf S-a
│
├─ N-2  输出空间与任务形态（嘴是什么）                        .25   split
│  ├─ N-2.1  CLIP → 相似度标量/嵌入：检索、zero-shot 分类
│  │         （ImageNet zero-shot top-1 76.2% ≈ 有监督
│  │         ResNet-50 的 76.1%）                               leaf S-a
│  ├─ N-2.2  SAM → mask：promptable 分割（点/框/mask 提示）；
│  │         SA-1B = 11M 图像 + 1.1B masks；zero-shot 常超
│  │         有监督结果                                          leaf S-a
│  ├─ N-2.3  GPT-4V → 自回归文本：通用 VQA/文档理解/多模态推理
│  │         （模拟律考 top ~10% 为能力锚点）                    leaf S-a
│  └─ N-2.4  Gemini → 自回归多模态文本 + 超长上下文：跨模态
│            near-perfect recall >99% 直至 ≥10M tokens
│            （对照 Claude 3.0 200k / GPT-4 Turbo 128k）        leaf S-a
│
├─ N-3  训练策略（怎么养成）                                  .20   split
│  ├─ N-3.1  CLIP：对比损失从零预训练；batch 32,768（每 batch
│  │         32,768 个对比负例）；32 epochs；256×V100 12 天
│  │         （@336px 版 18 天）                                 leaf S-a
│  ├─ N-3.2  SAM：model-in-the-loop 数据引擎三阶段
│  │         assisted-manual → semi-automatic → fully-automatic
│  │         （32×32 点网格全自动标注产出 SA-1B）                leaf S-a
│  ├─ N-3.3  GPT-4V：next-token 预训练 + 后训练对齐（技术报告
│  │         口径）；视觉阶段的训练数据/配比未公开               leaf B1  黑盒
│  ├─ N-3.4  LLaVA 式两阶段（参照）：Stage1 只训投影（595K 过滤
│  │         CC3M 对齐）；Stage2 冻 CLIP 训投影+LLM（158K GPT-4
│  │         生成指令数据）；对齐预训练贡献 ScienceQA +5.11pp    leaf S-a
│  └─ N-3.5  Gemini 1.5：MoE 系"compute-efficient"+ 长上下文
│            能力（10M tokens 研究档）                            leaf S-b
│
├─ N-4  适用场景匹配（谁干什么）                              .15   split  ★F-B
│  ├─ N-4.1  检索 / zero-shot 分类 / 图文相似度 → CLIP
│  │         （双塔可预计算索引，唯一能建 ANN 库的路线）         leaf S-c
│  ├─ N-4.2  分割 / 标注引擎 / 数据工厂 → SAM                    leaf S-c
│  │  └─ N-4.2.1  视频扩展：SAM 2 = Hiera-L 224.4M、SA-V ~51K
│  │              视频 / ~643K masklets、图像上比 SAM 1 快 6×   leaf S-b
│  ├─ N-4.3  通用 VQA / 文档理解 / 多模态 agent → GPT-4V
│  │         （生成式输出 + tiling 高分辨率细节）                leaf S-c
│  ├─ N-4.4  长视频 / 超长文档 / 交错图文检索 → Gemini
│  │         （10M 级上下文是唯一量级）                          leaf S-c
│  └─ N-4.5  成本轴：单图 token 成本 GPT-4V 85–1,445 tokens
│            （9–17× 摆幅）vs CLIP 单 embedding（可预计算、
│            查询期近零）vs SAM 一次性编码+轻量解码              leaf S-b
│
└─ N-5  局限与失败模式（nuisance，改结论边界不改结构）        .05   split
   ├─ N-5.1  CLIP：无生成能力；细粒度空间关系/计数类任务弱
   │         （双塔独立编码的结构性后果，推导级）                leaf S-c
   ├─ N-5.2  SAM：mask 无类别标签（class-agnostic，语义归属需
   │         外接分类器——"分割一切但不认识一切"）               leaf S-b
   ├─ N-5.3  GPT-4V：幻觉/空间推理局限（System Card 口径的
   │         定性主张；本次未复核一手 PDF → 不引具体数值）      leaf B2  黑盒
   └─ N-5.4  Gemini：架构细节（参数量/MoE 路由/视觉编码器规格）
            公开度低，量化对比缺位                                leaf B3  黑盒
```

**图例**　`.35` SHARE（对根判据 M 的相对权重，按"选型错判危害 × 证据强度"归一，非账单占比）｜`leaf S-a` 停止：一手论文 abstract/官方口径可查｜`leaf S-b` 停止：二手一致转述或区间估计（GPT-4V tiling 三源一致，conf 封顶 0.8）｜`leaf S-c` 停止：可由架构定义推导｜`leaf B#` 停止：黑盒，见下表｜`★F-A/B` 本次分解中「不看就会比错」的两处

---

## 两处 ★ 判断（本树与「凭直觉列清单」的分水岭）

**★F-A：先按输出空间分组，再谈对比——四对象是三个不同物种。**
CLIP（embedding）、SAM（mask）、GPT-4V/Gemini（文本）的输出空间不同，任何"CLIP vs GPT-4V 谁强"的直接比较都不可判。可比的只有：① 组内（GPT-4V vs Gemini：生成式多模态，比上下文长度与图像 token 成本）；② 跨组的**任务适配**（同一任务谁能在结构上完成）。直觉清单会把四个名字并列打分——按本树这是根节点级错误。

**★F-B：分辨率处理机制是成本轴的主变量，不是实现细节。**
GPT-4V 的 tiling（85 + 170×tiles）让同一张图的推理成本随 detail 模式与尺寸在 85–1,445 tokens 间摆动（9–17×）；CLIP 的双塔则允许图像侧全部预计算、查询期成本近零；SAM 一次性编码 + 轻量 prompt 解码摊销交互成本。**三者的成本结构由架构决定，量级差不是价格谈判能抹平的**——大批量图文检索选 CLIP 是结构性的，不是省钱的权宜。

---

## 黑盒表

| 编号 | 参数 | 区间 | 为什么是黑盒 | 怎么实测 |
|---|---|---|---|---|
| B1 | GPT-4V 视觉阶段训练数据/配比 | 未公开 | 技术报告不含视觉训练细节 | 无法直接实测；用行为探测（分辨率敏感性实验）间接推断 |
| B2 | GPT-4V 幻觉/空间局限的量化率 | 未复核 | System Card 一手 PDF 本次未拉取 | MMMU/POPE 类基准自测 |
| B3 | Gemini 架构参数（总参数/MoE 路由/视觉编码器） | 未公开 | 官方从未披露 | 不可测；只能行为级对比 |
| B4 | 业务任务的真实分布（哪类查询占多少） | 题面未给 | 选型结论对任务分布敏感 | 拿业务查询日志按 N-4 四类打标 |

---

## OC-1 卡片（三个样例，字段定义见 `../rubric/output-contract.md`）

```
### N-0  任务-架构匹配判据
PARENT:  -
NOW:     未知
GOAL:    每个候选任务一行匹配结论（选谁 + 量化锚点），四维齐备
GAP:     缺「业务任务清单」（B4）——匹配矩阵的任务侧输入
IN:      题面 + 本树 N-1..N-5 + 黑盒表
OUT:     M(task, model) 矩阵
KIND:    signal
RES:     -
SHARE:   1.00
BOUND:   -
TEST:    跑本文件 §「算例」的 token 成本表 + 分组可判性检查
STATUS:  split
```

```
### N-1.4  GPT-4V 动态分辨率 tiling
PARENT:  N-1
NOW:     high：缩放进 2048×2048、短边至 768 → 切 512×512 tiles →
         85 + 170×tiles tokens；low：flat 85 tokens
GOAL:    给定图像尺寸直接算出 token 成本
GAP:     官方一手文档现状未复核（三社区源一致，conf 0.8 封顶）
IN:      图像宽高 + detail 模式
OUT:     tokens/image
KIND:    signal
RES:     公式
SHARE:   —
BOUND:   9–17× 摆幅（85 → 765 → 1,445）
TEST:    1024×1024 high：短边 768 → 768×768 → 2×2 tiles → 85+680 = 765 ✓
STATUS:  leaf:S-b
```

```
### N-2.2  SAM 输出空间
PARENT:  N-2
NOW:     mask（class-agnostic）；SA-1B 11M 图 / 1.1B masks
GOAL:    判定"分割类任务"归 SAM，"识别类任务"不归 SAM
GAP:     无（一手 abstract + 两独立二手一致）
IN:      任务是否需要类别语义
OUT:     匹配/不匹配 + 需外接分类器的边界声明
KIND:    signal
RES:     —
SHARE:   —
BOUND:   语义归属必须外接（CLIP 或 LLM）——组合成本进 N-4.5
TEST:    对"数图里有几只猫"类任务：SAM 单独不可完成（分割≠计数≠分类）
STATUS:  leaf:S-a
```

---

## 算例（可复算，用于后续判分）

**① GPT-4V tiling token 成本表**（公式：先缩放进 2048²、短边至 768，tiles = ⌈w/512⌉×⌈h/512⌉）：

| 原图 | 缩放后 | tiles | tokens（high） | tokens（low） | 倍差 |
|---|---|---|---|---|---|
| 512×512 | 768×768? 否——短边已 ≤768 不放大，512×512 | 1×1 | 85+170 = 255 | 85 | 3.0× |
| 1024×1024 | 768×768（短边缩至 768） | 2×2 = 4 | 85+680 = **765** | 85 | 9.0× |
| 768×2048 | 短边 768 保持 | 2×4 = 8 | 85+1360 = **1,445** | 85 | 17.0× |

**② 检索场景成本结构对比**（1M 张图入库、日均 10 万次查询）：
- CLIP 路线：图像嵌入**一次性预计算**（1M × 单图编码），查询期只有文本编码 + ANN 近邻（近零边际）；
- GPT-4V 路线：每次查询若带图 → 255–1,445 tokens/图 × 10 万/日，token 成本随查询量**线性**增长。
→ 判别式检索任务上双塔是结构性胜者（★F-B 的算例化）；反之"看懂这张图的细节并回答开放问题"只有生成式路线可完成（★F-A 的分组可判性）。

**③ 匹配矩阵骨架**（可判性检查用）：

| 任务 | CLIP | SAM | GPT-4V | Gemini |
|---|---|---|---|---|
| 图文检索/zero-shot 分类 | ✅ 结构适配（76.2% 锚点） | ❌ 无此输出 | ⚠️ 可行但成本结构错（②） | ⚠️ 同左 |
| 分割/标注 | ❌ 无 mask 输出 | ✅（1.1B masks 锚点） | ❌ | ❌ |
| 开放 VQA/文档理解 | ❌ 无生成 | ❌ | ✅（tiling 细节） | ✅ |
| 数小时视频/超长文档 | ❌ | ⚠️ 仅逐帧分割（SAM 2） | ⚠️ 128k 级 | ✅（10M tokens、>99% recall） |

---

## 来源表

| # | 事实 | URL | 观察日 | conf |
|---|---|---|---|---|
| S1 | CLIP：400M 图文对（WIT）从零训练；zero-shot 匹配有监督 ResNet-50；30+ 数据集迁移 | http://arxiv.org/abs/2103.00020 | 2026-11-07 | 0.95 |
| S2 | CLIP ViT-L/14@336：zero-shot ImageNet 76.2%（vs supervised ResNet-50 76.1%）；batch 32,768；32 epochs；256×V100 12 天/18 天；prompt ensemble +3.5pp | https://www.abhik.ai/papers/clip | 2026-11-07 | 0.85 |
| S3 | CLIP ViT-L/14 共享 embedding = 768-dim（open_clip 配置口径）；ALIGN 1.8B 噪声对/SigLIP sigmoid 损失对照 | https://pristren.com/blog/clip-image-text-similarity/ | 2026-11-07 | 0.8 |
| S4 | SAM：11M 图像 + 1.1B masks（SA-1B）；promptable；zero-shot 常超有监督 | http://arxiv.org/abs/2304.02643 | 2026-11-07 | 0.95 |
| S5 | SAM ViT-H ~636M、1024×1024 → 64×64×256、每图一次编码；数据引擎三阶段（32×32 点网格全自动） | https://labhub.hopto.org/blog/ai-papers/segment_anything_model_sam_evolution?lang=en | 2026-11-07 | 0.85 |
| S5' | 同上（第二独立源：636M/ViT-H、三阶段数据引擎、SAM2 对照表） | https://aiwiki.ai/wiki/segment_anything_model_and_dataset_sam_and_sa-1b | 2026-11-07 | 0.8 |
| S6 | GPT-4：图+文入文出；模拟律考 top ~10%；next-token 预训练 + 后训练对齐 | http://arxiv.org/abs/2303.08774 | 2026-11-07 | 0.95 |
| S7 | GPT-4V tiling：2048 cap / 短边 768 / 512×512 tiles / 85+170×tiles / low=85 / 1024²≈765 / 上限样例 1,445 | https://ai-tldr.dev/learn/multimodal-ai/vision-models/how-vision-models-see/ | 2026-11-07 | 0.8 |
| S7' | 同上（第二源，公式与算例逐项一致） | https://fast.io/resources/chatgpt-image-upload-limit/ | 2026-11-07 | 0.8 |
| S7'' | 同上（第三源，含 2048×2048 缩放规则） | https://artificial-intelligence-wiki.com/ai-tools/chatgpt/chatgpt-vision-guide/ | 2026-11-07 | 0.75 |
| S8 | Flamingo：桥接冻结视觉塔与冻结 LLM（Perceiver Resampler + gated cross-attention 为论文正文组件名）；交错图文；few-shot SOTA | http://arxiv.org/abs/2204.14198 | 2026-11-07 | 0.85 |
| S9 | LLaVA：GPT-4 纯文本侧生成多模态指令数据；CLIP ViT-L/14 + 投影 + Vicuna 端到端 | http://arxiv.org/abs/2304.08485 | 2026-11-07 | 0.9 |
| S9' | LLaVA 细节：线性投影 1024→5120；Stage1 595K 过滤 CC3M；Stage2 158K；ScienceQA +5.11pp；1.5 版 336px/MLP/558K+665K；两源一致 | https://pixelbank.dev/concepts/llava + https://github.com/jjakimoto/research-issues/issues/1311 | 2026-11-07 | 0.85 |
| S10 | Gemini 1.5：>99% recall 直至 ≥10M tokens；对照 Claude 3.0 200k / GPT-4 Turbo 128k；长文档/长视频 QA/长上下文 ASR SOTA；匹配或超 Gemini 1.0 Ultra；职业任务省时 26-75% | http://arxiv.org/abs/2403.05530 | 2026-11-07 | 0.95 |
| S11 | Gemini 1.0 定位"原生多模态"（URL 有效，abstract 本次未复读，只采谱系级主张） | http://arxiv.org/abs/2312.11805 | 2026-11-07 | 0.7 |
| S12 | SAM 2：Hiera-L 224.4M；SA-V ~51K 视频 / ~643K masklets；比 SAM 1 快 6× | https://aiwiki.ai/wiki/segment_anything_model_and_dataset_sam_and_sa-1b | 2026-11-07 | 0.75 |

## 找不到 / 未验证

1. **GPT-4V tiling 的官方一手文档**：OpenAI/Azure 文档页本沙箱未能直接复核现状，三个独立社区源逐项一致（S7/S7'/S7''），conf 封顶 0.8，N-1.4 系叶子全部按 S-b 计。
2. **Gemini 架构参数**（参数量/MoE 路由细节/视觉编码器规格）：官方从未披露 → B3 黑盒，树内不引任何具体数字。
3. **CLIP 768-dim 的一手表格页**：论文正文表格未拉取原文，采用 open_clip 配置口径（S3，conf 0.8）+ ViT-Large 标准宽度通识，双挂来源。
4. **GPT-4V System Card 的量化幻觉率**：一手 PDF 未复核 → N-5.3 只作定性黑盒，不引数值。
