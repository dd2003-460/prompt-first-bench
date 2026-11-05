# Divergence Taxonomy (90 cells)

> generated: CJ-RUBRIC-ALIGN stage A2

## Summary

| Type | Count | Mean Δ | Cells |
|------|-------|--------|-------|
| zero-fact | 13 | 0.835 | S0Q2r3, S0Q4r1, S0Q4r2, S0Q4r3, S0Q5r2, S0Q5r3, S1Q4r1, S2Q4r1 (+5) |
| derivation-scope | 17 | 0.304 | S1Q4r2, S1Q4r3, S1Q5r1, S1Q5r2, S1Q5r3, S2Q4r2, S2Q5r1, S2Q5r2 (+9) |
| granularity | 14 | 0.257 | S1Q1r1, S1Q1r2, S1Q1r3, S2Q2r1, S2Q2r2, S2Q2r3, S3Q1r2, S3Q1r3 (+6) |
| assumption-swap | 11 | 0.222 | S0Q3r2, S1Q3r1, S1Q3r2, S1Q3r3, S2Q3r2, S3Q3r1, S3Q3r2, S3Q3r3 (+3) |
| noise | 35 | 0.083 | S0Q1r1, S0Q1r2, S0Q1r3, S0Q2r1, S0Q2r2, S0Q3r1, S0Q3r3, S0Q5r1 (+27) |

## Per-cell detail

