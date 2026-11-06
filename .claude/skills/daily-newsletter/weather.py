#!/usr/bin/env python3
"""Cairo's forecast for the Weather section, from two services side by side so the figures are checked.

Usage:
  python3 .claude/skills/daily-newsletter/weather.py [DAYS]

Prints today and the next DAYS-1 days (default 4): high and low in °C, the sky, the chance of rain and the wind,
from Open-Meteo or, when it refuses (it has a shared daily limit), Norway's MET service, and from wttr.in. Write the
section from these numbers, not from a search result; where the two differ by more than 2°C, give a range or say so.
"""
import datetime
import json
import sys
import urllib.request
from collections import defaultdict

LAT, LON = 30.0444, 31.2357
UA = "DailyNewsletter/1.0 github.com/omarelabd318/daily-newsletter"
CAIRO = datetime.timezone(datetime.timedelta(hours=2))   # Egypt keeps UTC+2 in winter; summer time is UTC+3
WMO = {0: "clear", 1: "mostly clear", 2: "partly cloudy", 3: "cloudy", 45: "fog", 48: "fog", 51: "light drizzle", 53: "drizzle",
       55: "drizzle", 61: "light rain", 63: "rain", 65: "heavy rain", 71: "snow", 80: "showers", 81: "showers", 82: "heavy showers",
       95: "thunderstorms", 96: "thunderstorms with hail", 99: "thunderstorms with hail"}


def get(url):
    return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=25).read())


def open_meteo(n):
    j = get(f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&daily=temperature_2m_max,temperature_2m_min,"
            f"weather_code,precipitation_probability_max,wind_speed_10m_max&timezone=Africa%2FCairo&forecast_days={n}")
    if j.get("error"):
        raise RuntimeError(j.get("reason"))
    d = j["daily"]
    return [{"date": d["time"][i], "high": round(d["temperature_2m_max"][i]), "low": round(d["temperature_2m_min"][i]),
             "sky": WMO.get(d["weather_code"][i], "mixed"), "rain": d["precipitation_probability_max"][i],
             "wind": round(d["wind_speed_10m_max"][i])} for i in range(len(d["time"]))]


def met_norway(n):
    j = get(f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={LAT:.2f}&lon={LON:.2f}")
    by = defaultdict(lambda: {"t": [], "sky": [], "wind": []})
    for p in j["properties"]["timeseries"]:
        t = datetime.datetime.fromisoformat(p["time"].replace("Z", "+00:00")).astimezone(CAIRO)
        det = p["data"]["instant"]["details"]
        b = by[t.date().isoformat()]
        b["t"].append(det["air_temperature"])
        b["wind"].append(det.get("wind_speed", 0) * 3.6)
        sym = ((p["data"].get("next_6_hours") or p["data"].get("next_1_hours") or {}).get("summary") or {}).get("symbol_code")
        if sym and 9 <= t.hour <= 18:
            b["sky"].append(sym.split("_")[0].replace("fair", "mostly clear").replace("clearsky", "clear").replace("partlycloudy", "partly cloudy"))
    out = []
    for day in sorted(by)[:n]:
        b = by[day]
        out.append({"date": day, "high": round(max(b["t"])), "low": round(min(b["t"])),
                    "sky": max(set(b["sky"]), key=b["sky"].count) if b["sky"] else "—", "rain": None, "wind": round(max(b["wind"]))})
    return out


def wttr(n):
    j = get("https://wttr.in/Cairo?format=j1")
    return [{"date": d["date"], "high": int(d["maxtempC"]), "low": int(d["mintempC"]), "sky": d["hourly"][4]["weatherDesc"][0]["value"].strip().lower(),
             "rain": max(int(h.get("chanceofrain", 0)) for h in d["hourly"]), "wind": max(int(h["windspeedKmph"]) for h in d["hourly"])} for d in j["weather"][:n]]


def main(args):
    n = int(args[0]) if args else 4
    got = []
    for name, fn in (("Open-Meteo", open_meteo), ("MET Norway", met_norway), ("wttr.in", wttr)):
        if len(got) == 2:
            break
        try:
            got.append((name, {d["date"]: d for d in fn(n)}))
        except Exception as e:
            print(f"{name}: unavailable ({e})")
    if not got:
        sys.exit("No forecast service answered: take the forecast from the Egyptian Meteorological Authority and one other outlet.")
    dates = sorted(set().union(*[set(g) for _, g in got]))[:n]
    for day in dates:
        dd = datetime.date.fromisoformat(day)
        parts = []
        for name, g in got:
            x = g.get(day)
            if x:
                parts.append(f"{name}: {x['high']}°C / {x['low']}°C, {x['sky']}" + (f", rain {x['rain']}%" if x["rain"] is not None else "") + f", wind up to {x['wind']} km/h")
        highs = [g[day]["high"] for _, g in got if day in g]
        flag = "  <- the services differ by more than 2°C: give a range" if len(highs) == 2 and abs(highs[0] - highs[1]) > 2 else ""
        print(f"{dd:%a %b} {dd.day}: " + " | ".join(parts) + flag)


if __name__ == "__main__":
    main(sys.argv[1:])
