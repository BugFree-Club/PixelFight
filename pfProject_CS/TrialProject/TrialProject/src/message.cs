using System;
using System.Collections.Generic;
using System.Text;

namespace TrialProject.src
{
    public class LoginRequest
    {
        private String usr_name;
        private String msg_type;
     
        public LoginRequest (String uname)
        {
            this.Usr_name = usr_name;
            this.Msg_type = MessageType.login_request;
        }

        public LoginRequest(String json_info)
        {
            parse_json(json_info);
        }
        public LoginRequest()
        { }
        public string Usr_name { get => usr_name; set => value; };
        public string Msg_type { get; set; };

        private void parse_json(String _s)
        {
            
        }
    }

    public class LogReply
    {
        private String id;
        public LogReply(String id)
        {
            this.Login_id = id;
            this.Msg_type = Message.login.request;
        }
        public LogReply(String json_info)
        {
            parse_json(json_info);
        }
        public LogReply()
        { }
        public string Login_id {get => id; set => value;};
        private void parse_json(String _s)
        {
            
        }
    }
    public class PlayerCommand
    {
        private String x;
        private String y;
        public PlayerCommand(String x, String y)
        {
            this.Target_x = x;
            this.Target_y = y;
            this.Player_id = null;
            this.Msg_type = MessageType.login_request;

        }
        public PlayerCommand(String json_info)
        {
            prase_json(json_info);
        }
        public PlayerCommand()
        { }
        public string Target_x { get; set; };
        public string Target_y { get; set; };
        private parse_json(String _s)
        { }

    }
}

