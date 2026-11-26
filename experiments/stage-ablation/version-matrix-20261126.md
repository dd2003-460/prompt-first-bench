# 消融矩阵 arm×qid（v2，脚本生成）

生成: matrix2.py @ 2026-11-26 22:17 · 扫描 676 个分数文件（排除 checkpoints/、*.log、*.lock、>1MB）· 成功解析 676 · 字段映射 arm/qid/total（probe 2026-11-26 确认）

| arm \ qid | Q1 | Q2 | Q3 | Q4 | Q5 | Q8 | Q9 |
|---|---|---|---|---|---|---|---|
| **Arena** | 0.67(n=1, j=Arena-Q1-r1) / 13.00(n=1, j=v3-secondary) | 19.00(n=1, j=v3-secondary) | 0.56(n=1, j=Arena-Q3-r1) / 15.00(n=1, j=v3-secondary) | — | — | — | — |
| **D1** | 0.54(n=3, j=d1-rep15-v2(rubric=v2)) | — | 0.53(n=3, j=d1-rep15-v2(rubric=v2)) | 0.50(n=3, j=d1-rep15-v2(rubric=v2)) | — | 0.61(n=3, j=d1-rep15-v2(rubric=v2)) | 0.33(n=3, j=d1-rep15-v2(rubric=v2)) |
| **S0** | 0.48(n=3, j=final) / 0.75(n=3, j=m7-results) / 0.48(n=3, j=r293) / 0.41(n=3, j=v2) / 0.58(n=3, j=v3) / 9.33(n=3, j=v3-expansion) / 5.33(n=3, j=v3-m1-fixed) | 0.46(n=3, j=final) / 0.11(n=3, j=m7-results) / 0.46(n=3, j=r293) / 0.38(n=3, j=v2) / 0.45(n=3, j=v3) / 8.67(n=3, j=v3-expansion) / 3.00(n=3, j=v3-m1-fixed) | 0.50(n=3, j=final) / 0.00(n=3, j=m7-results) / 0.50(n=3, j=r293) / 0.61(n=3, j=v2) / 0.69(n=3, j=v3) / 10.67(n=3, j=v3-expansion) / 3.00(n=3, j=v3-m1-fixed) | 0.46(n=3, j=Q4-fixed) / 0.46(n=3, j=final) / 0.11(n=3, j=m7-results) / 0.45(n=3, j=r293) / 0.57(n=3, j=v2) / 0.69(n=3, j=v3) / 11.00(n=4, j=v3-expansion) | 0.56(n=3, j=final) / 0.56(n=3, j=m7-results) / 0.56(n=3, j=r293) / 0.61(n=3, j=v2) / 0.66(n=3, j=v3) / 2.00(n=3, j=v3-expansion) | — | — |
| **S1** | 0.54(n=3, j=final) / 0.50(n=3, j=m7-results) / 0.54(n=3, j=r293) / 0.53(n=3, j=v2) / 0.56(n=3, j=v3) / 7.67(n=3, j=v3-expansion) | 0.70(n=3, j=final) / 0.33(n=3, j=m7-results) / 0.70(n=3, j=r293) / 0.65(n=3, j=v2) / 0.64(n=3, j=v3) / 11.50(n=2, j=v3-expansion) | 0.67(n=3, j=final) / 0.00(n=3, j=m7-results) / 0.67(n=3, j=r293) / 0.62(n=3, j=v2) / 0.67(n=3, j=v3) | 0.45(n=3, j=Q4-fixed) / 0.45(n=3, j=final) / 0.00(n=3, j=m7-results) / 0.55(n=3, j=r293) / 0.44(n=3, j=v2) / 0.65(n=3, j=v3) | 0.67(n=3, j=final) / 0.44(n=3, j=m7-results) / 0.67(n=3, j=r293) / 0.62(n=3, j=v2) / 0.62(n=3, j=v3) | — | — |
| **S10-A** | 0.37(n=6, j=s10) / 0.34(n=6, j=s10-scores-v2(rubric=v2)) | — | 0.47(n=6, j=s10) / 0.56(n=6, j=s10-scores-v2(rubric=v2)) | 0.44(n=6, j=s10) / 0.49(n=6, j=s10-scores-v2(rubric=v2)) | — | — | — |
| **S10-B** | 0.63(n=6, j=s10) / 0.49(n=6, j=s10-scores-v2(rubric=v2)) | — | 0.79(n=6, j=s10) / 0.66(n=6, j=s10-scores-v2(rubric=v2)) | 0.82(n=6, j=s10) / 0.62(n=6, j=s10-scores-v2(rubric=v2)) | — | — | — |
| **S10-C** | 0.60(n=6, j=s10) / 0.48(n=6, j=s10-scores-v2(rubric=v2)) | — | 0.74(n=6, j=s10) / 0.64(n=6, j=s10-scores-v2(rubric=v2)) | 0.78(n=6, j=s10) / 0.27(n=6, j=s10-scores-v2(rubric=v2)) | — | — | — |
| **S10-D** | 0.63(n=6, j=s10) / 0.26(n=6, j=s10-scores-v2(rubric=v2)) | — | 0.79(n=6, j=s10) / 0.39(n=6, j=s10-scores-v2(rubric=v2)) | 0.83(n=6, j=s10) / 0.33(n=6, j=s10-scores-v2(rubric=v2)) | — | — | — |
| **S10-E** | 0.64(n=6, j=s10) / 0.44(n=6, j=s10-scores-v2(rubric=v2)) | — | 0.83(n=6, j=s10) / 0.48(n=6, j=s10-scores-v2(rubric=v2)) | 0.77(n=6, j=s10) / 0.28(n=6, j=s10-scores-v2(rubric=v2)) | — | — | — |
| **S2** | 0.83(n=3, j=m7-results) | 0.11(n=3, j=m7-results) | 0.00(n=3, j=m7-results) | 0.11(n=3, j=m7-results) | 0.56(n=3, j=m7-results) | — | — |
| **S3** | 0.83(n=3, j=m7-results) | 0.11(n=3, j=m7-results) | 0.00(n=3, j=m7-results) | 0.11(n=3, j=m7-results) | 0.44(n=3, j=m7-results) | — | — |
| **S4** | 0.58(n=3, j=m7-results) | 0.00(n=3, j=m7-results) | 0.11(n=3, j=m7-results) | 0.11(n=3, j=m7-results) | 0.44(n=3, j=m7-results) | — | — |
| **S5** | 0.74(n=3, j=final) / 0.83(n=3, j=m7-results) / 0.74(n=3, j=r293) / 0.43(n=3, j=s5(rubric=v2)) / 0.62(n=3, j=v2) / 0.83(n=3, j=v3) | 0.71(n=3, j=final) / 0.11(n=3, j=m7-results) / 0.71(n=3, j=r293) / 0.60(n=6, j=s5(rubric=v2)) / 0.66(n=3, j=v2) / 0.78(n=3, j=v3) | 0.68(n=3, j=final) / 0.00(n=3, j=m7-results) / 0.68(n=3, j=r293) / 0.58(n=6, j=s5(rubric=v2)) / 0.75(n=3, j=v2) / 0.81(n=3, j=v3) | 0.67(n=3, j=Q4-fixed) / 0.67(n=3, j=final) / 0.00(n=3, j=m7-results) / 0.66(n=3, j=r293) / 0.54(n=6, j=s5(rubric=v2)) / 0.55(n=3, j=v2) / 0.86(n=3, j=v3) | 0.77(n=3, j=final) / 0.44(n=3, j=m7-results) / 0.77(n=3, j=r293) / 0.60(n=6, j=s5(rubric=v2)) / 0.57(n=3, j=v2) / 0.74(n=3, j=v3) | — | — |
| **S6** | 0.73(n=3, j=hetero-judge-s6s7-results) | 0.60(n=3, j=hetero-judge-s6s7-results) | 0.55(n=3, j=hetero-judge-s6s7-results) | 0.55(n=3, j=hetero-judge-s6s7-results) | 0.70(n=3, j=hetero-judge-s6s7-results) | — | — |
| **S7** | 0.80(n=3, j=hetero-judge-s6s7-results) | 0.70(n=3, j=hetero-judge-s6s7-results) | 0.55(n=3, j=hetero-judge-s6s7-results) | 0.78(n=3, j=hetero-judge-s6s7-results) | 0.70(n=3, j=hetero-judge-s6s7-results) | — | — |
| **S7F** | 0.55(n=1, j=S7F-Q1-r1) | — | — | 0.54(n=1, j=S7F-Q4-r1) | 0.67(n=1, j=S7F-Q5-r1) | — | — |
| **S7V** | 0.42(n=1, j=S7V-Q1-r1) | — | — | 0.64(n=1, j=S7V-Q4-r1) | 0.83(n=1, j=S7V-Q5-r1) | — | — |
| **S8A** | — | 0.55(n=1, j=v3-secondary) | — | — | — | — | — |
| **S8B** | — | 0.53(n=1, j=v3-secondary) | — | — | — | — | — |
| **S8C** | — | 0.71(n=1, j=v3-secondary) | — | — | — | — | — |
| **S8D** | 0.59(n=1, j=S8D) / 0.72(n=1, j=v3-secondary) | 0.45(n=3, j=S8D) / 0.73(n=3, j=v3-secondary) | 0.48(n=1, j=S8D) / 0.60(n=1, j=v3-secondary) | 0.47(n=1, j=S8D) / 0.70(n=1, j=v3-secondary) | 0.60(n=1, j=S8D) / 0.83(n=1, j=v3-secondary) | — | — |
| **S8E** | — | 0.62(n=3, j=v3-secondary) | — | — | — | — | — |
| **S8G** | 0.84(n=1, j=S8G-Q1-r1) / 0.74(n=1, j=S8G-Q1-r2) | — | — | 0.73(n=1, j=S8G-Q4-r1) / 0.75(n=1, j=S8G-Q4-r2) | 0.69(n=1, j=S8G-r1) / 0.79(n=1, j=S8G-r2) / 0.83(n=1, j=S8G-r3) / 0.82(n=1, j=S8G-r4) / 0.85(n=1, j=S8G-r5) / 3.00(n=1, j=v3-secondary) | — | — |
| **T2** | 0.62(n=3, j=t2) / 0.67(n=3, j=t2-scores-withhook) | 0.65(n=3, j=t2) / 0.70(n=3, j=t2-scores-withhook) | 0.64(n=3, j=t2) / 0.83(n=3, j=t2-scores-withhook) | 0.64(n=3, j=t2) / 0.72(n=3, j=t2-scores-withhook) | 0.69(n=3, j=t2) / 0.78(n=3, j=t2-scores-withhook) | — | — |

