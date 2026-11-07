# Q8 Gold Tree — LLM 代码生成 Benchmark 设计：判别力 × 抗泄漏可信度联合判据

> 题面：`bench/questions/Q8-eval-benchmark.txt`｜域：AI/ML — LLM evaluation（B 面域内新题）
> **独立调研声明：本树全部数值来自 T50 任务期间的独立调研（arXiv 一手 abstract + 公开数据集卡/技术页，观察日 2026-11-07），未引用 `gold-tree.md`（Q1）及任何 Q1-Q5 gold 内容。**
> 节点计数：**36 节点 / 主干深度 4 / 叶子 28 个**（含 4 个黑盒叶子）。

## 结论先行

- **判别力与抗泄漏是一对耦合约束，不是两张清单**：滚动新题（LiveCodeBench 式时间窗）抗泄漏最强，但新题缺少难度标定历史；固定题库（HumanEval/MBPP）判别力标定成熟，但泄漏已被实证——预训练语料（RedPajama-1T/StarCoder-Data）中检出 **8–18% 的 HumanEval 重叠**。
- **比泄漏更隐蔽的威胁是测试不充分**：EvalPlus 把 HumanEval 测试扩 **80×** 后，26 个 LLM 的 pass@k 普降 **19.3–28.9%**，且发生**误排序**（WizardCoder-CodeLlama / Phind-CodeLlama 在 HumanEval+ 上反超 ChatGPT，旧榜不能）。泄漏抬高绝对分，测试不足扭曲相对序——后者对选型的破坏更大。
- **最容易被漏掉的判断（★）**：字符串级去污染（n-gram 匹配）**实际无效**——paraphrase/翻译即可绕过，绕过后可让 13B 模型刷出 GPT-4 级分数。可信的防泄漏必须是「行为检测（DCQ 类黑盒 quiz）+ LLM 语义级去污染 + 时间窗滚动」三件套，缺一件都有已知绕过路径。

---

## 全树

