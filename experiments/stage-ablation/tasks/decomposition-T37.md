# decomposition — T37 paper 投稿就绪（2026-11-06）

> goal: T37-paper-submission-ready · stage-gate @ 00-decomp
> 对标物：顶会论文投稿标准（ICLR/NeurIPS workshop 或 arXiv preprint 完整格式）

## 分解树

```
T37 paper 投稿就绪
├── A. 统计显著性（纯本地计算，无外部依赖）
│   ├── A1. 数据聚合：raw-data-full-perdim.json (S0-S5, 90 runs) + optimize-T35/scores.json (S7/S7V/S8E, 12 runs) + S6/S7 per-run scores [待核验: S6/S7 的 per-run 分数是否存在于某个文件，还是只有 arm-level 均值]
│   ├── A2. Bootstrap CI：每个 arm×dim (M1-M6+total)，B=1000，per-run 口径，标注 tie-break 规则
│   ├── A3. 配对检验：S7V vs S7（同 qid×rep 配对），Wilcoxon signed-rank 或 paired bootstrap；n=15 对
│   ├── A4. 效应量：Cohen's d 或 Hedges' g（小样本修正）
│   └── A5. 写入 paper-draft §4.x：所有统计量带口径限定（§4 硬规则）
│
├── B. Related Work 深化（调研 → arena 外包）
│   ├── B1. 缺口分析：当前 10 篇引用覆盖哪些子领域，缺哪些（LLM eval / prompt engineering / calibration / RAG / agent benchmarks）
│   ├── B2. 补充引用：≥10 篇新文献（目标 ≥20 总），每篇必须被正文引用
│   ├── B3. 交叉验证：新引用的 arXiv ID / 会议名 / 年份通过 arena 多源核验
│   └── B4. 正文改写：§2 各小节扩写，新增引用自然嵌入
│
├── C. Reproducibility Package（纯本地工程）
│   ├── C1. 打包清单：ablation_harness.py + score.py + gates.py + research_hook.py + gold/*.md + runs/*.json (165 files) + seeds
│   ├── C2. README.md：环境要求 (Python 3.10+, vLLM or OpenAI-compatible API) + 复现步骤 (3 条命令) + 数据目录结构
│   ├── C3. Exact prompts：Appendix C 已有缩写版，需补完整版（5 题 × 8 arms = 40 prompt variants）[待核验: 完整 prompt 是否可从 ablation_harness.py 自动生成，还是需要手动提取]
│   ├── C4. Score 可复现性声明：judge 非确定性 caveat + "评分为单次 pass，重跑会产生 ±0.05 级别漂移"
│   └── C5. Git tag：v1.0-submission-ready + archive tarball
│
└── D. 全文终审（反方视角 subagent）
    ├── D1. 数字一致性：主表 ↔ per-question 表 ↔ abstract ↔ conclusion 交叉核对
    ├── D2. 引用完整性：每篇 reference 在正文出现 ≥1 次；每个正文引用在 references 列表存在
    ├── D3. 审稿人攻击面：3 个最可能被拒的理由 + 防御方案
    └── D4. 格式检查：LaTeX 编译通过（如转 LaTeX）或 markdown lint
```

## 正交性核对

| 对 | 重叠？ | 说明 |
|----|--------|------|
| A↔B | 无 | A 是计算，B 是写作+调研 |
| A↔C | 无 | A 产出统计数字写入 paper，C 是代码打包 |
| A↔D | 弱依赖 | D1 数字一致性检查需要 A 完成后才能做（A 的数字进 paper 后 D 才验） |
| B↔C | 无 | B 改正文，C 打代码包 |
| B↔D | 弱依赖 | D2 引用检查需要 B 完成后 |
| C↔D | 无 | C 是工程，D 是内容审查 |

完备性：验收标准 (a)→A, (b)→A3, (c)→B, (d)→C, (e)→A5+D。全覆盖。

## 缺口清单

| # | 缺口 | 影响 | 处置 |
|---|------|------|------|
| G1 | ~~S6/S7 per-run scores 来源不明~~ **已解决**：`runs/hetero-judge-s6s7-results.json` (30 runs, S6+S7, M1+M4 only)；完整 6-dim 仅 S0-S5 有（raw-data-full-perdim.json）。S6/S7 的 M2/M3/M5/M6 需重跑 score.py 或标注"仅 M1/M4 可 bootstrap" | A2 覆盖范围受限 | ✅ 核验完成 |
| G2 | ~~S7T/S7F/S7V per-run scores~~ **已确认不存在**：runs/ 下只有原始 output JSON（无 scores 字段），§5.1 的 arm-level 均值来自单次 scoring pass 未落盘 | A2 无法覆盖工具臂 | 需重跑 score.py（vLLM 可用，~15min）或标注"工具臂仅报告点估计" |
| G3 | ~~完整 prompt 提取方式~~ **已解决**：`ablation_harness.py:build_prompt(arm, qid)` 硬编码全部 8 个 arm 的 prompt 模板；问题文本从 5 个 .txt 文件加载（路径在 QUESTIONS dict）→ 可直接 `python3 -c "from ablation_harness import build_prompt; ..."` 导出全部 40 variants | C3 工作量 = 写个 10 行脚本 | ✅ 核验完成 |
| G4 | 投稿目标未定：arXiv preprint vs ICLR/NeurIPS workshop vs ACL workshop？格式要求不同 | D4 格式检查标准 | 默认 arXiv preprint（最快路径），成璐可改 |
| G5 | related work 具体缺哪些方向：需要调研后才能确定 B2 的文献清单 | B2 无法启动 | 走 arena 调研（02-information-research 阶段） |
| G6 | n=3/cell 的统计功效：bootstrap CI 在 n=3 时极宽（几乎无信息量），是否需要诚实报告"CI 过宽，仅报告点估计+方向性结论"？ | A2 产出形式 | [待核验] 先算一组看 CI 宽度再决定呈现方式 |

## 执行顺序

1. **G1+G2 核验**（5min）：grep 全部 JSON 找 S6/S7/S7T/S7F/S7V per-run scores
2. **A 组**（纯本地，~30min）：数据聚合 → bootstrap → 配对检验 → 写入 paper
3. **B 组**（arena 外包，~1h wall time）：related work 调研 + 交叉验证
4. **C 组**（纯本地，~30min）：reproducibility package 打包
5. **D 组**（subagent 反方视角，~20min）：终审

并行机会：A 和 C 可并行（无依赖）；B 外包 arena 期间本地做 A+C。