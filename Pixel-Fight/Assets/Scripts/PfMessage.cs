using System;
using System.Collections.Generic;
using Newtonsoft.Json;

    public class MessageType {
        public static String loginRequest = "LoginRequest";
        public static String loginReply = "LoginReply";
        public static String playerCommand = "PlayerCommand";
        public static String gameInfo = "GameInfo";
    }

public class LoginRequest {
    private String msgType;
    private String usrName;

    public string UsrName { get => usrName; set => usrName = value; }
    public string MsgType { get => msgType; set => msgType = value; }
    public LoginRequest() { }
    public LoginRequest(String _info, bool _isJson = false) {
        if (_isJson) {
            ParseJson(_info);
        } else {
            MsgType = MessageType.loginRequest;
            UsrName = _info;
        }
    }
    public void ParseJson(String _s) {
        LoginRequest tmp_r = JsonConvert.DeserializeObject<LoginRequest>(_s);
        this.msgType = tmp_r.MsgType;
        this.usrName = tmp_r.UsrName;
    }

    public String dumpJson() {
        return JsonConvert.SerializeObject(this);
    }
}

    public class LoginReply {
        private String msgType;
        private string id1;
        public string MsgType { get => msgType; set => msgType = value; }
        public string Id { get => id1; set => id1 = value; }

        public LoginReply() { }
        public LoginReply(String _info, bool _isJson = false) {
            if (_isJson) {
                ParseJson(_info);
            } else {
                MsgType = MessageType.loginReply;
                Id = Id;
            }
        }

        private void ParseJson(String _s) {

        }
    }

    public class PlayerCommand {
        private string msgType;
        private string playerId;
        private string targetX;
        private string targetY;

        public PlayerCommand() { }
        public PlayerCommand(String _info, bool _isJson = false) {
            if (_isJson){
                ParseJson(_info);
            } else{
                MsgType = MessageType.playerCommand;
                PlayerId = null;
                TargetX = TargetX;
                TargetY = TargetY;
            }
        }

        public string MsgType { get => msgType; set => msgType = value; }
        public string PlayerId { get => playerId; set => playerId = value; }
        public string TargetX { get => targetX; set => targetX = value; }
        public string TargetY { get => targetY; set => targetY = value; }

        private void ParseJson(String _s) { }   
    }

    public class GameInfo{
        private string msgType;
        private string mapInfo;
        private string round;
        public GameInfo(String _info, bool _isJson = false) {
            if (_isJson){
                ParseJson(_info);
            }
            else {
                MsgType = MessageType.gameInfo;
                MapInfo = MapInfo;
                Round = Round;
            }
                }
        public string MsgType { get => msgType; set => msgType = value; }
        public string MapInfo { get => mapInfo; set => mapInfo = value; }
        public string Round { get => round; set => round = value; }

        private void ParseJson(String _s) { }
    }

public class JsonAttribute {
    public static String msgType = "MsgType";
    //LoginRequest
    public static String lrUsrName = "UsrName";
    //LoginReply
    public static String lreLoginId = "LoginId";
    //PlayerCommand
    public static String pcPlayerId = "PlayerId";
    public static String pcTargetX = "TargetX";
    public static String pcTargetY = "TargetY";
    //GameInfo
    public static String giMapInfo = "MapInfo";
    public static String giRound = "Round";
    //PfRule
    public static String pfrMaxRound = "MaxRound";
    public static String pfrMapHeight = "MapHeight";
    public static String pfrMapWidth = "MapWidth";
    public static String pfrPlayerNum = "PlayerNum";
    public static String pfrEmptyGridTime = "EmptyGridTime";
    public static String pfrPlayerGridTime = "PlayerGridTime";
}