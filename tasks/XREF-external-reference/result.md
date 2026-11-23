# XREF-Q2 result — frontier 模型外部参照(Q2 模型选型)

- 执行:arena agent(frontier 模型 + 真搜索),2026-11-23
- 搜索调用:19 次(预算 ≤20);全程用时 ~10 分钟(预算 ≤15 分钟)
- 回执指纹:
  - 题面 sha1:`f45ad104dff8544d6bb2b75a43a7e51021282051`
  - 任务书 sha256(全文去掉该行后):`2fec587c69158018abfb6f3987b9b428eab63bc6d06b54bab1551cb5ab00000e`

## 输出

### 1. 分解:「每千次合格回答的总成本」¢/1k_acc 的全部因素

**根标量定义**:¢/1k_acc = 每请求总成本 ÷ P(合格) × 1000(美分)。
按题面对「合格」的口径:函数级补全请求须**通过测试**,指令跟随请求须**达标**;混合负载下合格率按流量加权。分母 P(合格) 同时充当**重试放大系数**——合格率 0.5 意味着每产出 1 个合格回答平均要花 2 次请求的钱。

**分子:每请求总成本,由四组因素决定**

1. **token 消耗量**:输入侧 = FIM 前缀+后缀上下文(函数级补全的 prompt 形态与 chat 完全不同)、仓库上下文注入;输出侧 = 补全长度(通常 64~256 tok)或指令回答长度;前缀缓存命中率(同文件连续补全场景命中率高,能砍掉大半 prefill 成本)。
2. **有效吞吐(决定每请求摊到的 GPU 秒)**:参数量、量化位数、并行策略(TP/PP)、连续批处理、推理引擎(vLLM vs TensorRT-LLM 后者同硬件约 1.5× 吞吐)、并发上限。补全场景 TTFT 敏感,批量上不去,吞吐打折。
3. **单价**:API 路线 = 各家 in/out 每 M token 价目(同一开源模型不同供应商差 5~10 倍);自托管路线 = 硬件摊销 + 电费 + 运维人力 + serving 栈工程成本。
4. **工程与合规成本(摊销)**:FIM 模板/特殊 token 适配、量化质量验证、内部评测集建设、许可证审查。低流量下这部分比 GPU 贵,高流量下趋近于零。

**分母:P(合格),由五组因素决定**

