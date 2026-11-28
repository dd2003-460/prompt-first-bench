# 三探针目标函数提取（S1 纯提取）
# origin: ai (sub extraction, 2026-11-28)

## 探针1 #48 激活子图投影
- 目标函数：度量耦合图质量——外部证据节点与内部概念的耦合强度 c(v)（verified=1.0/degraded=0.5/failed=0.0）及三个质量指标（源:pfb-thinkmech/modules/F-theory/research/2026-11-15-idea48-activation-subgraph.md:38-48）
- 变量：X=问题 q(+外部检索 R={r_1..r_n})，Y=分解树 T（无检索 T_0≈激活子图 G_a 树状投影；有检索 T_1≈耦合图 G_coupled 投影）（源:同文件:19-36）
- 参照：激活强度 act(v,q)（attention weight/probing score/生成概率，阈值 θ）vs 外部证据 verify 状态；预测 2 参照 bench 分数相关性（源:同文件:22,72）
- 现有测量量：耦合覆盖率 cc=v/(v+d+p)：knowledge 0.743 vs search 0.033（GPU 22x；三域全 corpus 5.5x-22.8x）；预测 2 r(cc,depth)=0.100（GPU n=28 不显著，原 0.738 为 bug 已废弃）；脚本 idea48-pred2-coupling-depth.py / idea48-source-depth-coupling.py（源:同文件:111-228；辅源 IDEA-INDEX.md:67）
- 朴素打分基线：未定义（源:全文无朴素基线定义，参照物为 bench 分数相关性）

## 探针2 OOD transfer 判据
- 目标函数：度量不变核 C 换域后是否无损迁移（general=同核换域 D∘C 仍无损），操作化为域外净增益而非域内精度（源:pfb-thinkmech/modules/G-think-mechanism/oood-general-probe/oood-battery-spec.md:3,19）
- 变量：X=不变核 C（控制流+生产 prompt+检索通道，ON/OFF），Y=每域得分 SM_d（机制覆盖/定量 claim 数/L1 结构）；对照 BL_d（裸基线）、MC_d=max(C_d,E_d)（源:spec:7-16；decomposition.md:7-9）
- 参照：计算匹配最强通用对照 MC_d（臂 C BoN N=SM 实际 LLM 调用数 / 臂 E GenericMultiStep token 匹配，事前冻结）；迁移 gap=G_s−G_t，G=P_SM−P_MC（相对增益非绝对准确率）（源:spec:13-18）
- 现有测量量：预注册四必要条件（Kernel Invariance/Compute-Adjusted Gain Δ_d=SM_d−MC_d>0 且单侧 CI 下界>0 n≥3/Low Migration Gap G_s−G_t≤ε=10pp/LODO 纪律）；S0 气象半程：SM 覆盖 4/4=基线 4/4、定量 claim 27 vs 38、L1=6，判决 inconclusive（源:spec:20-28；decomposition.md:48-54，metrics-s0-cyclone.json）
- 朴素打分基线：裸 27b 单发基线 BL（同题直接作答，无分解无核验）+ 计算匹配 C/E 臂（源:decomposition.md:9；spec:13-16）

## 探针3 budget Pareto
- 目标函数：[未找到精确定式化] 最近表述="通过预算直接控制 AI 在 Pareto 边界上研究（预算大→完整覆盖所有贡献因子如 gold；预算小→压缩细节）"；操作化=judge_total 随节点预算的响应曲线/凹 Pareto 前沿（源:pfb/tasks/00-ops/budget-scan-status-20261126.json:39；pfb-thinkmech/modules/B-pipeline-ablation/data/q7-budget-scan/q7-budget-response-curve.json:conclusion）
- 变量：X=节点预算 budget（max_nodes 档 50/100/150/300/719，soft cap 下界非上限），Y=judge_total=0.5*struct(depth/GOLD_DEPTH)+0.5*cov（源:e-synth-pareto-synthesis-20261126.md:117-118）
- 参照：域内 gold（gpu 36 units / q6 46 units）：cov=bge-m3 cosine≥0.70 命中 gold 单元比例，depth 归一到 GOLD_DEPTH；judge_v1（qwen3.8-27b×1 non-IRR）（源:e-synth:117-120）
- 现有测量量：Q7 五点 log 饱和拟合 jt=−0.1231+0.1208·ln(budget)，R²=0.987，719 实测 0.6603 残差 −0.011；三域 300→719 每节点边际收益塌 2-3.4×；推荐工作点 budget=300（conf 0.6）（源:q7-budget-response-curve.json:fits/marginal_gains；e-synth:86-100）
- 朴素打分基线：未定义（源:两源均无"不用预算扫描的朴素度量"定义；辅源 pfb/tasks/think-trigger/decomposition.md:133,138 仅涉 harness per-stage 4096 cap 预算缺陷，非本探针基线）
