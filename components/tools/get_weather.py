from __future__ import annotations

from typing import Any

import httpx
from langbot_plugin.api.definition.components.tool.tool import Tool
from langbot_plugin.api.entities.builtin.provider import session as provider_session


class GetWeather(Tool):

    async def call(
        self,
        params: dict[str, Any],
        session: provider_session.Session,
        query_id: int,
    ) -> str:
        city = params.get("city", "Beijing")

        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(
                f"https://wttr.in/{city}",
                params={"format": "%C|%t|%h|%w|%S|%u"},
            )
            text = resp.text.strip()

        parts = text.split("|")
        if len(parts) >= 5:
            condition, temp, humidity, wind, sunrise = parts[0], parts[1], parts[2], parts[3], parts[4]
            return (
                f"{city} 实时天气：\n"
                f"🌤 天气：{condition}\n"
                f"🌡 温度：{temp}\n"
                f"💧 湿度：{humidity}\n"
                f"💨 风速：{wind}\n"
                f"🌅 日出/日落：{sunrise}"
            )
        return f"{city} 当前天气：{text}"
