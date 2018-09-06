using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using System.Web;

namespace TrialProject.src {

    public class LoginRequest {
        private String msgType;
        private String usrName;

        public string UsrName { get => usrName; set => usrName = value; }
        public string MsgType { get => msgType; set => msgType = value; }
        public LoginRequest() { }
        public LoginRequest(String _info, String uname, bool _isJson = false) {
            if (_isJson) {
                ParseJson(_info);
            } else {
                MsgType = MessageType.loginRequest;
                UsrName = uname;
            }
        }
        public void ParseJson(String _s) {
            LoginRequest tmp_r = JsonConvert.DeserializeObject<LoginRequest>(_s);
            this.msgType = tmp_r.MsgType;
            this.usrName = tmp_r.UsrName;
        }

        public String DumpJson() {
            return JsonConvert.SerializeObject(this);
        }
    }

    public class LoginReply {
        private String msgType;
        private string loginId;
        public string MsgType { get => msgType; set => msgType = value; }
        public string LoginId { get => loginId; set => loginId = value; }

        
        public LoginReply() { }
        public LoginReply(String _info, String id, bool _isJson = false) {
            if (_isJson) {
                ParseJson(_info);
            } else {
                MsgType = MessageType.loginReply;
                LoginId = id;
            }
        }

        private void ParseJson(String _s) {
            LoginReply tmp_r = JsonConvert.DeserializeObject<LoginReply>(_s);
            this.msgType = tmp_r.MsgType;
            this.loginId = tmp_r.LoginId;
        }

        private string DumpJson() {
            return JsonConvert.SerializeObject(this);
        }
    }

    public class AttackRequest {
        private string msgType;
        private string playerId;
        private int targetY;
        private int targetX;
        public AttackRequest() { }
        public AttackRequest(String _info, int x, int y, String playerId, bool _isJson = false) {
            if (_isJson){
                ParseJson(_info);
            } else{
                MsgType = MessageType.attackRequest;
                PlayerId = playerId;
                TargetX = x;
                TargetY = y;
            }
        }

        public string MsgType { get => msgType; set => msgType = value; }
        public string PlayerId { get => playerId; set => playerId = value; }
        public int TargetX { get => targetX; set => targetX = value; }
        public int TargetY { get => targetY; set => targetY = value; }

        
        private void ParseJson(String _s) {
            AttackRequest tmp_r = JsonConvert.DeserializeObject<AttackRequest>(_s);
            this.msgType = tmp_r.MsgType;
            this.playerId = tmp_r.PlayerId;
            this.targetX = tmp_r.TargetX;
            this.targetY = tmp_r.TargetY;
        }   

        private string DumpJson(){
            return JsonConvert.SerializeObject(this);
        }
    }

    public class AttackReply {
        private string msgType;
        private string isSuc;

        public AttackReply() { }
        public AttackReply(String _info, String isSuc, bool _isJson = false) {
            if (_isJson) {
                ParseJson(_info);
            }
            else {
                MsgType = MessageType.attackReply;
                IsSuc = isSuc;
            }
        }

        private void ParseJson(String _s){
            AttackReply tmp_r = JsonConvert.DeserializeObject<AttackReply>(_s);
            msgType = tmp_r.MsgType;
            isSuc = tmp_r.IsSuc;
        }

        private string DumpJson(){
            return JsonConvert.SerializeObject(this);
        }

        public string MsgType { get => msgType; set => msgType = value; }
        public string IsSuc { get => isSuc; set => isSuc = value; }
    }
    public class GameInfo{
        private string msgType;
        private string mapInfo;
        private string perPos;
        private int round;
        public GameInfo(String _info, String pfMap, int pfRound, String perPos, bool _isJson = false) {
            if (_isJson){
                ParseJson(_info);
            }
            else {
                MsgType = MessageType.gameInfo;
                MapInfo = pfMap;
                PerPos = perPos;
                Round = pfRound;
            }
                }
        public string MsgType { get => msgType; set => msgType = value; }
        public string MapInfo { get => mapInfo; set => mapInfo = value; }
        public string PerPos { get => perPos; set => perPos = value; }
        public int Round { get => round; set => round = value; }

        private void ParseJson(String _s) {
            GameInfo tmp_r = JsonConvert.DeserializeObject<GameInfo>(_s);
            msgType = tmp_r.MsgType;
            mapInfo = tmp_r.MapInfo;
            perPos = tmp_r.PerPos;
            round = tmp_r.Round;
        }

        private string DumpJson() {
            return JsonConvert.SerializeObject(this);
        }

        private string GetMsgType(String _s){
            GameInfo tmp_s = JsonConvert.DeserializeObject<GameInfo>(_s);
            return tmp_s.MsgType;
        }
    }
}

