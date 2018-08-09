using System;
using Newtonsoft.Json;

namespace TrialProject.src{
    public class NetworkService{
        private string hostIp;
        private string port;
        private string socket;

        private void SocketBind() { }

        public NetworkService(String ip, String _p){
            HostIp = ip;
            Port = _p;
        }
        public NetworkService() { }
        public int MaxConnect = 512;
        public string HostIp { get => hostIp; set => hostIp = value; }
        public string Port { get => port; set => port = value; }
        public string Socket { get => socket; set => socket = value; }
    }

}