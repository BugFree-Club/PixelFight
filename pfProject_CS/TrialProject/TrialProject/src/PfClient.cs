using System;
using Newtonsoft.Json;

namespace TrialProject.src{
    public class PixelFightClient {
        private string serverIp;
        private string serverPort;
        private string usrName;
        private string loginId;
        private string pfMap;
        private string message;
        public PixelFightClient(String usrName, String ip = "127.0.0.1", int port = 7707) {
            ServerIp = ip;
            ServerPort = port;
            UsrName = usrName;
            LoginId = null;
            PfMap = null;
            IsBusy = false;
            Message = null;
            CurRound = 0;
        }
        public PixelFightClient() { }
        public string ServerIp { get => serverIp; set => serverIp = value; }
        public string UsrName { get => usrName; set => usrName = value; }
        public string LoginId { get => loginId; set => loginId = value; }
        public string PfMap { get => pfMap; set => pfMap = value; }
        public string Message { get => message; set => message = value; }
        public bool IsBusy;
        public int CurRound;
        public int ServerPort;
        public string ClientSocket;
        public void Request(String msg) { }
        private string loginRequest() {
            return "abc";
        }       
    }
}