```
N-0  Benchmark 联合判据  J = 判别力 × 抗泄漏可信度          SHARE 1.00   split
│    判别力 = 强弱模型分数差（可复算：pass@k 协议 + 测试充分性）
│    抗泄漏 = 1 − 污染检出率（行为法 + 语义法 + 时间窗机制）
│
├─ N-1  任务空间设计（考什么）                                .30   split
│  ├─ N-1.1  docstring→单函数档：HumanEval 164 题，平均 7.7 tests/题   leaf S-a
│  ├─ N-1.2  入门级短程序档：MBPP full 974 题（test 500 / sanitized 427）leaf S-a
│  ├─ N-1.3  竞赛档：LeetCode/AtCoder/Codeforces 滚动收题，LCB v2 = 400 题
│  │         （2023-05 ~ 2024-05 发布窗口）                            leaf S-a
│  ├─ N-1.4  真实工程档：SWE-bench 2,294 个 GitHub issue×PR，跨 12 个
│  │         Python 仓库（最佳模型 Claude 2 仅解 1.96%）               leaf S-a
│  ├─ N-1.5  库调用组合档：BigCodeBench 1,140 任务 / 139 库 / 7 域      leaf S-a
│  └─ N-1.6  能力场景覆盖：生成 / self-repair / code execution /
│            test output prediction（LiveCodeBench 四场景口径）        leaf S-a
│
├─ N-2  指标与测试充分性（怎么算分）                           .30   split  ★F-A
│  ├─ N-2.1  pass@k 无偏估计量：pass@k = 1 − C(n−c,k)/C(n,k)
│  │         （naive 1−(1−c/n)^k 有偏；pass@1 = c/n 恒等式自检）        leaf S-a
│  ├─ N-2.2  采样协议 n/k：Codex 论文 n=100/题（pass@1 28.8% →
│  │         pass@100 70.2%，repeated sampling 是一手实证）            leaf S-a
│  ├─ N-2.3  测试充分性                                                  split
│  │  ├─ N-2.3.1  基线不足证据：HumanEval 平均仅 7.7 tests/题 →
│  │  │           EvalPlus 扩充 80×（LLM+变异双策略自动生测试）        leaf S-a
│  │  └─ N-2.3.2  后果量化：pass@k 虚高 19.3–28.9% + 误排序实例        leaf S-a
│  ├─ N-2.4  误排序风险 = 榜单判别力失效（测试不足时强弱序翻转）        leaf S-c
│  ├─ N-2.5  覆盖率判据：BigCodeBench 平均 5.6 tests/任务、
│  │         99% 分支覆盖（测试充分性的可操作标杆）                     leaf S-a
│  └─ N-2.6  人类天花板参照：BigCodeBench 人类 97% vs 最佳 LLM ~60%
│            （难度余量判据：天花板贴顶的题无判别力）                    leaf S-a
│
├─ N-3  数据泄漏防护（防"见过题"）                             .25   split  ★F-B
│  ├─ N-3.1  泄漏途径实证：RedPajama-1T / StarCoder-Data 中检出
│  │         8–18% 的 HumanEval 重叠（含 GPT-3.5/4 合成数据的
│  │         无意污染）                                                  leaf S-a
│  ├─ N-3.2  检测——字符串级                                              split
│  │  ├─ N-3.2.1  n-gram/字符串匹配去污染：主流做法                     leaf S-b
│  │  └─ N-3.2.2  失效证据：paraphrase/翻译绕过 → 13B 过拟合可达
│  │              GPT-4 级分数（MMLU/GSM8K/HumanEval 上验证）           leaf S-a
│  ├─ N-3.3  检测——语义级：LLM-based decontamination
│  │         （llm-decontaminator，开源）                               leaf S-a
│  ├─ N-3.4  检测——行为级黑盒：DCQ 数据污染测验（词级扰动 3 变体
│  │         +原文构成多选题，被污染模型倾向选中原文；无需训练数据
│  │         /参数访问；TACL）                                           leaf S-a
│  ├─ N-3.5  检测——canary string 埋点法  [待核验]（本次未核验一手
│  │         细节，只登记方法名）                                        leaf S-b
│  ├─ N-3.6  结构性防御：滚动时间窗——只收「发布日期 > 模型训练
│  │         截止」的竞赛新题（LiveCodeBench 机制）                     leaf S-a
│  └─ N-3.7  时效半衰期：模型训练截止日期通常不披露 → 时间窗的
│            安全边距不可精确计算                                        leaf B1  黑盒
│
├─ N-4  过拟合/榜单 hacking 防护（防"背题"）                   .10   split
│  ├─ N-4.1  隐藏测试集私有 hold-out（提交制评测，不公开 tests）        leaf S-c
│  ├─ N-4.2  测试增强：EvalPlus 式自动扩测（生成侧 LLM + 变异侧
│  │         双策略），把"背对少量测试"变成不可行                        leaf S-a
│  ├─ N-4.3  fresh one-time exams：一次性新题倡议（rephrased-samples
│  │         论文结论：社区应持续出新题而非复用旧榜）                    leaf S-a
│  └─ N-4.4  多样性防模式记忆：139 库 × 7 域的组合空间（BigCodeBench
│            设计动机：任务组合多样性 > 单题难度）                      leaf S-c
│
└─ N-5  运营与可信度（nuisance，不改结构但改结论可信性）        .05   split
   ├─ N-5.1  透明度：公开全部 prompts + model completions
   │         （LiveCodeBench 承诺，供第三方复查污染/过拟合）            leaf S-a
   ├─ N-5.2  版本化滚动发布：release tag 化题目窗口（评测结果必须
   │         绑定题目版本，否则跨期不可比）                              leaf S-c
   └─ N-5.3  评测预算：LCB 实测规模 18 base + 34 instruct 模型 ×
            多场景采样（预算 = 题数 × n 采样 × 模型数 × 单补全成本）    leaf B2  黑盒
```

**图例**　`.30` SHARE（对根判据 J 的相对权重，本树按"失败模式危害 × 实证强度"归一，非账单占比）｜`leaf S-a` 停止：一手论文 abstract/数据集卡可查｜`leaf S-b` 停止：二手转述或区间估计｜`leaf S-c` 停止：可由定义/公式推导｜`leaf B#` 停止：黑盒，见下表｜`★F-A/B` 本次分解中「不看就会设计错」的两处

---

## 两处 ★ 判断（本树与「凭直觉列清单」的分水岭）

**★F-A：测试充分性是判别力的前置条件，先于一切难度设计。**
pass@k 的输入是"通过全部测试"，测试不足 → c 被高估 → 所有下游结论（排名、scaling 曲线、pass@k 收益）系统性失真。EvalPlus 一手证据：80× 扩测后 pass@k 普降 19.3–28.9% 且**强弱序翻转**。设计顺序必须是「先定测试生成与覆盖率判据（对标 BigCodeBench 5.6 tests/任务、99% 分支覆盖），再谈题目难度分布」——直觉清单几乎都把难度放第一位。

