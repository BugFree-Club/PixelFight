using System;

namespace TrialProject.src{
    public class PixelFightPlayer{
        private string usrName;
        private string loginId;
        public PixelFightPlayer(String usrName, String loginId){
            UsrName = usrName;
            LoginId = loginId;
        }
        public PixelFightPlayer() { }
        public string UsrName { get => usrName; set => usrName = value; }
        public string LoginId { get => loginId; set => loginId = value; }
    }
}