import requests
from bs4 import BeautifulSoup

async def sozlar_manosi(soz: str):
    response = requests.get(f"https://izoh.uz/word/{soz}")
    soup = BeautifulSoup(response.text, "html.parser")
    turi = soup.find("div", class_="italic").text.replace("  ", "").replace("\n", "").strip()
    manosi = soup.find("p", class_="font-bold").text.replace("  ", "").replace("\n", "").strip()
    misollar = soup.find("ol", class_="list-disc pl-10 space-y-1")
    soup2 = BeautifulSoup(misollar.prettify(), "html.parser")
    tayyor_misollar = [misol.text.replace("  ", "").replace("\n", "").strip() for misol in soup2.find_all("li")]
    sozni_teskarisi = tayyor_misollar[::-1]
    return {"so'z": soz, "turi": turi, "manosi": manosi, "misollar": tayyor_misollar, "sozni_teskarisi": sozni_teskarisi}