**★F-B：字符串去污染 = 假防御；可信防泄漏是三层结构。**
第 1 层（n-gram）已被实证可被 paraphrase/翻译绕过，且绕过后过拟合收益巨大（13B→GPT-4 级分数）；第 2 层（LLM 语义去污染）能查出 8–18% 的存量重叠但依赖去污工具质量；第 3 层（行为检测 DCQ + 时间窗滚动新题）不依赖训练数据访问、从机制上让"见过"不可能。**三层各自都有已知失败模式，只有叠加才闭合**——报告若只写"我们做了 n-gram 去重"，按本树应判抗泄漏项为 0。

---

## 黑盒表

| 编号 | 参数 | 区间 | 为什么是黑盒 | 怎么实测 |
|---|---|---|---|---|
| B1 | 目标模型训练截止日期 | 未披露为主 | 厂商普遍不公布精确 cutoff，时间窗安全边距无法计算 | DCQ 行为测验逐模型探测（不需厂商配合） |
| B2 | 单补全评测成本 | 依模型/采样数 | = 题数 × n × 单价，私有 API 价格随时间变 | 按当期 API 价目 × 协议实算 |
| B3 | n-gram 去污染的重叠阈值（取多少 n、多长匹配算污染） | 无公认标准 | 各论文实现不一，无行业常数 | 用已知污染样本标定阈值后报 ROC |
| B4 | 新题难度标定周期 | 未知 | 滚动新题没有历史通过率，判别力标定需时间积累 | 首批模型跑完后回填难度分层 |

---

## OC-1 卡片（三个样例，字段定义见 `../rubric/output-contract.md`）

```
### N-0  Benchmark 联合判据
PARENT:  -
NOW:     未知
GOAL:    J 的两个分量各有一个可复算数：判别力 = 强弱模型 pass@k 差；
         抗泄漏 = 1 − 三层检测的污染检出率
GAP:     缺「目标模型清单」「评测预算」「题目版本窗口」
IN:      题面 + 本树 N-1..N-5 + 黑盒表 B1-B4
OUT:     J
KIND:    signal
RES:     -
SHARE:   1.00
BOUND:   -
TEST:    跑本文件 §「算例」：pass@k 协议自检 + KL 无关（本题无 RL 项）
STATUS:  split
```

```
### N-2.1  pass@k 无偏估计量
PARENT:  N-2
NOW:     pass@k = 1 − C(n−c,k)/C(n,k)（Chen et al. 2021 定义）
GOAL:    评分代码实现 + 恒等式自检通过
GAP:     无（公式一手可查）
IN:      n（采样数）、c（通过数）、k
OUT:     pass@k
KIND:    signal
RES:     公式
SHARE:   —
BOUND:   朴素式 1−(1−c/n)^k 有偏（把不放回抽样当放回），n 小时偏差大
TEST:    pass@1 必须 = c/n（telescoping 恒等式）；c=0 → 0；c>n−k → 1
STATUS:  leaf:S-a
```

```
### N-3.6  滚动时间窗
PARENT:  N-3
NOW:     LiveCodeBench 机制：持续收 LeetCode/AtCoder/Codeforces 新题，
         v2 收录 2023-05~2024-05 发布的 400 题
GOAL:    对本 benchmark 定义「题目发布时间 > 模型 cutoff + 安全边距」的收题规则
GAP:     模型 cutoff 不披露（B1）→ 边距只能按最坏假设
IN:      竞赛平台题源 + 发布时间戳
OUT:     抗泄漏机制描述 + 边界条件
KIND:    signal
RES:     —
SHARE:   —
BOUND:   对 cutoff 晚于收题窗口的模型失效（需用 DCQ 补测）
TEST:    对任一被测模型跑 DCQ；quiz 命中率 ≈ 随机基线则时间窗有效
STATUS:  leaf:S-a
```

---

## 算例（可复算，用于后续判分）

**① pass@k 协议自检**（Codex 论文锚点：pass@1 28.8% → pass@100 70.2%，n=100/题）：
取 n=100、c=29（≈ pass@1 = c/n = 0.29，与 Codex 28.8% 同量级）：
- pass@1 = 29/100 = **0.29**（恒等式自检通过）
- pass@10 = 1 − C(71,10)/C(100,10) = 1 − ∏ᵢ₌₀..₉ (71−i)/(100−i) ≈ 1 − 0.0267 ≈ **0.973**（近似值，逐项比连乘）
- 对照朴素有偏式：1 − (1−0.29)^10 ≈ 0.968 —— 与无偏式差 ~0.5pp，n 越小差越大，故必须用无偏式。