## judge 漂移格

同 (arm,qid) 多 judge_tag 且均值差 > 0.05 的格子（judge 漂移 = 本矩阵关键输出）：

| arm | qid | 各 judge_tag 均值 |
|---|---|---|
| Arena | Q1 | Arena-Q1-r1=0.67 / v3-secondary=13.00 |
| Arena | Q3 | Arena-Q3-r1=0.56 / v3-secondary=15.00 |
| S0 | Q1 | final=0.48 / m7-results=0.75 / r293=0.48 / v2=0.41 / v3=0.58 / v3-expansion=9.33 / v3-m1-fixed=5.33 |
| S0 | Q2 | final=0.46 / m7-results=0.11 / r293=0.46 / v2=0.38 / v3=0.45 / v3-expansion=8.67 / v3-m1-fixed=3.00 |
| S0 | Q3 | final=0.50 / m7-results=0.00 / r293=0.50 / v2=0.61 / v3=0.69 / v3-expansion=10.67 / v3-m1-fixed=3.00 |
| S0 | Q4 | Q4-fixed=0.46 / final=0.46 / m7-results=0.11 / r293=0.45 / v2=0.57 / v3=0.69 / v3-expansion=11.00 |
| S0 | Q5 | final=0.56 / m7-results=0.56 / r293=0.56 / v2=0.61 / v3=0.66 / v3-expansion=2.00 |
| S1 | Q1 | final=0.54 / m7-results=0.50 / r293=0.54 / v2=0.53 / v3=0.56 / v3-expansion=7.67 |
| S1 | Q2 | final=0.70 / m7-results=0.33 / r293=0.70 / v2=0.65 / v3=0.64 / v3-expansion=11.50 |
| S1 | Q3 | final=0.67 / m7-results=0.00 / r293=0.67 / v2=0.62 / v3=0.67 |
| S1 | Q4 | Q4-fixed=0.45 / final=0.45 / m7-results=0.00 / r293=0.55 / v2=0.44 / v3=0.65 |
| S1 | Q5 | final=0.67 / m7-results=0.44 / r293=0.67 / v2=0.62 / v3=0.62 |
| S10-A | Q3 | s10=0.47 / s10-scores-v2(rubric=v2)=0.56 |
| S10-A | Q4 | s10=0.44 / s10-scores-v2(rubric=v2)=0.49 |
| S10-B | Q1 | s10=0.63 / s10-scores-v2(rubric=v2)=0.49 |
| S10-B | Q3 | s10=0.79 / s10-scores-v2(rubric=v2)=0.66 |
| S10-B | Q4 | s10=0.82 / s10-scores-v2(rubric=v2)=0.62 |
| S10-C | Q1 | s10=0.60 / s10-scores-v2(rubric=v2)=0.48 |
| S10-C | Q3 | s10=0.74 / s10-scores-v2(rubric=v2)=0.64 |
| S10-C | Q4 | s10=0.78 / s10-scores-v2(rubric=v2)=0.27 |
| S10-D | Q1 | s10=0.63 / s10-scores-v2(rubric=v2)=0.26 |
| S10-D | Q3 | s10=0.79 / s10-scores-v2(rubric=v2)=0.39 |
| S10-D | Q4 | s10=0.83 / s10-scores-v2(rubric=v2)=0.33 |
| S10-E | Q1 | s10=0.64 / s10-scores-v2(rubric=v2)=0.44 |
| S10-E | Q3 | s10=0.83 / s10-scores-v2(rubric=v2)=0.48 |
| S10-E | Q4 | s10=0.77 / s10-scores-v2(rubric=v2)=0.28 |
| S5 | Q1 | final=0.74 / m7-results=0.83 / r293=0.74 / s5(rubric=v2)=0.43 / v2=0.62 / v3=0.83 |
| S5 | Q2 | final=0.71 / m7-results=0.11 / r293=0.71 / s5(rubric=v2)=0.60 / v2=0.66 / v3=0.78 |
| S5 | Q3 | final=0.68 / m7-results=0.00 / r293=0.68 / s5(rubric=v2)=0.58 / v2=0.75 / v3=0.81 |
| S5 | Q4 | Q4-fixed=0.67 / final=0.67 / m7-results=0.00 / r293=0.66 / s5(rubric=v2)=0.54 / v2=0.55 / v3=0.86 |
| S5 | Q5 | final=0.77 / m7-results=0.44 / r293=0.77 / s5(rubric=v2)=0.60 / v2=0.57 / v3=0.74 |
| S8D | Q1 | S8D=0.59 / v3-secondary=0.72 |
| S8D | Q2 | S8D=0.45 / v3-secondary=0.73 |
| S8D | Q3 | S8D=0.48 / v3-secondary=0.60 |
| S8D | Q4 | S8D=0.47 / v3-secondary=0.70 |
| S8D | Q5 | S8D=0.60 / v3-secondary=0.83 |
| S8G | Q1 | S8G-Q1-r1=0.84 / S8G-Q1-r2=0.74 |
| S8G | Q5 | S8G-r1=0.69 / S8G-r2=0.79 / S8G-r3=0.83 / S8G-r4=0.82 / S8G-r5=0.85 / v3-secondary=3.00 |
| T2 | Q1 | t2=0.62 / t2-scores-withhook=0.67 |
| T2 | Q2 | t2=0.65 / t2-scores-withhook=0.70 |
| T2 | Q3 | t2=0.64 / t2-scores-withhook=0.83 |
| T2 | Q4 | t2=0.64 / t2-scores-withhook=0.72 |
| T2 | Q5 | t2=0.69 / t2-scores-withhook=0.78 |

