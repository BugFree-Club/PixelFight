using System;
using System.Collections.Generic;
using System.Text;
using Newtonsoft.Json;

namespace TrialProject.src {
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
                UsrName = UsrName;
            }
        }

        private void ParseJson(String _s) {
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

        private void ParseJson(String _s) { }
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
        public string MsgType = "MsgType";
    }

/*
*   LoginRequest
    lr_usr_name = u'usr_name'
    LoginReply
    lre_login_id = u'login_id'
    PlayCommand
    pc_player_id = u'player_id'
    pc_target_x = u'target_x'
    pc_target_y = u'target_y'
    GameInfo
    gi_map_info = u'map_info'
    gi_round = u'round'
    pfRule
    pfr_max_round = u'max_round'
    pfr_map_height = u'map_height'
    pfr_map_width = u'map_width'
    pfr_player_num = u'player_num'
    pfr_empty_grid_time = u'empty_grid_time'
     pfr_player_grid_time = u'player_grid_time'
*/
}

