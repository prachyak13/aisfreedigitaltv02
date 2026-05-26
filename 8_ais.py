import asyncio, json
from playwright.async_api import async_playwright

async def run_automation():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = await browser.new_page()
        await page.goto("https://app.ais-vidnt.com/portal/live", wait_until="load", timeout=60000)
        
        await page.click("text=เข้าใช้งานแบบไม่ลงทะเบียน")
        await page.locator("button:has-text('ตกลง')").click(force=True)
        await asyncio.sleep(5)
        
        data = {}
        for ch in ["23", "2"]:
            await page.click(f"text={ch}")
            await asyncio.sleep(3)
            data[ch] = page.url
            
        with open("links.json", "w") as f:
            json.dump(data, f)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_automation())