1. **基准分**:HumanEval(+/MBPP+(+)(函数级)、LiveCodeBench(防污染)、IFEval/BFCL(指令跟随)。注意口径:thinking/非 thinking、benchmark 版本、评测 harness 都会大幅移动分数(见候选表脚注)。
2. **基准→真实任务的 transfer 率(主导黑盒,无公开数字)**:公开证据显示排名会反转、污染普遍存在、过测≠可用(见下文"矛盾与口径警报")。这是整个成本模型里**不确定性最大**的因子:transfer 率从 0.9 掉到 0.6,¢/1k_acc 直接涨 50%,足以颠覆所有基准排名。
3. **量化质量恢复率**:W4/AWQ/GPTQ 相对 BF16 的能力折损。w8a8 有公开 100% 恢复数据(Llama-3.3),W4 没有公开恢复率数据。
4. **FIM(填充中间)支持——函数级补全的硬门槛**:不支持原生 FIM 的模型只能用 chat 方式"伪补全",前缀/后缀信息利用不完整,补全合格率结构性受损,且 token 成本上升。
5. **thinking 开关**:如 Qwen3-32B 双模式,thinking 提质量但输出 token 数翻倍以上、TTFT 变差——对"每千次合格回答"是分子分母同时动,方向依任务难度而定。

**约束(一票否决,先于成本计算)**

1. **许可证一票否决**:对外分发/对外提供服务时——Llama 3.3 Community License 要求显著标注 "Built with Llama"、衍生模型名以 Llama 开头、>700M MAU 需向 Meta 申请;DeepSeek Model License 禁止军事等用途且限制须传导至衍生品。仅内部使用时二者均可用。Apache 2.0(Qwen3/Qwen2.5-Coder/Mistral-Small)、MIT(GLM-4-32B-0414)无任何附加义务。
2. **显存一票否决(单台双卡 24GB = 48GB 总显存)**:DeepSeek-Coder-V2-236B(若按族内映射)Q4 也要 ~118GB+ → 否决;Llama-70B W4 权重 ~35-40GB,4K 上下文全量入卡需 ~45-52GB → **贴边**,KV cache 与并发被严重压缩,长上下文直接 OOM;32B 级 Q4 ~14-20GB → 单卡即可富余跑,双卡可做 TP 或双实例。
3. **候选存在性一票否决**:「DeepSeek-Coder-V2-33B」**不存在**。DeepSeek-Coder-V2 只有 16B(Lite,2.4B 激活)与 236B(21B 激活)两个规格;33B 是上一代 DeepSeek-Coder(-Instruct) 的规格。该候选要么按 V2-Lite-16B、要么按 V1-33B、要么按 V2-236B 重定义,三者结论完全不同(见候选评估)。

**SHARED 参数:params(参数量)的三路径耦合**——这是本题"哪个最划算"的枢纽:

- 能力路径:params↑ → 基准分↑(分母受益)
- 显存路径:params↑ → 量化位数被迫↓/并行度↑ → 质量恢复与稳定性↓(分母受损、运维成本↑)
- 成本路径:params↑ → tokens/s↓ → 每请求 GPU 秒↑(分子受损)

在 2×24GB 约束下,70B(W4)同时踩后两条路径:它比 32B 多出的能力优势,被 W4 折损 + 贴边显存吃掉,还要付更高的每请求成本。**32B 是这个显存预算下的甜点尺寸**。

**主导黑盒:基准→真实任务 transfer 率**,用一整节展开(见"矛盾与口径警报")。

### 2. 候选评估

(基准分均为 pass@1,来源见"## 来源";同一指标多个口径时并列)

| 候选 | 存在性 | 函数级基准 | 指令跟随 | LCB | 许可证(一票否决检查) | FIM | 2×24GB 适配 | API 单价(in/out $/M) |
|---|---|---|---|---|---|---|---|---|
| Qwen3-32B | ✓(Apache 2.0, 32.8B dense, 128K) | HumanEval+ 79.0(第三方);SWE-bench V 30.0 | IFEval 83.2(非 thinking,strict);官方报告 79.3~84.7 随模式 | v5:非 thinking 31.3 / thinking 68.4;第三方榜 28.8(口径不同) | Apache 2.0,无附加义务 ✓ | Qwen3-Coder 系列确认支持;**Qwen3-32B 本身未确认** | Q4 ≈ 17.4GB,单卡富余 ✓ | 0.08 / 0.28 |
| Qwen2.5-Coder-32B-Instruct | ✓(Apache 2.0, 32K ctx) | **HumanEval 92.7(官方)/ 92.1(EvalPlus);HumanEval+ 87.2;MBPP 90.2~90.5;MBPP+ 75.1~77;BigCodeBench-Instr 49.6;Aider edit 73.7(pass@2)** | IFEval 没查到该型号;通用 Qwen2.5-32B 为 84.01 | 31.4 | Apache 2.0 ✓ | **原生 FIM( <|fim_prefix|> 等),训练内建** | Q4 ≈ 19GB,单卡 ✓ | DeepInfra 列 $0.80(口径不明,存疑) |
| Mistral-Small-2501-24B | ✓(= Mistral-Small-24B-Instruct-2501, Apache 2.0, 32K) | HumanEval 84.8 | IFEval 82.9;MT-Bench 8.35;Arena-Hard 0.873 | 25.2(第三方榜) | Apache 2.0 ✓ | 没查到支持证据(Mistral 的 FIM 模型是 Codestral) | Q4 ≈ 14GB,最轻松;官方定位低延迟(称较 70B 级快 3×)✓ | 0.04~0.05 / 0.064~0.08 |
| GLM-4-32B-0414 | ✓(MIT, 32K+YaRN 128K) | **HumanEval/MBPP 官方未公布,没查到可信第三方分数**;SWE-bench Verified 33.8(Moatless)/30.7(Agentless)/27.2(OpenHands) | **IFEval 87.6(候选中最高)**;BFCL-v3 69.6 | 没查到 | MIT ✓ | 没查到支持证据 | Q4 ≈ 19-23GB,单卡 ✓ | 0.10(in) |
| DeepSeek-Coder-V2-33B | **✗ 不存在**(V2 仅 16B/236B;33B 是 V1 规格) | 按映射:V2-Lite-16B 81.1 / V1-33B 79.3 / V2-236B 90.2 | 没查到(各映射) | Lite 24.3 / V1-33B 22.5 / 236B 43.4 | DeepSeek Model License:商用允许,军事等用途禁止、限制须传导(对外分发时是约束,非否决) | V1/V2 均有 FIM token( ｜fim begin｜ 等) | Lite-16B 轻松;236B 否决;V1-33B Q4 ≈ 20GB 可跑 | 没查到该组合的有效价目 |
| Llama-3.3-70B-Instruct(W4) | ✓(Llama 3.3 Community) | **HumanEval 口径分歧极大:88.4(Meta 官方 0-shot)/ 83.2(w8a8 评测基线)/ 80.5 / 78.4(Artificial Analysis)**;HumanEval+ 78.4;MBPP EvalPlus base 87.6 | IFEval 88.35(Mistral 卡)/ 92.1(多个二手来源) | 28.8 | **对外分发触发:署名 "Built with Llama"+ 衍生名 Llama 开头+ >700M MAU 门槛;内部使用不触发** | 没查到支持证据 | **W4 全入卡需 ~48GB = 双 24GB 贴边;4K ctx 需 45-52GB,KV/并发严重受限;无 NVLink 时 TP 效率 ~60%** | 0.10 / 0.32(DeepInfra Turbo)~ 1.04(Together) |

**矛盾与口径警报(每千次合格回答的"合格率"被这些直接扰动)**

1. **排名反转(最强证据,直接打脸"按基准选型")**:有研究实测发现 Qwen3-32B 在 SWE-bench 上高于 Qwen2.5-Coder-32B-Instruct,但在代码补全任务上**明显更差**(arXiv:2608.13566)。结论:agentic 修 issue 的基准排名与函数级补全能力是两个维度,跨维度按榜单选型会选反。
2. **HumanEval 污染**:每个 HumanEval prompt 在 GitHub 上至少出现 43 次(中位 99 次);EvoEval 改写题面后 top 模型 pass@1 掉 19~47pp——高分里有大量记忆成分。对 2024 年前发布的候选(Qwen2.5-Coder、DeepSeek-Coder 系列)尤其要打折读。
3. **过测 ≠ 合格**:METR(2026-03)发现 >50% SWE-bench 过测 patch 过不了人类 code review;ICSE 2026 发现 7.2~8.4% 被判对的 patch 在全量测试下功能坏;Claude Opus 4.5 同一 scaffold 下 SWE-bench Verified 80.9 → Pro 45.9。"通过测试"这个合格口径本身有 5~35pp 的虚高。
4. **同一模型跨来源分差**:Llama-3.3-70B 的 HumanEval 四个来源相差 10pp(78.4~88.4),IFEval 相差 3.8pp(88.35/92.1);Qwen3-32B 的 LiveCodeBench 因 thinking 开关/版本不同在 28.8~68.4 之间摆动。**任何跨候选比较必须先对齐 harness,否则比的是口径不是模型。**
5. Mistral 官方自评(1k 条内部 prompt 人类偏好)与其公开基准自相矛盾的倾向,官方模型卡自己都写了"公开基准与人类判断有时差异巨大"。

### 3. 条件化结论(哪个最划算——按条件分支)

**条件 A:负载以函数级代码补全(Python/JS)为主,需要 FIM 式光标处补全**
→ **Qwen2.5-Coder-32B-Instruct 自托管,最划算**。理由:六个候选里唯一确认原生 FIM(训练内建、官方 token 体系)、函数级基准全维度第一(HumanEval+ 87.2 vs 次优 ~79;MBPP+ 77)、Apache 2.0 无义务、32B Q4 单卡 24GB 就能跑(双卡可跑双实例,每美元吞吐翻倍)。分母(合格率)优势在补全场景是结构性的(FIM 硬门槛 + rank-reversal 论文直接测得它补全强于 Qwen3-32B),足以覆盖它 API 单价的存疑劣势。**注意其 API 价($0.80/M)是候选里最贵且口径不明——这条路线应自托管而非买 API。**

**条件 B:负载以通用指令跟随/工具调用/文档化回答为主**
→ **GLM-4-32B-0414**。IFEval 87.6 候选最高、SWE-bench Verified 33.8 候选最高、MIT 最干净、API in $0.10 属最便宜档、32B 显存舒适。风险:官方不公布 HumanEval/MBPP(没查到),函数级补全能力无数据背书;选定前必须用自家补全任务跑影子评测。次选 Qwen3-32B(IFEval ~83,thinking 模式解难题更强但 token 成本翻倍)。

**条件 C:预算极紧/快速试水/低延迟优先,补全质量要求可放宽**
→ **Mistral-Small-2501-24B**。API 最便宜(in $0.04~0.05 / out $0.064~0.08)、显存最小、官方主打低延迟(自称较 Llama-70B 级快 3×)。代价:HumanEval 84.8 与 LCB 25.2 均为候选末段、无 FIM 证据。¢/1k_req 最低,但 ¢/1k_acc 取决于你对"合格"的要求放多宽。

**条件 D:明确要 70B 级质量,能接受低并发 + 合规条款,且预算走 API**
→ **Llama-3.3-70B 走 API(DeepInfra $0.10/$0.32)而非本地 W4**。本地 W4 是本题最差的性价比陷阱:48GB 贴边装下后 KV cache 极小 → 并发崩 → 每请求 GPU 秒大涨(分子↑);W4 相对 BF16 的质量恢复率无公开数据,88.4 的官方 HumanEval 分对 W4 不可直接引用(分母存疑);TP 无 NVLink 效率 ~60%。两头挨打,¢/1k_acc 大概率高于 32B 专职模型。若必须本地 70B,先做 W4 恢复率实测再决策。

**条件 E:「DeepSeek-Coder-V2-33B」按原名不成立,须先重定义候选**
- 若指 V2-Lite-16B-Instruct:便宜、快、带 FIM,但 HumanEval 81.1/MBPP+ 68.8 明显弱于 Qwen2.5-Coder-32B,只在极端成本敏感时有意义;
- 若指 V1 DeepSeek-Coder-Instruct-33B:老一代(HumanEval 79.3),被 Qwen2.5-Coder-32B 全面压制,不推荐;
- 若指 V2-236B:2×24GB 物理装不下,一票否决。
→ 三条映射没有一条能赢下"最划算";此候选出局。

**条件 F(总开关):内部真实任务与公开基准的 transfer 率未知**
这是所有结论的公因子。若内部评测发现 transfer 率低(比如 0.5~0.7)或排名与基准不一致,**以内部影子评测排名为准,上文所有基于公开基准的排序作废**。实操建议:取 100~200 条真实补全/指令请求建小评测集,六候选(或其可行子集)各跑一遍,按 ¢/1k_acc 实测定标——一次评测成本约几十美元,低于选错模型一个月的浪费。

**默认推荐(混合负载,补全 ≥50%):自托管 Qwen2.5-Coder-32B-Instruct(Q4,vLLM)为主;若指令流量大且质量要求高,加 GLM-4-32B-0414 做双模型路由(补全→Coder,指令→GLM)。低流量(<几千次/天)时路由不划算,退化为单模型 + 内部评测集定夺。**

### 4. 不确定点清单(结论依赖处显式标注)

1. 「DeepSeek-Coder-V2-33B」不存在——题面候选名与实际模型家族不符,需出题侧澄清意图(已给出三种映射的答案)。
2. GLM-4-32B-0414 的 HumanEval/MBPP 分数:官方未公布,多轮检索没查到可信第三方数字。条件 B 的结论因此带影子评测前置条件。
3. Qwen3-32B(非 Coder)是否支持 FIM:Qwen3-Coder 系列确认支持,但 Qwen3-32B 本身未查到确认;若不支持,条件 A 下它出局。
4. Mistral-Small-2501 / GLM-4-32B / Llama-3.3 的 FIM 均为**消极证据**(没查到支持),不是确证不支持。
5. Qwen2.5-Coder-32B-Instruct 自身的 IFEval 分没查到(只找到通用 Qwen2.5-32B 的 84.01,不能直接挪用)。
6. DeepInfra 列的 Qwen2.5-Coder-32B $0.80/M 不明是输入、输出还是混合口径,与其它模型价格不可直接比。
7. W4 量化对 Llama-70B 的质量恢复率无公开数据(w8a8 有 ~100% 恢复,W4 无)。
8. transfer 率(基准→真实任务)无任何公开数字,只有排名反转与污染的定性/半定量证据;本报告所有 ¢/1k_acc 排序都继承这个不确定性。
9. 自托管算例中的电价、折旧年限、利用率是明示假设,非查得数据。
10. LiveCodeBench 各数字跨版本(v3/v5)与模式(thinking)不可比,表中已标注口径但无法完全对齐。
11. "合格"的联合口径(补全过测试 + 指令达标)没有任何公开基准直接测得,必须内部定义与实测。
12. 未检索 2026 年内新发布但不在候选名单内的模型(如 Qwen3-Coder-30B、Mistral Small 3.2)——题面限定候选范围,但选型结论在 2026-11 有"候选清单本身过时"的风险。

## 来源

(全部来自本次真实搜索;每条注明取用信息)

1. https://github.com/deepseek-ai/DeepSeek-Coder-V2 — V2 仅有 16B/236B 规格(33B 不存在的关键证据)、各变体 HumanEval/MBPP+/LCB 分、V1-33B=79.3、许可声明
2. https://arxiv.org/html/2505.09388v1 — Qwen3 技术报告:LCB v5(thinking 68.4/非 thinking 31.3)、IFEval 各模式分数
3. https://serenitiesai.com/benchmark/models/qwen3-32b — Qwen3-32B:HumanEval+ 79.0、SWE-bench V 30.0、LCB 36.0(第三方口径)
4. https://benchlm.ai/models/qwen3-32b — Qwen3-32B 非 thinking LCB v5 31.3、IFEval 83.2(strict)
5. https://ai-tldr.dev/models/qwen2-5-coder/ — Qwen2.5-Coder-32B 全套基准(HumanEval 92.7、HE+ 87.2、MBPP 90.2、MBPP+ 75.1、BigCodeBench 49.6、LCB 31.4、Aider 73.7)、Apache 2.0(3B 除外)
6. https://benchmarklist.com/benchmarks/humaneval/ — EvalPlus 快照:HumanEval 92.1 / HE+ 87.2
7. https://benchmarklist.com/benchmarks/mbpp/ — MBPP+ 77、EvalPlus Average 82.1
8. https://klu.ai/benchmarks/humaneval — EvalPlus 快照口径说明、HumanEval 已饱和/停止更新的现状
9. https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501 — Mistral-Small-2501 官方基准(HumanEval 84.8、IFEval 82.9、MT-Bench 8.35、Arena-Hard 0.873)及对 Llama-3.3/Qwen2.5-32B 的同表对比
10. https://www.marktechpost.com/2025/01/31/mistral-ai-releases-the-mistral-small-24b-instruct-2501-a-latency-optimized-24b-parameter-model-released-under-the-apache-2-0-license/ — Apache 2.0、32K 上下文、低延迟定位
11. https://www.datacamp.com/blog/llama-3-3-70b — Llama 3.3 官方口径(HumanEval 88.4、MBPP EvalPlus 87.6、BFCL v2 77.3)
12. https://huggingface.co/neuralmagic/Llama-3.3-70B-Instruct-quantized.w8a8 — HumanEval 83.2 / HE+ 78.4(BF16 基线)、w8a8 量化恢复率 100%
13. https://everylocalai.com/model/llama3-3-70b — Artificial Analysis 口径 HumanEval 78.4、LCB 28.8
14. https://www.emergentmind.com/topics/llama-3-3-70b-instruct — 又一口径 HumanEval 80.5(引 Grattafiori et al.)、4-bit 量化评测欠佳记录
15. https://huggingface.co/zai-org/GLM-4-32B-0414 — GLM-4-32B-0414 官方模型卡(15T 预训练、工程代码/函数调用定位、**无 HumanEval 数据**)
16. https://github.com/zai-org/GLM-4 — IFEval 87.6、BFCL-v3 69.6/41.5、TAU-Bench、SimpleQA/HotpotQA
17. https://deepwiki.com/THUDM/GLM-4/1.3-performance-and-capabilities — SWE-bench Verified 33.8(Moatless)/30.7(Agentless)/27.2(OpenHands)
18. https://www.marktechpost.com/2025/04/14/thudm-releases-glm-4-a-32b-parameter-model-competing-head-to-head-with-gpt-4o-and-deepseek-v3/ — MIT 许可、发布定位
19. https://deepwiki.com/deepseek-ai/DeepSeek-Coder-V2/7-commercial-considerations — DeepSeek 双许可结构(代码 MIT/权重 DeepSeek Model License)、商用允许、硬件需求(236B 需 8×80GB)
20. https://www.aipotluck.org/product/deepseek-coder — DeepSeek Model License 细节:Attachment A 用途限制、衍生品限制传导义务
21. https://github.com/huggingface/Qwen2.5-Coder — FIM 特殊 token 官方定义与用法( <|fim_prefix|> <|fim_suffix|> <|fim_middle|> )
22. https://www.alphaxiv.org/abs/2409.12186v2 — Qwen2.5-Coder 技术报告:FIM 基准对比 DS-Coder-33B-Base(CrossCodeEval +3.7%、RepoEval +7.9% EM)、FIM 训练细节
23. https://llmpodium.com/blog/fill-in-the-middle-fim-code-completion-guide — 各家族 FIM token 对照表(DeepSeek Coder V1/2 、Codestral、CodeLlama 等)
24. https://deepwiki.com/QwenLM/Qwen3-Coder/3.3-fill-in-the-middle-(fim) — Qwen3-Coder 全系 FIM 支持("FIM is supported in every version of Qwen3-Coder")
25. https://vdf.ai/blog/llama-on-premises-enterprise-deployment/ — Llama 许可条款表(700M MAU、Built with Llama、衍生命名、AUP)
26. https://canirun.ai/license/llama-3-3-community/ — Llama 3.3 许可清单:内部/私人使用不受署名条款约束
27. https://maple.ai/blog/llama-3-3-70b-guide — 70B W4 全入显存需 ~48GB、许可义务摘要
28. https://apxml.com/models/qwen3-32b — Qwen3-32B 显存需求(Q4 ~17.4GB / FP16 ~62.1GB)、API 价 $0.08/$0.28
29. https://www.cloudzero.com/blog/llm-inference-providers/ — 同一 Llama-3.3-70B 跨供应商 $0.10~$1.04/M 输入价差
30. https://pricepertoken.com/endpoints/compare/deepinfra-vs-together — DeepInfra 价目:Mistral-2501 $0.04/M、Qwen2.5-Coder-32B $0.80/M、Llama-3.3-70B $0.10/$0.32
31. https://pricepertoken.com/endpoints/compare/deepinfra-vs-openrouter — Mistral-Small-2501 $0.04/$0.064;Qwen2.5-Coder $0.66(OpenRouter)
32. https://pricepertoken.com/leaderboards/benchmark/livecodebench — LCB 榜与价格:Qwen3-32B 28.8($0.08/$0.28)、Mistral-2501 25.2($0.05/$0.08)
33. https://www.misar.blog/@synor/articles/vram-requirements-70b-llm — 70B INT4 需 45-52GB(4K ctx)、2 卡无 NVLink TP 效率 ~60%、4090 单卡 70B 需 offload 1-3 t/s
34. https://www.myaihardware.com/deep-dive/economics-of-running-70b-405b-671b-on-prem — 吞吐经济:引擎差异 2-4×(TensorRT-LLM ~1.5× vLLM)、70B FP8 H100 80 t/s(bs=1)
35. https://arxiv.org/html/2608.13566 — 核心 transfer 证据:Qwen3-32B SWE-bench 高于但代码补全明显差于 Qwen2.5-Coder-32B(rank reversal);SWE-bench 优化不跨任务迁移
36. https://pakodas.substack.com/p/how-code-is-evaluated-in-benchmarks — 污染指纹(EvoEval -19~47pp)、Claude Opus 4.5 Verified 80.9→Pro 45.9、METR 过测 patch >50% 过不了 review、ICSE 2026 7.2~8.4% 误判
37. https://futureagi.com/blog/humaneval-benchmark/ — HumanEval 污染量化(每题 GitHub ≥43 次、中位 99 次)、pass@k 不覆盖的质量维度
38. https://datavlab.ai/post/llm-benchmarks-2026-which-model-for-which-job — SWE-bench 随 scaffold 波动 25pp、LCB 防污染定位、单基准选型不可靠
39. https://www.reddit.com/r/LocalLLaMA/comments/1k4god7/glm4_32b_is_mind_blowing/ — 32B Q4 显存实测 19-23GB、RTX 3090 上 Q4_K_M ~36 t/s(自托管吞吐参考)
40. https://zeroshotmind.com/blog/llm-eval-instruction-following — IFEval 已饱和(top-10 仅 2.9pp)、85% 以下不适配生产的判据

## 自述缺口

(明确标"没查到/不确定/需进一步验证"的点;禁止编造,故以下均如实留白)

1. **没查到**:「DeepSeek-Coder-V2-33B」的任何官方/第三方存在证据——它不是真实发布的型号(缺口本身就是发现)。
2. **没查到**:GLM-4-32B-0414 的 HumanEval、MBPP、LiveCodeBench 分数(官方模型卡不公布,第三方无可靠数字)。
3. **没查到**:Qwen3-32B(非 Coder 版)的 FIM 支持确认;Qwen3-Coder 系列确认支持,不能自动外推。
4. **没查到**(消极证据,非确证):Mistral-Small-2501、GLM-4-32B-0414、Llama-3.3-70B 的 FIM 支持——检索未见支持证据,仅知 Mistral 的 FIM 模型是 Codestral、Llama 的 FIM 在 CodeLlama 一代。
5. **没查到**:Qwen2.5-Coder-32B-Instruct 的 IFEval 分数。
6. **没查到**:DeepSeek-Coder-V2 各变体的 IFEval;其 V1-33B 的 API 价目。
7. **不确定**:DeepInfra Qwen2.5-Coder-32B $0.80/M 的计价口径(输入/输出/混合),与它模型价差 10 倍的合理性存疑,需查价目页原文核实。
8. **不确定**:W4 量化对 Llama-3.3-70B 的质量恢复率(无公开数据;88.4 的 BF16 分数不能直接套给 W4 部署)。
9. **不确定**:基准→真实任务 transfer 率的具体数值——本报告 ¢/1k_acc 的排序在 transfer 率剧烈变化时可能反转,须内部实测。
10. **需进一步验证**:自托管算例的电价/折旧/利用率假设;Qwen3-32B HumanEval+(79.0)是单一第三方来源;LiveCodeBench 跨版本数字的严格对齐。
11. **范围外未查**:候选名单之外的 2025-2026 新模型(如 Qwen3-Coder-30B-A3B、Mistral Small 3.2)——题面限定候选,但选型时点上清单可能已过时。
