using System;

namespace TrialProject.src{
    public class MessageType{
        public static String loginRequest = "LoginRequest";
        public static String loginReply = "LoginReply";
        public static String attackRequest = "AttackRequest";
        public static String attackReply = "AttackReply";
        public static String gameInfo = "GameInfo";
    }
    public class JsonAttribute
    {
        public static String msgType = "MsgType";
        //LoginRequest
        public static String lrUsrName = "UsrName";
        //LoginReply
        public static String lreLoginId = "LoginId";
        //AttackRequest
        public static String arPlayerId = "PlayerId";
        public static String arTargetX = "TargetX";
        public static String arTargetY = "TargetY";
        //AttackReply
        public static String arIsSuc = "IsSuc";
        //GameInfo
        public static String giMapInfo = "MapInfo";
        public static String giRound = "Round";
        public static String giPerPos = "PerPos";
        //PfRule
        public static String pfrMaxRound = "MaxRound";
        public static String pfrMapHeight = "MapHeight";
        public static String pfrMapWidth = "MapWidth";
        public static String pfrPlayerNum = "PlayerNum";
        public static String pfrEmptyGridTime = "EmptyGridTime";
        public static String pfrPlayerGridTime = "PlayerGridTime";
        //PfMap
        public static String pfmHeight = "Height";
        public static String pfmWidth = "Width";
        public static String pfmGridMap = "GridMap";
        //PfGrid
        public static String pfgType = "Type";
        public static String pfgAttrbution = "Attribution";
        public static String pfgValue = "Value";
    }

}