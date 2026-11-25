import asyncio
import sys

import httpx


async def check_example() -> int:
    async with httpx.AsyncClient(
        timeout=5.0,
        follow_redirects=False,
    ) as client:
        response = await client.get("https://example.com/")
        return response.status_code


def main() -> int:
    try:
        status_code = asyncio.run(check_example())
    except httpx.TimeoutException as exc:
        print(f"Request timed out: {type(exc).__name__}", file=sys.stderr)
        return 1
    except httpx.RequestError as exc:
        print(f"Request failed: {type(exc).__name__}", file=sys.stderr)
        return 1

    print(f"HTTP status: {status_code}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
