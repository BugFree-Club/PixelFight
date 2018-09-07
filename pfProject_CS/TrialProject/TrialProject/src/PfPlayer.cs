using System;

namespace TrialProject.src{
    public class PixelFightPlayer{
        private string usrName;
        private string loginId;
        private string socketInfo;
        public PixelFightPlayer(String usrName, String loginId, String socket){
            UsrName = usrName;
            LoginId = loginId;
            SocketInfo = socket;
        }
        public PixelFightPlayer() { }
        public string UsrName { get => usrName; set => usrName = value; }
        public string LoginId { get => loginId; set => loginId = value; }
        public string SocketInfo { get => socketInfo; set => socketInfo = value; }

        
    }
}