## 数据缺口

空单元格（82/168）：

- Arena × Q4
- Arena × Q5
- Arena × Q8
- Arena × Q9
- D1 × Q2
- D1 × Q5
- S0 × Q8
- S0 × Q9
- S1 × Q8
- S1 × Q9
- S10-A × Q2
- S10-A × Q5
- S10-A × Q8
- S10-A × Q9
- S10-B × Q2
- S10-B × Q5
- S10-B × Q8
- S10-B × Q9
- S10-C × Q2
- S10-C × Q5
- S10-C × Q8
- S10-C × Q9
- S10-D × Q2
- S10-D × Q5
- S10-D × Q8
- S10-D × Q9
- S10-E × Q2
- S10-E × Q5
- S10-E × Q8
- S10-E × Q9
- S2 × Q8
- S2 × Q9
- S3 × Q8
- S3 × Q9
- S4 × Q8
- S4 × Q9
- S5 × Q8
- S5 × Q9
- S6 × Q8
- S6 × Q9
- S7 × Q8
- S7 × Q9
- S7F × Q2
- S7F × Q3
- S7F × Q8
- S7F × Q9
- S7V × Q2
- S7V × Q3
- S7V × Q8
- S7V × Q9
- S8A × Q1
- S8A × Q3
- S8A × Q4
- S8A × Q5
- S8A × Q8
- S8A × Q9
- S8B × Q1
- S8B × Q3
- S8B × Q4
- S8B × Q5
- S8B × Q8
- S8B × Q9
- S8C × Q1
- S8C × Q3
- S8C × Q4
- S8C × Q5
- S8C × Q8
- S8C × Q9
- S8D × Q8
- S8D × Q9
- S8E × Q1
- S8E × Q3
- S8E × Q4
- S8E × Q5
- S8E × Q8
- S8E × Q9
- S8G × Q2
- S8G × Q3
- S8G × Q8
- S8G × Q9
- T2 × Q8
- T2 × Q9