| Cell | Local M1 | Arena M1 | Δ | Type | Arena Note (trunc) |
|------|----------|----------|---|------|--------------------|
| S2-Q4-r3 | 0.00 | 0.93 | 0.929 | zero-fact | 在 r2 基础上给出可复算推导：50万页x500token≈2.5亿token 远超 128K，判定纯长上下文物理不可行 |
| S2-Q4-r1 | 0.00 | 0.92 | 0.917 | zero-fact | CPCA=总成本/正确回答数×1000 与 gold 的 c_correct 同构，50万页→50-100万 chunk |
| S4-Q4-r1 | 0.00 | 0.92 | 0.917 | zero-fact | CPCA=总成本/(总请求x正确率) 拆分正确、chunk 256/512/1024 与解析/嵌入/切块三类建设成本齐全 |
| S5-Q2-r3 | 0.00 | 0.92 | 0.917 | zero-fact | 70B W4 35-40GB、32B/33B W8 32-35GB、24B W8 24-26GB 均合理（略高估 W8， |
| S5-Q4-r1 | 0.00 | 0.92 | 0.917 | zero-fact | 根节点定义与 A-E 五支分解合理，并正确把'50万页总 token 是否超 128K'列为阻塞纯长上下文可行性的 G1 |
| S0-Q4-r2 | 0.00 | 0.83 | 0.830 | zero-fact | 三档 chunk(256/512/1024)、HNSW<10ms、100万x1536x4B≈6GB 均合理；同样缺建设摊 |
| S0-Q4-r3 | 0.00 | 0.83 | 0.830 | zero-fact | 与 S0-Q4-r2 逐字重复（temp=0 复现），评分同 r2 |
| S0-Q5-r2 | 0.00 | 0.83 | 0.830 | zero-fact | 显式把制度约束设为硬约束（与 gold 一致）、正确引用 Bernstein-von Mises 渐近等价与小 n 时频 |
| S0-Q5-r3 | 0.00 | 0.83 | 0.830 | zero-fact | 与 S0-Q5-r2 逐字重复（temp=0 复现），评分同 r2 |
| S0-Q4-r1 | 0.00 | 0.81 | 0.810 | zero-fact | embedding 成本链完全可复算（2.5亿token x $0.02/1M = $5、100万x512x4B≈2GB |
| S1-Q4-r1 | 0.00 | 0.79 | 0.786 | zero-fact | 50万页x500token≈2.5亿token、长上下文输入为 RAG 的 10-50x、混合方案幻觉率最低均与 gol |
| S5-Q4-r2 | 0.00 | 0.71 | 0.714 | zero-fact | 2.5亿 token、128K≈256 页、'无文档选择时长上下文仅覆盖 0.05% 文档故正确率低'的推导正确；但引用 |
| S3-Q4-r3 | 0.25 | 0.95 | 0.700 | derivation-scope | 同 r2 且把 250M>>128K 写成显式可复核算术，另覆盖嵌入/向量存储/索引覆盖度的成本叶子；数字均可复算 |
| S0-Q2-r3 | 0.00 | 0.63 | 0.630 | zero-fact | 答案在 tool_call 处截断，只有根式与 48GB 口径可核；叶子未填、无任何量化数字，属 truncated 而 |
| S3-Q4-r2 | 0.38 | 0.95 | 0.570 | derivation-scope | CPCA 分解正确，并给出可复算推导：50万页x500token≈2.5亿token、128K≈256 页，据此判定纯长 |
| S2-Q5-r1 | 0.27 | 0.83 | 0.563 | derivation-scope | EDL 根标量、大样本 n>1000 时两派统计精度差异≈0、期刊 p 值要求作为一票否决项均与 gold 一致；但给出 |
| S3-Q2-r1 | 0.50 | 0.93 | 0.429 | granularity | 48GB=2x24GB 口径、32B FP16 64-66GB 超预算必须量化、70B W4 ~35GB+KV 后可行但 |
| S2-Q4-r2 | 0.50 | 0.92 | 0.417 | derivation-scope | CPCA 代数化简为 (FC/N+VCQ)/AR 正确，明确 50万页远超 128K 因而'纯长上下文需澄清含义/可能不 |
| S1-Q1-r2 | 0.50 | 0.82 | 0.318 | granularity | 带宽比 1.675、单卡 1.5-1.7x、batch 增大转 compute-bound 均正确，且不再误称 PCIe |
| S1-Q1-r3 | 0.50 | 0.82 | 0.318 | granularity | 与 S1-Q1-r2 逐字重复（temp=0 复现），评分同 r2 |
| S3-Q1-r3 | 0.40 | 0.71 | 0.314 | granularity | 80GB 容量、NVLink 900、无 NVLink、700/350W 正确，并诚实标注'待核验/未解决'；错在默认两 |
| S4-Q3-r1 | 0.50 | 0.81 | 0.313 | assumption-swap | 27B 54/27/13.5GB、框架吞吐差 2-5x 而功耗差 <20%、利用率 0.99→0.80 使成本升 24% |
| S5-Q3-r2 | 0.62 | 0.93 | 0.309 | assumption-swap | decode 占 80-90% 且 memory-bound、vLLM 比 transformers 快 2-4x、TG |
| S1-Q5-r2 | 1.00 | 0.70 | 0.300 | derivation-scope | 显式写出 C_FP/C_FN 型损失（与 gold 的 L_err=P(FP)C_FP+P(FN)C_FN 同构），并正 |
| S1-Q5-r3 | 1.00 | 0.70 | 0.300 | derivation-scope | 与 S1-Q5-r2 逐字重复（temp=0 复现），评分同 r2 |
| S4-Q1-r2 | 0.80 | 0.50 | 0.300 | granularity | PCIe 无 NVLink、900/64≈14x 正确；三处硬错：称两版 HBM 均 3.35 TB/s、称两版 TDP |
| S1-Q5-r1 | 1.00 | 0.72 | 0.281 | derivation-scope | EDL 根标量与'没有绝对最划算的学派'结论正确，三场景条件化建议与 gold 方向一致；但 TDC 未覆盖 gold  |
| S5-Q5-r2 | 0.60 | 0.88 | 0.275 | derivation-scope | 根标量与'损失函数须事先指定'正确，结论明确限定在'0-1 损失+先验可得'假设下推荐贝叶斯，属条件化表述与 gold  |
| S1-Q1-r1 | 0.50 | 0.77 | 0.273 | granularity | 正确取用 PCIe 2.0 vs SXM 3.35 TB/s 并推出 1.675x（与 gold 的 1.68x 一致） |
| S3-Q1-r2 | 0.38 | 0.64 | 0.263 | granularity | NVLink 900GB/s、PCIe 无 NVLink、700/350W、Gen5 x16~64GB/s 正确；两处硬 |
| S0-Q3-r2 | 0.91 | 0.65 | 0.260 | assumption-swap | 电价 0.6-1.2、PUE 1.2-1.5、27B 显存换算均对；但同时把 27B 误猜成 Llama-3-70B/Q |
| S3-Q3-r2 | 0.50 | 0.75 | 0.250 | assumption-swap | 沉没成本口径与'吞吐是核心变量'正确；但凭空造出'Llama-3-70B 的 27B 变体/Qwen-2-72B 的 2 |
| S3-Q4-r1 | 0.67 | 0.90 | 0.230 | derivation-scope | CPCA=单次成本/正确率 的代数拆分正确、50万页→100-250万向量、每页 500-1000 token、128K |
| S5-Q3-r3 | 0.62 | 0.85 | 0.230 | assumption-swap | 27B 54/27/14GB 权重换算正确、四支权重 70/15/10/5 的占比假设明确标注；但以 2xA100-80 |
| S5-Q5-r1 | 0.67 | 0.90 | 0.230 | derivation-scope | L*=E[ell(delta(D),theta)] 根标量、单位与'需先指定损失函数否则最划算无定义'的前提均正确；未展 |
| S2-Q2-r3 | 0.70 | 0.93 | 0.229 | granularity | FP16/INT8/INT4 = 2/1/0.5 bytes per param 的换算正确、代码补全 500-2000 |
| S2-Q2-r1 | 0.71 | 0.94 | 0.228 | granularity | 48GB 口径、32B FP16~64GB 放不下、32B INT4 16-20GB、70B W4 35-40GB 临界 |
| S1-Q4-r2 | 0.57 | 0.79 | 0.216 | derivation-scope | token 规模与输入分布估计正确；同样缺建设摊销、把 p95<15s 写成 3s，且幻觉率区间未给依据 |
| S1-Q4-r3 | 0.57 | 0.79 | 0.216 | derivation-scope | 结构同 r2 并加了份额占比表（0.05-0.30 各级），占比数字无依据；同样缺建设摊销、p95 口径错为 3s |
| S2-Q3-r2 | 1.00 | 0.79 | 0.214 | assumption-swap | 固定硬件下硬件采购为沉没成本的口径正确、FP16→INT4 省约 75% 显存正确、batch 1→32 吞吐 10-3 |
| S5-Q1-r2 | 0.29 | 0.50 | 0.210 | granularity | PCIe Gen5 x16 ~64GB/s 单向与非全互联拓扑正确；但称 HBM 带宽'标称相同 3.35'、TDP'两 |
| S2-Q5-r2 | 0.69 | 0.88 | 0.193 | derivation-scope | EDL 公式、硬约束/软成本口径分离、小样本频率 CI 实际覆盖率 90-95% 的偏差区间均合理，结论为条件化三选（贝 |
| S3-Q3-r3 | 0.64 | 0.83 | 0.193 | assumption-swap | 27B 三档权重显存全部算对、$0.1/kWh 与'可变成本差异<5%'合理、明确'框架对功耗影响小'与 gold 的  |
| S5-Q5-r3 | 0.71 | 0.90 | 0.190 | derivation-scope | L* 取三候选最小、制度约束作为划除候选的硬约束、MCMC 比解析解慢 10-1000x 的量级判断均合理；'30-70 |
| S2-Q2-r2 | 0.75 | 0.94 | 0.188 | granularity | 同 r1 的显存换算全对（Mistral-24B FP16~48GB/INT4 12-15GB、Llama-70B W4 |
| S1-Q3-r1 | 1.00 | 0.81 | 0.187 | assumption-swap | 硬件固定下 C_1k ∝ 1/T 的化简正确、27B FP16≈54GB/INT4≈14GB 换算正确、vLLM 首选/ |
| S4-Q1-r3 | 0.44 | 0.62 | 0.185 | granularity | PCIe5.0 x16~64GB/s、NVLink 900GB/s、无 NVLink 正确，并诚实标注检索未取得 ben |
| S5-Q2-r1 | 0.75 | 0.93 | 0.179 | granularity | 32B 64GB 超预算→INT8 32/INT4 16GB、24B 48GB 卡线、33B 66GB、70B W4 3 |
| S1-Q3-r2 | 1.00 | 0.83 | 0.167 | assumption-swap | 功耗 250-400W、TTFT 100-500ms、vLLM 150/TGI 80 tok/s → 成本 53% 的换 |
| S1-Q3-r3 | 1.00 | 0.83 | 0.167 | assumption-swap | 与 S1-Q3-r2 逐字重复（temp=0 复现），评分同 r2 |
| S4-Q4-r2 | 0.75 | 0.92 | 0.167 | derivation-scope | CPCA 乘性耦合口径正确，纯长上下文'128K token 输入成本极高 + 迷失在中间导致引用错段'的判断与 gol |
| S5-Q4-r3 | 0.75 | 0.92 | 0.167 | derivation-scope | 嵌入存储算账可复算：1536 维 float32 ≈ 6KB/chunk、50万页x10 chunks ≈ 30GB，模 |
| S5-Q1-r3 | 0.80 | 0.64 | 0.157 | granularity | 唯一正确写出 HBM 3.35 vs 2.0 TB/s 的 S5 答案，NVLink 900、PCIe x16 64 也 |
| S3-Q3-r1 | 0.60 | 0.75 | 0.150 | assumption-swap | 27B 54/27/13.5GB 换算正确、固定硬件下只看可变成本与吞吐的化简正确、0.5 元/kWh 合理；但把题给  |
| S3-Q5-r1 | 0.75 | 0.90 | 0.150 | derivation-scope | 根标量取 min over {FREQ,BAYES,HYBRID} E[L] 与 gold 的期望决策损失同构，制度约束 |
| S5-Q1-r1 | 0.43 | 0.57 | 0.141 | noise | NVLink 900GB/s、无 NVLink、700/350W、14x 互连比正确；但称两版 HBM 带宽均 3.35 |
| S0-Q1-r2 | 0.56 | 0.70 | 0.140 | noise | 结构同 r1 但表格改用 X/Y 占位、未编造 tok/s，故略高；仍是 PCIe HBM 带宽误报为 3.35TB/s |
| S0-Q2-r2 | 1.00 | 0.86 | 0.140 | noise | 量化显存表全对并显式澄清双卡 24GB 歧义；扣分项为电价假设 0.1 元/kWh（实际居民约 0.5）、未给出可复算的 |
| S4-Q3-r3 | 0.89 | 0.75 | 0.140 | noise | 27B 三档权重显存、残值 0-10%、INT4 可提 2-4x 吞吐均合理；但据'FP16 需 ≥80GB 单卡或 2 |
| S2-Q1-r2 | 0.67 | 0.80 | 0.130 | noise | 自行纠正了'H100 PCIe 是 GDDR6X'的误解并给出 2.0 TB/s，PCIe5.0 x16 双向 128G |
| S0-Q2-r1 | 1.00 | 0.88 | 0.120 | noise | 32B/24B/33B/70B 的 FP16/INT8/INT4 权重换算全部正确（64/32/16GB、70B W4≈ |
| S0-Q5-r1 | 0.81 | 0.69 | 0.120 | noise | EDL 根标量、弱先验下两派渐近等价、频率闭式 C_comp≈0、'没有永远最划算的学派' 均对；Type I 膨胀 2 |
| S2-Q3-r3 | 0.92 | 0.80 | 0.120 | noise | 27B 三档显存、GPU 服务器满载 500-1500W、L40S 48GB 均正确；但同样以 A100/H100/L4 |
| S4-Q5-r1 | 0.78 | 0.90 | 0.120 | noise | 开头指出检索源为无关成人/新闻链接后忽略（流程污染已登记），正文 EDL 根标量正确、'n>10,000 时两派结果几乎 |
| S4-Q4-r3 | 0.80 | 0.92 | 0.117 | noise | 给出可复算账：50万页x500字=2.5亿字、text-embedding-3-small $0.02/1M → 一次性 |
| S5-Q3-r1 | 0.77 | 0.88 | 0.105 | noise | 27B 54/27/13.5GB、电力差异 <5%、吞吐差 2-5x、KV cache 10-50GB 均正确，vLLM |
| S1-Q2-r1 | 1.00 | 0.90 | 0.100 | noise | 六候选的 FP16/INT4 显存估算全部落在合理区间，2x17500/36≈972 元/月 可复算，且正确指出合格率是 |
| S2-Q1-r1 | 0.85 | 0.95 | 0.100 | noise | 唯一同时写全 3.35/2.0 TB/s、700/350W、NVLink 900、PCIe x16 ~64GB/s 并算 |
| S4-Q5-r3 | 1.00 | 0.90 | 0.100 | noise | 把制度违反写成 lambda x 示性函数加入目标（等价于 gold 的可行域约束）表述正确，EDL 累加式 T 期决策 |
| S3-Q1-r1 | 0.59 | 0.69 | 0.098 | noise | 700/350W、NVLink 900GB/s、PCIe 无 NVLink、互连 ~14x 均正确；错在称两版 HBM  |
| S3-Q2-r3 | 1.00 | 0.92 | 0.083 | noise | 同 r2 的量化显存换算与'单次调用成本/合格率'的根式化简均正确；略短，未给候选模型的具体能力分 |
| S3-Q5-r2 | 1.00 | 0.92 | 0.083 | noise | 开头指出检索源为成人站点并与问题无关后忽略之（流程污染，已登记），正文统计陈述准确：制度要求 p<0.05 时后验概率无 |
| S4-Q2-r3 | 1.00 | 0.92 | 0.083 | noise | 48GB=2x24GB、32B/33B/70B FP16 必须量化、24B FP16≈48GB 卡线均正确；合格率减半使 |
| S4-Q5-r2 | 1.00 | 0.92 | 0.083 | noise | L* 根标量、制度约束作为硬约束先排除、n>1000 时两派损失差 <5%、强制 p 值时频率优先均正确；仅'先验敏感性 |
| S3-Q5-r3 | 0.82 | 0.90 | 0.080 | noise | L_expected 根标量、期刊 p<0.05 作为必须产出 p 值的制度约束、贝叶斯决策规则 P(theta>0|D |
| S4-Q2-r2 | 1.00 | 0.93 | 0.071 | noise | 32B INT4 16-20GB、24B INT8 24GB、33B INT8 33GB、70B W4 35-40GB  |
| S5-Q2-r2 | 1.00 | 0.93 | 0.071 | noise | 同上显存账全对，且明确'48GB 约束下排除 FP16 的 32B，其余经量化均可部署'，无与 gold 冲突的硬数字 |
| S2-Q5-r3 | 0.92 | 0.85 | 0.070 | noise | 开头因检索源污染（色情站点）触发拒绝声明后再作答，属流程污染而非事实错误；正文 p 值定义（H0 下观察到当前或更极端数 |
| S4-Q2-r1 | 0.86 | 0.93 | 0.069 | noise | 32B 64/32/16GB、24B 48GB 卡线、70B W4 35GB 余量极小、48GB 硬约束表均正确；单次调 |
| S4-Q3-r2 | 0.90 | 0.83 | 0.067 | noise | 54/27/13.5GB 换算、A 支占 70-80%、框架额外开销 1-2GB 均合理；'若服务器只有 1 张 48G |
| S0-Q1-r3 | 0.62 | 0.68 | 0.060 | noise | 唯一正确点出 NVLink/PCIe≈14x 属互联带宽比而非吞吐比（与 gold 一致）；但仍断言两者 HBM 均为  |
| S2-Q1-r3 | 0.89 | 0.83 | 0.057 | noise | 3.35/2.0、700/350W、PCIe4.0 x16~64GB/s、互连 10x+ 均正确，且诚实标注证据仅来自官 |
| S4-Q1-r1 | 0.55 | 0.61 | 0.057 | noise | 互连 900 vs 64GB/s、700/350W、NVSwitch 全互联正确；但称两版 FP16 算力相同（gold |
| S0-Q3-r1 | 0.67 | 0.72 | 0.050 | noise | c_serve 结构、沉没成本口径、27B 三档显存算术、TGI PagedAttention 均对；但忽略题给 RTX |
| S0-Q3-r3 | 0.67 | 0.72 | 0.050 | noise | 与 S0-Q3-r1 逐字重复（temp=0 复现），评分同 r1；同样未用题给 3090x4 且漏 SLO |
| S0-Q1-r1 | 0.62 | 0.65 | 0.030 | noise | NVLink 900GB/s、TDP 700/350W、80GB 容量、prefill compute-bound 均对 |
| S3-Q2-r2 | 0.90 | 0.93 | 0.029 | noise | 32B(64GB)/33B(66GB)/24B(48GB)/70B-W4(35GB) 的显存账全部算对，24GB 卡 T |
| S2-Q3-r1 | 0.79 | 0.81 | 0.023 | noise | 27B FP16/INT8/INT4 = 54/27/13.5GB 换算正确、A-E 五维分解与'B 单流速度 vs C |
| S1-Q2-r2 | 0.83 | 0.83 | 0.003 | noise | 70B W4≈35GB+KV 后临界、32B W8≈32GB 可行、32B W4≈16GB 宽裕均正确，合格率 0.6→ |
| S1-Q2-r3 | 0.83 | 0.83 | 0.003 | noise | 与 S1-Q2-r2 逐字重复（temp=0 复现），评分同 r2 |
