# 任务：rubric-v3 O3 权重消融实验（arena 执行）

## 背景
gap analysis（`receipts/rubric-v3-gap-analysis.md`，在 research/deepresearch-bench-survey 分支，git show 可取）判定：surprisal 加权公式 w_v = 1 + min(−log₂ p̃_v, log₂(1/ε)) 是通用 research bench 的真空白，但称"有效方法"前必须补两个证据：
1. **消融**：无权重 vs importance-only vs surprisal 三种打分下，同一批产出的分数排序是否不同、哪种更符合人工判断
2. **构念效度**：高权重节点确实更重要而不只是更罕见

本任务做第 1 条（第 2 条需要新域盲测，另开任务）。

## 输入材料（都在本目录 bench/rubric-v3/ablation/）
- `gold-tree.md` — decomp 硬件域 gold 树，31 节点带 ID（N-0, N-1, N-1.1, ...），含 SHARE 份额标注
- `prompt-V0.txt` — baseline 题面（C9-plain 档，无引导）
- `runs-C0-run1.md` ~ `runs-C0-run8.md` — 8 个已有模型产出（同一 prompt 的 8 次独立 run，真实数据不是编的）

## 你要做的三步

### Step 1: 逐节点命中判定（h_v ∈ {0,1}）
对每个 run × 每个 gold 节点，判 h_v：产出中该节点被实质性覆盖（有对应内容且方向正确）=1，否则 0。
- 判据从严：提到名词但没有实质内容（没给数值/区间/机制）= 0
- 黑盒标注算覆盖：显式标"不知道+区间+怎么测"的叶子 = 1
- 输出 `hit-matrix.json`：{run_id: {node_id: {h: 0|1, evidence: "产出中的原文片段≤40字"}}}
- 每个 h=1 必须附 evidence，evidence 必须是 run 文件里真实存在的句子（不许改写）

### Step 2: 三套权重
- **W0 flat**：所有节点 w=1
- **W1 importance**：用 gold-tree.md 里的 SHARE 份额映射——w = 1 + 4×SHARE_parent_of_node（父节点 SHARE≥0.25 → w≈2；SHARE 0.1-0.25 → w≈1.5；<0.1 → w≈1.2）。这是 ResearcherBench 式的"专家觉得重要"权重
- **W2 surprisal**：按 rubric-v3 协议模拟 p̃——你（作为 judge LLM）对每个节点回答："一个没见过 gold 的 LLM，在这个父节点上下文下盲生成分解时，提出这个子拆分的概率大概是多少？"给 p̃ 估计（0-1），然后 w = 1 + min(−log₂ p̃, log₂(1/0.01)) ≈ 封顶 8。p̃ 估计要写理由（为什么模型容易/不容易想到这一刀），存 `prior-estimates.json`

O3_score(run, W) = Σ w_v·h_v / Σ w_v（只对 h 有定义的节点求和，即全部 31 节点）

### Step 3: 对比分析
输出 `ablation-result.md`：
1. 8 个 run 在三套权重下的 O3 分数表 + 排名
2. **排名差异**：W0 vs W1 vs W2 的排名相关（Spearman ρ）；哪两套之间分歧最大
3. **关键案例**：找出至少 2 个"平权下打平/接近、加权后拉开差距"的 run 对，说明拉开它的是哪些节点（这些就是权重起作用的节点）
4. **构念效度初检**：W2 里权重最高的 5 个节点列出来，逐个判断"重要"还是"只是罕见"（对照 gold-tree 的瓶颈标记 ■瓶颈 和 ★订正 符号）。如果 top-5 权重节点里 ≥3 个同时是瓶颈/订正节点 → 构念效度初步支持；否则报告矛盾
5. **judge 稳定性自检**：随机抽 10 个 (run, node) 判定，重新独立判一遍（不看第一次答案），报一致率；<80% 要在结论里降级声明

## 约束
- 所有数字必须可复算：hit-matrix.json + prior-estimates.json 是原始数据，分数表从它们算出
- 不许改 gold tree，不许改 run 文件
- 中文输出，完成后 git add/commit/push 到当前分支