**② 测试充分性代价换算**（EvalPlus 锚点）：
某模型 HumanEval pass@1 = 0.72 → 扩测 80× 后按实测降幅区间 19.3–28.9%（相对）折算：
- 下界：0.72 × (1−0.193) = **0.581**
- 上界：0.72 × (1−0.289) = **0.512**
→ 榜单若用未扩测题集，绝对分虚高 **0.14–0.21**，且此量级足以翻转相邻名次（EvalPlus 误排序实例的数值基础）。

**③ 泄漏检出率的三层合并**（本树定义，可复算）：
设三层检测对同一题库的独立检出率 n-gram = 0.30（已被证低估，仅示意）、LLM 语义 = 0.60、DCQ 行为 = 0.50，则合并漏检率 = 0.70 × 0.40 × 0.50 = 0.14 → 抗泄漏分量 = **0.86**；只用 n-gram 单层 = **0.30**。—— 权重数字为示意，结构（乘法合并、单层不合格）是判分点。

---

## 来源表

| # | 事实 | URL | 观察日 | conf |
|---|---|---|---|---|
| S1 | Codex/HumanEval：pass@1 28.8%、GPT-3 0%、GPT-J 11.4%；100 采样/题解 70.2% | http://arxiv.org/abs/2107.03374 | 2026-11-07 | 0.95 |
| S2 | HumanEval = 164 题、平均 7.7 tests/题、pass@k 定义 | https://www.emergentmind.com/topics/humaneval-benchmark | 2026-11-07 | 0.85 |
| S3 | pass@k 无偏估计量 1−C(n−c,k)/C(n,k)；朴素式有偏；pass@1=c/n | https://rajeevraibhatia.com/blog/pass-at-k-evaluation-metric-explained/ | 2026-11-07 | 0.9 |
| S3' | 同上（第二独立源，含数值稳定实现与恒等式自检） | https://induwara.lk/tools/ai-pass-at-k-calculator | 2026-11-07 | 0.85 |
| S4 | MBPP = 974 任务；few-shot 最佳 59.6%；MathQA-Python 23,914 | http://arxiv.org/abs/2108.07732 | 2026-11-07 | 0.95 |
| S5 | MBPP 切分 prompt 1-10 / test 11-510 / validation 511-600 / train 601-974；sanitized 427 | https://huggingface.co/datasets/google-research-datasets/mbpp | 2026-11-07 | 0.9 |
| S5' | 同上（第二源，切分代码逐 task_id 一致） | https://huggingface.co/datasets/arjunguha/mbpp | 2026-11-07 | 0.85 |
| S6 | LiveCodeBench：滚动收 LeetCode/AtCoder/Codeforces 新题；v2 = 400 题（2023-05~2024-05）；四场景；18 base + 34 instruct 评测；公开 prompts+completions | http://arxiv.org/abs/2403.07974 | 2026-11-07 | 0.95 |
| S7 | EvalPlus/HumanEval+：测试扩 80×；26 LLM pass@k 虚高 19.3–28.9%；误排序（WizardCoder-CodeLlama/Phind-CodeLlama 反超 ChatGPT） | http://arxiv.org/abs/2305.01210 | 2026-11-07 | 0.95 |
| S8 | SWE-bench：2,294 任务、12 仓库、Claude 2 解 1.96% | http://arxiv.org/abs/2310.06770 | 2026-11-07 | 0.95 |
| S9 | BigCodeBench：1,140 任务/139 库/7 域；5.6 tests/任务、99% 分支覆盖；LLM ≤60% vs 人类 97% | http://arxiv.org/abs/2406.15877 | 2026-11-07 | 0.95 |
| S10 | n-gram 去污染被 paraphrase/翻译绕过；13B 过拟合达 GPT-4 级；RedPajama-1T/StarCoder 检出 8–18% HumanEval 重叠；llm-decontaminator 开源；fresh one-time exams 倡议 | http://arxiv.org/abs/2311.04850 | 2026-11-07 | 0.95 |
| S11 | DCQ：词级扰动多选题黑盒污染检测，无需训练数据/参数访问，TACL | http://arxiv.org/abs/2311.06233 | 2026-11-07 | 0.9 |

## 找不到 / 未验证

1. **canary string 埋点法的一手细节**（Carlini et al. 提取训练数据谱系）：本次调研未拉取一手原文，N-3.5 只登记方法名并标 `[待核验]`，不引具体数值。
2. **n-gram 去污染的行业标准阈值**（N 取几、匹配长度多少算污染）：各实现不一，无公认常数 → B3 黑盒。
3. **LiveCodeBench v2 之后（2024-05 以后窗口）的题量**：一手 abstract（v2）只给 400 题；后续版本增量未在本次核验范围 → 树内只写 v2 口径，不引更新数字。
