# GOAL: idea53-cross-gradient（#53 独立短文）

> stage-gate goal_id: idea53-cross-gradient · 2026-11-24 D 指令"定 idea53 这个目标"
> 定位：从 #10 模块升格为**独立 goal**（D 判断：最快最小可发表）。#10 主线论文不受影响，#53 若成立可反哺 #10 analysis 章节。

## 1. 本地背景扫描（4 项，有证据）

| 项 | 证据 |
|---|---|
| 项目 research/ | pfb/research/gpu-hardware-candidates-20261124.md（硬件候选集+V_fine 构造样例）；pfb/modules/F-theory/research/idea53-info-theoretic-contribution.py+.json（节点级 MI 已有） |
| 项目 memory/ | pfb/modules/IDEA-INDEX.md #53 行（四轮 arena 核验全记录，commits 70dca8efa/81be67cb9/82a67df96） |
| 全局 lit-survey | pfb/tasks/IDEA-review/result.md（arena 四轮撞车核验：DDx 三阶段/信息增益消歧/步类型分类学三线占位，未见=树×类型×深度×信息贡献测量+两级判定交叉梯度） |
| 历史结论 | 第三轮"浅层主导"=误读（词表偏向枚举型）；重释后=claim 的另一半（coarse 级浅层主导已实测成立） |

## 2. 调研对象全集

- **纳入**：三份 GPU run 树（rep-scan n=3849 / t53b n=5497 / stage-ablation GPU域 n=18243）——已有数据，纯离线
- **纳入**：V_fine 构造样例（5090 发射砍半→慢40% 方向修正 / T5000 高精度→瓶颈80%+ 粒度细化）——纯 spec+计算
- **排除**：跑新实验（D 明确不想跑，数据已有）
- **排除**：进 gold 树（D 2026-11-24 决策：保 gold 正交性，硬件=领域知识不混入方法论骨架）
- **排除**：embedding 类测量（macOS sentence_transformers regex 坑，27b subagent 两次撞 repetition loop）——用纯数学闭式 MI

## 3. 正交维度拆解

- **V_coarse**（资源类标签："带宽受限/算力受限"）：词表可测，已有 is_bottleneck 词表
- **V_fine**（机制级判断："容量 vs 带宽"/"issue rate vs decode width"）：27b judge 打标（127.0.0.1:8787），降级判据=机制级词正则（容量/带宽/issue rate/decode width/发射/occupancy）
- **正交性**：V_fine 条件化 V_coarse（I(L;V_fine|V_coarse)），粗/细两级不混算
- **完备性**：两级覆盖"枚举→判断"全链（arena 第四轮确认词表只够 coarse 级）

## 4. 量化定义（公式，无模糊词）

- I(L_k; V_coarse) = Σ p(l,v) log p(l,v)/p(l)p(v)，各层 k 分别算
- I(L_k; V_fine | V_coarse) = Σ p(l,vf,vc) log p(l,vf|vc)/p(l,vf|vc)
- **生死线**：I(L_k; V_fine|V_coarse) 随 k 单调不降（L4 > L1）→ claim 成立；不升 → claim 死
- **对照臂**：①深度置换（层标签随机打乱，MI 应→0）②fake-run 占位（无瓶颈节点，MI 应→0）③浅深节点数配平 ④层内类型对照（同层内判断型 vs 枚举型 fine-MI 比较，解 type×depth 混淆）
- **HARKing 防御**：判据+公式预注册（本文件即预注册），held-out=stage-ablation 域（前三轮未用其做 claim 推导）

## 5. 任务书（已派发，含失败降级）

| 任务 | 通道 | 状态 | 失败降级 |
|---|---|---|---|
| 交叉梯度计算（V_coarse 词表 + V_fine 27b judge） | subagent deleg_53e3a082 | running | 27b 打标失败→机制级词正则降级判据（标"降级"） |
| 投稿策略（对标/免费 venue/接受概率/最快路径） | arena 第五轮 session 01a20b11 | running | arena 超时→ego-browser 直接问 ChatGPT/Perplexity 交叉 |

## 6. 验收标准（逐项勾选）

- [ ] idea53-cross-gradient.json 落盘：I(L_k;V_coarse) 各层值 + I(L_k;V_fine|V_coarse) 各层值 + 三对照臂
- [ ] 生死线判定：fine-conditional 随深度升/不升，明确结论
- [ ] 预注册合规：判据在数据出来**之前**已落盘（本文件 commit 时间 < 数据产出时间）
- [ ] venue 决策：免费渠道排序 + 概率估计（arena 第五轮回执）
- [ ] 若成立：短文大纲（claim+方法+结果+对照臂）落盘；若不成立：负结果记录（排除什么错误解释）
- [ ] IDEA-INDEX #53 行更新最终状态

## 约束

- 纯离线计算，不跑新实验（D 指令）
- 免费渠道优先（D 没钱，venue 无版面费）
- 27b 打标 prompt <200 token，分小节增量写盘（防 token 上限）
- 结果不信汇报信 git（fetch → show → 独立复算数字）
