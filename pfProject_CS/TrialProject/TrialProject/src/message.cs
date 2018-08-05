using System;
using System.Collections.Generic;
using System.Text;

namespace TrialProject.src {
    public class MessageType {
        public static String loginRequest = "LoginRequest";
        public static String loginReply = "LoginReply";
    }
    public class LoginRequest {
        private String msgType;
        private String usrName;


        public string UsrName { get => usrName; set => usrName = value; }
        public string MsgType { get => msgType; set => msgType = value; }
        public LoginRequest() { }
        public LoginRequest(String _info, bool _isJson = false) {
            if (_isJson) {
                parseJson(_info);
            } else {
                this.MsgType = MessageType.loginRequest;
                this.UsrName = UsrName;
            }

        }

        private void parseJson(String _s) {

        }
    }

    public class LogReply {
        private String msgType;
        private String id;

        public string MsgType { get => msgType; set => msgType = value; }
        public string Id { get => id; set => id = value; }

        public LogReply() { }
        public LogReply(String _info, bool _isJson = false) {
            if (_isJson) {
                parseJson(_info);
            } else {
                this.msgType = MessageType.loginReply;
                this.Id = _info;

            }
        }

        private void parseJson(String _s) {

        }
    }
    public class PlayerCommand {
        private String msgType;
        private String playerId;
        private String x;
        private String y;
        public PlayerCommand(String x, String y) {


        }
        public PlayerCommand(String json_info) {
            parseJson(json_info);
        }

        private void parseJson(String _s) { }

    }
}

