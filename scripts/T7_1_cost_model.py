#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T7.1 会议室预约系统选型 — 成本模型（阶段 03 步骤 A1 + A3 的可复跑实现）

数据来源编号对应 loop-artifacts/stages/02/T7.1-02-research.md 的 S 编号，
未核验项对应该文件 §5 的 U 编号。本脚本不编造任何未核验价格：
不可核验的价格一律输出 null + reason，而不是猜测数字。

运行：python3 scripts/T7_1_cost_model.py
输出：outputs/T7.1-cost-model.json（并在 stdout 打印人类可读表）
"""
import json
import os
from datetime import datetime, timezone

OBSERVED_AT = "2026-10-28"
BUDGET_CNY_YEAR = 20000.0

# --- A1 汇率与预算基线（来源 S53 exchange-rates.org 2026-10-27, S54 macrotrends 2026-10-26）---
FX = {
    "pair": "USD->CNY",
    "base": 6.68,            # 计算基准（S53 6.6679 / S54 6.6781 取近似上沿）
    "observed_low": 6.6679,  # S53
    "observed_high": 6.6781, # S54
    "sensitivity_high": 6.75,  # 波动敏感性上界（显式假设，非观测值）
    "sources": ["S53", "S54"],
    "note": "EUR->CNY 未核验（U9），欧元标价不换算",
}

ROOM_SCENARIOS = [3, 5, 10]   # DA-1 默认 n=3，另给 5/10 敏感性

# --- 自托管估算参数（U18：R7 未执行，显式标注为估算-未核验）---
SELF_HOST = {
    "server_cny_year_low": 300,    # 估算-未核验
    "server_cny_year_high": 1200,  # 估算-未核验
    "ops_hours_year_low": 12,      # 估算-未核验
    "ops_hours_year_high": 24,     # 估算-未核验
    "ops_hourly_cny": 150,         # 估算-未核验（内部工时折算，DA-4 下不计入预算）
}


def cny(usd, fx=None):
    return round(usd * (fx or FX["base"]), 0)


def pct(v):
    return round(v / BUDGET_CNY_YEAR * 100, 1)


def build():
    out = {
        "task": "T7.1 30人团队会议室预约系统选型",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "observed_at": OBSERVED_AT,
        "budget": {
            "cny_year": BUDGET_CNY_YEAR,
            "cny_month": round(BUDGET_CNY_YEAR / 12, 2),
            "usd_year_at_base": round(BUDGET_CNY_YEAR / FX["base"], 2),
            "usd_month_at_base": round(BUDGET_CNY_YEAR / FX["base"] / 12, 2),
            "usd_year_at_sensitivity": round(BUDGET_CNY_YEAR / FX["sensitivity_high"], 2),
            "fx": FX,
        },
        "assumptions": {
            "DA-1": "会议室数 n 默认 3，另算 5 / 10",
            "DA-4": "口径=含税年度现金支出（订阅+硬件+服务器），内部运维工时单列不计入预算",
            "DA-6": "Skedda 适用 EMEA/APAC 价目（U8 未核验），美加价目作上界敏感性",
        },
        "candidates": [],
    }

    for n in ROOM_SCENARIOS:
        rows = []

        # C2 Skedda（S1 官方定价页，当日抓取）
        rows.append({
            "id": "C2-Skedda-APAC-Starter",
            "category": "C2 海外专用 SaaS",
            "pricing_model": "按档位含空间额度（$99/月含 15 空间，不限用户，年付）",
            "source": ["S1"],
            "annual_usd": 99 * 12,
            "annual_cny": cny(99 * 12),
            "budget_pct": pct(cny(99 * 12)),
            "fits_n": n <= 15,
            "unverified": ["U7 Integrations Pack 是否额外收费", "U8 中国大陆适用哪一区定价"],
        })
        rows.append({
            "id": "C2-Skedda-US-Plus（DA-6 被证伪时的上界）",
            "category": "C2 海外专用 SaaS",
            "pricing_model": "$249/月含 35 空间，年付",
            "source": ["S1"],
            "annual_usd": 249 * 12,
            "annual_cny": cny(249 * 12),
            "budget_pct": pct(cny(249 * 12)),
            "fits_n": n <= 35,
            "unverified": ["U7", "U8"],
        })

        # C2 Envoy（S9 官方 + 5 个独立二手）
        envoy_usd = 5 * 12 * n
        rows.append({
            "id": "C2-Envoy-Reservations",
            "category": "C2 海外专用 SaaS",
            "pricing_model": "$5/可预订资源/月（年付）+ 未公开 platform fee",
            "source": ["S9", "S21", "S22", "S23", "S26", "S34"],
            "annual_usd": envoy_usd,
            "annual_cny": cny(envoy_usd),
            "budget_pct": pct(cny(envoy_usd)),
            "total_cost_known": False,
            "unverified": ["U6 platform fee 金额未公开 → 总价不可核验"],
        })

        # C2 Whatspot（价格四源矛盾 → 区间）
        rows.append({
            "id": "C2-Whatspot-Premium",
            "category": "C2 海外专用 SaaS",
            "pricing_model": "按 spot 档位；日历同步需 Premium（单源 S19）",
            "source": ["S18", "S19", "S35", "S36"],
            "annual_usd_low": 25 * 12,
            "annual_usd_high": 30 * 12,
            "annual_cny_low": cny(25 * 12),
            "annual_cny_high": cny(30 * 12),
            "budget_pct_high": pct(cny(30 * 12)),
            "unverified": ["U4 官方页未抓取，4 个二手价格互相矛盾（X5）"],
        })

        # C5 Joan（S4 官方定价页当日抓取）
        joan_sw = 51 * 12
        rows.append({
            "id": "C5-Joan-软件部分",
            "category": "C5 门牌硬件+平台",
            "pricing_model": "$51/月起（含一定用户与设备额度）；额外用户 $1.09/月、额外设备 $10.99/月；经 Outlook/Google 预订的员工不计费",
            "source": ["S4"],
            "annual_usd": joan_sw,
            "annual_cny": cny(joan_sw),
            "budget_pct": pct(cny(joan_sw)),
            "hardware_capex_cny": None,
            "unverified": ["U10 面板硬件单价（竞品页单源 $399/台，未核验）", "起价所含用户/设备额度数量未在定价页写明"],
        })

        # C1 套件原生
        rows.append({
            "id": "C1-M365-房间邮箱/Places",
            "category": "C1 套件原生",
            "pricing_model": "预订会议室零许可证成本（S2 官方）；autorelease/占用分析需 space license",
            "source": ["S2", "S45"],
            "annual_cny": 0,
            "budget_pct": 0.0,
            "precondition": "组织已持有 Microsoft 365（G2 未确认）",
            "unverified": ["U11 Teams Shared Space License 价格（S43 称 $8.55/月，非官方价格页）"],
        })
        rows.append({
            "id": "C1-Google-Workspace-资源日历",
            "category": "C1 套件原生",
            "pricing_model": "Admin console 创建楼宇/会议室资源供日历预订（S3 官方）",
            "source": ["S3"],
            "annual_cny": 0,
            "budget_pct": 0.0,
            "precondition": "组织已持有 Google Workspace（G2 未确认）",
            "unverified": ["U1 版本门槛与是否零增量成本未在官方页核验"],
        })

        # C3 国内套件
        rows.append({
            "id": "C3-飞书会议室",
            "category": "C3 国内协同套件",
            "pricing_model": "会议室预定管理功能在基础版（免费）亦标注适用（S6 官方）；套餐价格未核验",
            "source": ["S6", "S7", "S8"],
            "annual_cny": None,
            "unverified": ["U3 套餐价格五源矛盾（X10）", "U2 会议室资源能否被外部 Google 日历用户预订（关键）"],
        })
        rows.append({
            "id": "C3-钉钉智能会议室",
            "category": "C3 国内协同套件",
            "pricing_model": "基础版疑似免费 / 高级版疑似 ¥498/间/年（两源矛盾，均非官网）",
            "source": ["S51", "S52"],
            "annual_cny": None,
            "annual_cny_if_advanced": 498 * n,
            "unverified": ["U12 收费口径矛盾（X9）", "无任何 Google Calendar 集成证据"],
        })
        rows.append({
            "id": "C3-企业微信+腾讯会议",
            "category": "C3 国内协同套件",
            "pricing_model": "未取得可核验的内置会议室预定能力与定价",
            "source": [],
            "annual_cny": None,
            "unverified": ["U13 2 次检索无官方来源"],
        })

        # C2 Robin（价格不可核验）
        rows.append({
            "id": "C2-Robin",
            "category": "C2 海外专用 SaaS",
            "pricing_model": "仅定制报价；二手价格 $4–35 互相矛盾",
            "source": ["S29", "S30", "S31", "S32", "S33"],
            "annual_cny": None,
            "unverified": ["U5 命中阶段 01 排除规则 X4（价格不可核验）"],
        })

        # C4 开源自托管
        for pid, releases, cal in [
            ("C4-MRBS", "v1.12.2 @2026-05-26 (S11)", "仅 iCal 导出，caldav 代码 0 命中 (S14/S15)"),
            ("C4-LibreBooking", "v7.1.0 @2026-10-13 (S12)", "iCal 导入+导出 (S16)"),
            ("C4-Seatsurfing", "v1.138.2 @2026-10-28 (S13)", "内建 CalDAV 客户端 (S13/S17)"),
        ]:
            rows.append({
                "id": pid,
                "category": "C4 开源自托管",
                "pricing_model": "软件零许可费（GPL）+ 服务器 + 运维工时",
                "source": ["S11", "S12", "S13", "S14", "S15", "S16", "S17"],
                "license_fee_cny": 0,
                "server_cny_year_range": [SELF_HOST["server_cny_year_low"], SELF_HOST["server_cny_year_high"]],
                "ops_cny_year_range": [
                    SELF_HOST["ops_hours_year_low"] * SELF_HOST["ops_hourly_cny"],
                    SELF_HOST["ops_hours_year_high"] * SELF_HOST["ops_hourly_cny"],
                ],
                "in_budget_cash_cny_range": [SELF_HOST["server_cny_year_low"], SELF_HOST["server_cny_year_high"]],
                "release_evidence": releases,
                "calendar_capability": cal,
                "unverified": ["U18 服务器年费与运维工时均为估算-未核验（R7 未执行）"],
            })

        out["candidates"].append({"rooms_n": n, "rows": rows})

    return out


def main():
    data = build()
    os.makedirs("outputs", exist_ok=True)
    path = os.path.join("outputs", "T7.1-cost-model.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    b = data["budget"]
    print("=== A1 预算基线 ===")
    print(f"预算 ¥{b['cny_year']:.0f}/年 = ¥{b['cny_month']:.2f}/月")
    print(f"汇率基准 1 USD = {FX['base']} CNY（S53 {FX['observed_low']} / S54 {FX['observed_high']}）")
    print(f"预算折美元 ≈ ${b['usd_year_at_base']:.2f}/年 ≈ ${b['usd_month_at_base']:.2f}/月")
    print(f"敏感性（1 USD = {FX['sensitivity_high']}）≈ ${b['usd_year_at_sensitivity']:.2f}/年")

    for block in data["candidates"]:
        print(f"\n=== A3 成本情景：会议室 n = {block['rooms_n']} ===")
        for r in block["rows"]:
            if r.get("annual_cny") is not None:
                val = f"¥{r['annual_cny']:.0f}/年（占预算 {r.get('budget_pct', 0)}%）"
            elif r.get("annual_cny_low") is not None:
                val = f"¥{r['annual_cny_low']:.0f}–{r['annual_cny_high']:.0f}/年（上界占 {r.get('budget_pct_high')}%）"
            elif r.get("in_budget_cash_cny_range"):
                lo, hi = r["in_budget_cash_cny_range"]
                val = f"现金 ¥{lo}–{hi}/年（估算-未核验）+ 工时 ¥{r['ops_cny_year_range'][0]}–{r['ops_cny_year_range'][1]}（不计入预算）"
            else:
                val = "不可核验（无公开价格）"
            flag = "" if r.get("fits_n", True) else "  [额度不足]"
            print(f"  - {r['id']:<42} {val}{flag}")
    print(f"\n已写入 {path}")


if __name__ == "__main__":
    main()
