# T50: B1 新题 Gold Tree 构建（Q8/Q9/Q10）

【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00-common-review.md + 01..04.5（仓库内）。
2. 每阶段产出落盘 loop-artifacts/stages/<N>/，阶段判定 pass 才进下一阶段。
3. 完成后 commit + push（含全部 loop-artifacts/）。
4. 通道故障（403/沙箱）→ 报告 Lead，由 Lead 降级本地执行，不得静默跳过 loop。

## 背景（arena 不知道的部分）

pfb（prompt-first-bench）是测量 prompt engineering 各臂对 LLM 事实调研质量影响的 benchmark。当前状态：

- 主实验（S0/S1/S5 × Q1-Q5 × 6 reps = 150 runs）已完成，n=30/arm 统计显著（S5-S0 Δ+0.235, p=5.8e-08）
- S10 tone 实验（A-E × Q1/Q3/Q4 × 6 reps = 90 runs）已完成，核心 finding：reviewer 语气比信息量更重要（机械清单 0.426 vs 人话/讲原因/安抚 0.70-0.75）
- D-face 跨域盲测（Q6 CDN / Q7 存储）确认 27b 模型能力上限（覆盖率 ~0.44），范围已限定为 AI/ML 域
- **B 面（真实泛化）需要在 AI/ML 域内加新题验证**——不同子领域之间 pfb 是否仍然有效

现有 5 题覆盖的子领域：GPU 硬件规格、模型选型、推理基础设施、数据处理架构、科研方法论。需要加 3 道新题，覆盖不同子领域且与现有 5 题正交。

## 具体任务

为以下 3 道题各构建一份 gold tree：

### Q8: LLM 评估方法 — 代码生成 Benchmark 设计
题面方向："设计一个 LLM benchmark 评估代码生成能力，需要考虑哪些维度？如何防止数据泄漏和过拟合？"
- Gold 可参考：HumanEval/MBPP/Codeforces/LiveCodeBench 设计文献、contamination detection 方法
- 关键叶子值示例：pass@k 公式、HumanEval 164 题、MBPP 974 题、LiveCodeBench 时间窗口防泄漏机制

### Q9: 多模态架构 — VLM 对比
题面方向："Vision-Language Model (CLIP/SAM/GPT-4V/Gemini) 的架构差异、训练策略和适用场景对比"
- Gold 可参考：CLIP 400M pairs contrastive learning、SAM mask generation、GPT-4V dynamic tiling
- 关键叶子值示例：CLIP ViT-L/14 768-dim embedding、SAM 11M images、GPT-4V 动态分辨率 tile 数

### Q10: RLHF/对齐 — Pipeline 与对齐税
题面方向："RLHF pipeline 的关键步骤、超参选择和对齐税(alignment tax)的量化"
- Gold 可参考：InstructGPT PPO pipeline、DPO 简化方案、alignment tax 测量方法
- 关键叶子值示例：PPO KL coefficient β=0.2、DPO β=0.1、alignment tax MMLU -5~15pp

### 每道题的交付物

1. **题面文件**：`bench/questions/Q{N}-<topic>.txt`
   - 格式参照 `bench/questions/Q6-network-arch.txt`（问题描述 + 约束条件 + 要求）
   
2. **Gold tree**：`bench/rubric-v3/ablation/gold-Q{N}.md`
   - 格式严格对标 `bench/rubric-v3/ablation/gold-Q6.md`（节点编号 N-X.Y、深度 ≤4、叶子带具体数值 + 来源标注）
   - 标准：≥30 节点、≥10 叶子、主干深度 ≤4
   - 每个叶子值必须有来源 URL + 访问日期
   - 独立调研：不得引用 Q1-Q5 的 gold 内容
   
3. **QUESTIONS 注册**：`experiments/stage-ablation/ablation_harness.py` → QUESTIONS dict 新增 Q8/Q9/Q10 条目
   - 格式参照已有 Q6/Q7 条目

4. **搜索 query**：`experiments/stage-ablation/research_hook.py` → ARXIV_QUERIES dict 新增每题一条 arXiv 检索 query

## 验收标准（机器可查）

- [ ] `bench/questions/Q8-*.txt`、`Q9-*.txt`、`Q10-*.txt` 存在且非空
- [ ] `bench/rubric-v3/ablation/gold-Q8.md`、`gold-Q9.md`、`gold-Q10.md` 存在
- [ ] 每份 gold tree ≥30 节点、≥10 叶子（grep 计数验证）
- [ ] `ablation_harness.py` QUESTIONS dict 含 "Q8"/"Q9"/"Q10" key
- [ ] `research_hook.py` ARXIV_QUERIES dict 含 "Q8"/"Q9"/"Q10" key
- [ ] 独立调研声明（每份 gold 顶部注明"未引用 Q1-Q5 gold"）
- [ ] git log 有新 commit 且 message 含 "T50"
- [ ] 所有文件在 arena 分支上可 fetch

## 约束

- 不要修改 Q1-Q5 的任何文件（它们是其他实验的数据）
- 不要修改 score.py / score_s10.py / gates.py（评分逻辑不在本任务范围）
- 新文件放上述指定路径，不要创建新目录
- 格式参照 gold-Q6.md（前 60 行有完整结构示例）
- 如果某道题的调研发现某个"关键数值"找不到可靠来源，标 `[待核验]` 而不是编一个

## 降级方案

- 如果 web 搜索不可用 → 用 arXiv API（http://export.arxiv.org/api/query?search_query=...）+ 已知论文内容，标注 conf 降为 0.2
- 如果超时 → 落盘已完成部分，commit message 标 "T50-partial"，说明哪道题完成了哪道题没完成