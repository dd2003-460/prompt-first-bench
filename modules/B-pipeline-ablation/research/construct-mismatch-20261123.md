# Construct Mismatch：模型树与 gold 树不在同一题面（2026-11-23）

> 来源：① 类事实（本轮从实际文件读，非记忆）。这是 judge construct validity 洞的
> **根因**，比权重/阈值/磁体伪影都上游。影响 workshop 对 cov 的全部解读。

## 三方对照（题面 vs gold vs 模型）

| 维度 | 题面 QUESTIONS['gpu'] | gold 树 (frozen ed552c4) | 模型树 idea2 A-r1 (316节点) |
|---|---|---|---|
| 上下文长度 | "≥ 32K tokens 作为**容量下限**保留" | **@64K 定值**（gold-tree.md:123 "token 画像…@64K"；KV 24.7GB/流@64K） | **32K 全程**（N9/N11/N12/N13 全用 32768） |
| 候选硬件集 | "**自行搜索**确定值得考虑的完整候选集" | **固定** 3090/M2Ultra/L40S/A100/V100/TPU（gold-tree.md:94 "原候选 4 类…新增 3 类"） | **自搜** 4090/A100/H100/MI300X/M3Ultra/6000Ada/L40S |
| 目标函数 | "性价比最优的完整选卡方案"（宽） | **c_pass [¢/task]** 成本分解树（N-0） | **吞吐/TCO 工作点**分析（N33/N36/N37） |
| V100 处理 | — | 候选之一（V100×8 SXM2 行） | **N131 显式排除**："排除带宽 < 600 GB/s 的老旧数据中心卡（如 V100）" |
| winner | — | 3090×4 / W4 / n=2 | 条件性推荐 4090/A100/H100（无 3090） |

**candidate 重叠只有 A100。** 模型树里 3090 零出现，V100 被主动排除。

## 为什么这是 construct 洞的根因

judge 的 cov 层测的是"模型树节点覆盖 gold 树单元的比例"。这个度量**隐含假设**
模型和 gold 在解同一道题。但：

1. **上下文长度不同**（32K vs 64K）→ KV 显存、带宽门槛、可行性判断全部错位。
   gold 的 bw_ok 门槛 774/1034/1574 GB/s 是 @64K 算的；模型 @32K 的 KV 只有
   gold 的一半，它的显存/带宽结论在 gold 坐标系里是错的。
2. **候选集不同**（自搜 4090 系 vs 固定 3090 系）→ 模型树里根本没有 3090 节点，
   gold 的 winner 分支（N-5 选卡）对模型树是**不可达**的——不是搜索不够深，
   是模型压根没把 3090 纳入候选。
3. **目标函数不同**（c_pass vs 吞吐/TCO）→ 同一硬件，两条分解路径，节点 claim
   文本不同 → embedding 匹配不上。

**结论：cov 偏低（0.22-0.39）有一部分不是"模型搜索不够深"，而是模型合法地解了
另一道题。** 题面的两处歧义（"≥32K 下限"被取下限、"自行搜索"搜出不同候选集）
让模型和 gold 分叉。judge 把这个分叉记成了"覆盖不足"。

## 对 workshop 的影响

- **finding 3（budget–quality 峰在 150）不受直接影响**：depth 层测的是"模型树
  达到 gold 树的深度"，与题面分叉正交（深度是结构量）。但 cov 层的解读被污染。
- **finding 4 / 所有 cov 相关结论**：cov 低 ≠ 模型能力弱，部分是题面歧义。
  "719 买 breadth 不买 depth" 的 breadth 部分可能包含"模型在解不同题面"。
- **construct validity 的修复方向**：不是改 judge，是**消解题面歧义**——
  ① 上下文长度定死（题面写 64K 定值，不是 ≥32K 下限）；
  ② 候选集定死（题面给固定候选集，不让模型自搜）；
  ③ 目标函数定死（题面明确 c_pass 口径）。
  三者都定死后，模型和 gold 才在同一题面，cov 才能干净地测"搜索深度"。

## 置信度

- 三方对照表（idea2 A-r1）：① 类（本轮从 QUESTIONS['gpu'] / gold-tree.md /
  idea2-A-r1.json 实际读），conf 0.95。
- **K7 抽查修正（2026-11-23 同日，① 类，5 棵 K7 树 n_nodes 匹配）**：mismatch
  **不均匀**，分两个维度：
  - **上下文长度：全数据集一致 mismatch**。K7 五棵树 32K 提及 16-192 次、
    64K 提及 0-11 次（b719_r1 偶有 64K）。模型普遍取 32K 下限，gold 锚 64K。
    这个错位在 K7 主表数据里**同样存在**，影响 cov 解读。
  - **候选集：K7 与 idea2 A-r1 不同**。K7 树 3090 出现 7-40 次（winner 分支
    可达），V100 出现 0-2 次；而 idea2 A-r1 3090 零出现、V100 被主动排除。
    → K7 更接近 gold（winner 在候选集内），idea2 A-r1 偏离更大。
  - **净结论**：上下文长度 mismatch 是全局的（K7 + idea2 都有），候选集
    mismatch 是 run 间变化的（K7 部分重叠，idea2 A-r1 几乎不重叠）。
    之前"K7 大概率同样分叉"的 ③ 类推断只对了一半——上下文维度对，候选集
    维度 K7 比 idea2 好。
- "cov 低部分是题面分叉"：① 事实强支撑（32K vs 64K 全局错位 + K7 winner
  可达但 idea2 不可达），conf 0.8。
- **待验证**：32K vs 64K 错位对 cov 的定量贡献——需重跑一棵树强制 64K 题面，
  对比 cov 变化。这是消歧义实验，排 vLLM 队列后做。

## 文件

- 题面: `experiments/stage-ablation/s5_pipeline.py` QUESTIONS['gpu']
- gold: `bench/rubric-v3/ablation/gold-tree.md` (frozen ed552c4)
- 模型树: `modules/B-pipeline-ablation/data/idea2/idea2-A-r1-20261122-230045.json`
- 本记录: `modules/B-pipeline-ablation/research/construct-mismatch-20261123.md`
