from fastapi import FastAPI
import uvicorn

app = FastAPI()

import mysql.connector


@app.get("/api/robloxwhitelist/{robloxid}")
def index(robloxid: str):
    connection = mysql.connector.connect(
        host="54.38.50.59",
        user="www14268_weryfikacjabot",
        password="QggMg3pNufpKbr3gGWr9",
        database="www14268_weryfikacjabot")

    cursor = connection.cursor()

    cursor.execute(
        f"SELECT DiscordID, NickDiscord, Verified FROM tykocin WHERE RobloxID = '{robloxid}';"
    )

    results = cursor.fetchall()

    print(results)
    if results:

        return {
            'DiscordID': results[0][0],
            "DiscordNick": results[0][1],
            "Verified": results[0][2]
        }
    else:
        return {"Not found"}

    cursor.close()
    connection.close()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
