# stage-ablation 索引（T17/T22-T25）

> 1-loop 阶段消融实验：prompt 各阶段（调研/分解/核验...）对最终产出质量的影响。
> 本目录 = 单一实验项目，文件按「设计→数据→评分→报告」分层。

## 层 1：设计与问题
| 文件 | 内容 |
|---|---|
| DESIGN.md | 实验总设计（臂定义 S0-S5、假设 H1-H3） |
| README.md | 快速上手（怎么跑 score.py） |
| questions/ | Q1-Q5 完整题目（GPU 选型/27B 部署/推理框架/RAG/统计范式） |
| gold/ | Q1-Q5 gold 锚点文档（定性：规格表+常见误读+正确结论，非数值目标） |

## 层 2：原始数据
| 文件 | 内容 |
|---|---|
| **raw-data-full-perdim.json** | **全量汇编（137KB）**：90 run × 6 维同源分 + arena M1 90 run + 半异源 7B 18 artifact × 6 维 + T23-v2 arm 汇总。meta 里标了每个 judge 的覆盖范围和已知缺口 |
| runs/S{0-5}-Q{1-5}-r{1-3}.json | 120 份模型产出原文（含 output_text/sources/tokens/wall_s） |
| runs/arena-judge-results.jsonl | arena 异源 judge 的 M1 逐 run 评分（90 行） |
| hetero-scores-semihetero.jsonl | Qwen2.5-7B 半异源逐维度评分（108 行 = 18 artifact × 6 维） |
| runs/hetero-judge-v2-results.json | T23-v2 arena 异源 arm-level 汇总（per-dim 69KB 明细仍在 arena workspace，push 403 未落盘） |
| runs/local-rerun-aligned.jsonl | 本地对齐重跑的 M1 |

## 层 3：评分引擎与轮次
| 文件 | 内容 |
|---|---|
| score.py | 6 维评分器（M1-M6，权重见内） |
| gates.py | 保守后检查（数字锚点/冲突/限制声明；@582ba7e 修 claim-level anchor） |
| test_gates.py | gates 单测 |
| scoring.md → scoring-v2.md → scoring-v3-gatefixed.md | 三轮评分结果迭代（v3 = gate 修复后全量 90-run） |
| cross_judge.py / cross-judge-results.json | 跨 judge 对比脚本与结果 |

## 层 4：诊断与报告
| 文件 | 内容 |
|---|---|
| **T17-stage-ablation-final-report.md** | 最终报告（设计/逐臂表/H1 判定/跨 judge 对比/局限） |
| T23-gold-gap-diagnosis.md | gold 差距诊断（为什么最高臂只有 0.58） |
| T23-hetero-judge-prompt-v2.md / T23-hetero-judge-blocker.md | 异源 judge 任务书与阻塞记录 |
| T23-semihetero-analysis.md | 半异源 7B 分析 |
| T22-r2-result.md | T22 第二轮结果 |
| T25-research-hook-v2-validation.md | 调研 hook v2.2 五题验证 |
| lit-survey/ | T24 文献调研回执（65 篇，论文 related work 底稿） |
| competitor-survey.md | 竞品/bench 对标 |
| paper-draft.md | 论文草稿 |

## 当前瓶颈（2026-11-05 数据说话）
1. **M1 事实准确率（均分 0.60，拖累最大 0.100）**：27B 知识天花板——硬件细节（HBM 带宽/PCIe 代数）记错，gold 核心矛盾点（PCIe vs SXM 带宽比 1.68x）系统性漏掉。prompt 工程解决不了，换更强模型或强制查 datasheet 才有出路。
2. **M2/M5 是度量口径问题不是能力问题**：M5≈0 因为 65/90 产物正文行内无有效 URL（来源在独立 sources 字段且多为 bing 跳转链接）；M2≈0.1 因为 fact/inference 标签覆盖率≈0（模型不写标签）。gates.py 的行级锚点检测对这种输出形态天然失明，需要改成"sources 字段关联"口径再评。
3. **judge 依赖性（论文核心证据）**：同源 27B 判 H1 CONFIRMED (+0.129)，arena 异源判 REFUTED (-0.187, Q1)。同一份产物两个 judge 结论相反。
4. **数据缺口**：T23-v2 的 69KB per-dim 明细卡在 arena workspace（GitHub App token 只读），只有 arm-level 汇总落盘。