解析失败文件（0）：

（无）

跳过记录数：缺 arm=114 · 缺 qid=180 · 缺 score=1046（合计 1340）

## judge 版本清单

| judge_tag | 覆盖文件数 | rubric 值 |
|---|---|---|
| Arena-Q1-r1 | 1 | — |
| Arena-Q3-r1 | 1 | — |
| Q4-fixed | 1 | — |
| S7F-Q1-r1 | 1 | — |
| S7F-Q4-r1 | 1 | — |
| S7F-Q5-r1 | 1 | — |
| S7V-Q1-r1 | 1 | — |
| S7V-Q4-r1 | 1 | — |
| S7V-Q5-r1 | 1 | — |
| S8D | 1 | — |
| S8G-Q1-r1 | 1 | — |
| S8G-Q1-r2 | 1 | — |
| S8G-Q4-r1 | 1 | — |
| S8G-Q4-r2 | 1 | — |
| S8G-r1 | 1 | — |
| S8G-r2 | 1 | — |
| S8G-r3 | 1 | — |
| S8G-r4 | 1 | — |
| S8G-r5 | 1 | — |
| d1-rep15-v2 | 1 | v2 |
| final | 1 | — |
| hetero-judge-s6s7-results | 1 | — |
| m7-results | 1 | — |
| r293 | 1 | — |
| s10 | 1 | — |
| s10-scores-v2 | 1 | v2 |
| s5 | 1 | v2 |
| t2 | 1 | — |
| t2-scores-withhook | 1 | — |
| v2 | 1 | — |
| v3 | 1 | — |
| v3-expansion | 1 | — |
| v3-m1-fixed | 1 | — |
| v3-secondary | 1 | — |

## 未解析结构

