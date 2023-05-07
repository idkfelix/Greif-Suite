from wrapper import *

from time import sleep

class Tools():

    def SetConfig(uregion,ushard):
        uconfig = f"""
        region: {uregion}
        shard: {ushard}
        """

        if not os.path.exists(os.getenv("LOCALAPPDATA")+"\GreifSuite"):
            os.makedirs(os.getenv("LOCALAPPDATA")+"\GreifSuite")
        else:
            with open(os.getenv("LOCALAPPDATA")+"\GreifSuite\config.yaml", "w") as f:
                f.write(uconfig)

    def Spammer(count, text, cid):
        for i in range (0,count):
            Chat.Message(cid, text)

    def Counter():
        for i in range (0,999):
            Chat.Message(Chat.getGameCid(), str(i))

    def Instalock(AgentID):
        Match.AgentLock(Get.PreMatchID(), AgentID)

    def WheelOfFortune(AgentList):
        preMatchID = Get.PreMatchID()
        while True:
            for Agent in AgentList:
                Match.AgentSelect(preMatchID(), Agent)
                sleep(0.1)
