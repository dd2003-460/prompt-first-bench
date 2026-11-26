# T8c smoke 重跑 · 中期观察（run 未完，eval 前读）

# origin: ai · 2026-11-26 23:45 · pid 1383 仍在跑（10min+）

## repeat5（疑似复读循环指标）中期分布

| 臂 | rep | repeat5 | content 字符 |
|---|---|---|---|
| A direct | run1 | 6 | 2327 |
| A direct | run2 | 7 | 4326 |
| A direct | run3 | 8 | 3207 |
| B pfb run1 | 01/02/02.5/03/04 | 4/5/5/4/4 | 1095/4985/5596/3370/4678 |
| B pfb run1 | 04 末 | 2 | 3252 |
| B pfb run2 | 01/02/02.5/03/04 | 7/5/3/6/11 | 156/4901/8199/3915/4756 |

## 信号（待 eval 确认，非结论）

1. **B run1 复读率（均值~4）< A（均值~7）**——流程臂首 rep 复读更少，方向与"流程价值"claim 一致。
2. **B run2 复读率爬升（3→11）**：rep 内单调恶化，且 run2-01 content=156 字符 + repeat5=7 = 退化短输出。
   若 run3 继续爬升 → "流程臂复读随 rep 累积"是新现象（A 臂 3 rep 内 6→8 也在缓升，需对照斜率）。
3. A 臂 repeat5 也随 rep 升（6→7→8）——复读随 rep 累积可能是 27b 端点级现象，不是臂特异。
   **eval 时按臂算斜率（repeat5 vs rep 序号），不只看均值。**

## eval 提醒

- judge 同族限制：仅臂间相对有效（prereg 已声明）
- 复读警告行（WARNING: 疑似复读循环）是 run_exp_t8c.py 打的，阈值 repeat5≥5
- 日志：exp-results/t8c-smoke-rerun-20261126-232615.log（raw，勿混入笔记）