- `experiments/stage-ablation/J-drb-2-reverified.json` — 顶层键: B_in_band, B_ratio, C_expand, C_transmit_tokens, D_T_nat, H_star_nat, I, J, S_alpha_prime, _invalid, _invalid_at, _invalid_reason, cov, delta_nat, delta_over_Hstar, n_nodes, note, per_node_info_gain, qid, run, status_dist
- `experiments/stage-ablation/J-gpu.json` — 顶层键: B_in_band, B_ratio, C_expand, C_transmit_tokens, D_T_nat, H_star_nat, H_star_source, I, J, S_alpha_prime, cov, cov_hits, delta_nat, delta_over_Hstar, n_nodes, note, per_node_info_gain, qid, run, status_dist
- `experiments/stage-ablation/alignment-inputs.json` — 顶层键: arena_claims_checked, arena_m1, arm, local_m1, q, run
- `experiments/stage-ablation/arena-judge-s6s7-pack.json` — 顶层键: gold, runs
- `experiments/stage-ablation/arm-profiles-20261113.json` — 顶层键: arms, comparison, generated_at, note
- `experiments/stage-ablation/bootstrap-cis.json` — 顶层键: ci_level, m7, method, paired_s7v_vs_s7, s0_s5, s6_s7_m1m4
- `experiments/stage-ablation/cross-judge-results.json` — 顶层键: arm, claims_checked, local_m1, notes, perplexity_m1, qid, rep, tag, timestamp
- `experiments/stage-ablation/g9-independence-gpu.json` — 顶层键: n_dims, pairs, qid, timestamp
- `experiments/stage-ablation/g9-independence-nat.json` — 顶层键: n_dims, pairs, qid, timestamp
- `experiments/stage-ablation/g9-independence-soc.json` — 顶层键: n_dims, pairs, qid, timestamp
- `experiments/stage-ablation/monitor-state.json` — 顶层键: cc_state, log, process, status, synth, watcher
- `experiments/stage-ablation/p5-cdf-backlabel.json` — 顶层键: empirical_cdf, max, mean, min, n, note, recommendation, samples, std_pop
- `experiments/stage-ablation/raw-data-full-perdim.json` — 顶层键: arena_m1_per_run, local_gatefixed_per_run, meta, semihetero_7b_per_dim, t23v2_arm_summary
- `experiments/stage-ablation/replay_p3_results.json` — 顶层键: claim, n_srcs, new, new_ev, node, old, old_ev, rep
- `experiments/stage-ablation/runs-langgraph-pfb-gpu.json` — 顶层键: S_alpha_corr, contradiction_events, degraded, elapsed_s, leak_hits_total, nodes, objective, qid, question, rework_events, rounds, rounds_log, stop_reason, total_nodes, verified, verified_rate
- `experiments/stage-ablation/runs-langgraph-pfb-nat.json` — 顶层键: S_alpha_corr, elapsed_s, nodes, qid, recovery_note, rounds, stop_reason, total_nodes, verified, verified_rate
- `experiments/stage-ablation/runs-s5-sm-drb-1.json` — 顶层键: final_state, leak_hits, n_nodes, n_rounds, nodes, qid, rework_events, rounds
- `experiments/stage-ablation/runs-s5-sm-drb-2-checkpoint.json` — 顶层键: dropped_redundant, leak_hits_total, network_degraded, nodes, objective, qid, rework_events, round
- `experiments/stage-ablation/runs-s5-sm-drb-2-reverified.json` — 顶层键: final_state, leak_hits, n_nodes, n_rounds, nodes, objective, qid, question, rework_events, rounds
- `experiments/stage-ablation/runs-s5-sm-drb-2.json` — 顶层键: final_state, leak_hits, n_nodes, n_rounds, nodes, objective, qid, question, rework_events, rounds
- `experiments/stage-ablation/runs-s5-sm-gpu-formula-r2.json` — 顶层键: final_state, leak_hits, n_nodes, n_rounds, nodes, objective, objective_mode, qid, question, rework_events, rounds
- `experiments/stage-ablation/runs-s5-sm-gpu-synth.json` — 顶层键: answer, coverage, depth_score, final_state, judge, n_nodes, qid, source_run
- `experiments/stage-ablation/runs-s5-sm-gpu-textarm-r2.json` — 顶层键: contradiction_events, dropped_redundant, leak_hits_total, network_degraded, nodes, objective, objective_mode, qid, question, rework_events, round, state
- `experiments/stage-ablation/runs-s5-sm-gpu-textarm-seed.json` — 顶层键: contradiction_events, dropped_redundant, leak_hits_total, network_degraded, nodes, objective, objective_mode, qid, question, rework_events, round, state
- `experiments/stage-ablation/runs-s5-sm-gpu.json` — 顶层键: final_state, leak_hits, n_nodes, n_rounds, nodes, objective, qid, question, rework_events, rounds
- `experiments/stage-ablation/runs-s5-sm-nat-checkpoint.json` — 顶层键: contradiction_events, dropped_redundant, leak_hits_total, network_degraded, nodes, objective, objective_mode, qid, rework_events, round
- `experiments/stage-ablation/runs-s5-sm-nat-synth-multi.json` — 顶层键: baseline, covs, depths, gate, gate_pass, hflags, mean, n, qid, sd, valid, wall_s
- `experiments/stage-ablation/runs-s5-sm-nat-synth.json` — 顶层键: answer, coverage, depth_score, final_state, judge, n_nodes, qid, source_run
- `experiments/stage-ablation/runs-s5-sm-nat.json` — 顶层键: final_state, leak_hits, n_nodes, n_rounds, nodes, objective, qid, question, rework_events, rounds
- `experiments/stage-ablation/runs-s5-sm-q6-nev.json` — 顶层键: blocked_reason, channel_probe, harness_cmd, honesty_note, leak_check, qid, question_ref, question_sha1, question_text_in_record, runs_executed, scores, status, task_book, topic
- `experiments/stage-ablation/runs-s5-sm-q7-checkpoint.json` — 顶层键: challenge_log, contradiction_events, dropped_redundant, leak_hits_total, network_degraded, nodes, objective, objective_mode, qid, rework_events, round
- `experiments/stage-ablation/runs-s5-sm-q7-rd.json` — 顶层键: blocked_reason, channel_probe, harness_cmd, honesty_note, leak_check, qid, question_ref, question_sha1, question_text_in_record, runs_executed, scores, status, task_book, topic
- `experiments/stage-ablation/runs-s5-sm-q7.json` — 顶层键: final_state, leak_hits, n_nodes, n_rounds, nodes, objective, qid, question, rework_events, rounds
- `experiments/stage-ablation/runs-s5-sm-q8-nvda.json` — 顶层键: blocked_reason, channel_probe, harness_cmd, honesty_note, leak_check, qid, question_ref, question_sha1, question_text_in_record, runs_executed, scores, status, task_book, topic
- `experiments/stage-ablation/runs-s5-sm-soc-checkpoint.json` — 顶层键: contradiction_events, dropped_redundant, leak_hits_total, network_degraded, nodes, objective, objective_mode, qid, rework_events, round
- `experiments/stage-ablation/runs-s5-sm-soc-synth-multi.json` — 顶层键: baseline, covs, depths, gate, gate_pass, hflags, mean, n, sd, valid, wall_s
- `experiments/stage-ablation/runs-s5-sm-soc-synth.json` — 顶层键: answer, coverage, depth_score, final_state, judge, n_nodes, qid, source_run
- `experiments/stage-ablation/runs-s5-sm-soc.json` — 顶层键: final_state, leak_hits, n_nodes, n_rounds, nodes, objective, qid, question, rework_events, rounds
- `experiments/stage-ablation/s10-batch-1.json` — 顶层键: batch, instructions, samples, total_batches
- `experiments/stage-ablation/s10-batch-2.json` — 顶层键: batch, instructions, samples, total_batches
- `experiments/stage-ablation/s10-batch-3.json` — 顶层键: batch, instructions, samples, total_batches
- `experiments/stage-ablation/s10-batch-4.json` — 顶层键: batch, instructions, samples, total_batches
- `experiments/stage-ablation/s10-batch-5.json` — 顶层键: batch, instructions, samples, total_batches
- `experiments/stage-ablation/s10-blind-packet-v2.json` — 顶层键: date, formula, label_mapping, n_samples, prompt_char_count, question_id, rubric_version, task
- `experiments/stage-ablation/s10-blind-packet.json` — 顶层键: instructions, samples, task
- `experiments/stage-ablation/s10-hetero-scores-raw.json` — 顶层键: line, model
- `experiments/stage-ablation/s10-hetero-scores-v2-raw.json` — 顶层键: agreement, arena_conversation, arm_means, date, judge_A, judge_B, label_mapping, n_samples, question_id, rubric_version, task
- `experiments/stage-ablation/s10-run-summary.json` — 顶层键: arm, final_len, n_sources, qid, r2_substantive_fail, rep
- `experiments/stage-ablation/s8e-scores.json` — 顶层键: arm, local_m1, local_m4, m1_detail, qid, rep, tag, wall_s
- `experiments/stage-ablation/sm-gpu-formula-resume-ckpt.json` — 顶层键: dropped_redundant, final_state, leak_hits, n_nodes, n_rounds, network_degraded, nodes, objective, qid, question, rework_events, round, rounds
- `experiments/stage-ablation/verify-results.json` — 顶层键: results, summary
- `experiments/stage-ablation/hetero-scores-semihetero.jsonl` — 顶层键: arm, artifact, confidence, dim, evidence, qid, score
- `experiments/stage-ablation/runs-r293/Arena-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/Arena-Q3-r2.json` — 顶层键: M1, M1_matched, M1_note, M1_total_decidable, gold, gold_type, source
- `experiments/stage-ablation/runs-r293/Arena-Q4-r1.json` — 顶层键: M1, M1_matched, M1_note, M1_total_decidable, gold, gold_type, source
- `experiments/stage-ablation/runs-r293/Arena-Q5-r1.json` — 顶层键: M1, M1_matched, M1_note, M1_total_decidable, gold, gold_type, source
- `experiments/stage-ablation/runs-r293/Q4fix-S0-Q4-r1.json` — 顶层键: arm, model, note, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q1-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q1-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q1-r6.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q2-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q2-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q2-r6.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q3-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q3-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q3-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q3-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q3-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q3-r6.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q4-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q4-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q4-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q4-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q4-r6.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q5-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q5-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S0-Q5-r6.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q1-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q1-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q1-r6.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q2-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q2-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q2-r6.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q3-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q3-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q3-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q3-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q3-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q3-r6.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q4-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q4-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q4-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q4-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q4-r6.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q5-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q5-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S1-Q5-r6.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q1-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q1-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q1-r6.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q2-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q2-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q2-r6.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q3-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q3-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q3-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q3-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q3-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q3-r6.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q4-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q4-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q4-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q4-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q4-r6.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q5-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q5-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S5-Q5-r6.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S7F-Q1-r1.json` — 顶层键: arm, model, note, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S7F-Q4-r1.json` — 顶层键: arm, model, note, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S7F-Q5-r1.json` — 顶层键: arm, model, note, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S7V-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S7V-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S7V-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8A-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8B-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8C-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8D-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8D-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8D-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8D-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8D-Q3-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8D-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8D-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8E-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8E-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8E-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8F-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8G-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8G-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8G-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8G-Q4-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8G-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8G-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8G-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8G-Q5-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/S8G-Q5-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs-r293/scores-Arena.json` — 顶层键: Arena-Q1-r1, Arena-Q2-r1, Arena-Q3-r1, Q3-r2, Q4, Q5
- `experiments/stage-ablation/runs-r293/stats-n30.json` — 顶层键: bootstrap_ci, caveat, judge, method, n_per_arm, paired_deltas
- `experiments/stage-ablation/runs-r293/stats-v3.json` — 顶层键: bootstrap_ci, caveat, judge, method, paired_deltas, per_metric
- `experiments/stage-ablation/runs/D1-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q3-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q3-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q3-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q4-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q4-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q8-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q8-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q8-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q9-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q9-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1-Q9-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1deep-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1deep-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/D1deep-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S0-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S0-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S0-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S0-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S0-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S0-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S0-Q3-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S0-Q3-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S0-Q3-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S0-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S0-Q4-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S0-Q4-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S0-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S0-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S0-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S1-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S1-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S1-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S1-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S1-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S1-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S1-Q3-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S1-Q3-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S1-Q3-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S1-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S1-Q4-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S1-Q4-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S1-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S1-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S1-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q1-r1-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q1-r2-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q2-r1-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q2-r2-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q3-r1-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q3-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q3-r2-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q3-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q3-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q4-r1-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q4-r2-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q4-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q4-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q5-r1-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q5-r2-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S2-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q1-r1-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q1-r2-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q2-r1-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q2-r2-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q3-r1-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q3-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q3-r2-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q3-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q3-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q4-r1-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q4-r2-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q4-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q4-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q5-r1-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q5-r2-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S3-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S4-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S4-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S4-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S4-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S4-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S4-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S4-Q3-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S4-Q3-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S4-Q3-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S4-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S4-Q4-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S4-Q4-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S4-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S4-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S4-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q1-r1-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q1-r2-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q2-r1-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q2-r2-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q2-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q2-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q2-r6.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q3-r1-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q3-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q3-r2-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q3-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q3-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q3-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q3-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q3-r6.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q4-r1-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q4-r2-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q4-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q4-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q4-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q4-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q4-r6.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q5-r1-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q5-r2-old.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q5-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q5-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S5-Q5-r6.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S6-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S6-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S6-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S6-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S6-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S6-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S6-Q3-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S6-Q3-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S6-Q3-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S6-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S6-Q4-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S6-Q4-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S6-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S6-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S6-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7-Q3-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7-Q3-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7-Q3-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7-Q4-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7-Q4-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7F-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7F-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7F-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7F-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7F-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7F-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7F-Q3-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7F-Q3-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7F-Q3-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7F-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7F-Q4-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7F-Q4-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7F-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7F-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7F-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7T-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7T-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7T-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7T-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7T-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7T-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7T-Q3-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7T-Q3-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7T-Q3-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7T-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7T-Q4-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7T-Q4-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7T-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7T-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7T-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7V-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7V-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7V-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7V-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7V-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7V-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7V-Q3-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7V-Q3-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7V-Q3-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7V-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7V-Q4-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7V-Q4-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7V-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7V-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S7V-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8-Q3-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8-Q3-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8-Q3-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8-Q4-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8-Q4-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8C-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8C-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8C-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8C-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8C-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8C-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8E-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8E-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8E-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8E-Q4-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8L-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8L-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8L-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8L-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8L-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8L-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8M-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8M-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8M-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8M-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8M-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8M-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/S8M-m1-bface-multi3.json` — 顶层键: arm, detail, m1_median, n_ok, qid, run
- `experiments/stage-ablation/runs/T0-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T0-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T0-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T0-Q1-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T0-Q1-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T0-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T0-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T0-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T0-Q2-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T0-Q2-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T1-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T1-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T1-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T1-Q1-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T1-Q1-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T1-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T1-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T1-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T1-Q2-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T1-Q2-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T2-Q1-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T2-Q1-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T2-Q1-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T2-Q1-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T2-Q1-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T2-Q2-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T2-Q2-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T2-Q2-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T2-Q2-r4.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T2-Q2-r5.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T2-Q3-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T2-Q3-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T2-Q3-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T2-Q4-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T2-Q4-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T2-Q4-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T2-Q5-r1.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T2-Q5-r2.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/T2-Q5-r3.json` — 顶层键: arm, model, output_text, params, qid, rep, sources, timestamp, tokens, wall_s
- `experiments/stage-ablation/runs/hetero-judge-q2q5-summary.json` — 顶层键: arm_question_rep, artifacts_scored, core_conclusion, cross_question_curve, extracted_at, five_deltas, hypotheses, judge, note, payload_sha256, push_status, r5_self_check, rubric, source_session
- `experiments/stage-ablation/runs/hetero-judge-v2-results.json` — 顶层键: arxiv_verification, curve, gate_defect, hypotheses, known_weaknesses, m6_key_findings, meta, per_arm_summary
- `experiments/stage-ablation/runs/m7-7b-clean.json` — 顶层键: M7_7b_clean, adjudications, arm, n_adjudications, qid, rep
- `experiments/stage-ablation/runs/m7-llm-judge-results.json` — 顶层键: M7_llm, adjudications, arm, qid, rep
- `experiments/stage-ablation/runs/arena-judge-results.jsonl` — 顶层键: claims_checked, claims_correct, m1, notes, tag
- `experiments/stage-ablation/runs/local-rerun-aligned.jsonl` — 顶层键: arm, claims_checked, claims_correct, m1, notes, qid, rep, tag, timestamp
- `experiments/stage-ablation/s10-runs/S10-A-Q1-r1.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-A-Q1-r2.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-A-Q1-r3.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-A-Q1-r4.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-A-Q1-r5.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-A-Q1-r6.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-A-Q3-r1.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-A-Q3-r2.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-A-Q3-r3.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-A-Q3-r4.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-A-Q3-r5.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-A-Q3-r6.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-A-Q4-r1.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-A-Q4-r2.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-A-Q4-r3.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-A-Q4-r4.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-A-Q4-r5.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-A-Q4-r6.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-B-Q1-r1-WITHTOOLS.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-B-Q1-r1.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-B-Q1-r2.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-B-Q1-r3.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-B-Q1-r4.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-B-Q1-r5.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-B-Q1-r6.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-B-Q3-r1.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-B-Q3-r2.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-B-Q3-r3.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-B-Q3-r4.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-B-Q3-r5.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-B-Q3-r6.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-B-Q4-r1.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-B-Q4-r2.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-B-Q4-r3.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-B-Q4-r4.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-B-Q4-r5.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-B-Q4-r6.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-C-Q1-r1.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-C-Q1-r2.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-C-Q1-r3.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-C-Q1-r4.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-C-Q1-r5.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-C-Q1-r6.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-C-Q3-r1.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-C-Q3-r2.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-C-Q3-r3.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-C-Q3-r4.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-C-Q3-r5.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-C-Q3-r6.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-C-Q4-r1.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-C-Q4-r2.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-C-Q4-r3.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-C-Q4-r4.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-C-Q4-r5.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-C-Q4-r6.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-D-Q1-r1.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-D-Q1-r2.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-D-Q1-r3.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-D-Q1-r4.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-D-Q1-r5.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-D-Q1-r6.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-D-Q3-r1.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-D-Q3-r2.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-D-Q3-r3.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-D-Q3-r4.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-D-Q3-r5.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-D-Q3-r6.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-D-Q4-r1.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-D-Q4-r2.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-D-Q4-r3.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-D-Q4-r4.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-D-Q4-r5.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-D-Q4-r6.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-E-Q1-r1.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-E-Q1-r2.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-E-Q1-r3.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-E-Q1-r4.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-E-Q1-r5.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-E-Q1-r6.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-E-Q3-r1.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-E-Q3-r2.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-E-Q3-r3.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-E-Q3-r4.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-E-Q3-r5.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-E-Q3-r6.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-E-Q4-r1.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-E-Q4-r2.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-E-Q4-r3.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-E-Q4-r4.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-E-Q4-r5.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/S10-E-Q4-r6.json` — 顶层键: arm, final, model, qid, rejections, rep, rounds, soothed, sources, timestamp
- `experiments/stage-ablation/s10-runs/e3-dual-track.json` — 顶层键: arm, delta, final_claims, final_m1, n_rounds, process_claims, process_m1, qid, rep, tag, timestamp
- `experiments/stage-ablation/optimize-T35/scores.json` — 顶层键: gold, judge, runs, scorer
- `experiments/stage-ablation/tasks/l4-audit-m1m4-results.jsonl` — 顶层键: alt_config_recommended, answer_len, arm, budget, class, file, group, loose_3090_in_tail, note, qid, rec_snippet, regex_bare3090_full, regex_full_combo, regex_strict_tail, rep, run
- `experiments/stage-ablation/runs-s5-gpu-v10/S5-gpu-r1.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v11/S5-gpu-r1.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v12/S5-gpu-r1.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r1.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r10.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r11.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r12.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r13.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r14.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r15.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r16.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r17.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r18.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r19.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r2.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r20.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r21.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r22.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r23.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r24.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r25.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r26.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r27.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r28.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r29.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r3.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r30.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r31.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r32.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r33.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r34.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r4.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r5.json` — 顶层键: answer, arm, depth_score, error, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r6.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r7.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r8.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v13/S5-gpu-r9.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v14/S5-gpu-r0.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v14/S5-gpu-r1.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v14/S5-gpu-r2.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v14/S5-gpu-r3.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v14/S5-gpu-r4.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v14/S5-gpu-r5.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v3/S5-gpu-r1.json` — 顶层键: answer, arm, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v4/S5-gpu-r1.json` — 顶层键: answer, arm, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v5/S5-gpu-r1.json` — 顶层键: answer, arm, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v6/S5-gpu-r1.json` — 顶层键: answer, arm, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v7/S5-gpu-r1.json` — 顶层键: answer, arm, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v8/S5-gpu-r1.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
- `experiments/stage-ablation/runs-s5-gpu-v9/S5-gpu-r1.json` — 顶层键: answer, arm, budget_used, depth_score, judge, label_stats, model, n_nodes, n_verified, qid, rep, stages, tag, ts, usage, wall_s
