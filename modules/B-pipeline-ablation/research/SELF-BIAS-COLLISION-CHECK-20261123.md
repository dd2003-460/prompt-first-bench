# origin: ai — D 2026-11-23 idea "self-judge 偏好测量 → 跨领域偏好标尺 → 可解释性" 撞车核验

## 核验方式

arXiv 搜索页 (web_extract, 2026-11-23): 4 组查询, 命中 9+ 篇直接相关。

## 撞车清单 (按相关度)

| arXiv | 标题 | 做到哪一步 | 与我们重叠 |
|---|---|---|---|
| 2604.22891 | Quantifying and Mitigating Self-Preference Bias of LLM Judges (Yang et al.) | 全自动 SPB 量化, 20 LLM, 等质量对统计解耦判别力/偏袒, 免人工 gold, cognitive-load 分解 mitigation (降 31.5%) | **D idea 的"测量"部分已被做**, 方法不同 (他们用等质量对, 我们用 gold 树差值) |
| 2604.06996 | Self-Preference Bias in Rubric-Based Evaluation (Pombal et al.) | 自称 "rubric-based SPB 首个研究"; IFEval/LiveCodeBench 客观 rubric 上 SPB 仍存在 (自己输出被误判 satisfied 概率 +50%); 分析哪些 rubric 易中招 (负向/主观) | **恰好是我们的场景** (逐条 rubric 二元判定), 但他们是通用 benchmark, 我们是 gold-conditioned 研究树 |
| 2608.18091 | Self- and Other-Labels Induce Bidirectional Bias (EMNLP Findings 2026) | 标签诱导的双向 bias | 机制层面 |
| 2611.18616 | The Judge Is Not Impartial: Self-Preference in Medical LLM Evaluation | 医疗域 SPB | 域特定 (同我们的 per-domain 思路) |
| 2510.03399 | Know Thyself? AI Self-Recognition (Bai et al.) | self-recognition 系统性失败 + hierarchical bias (GPT/Claude 家族偏袒) | metacognition 连接最近的一篇 |
| 2504.03846 | Do LLM Evaluators Prefer Themselves for a Reason? | 偏袒的归因 | 归因层面 |
| 2609.30048 | Style, Not Self (Barkhordar) | 代码归因靠表面风格非真识别 | 替代解释 |
| Panickssery 2024 | LLM Evaluators Recognize and Favor Their Own Generations | 奠基 | — |

## Novelty 评估 (conf 0.7)

1. **"测量 self-judge 偏好" = 不 novel**: 2026 年至少 4 篇专做 SPB 量化, 含 rubric-based 场景 (2604.06996) 和免人工 gold 的自动化框架 (2604.22891)。
2. **跨领域偏好标尺 = 部分 novel**: 现有工作多在通用 benchmark (IFEval/LiveCodeBench/HealthBench) 上测; per-domain 研究树 (gold-conditioned, 机械基准) 上的 bias profile 没见到。2611.18616 做了医疗域, 说明 per-domain 方向有人走但没成体系。
3. **可解释性连接 = 最可能站住**: "bias 模式 = 模型自我认识的负镜像 (最偏袒处 = 最不知道自己不知道处)" — 2510.03399 碰了 self-recognition↔metacognition, 但没人把**评估偏袒**接到**信息状态监控**。这是 D 说的"应用到可解释性研究"部分, 唯一没被发过的角度。

## 对 workshop 的实际收益 (优先于新 idea)

§3 related work 无 LLM-judge self-bias 引用, §6 self-bias caveat 是裸的。补 4 篇引用后:
- §6 从"我们发现 bias" → "bias 是已确立现象 (Panickssery 2024; 2604.22891; 2604.06996; 2510.03399), 机械轴通过构造规避, depth 轴是其一个实例"
- 定位更稳, 审稿人不会问"你们知道 self-bias 吗"

## 决策建议

- workshop: 补引用 (现在做), 不动定位
- D 的 idea: 降级为 future work / 独立小项目, 不并入 workshop (测量部分撞车太重, 可解释性部分需要 nat/soc 的 LLM judge 补跑 ~60 棵才能起步, 且撞车面需 arena 多轮对抗核验)

## 补充 (2026-11-23 12:15): 可解释性端撞车核验 — 修正 novelty 评估

### 查询 (3 组)

1. "self-preference bias interpretability LLM" → 4 篇, 2 篇相关
2. "LLM self-knowledge evaluation bias metacognition" → 2 篇, 1 篇相关
3. "judge bias probe model self-awareness" → 0 篇

### 可解释性端撞车

| arXiv | 标题 | 做到哪一步 | 与我们窗口 |
|---|---|---|---|
| 2510.21723 | Recognizing internal states in AI: patterned preferences in LLMs (Hedberg) | paired-choice 范式, 12 LLM, 30 类内部状态描述识别 — **"偏好模式作为内部状态窗口"方向已占** | 操作化不同: 他们识别内部状态描述, 我们测评估偏袒↔信息缺口相关性 |
| 2510.03399 | Know Thyself? AI Self-Recognition | self-recognition 失败 + hierarchical bias, 定位 metacognition | 我们接的是"评估偏袒"不是"文本识别" |
| 2604.07506 | ReflectRM (GRM self-reflection) | reward model 自反思, 无关 | — |

### 修正结论 (conf 0.7 → 0.4)

- 两端都有邻接工作, 剩余窗口比初判窄
- 未被占的具体组合: **gold-conditioned 研究树上的评估偏袒差值 (LLM judge − 机械 judge) 作为信息状态探针**
  - 测量端: gold 树差值法 ≠ 2604.22891 等质量对法
  - 可解释性端: "偏袒模式 ↔ 信息缺口模式相关性" ≠ 2510.21723 paired-choice 内部状态识别
- 验证成本: nat/soc LLM judge 补跑 ~60 棵 (~2h vLLM) + 相关性分析 + arena 对抗核验
- **建议: 不立 goal, 记为 future-work 候选** — 窗口太窄, 撞车面未做对抗核验, 且 workshop 主线 (1-22 截止) 优先
