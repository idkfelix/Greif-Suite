from wrapper import *

from time import sleep

class Tools():

    def Spammer(count, text, cid):

        for i in range (0,count):
            Chat.Message(cid, text)

    def Instalock(AgentID):
        Match.AgentLock(Get.PreMatchID(), AgentID)

    def WheelOfFortune(AgentList):
        preMatchID = Get.PreMatchID()
        while True:
            for Agent in AgentList:
                Match.AgentSelect(preMatchID, Agent)
                sleep(0.1)
