using System;
using Newtonsoft.Json;

namespace TrialProject.src{
    public class PixelFightSystem
    {
        public String NetworkSev;
        public String Game;
        public PixelFightSystem() { }
        public PixelFightSystem(String ip, String port)
        {
            NetworkSev = netWorkService(ip, port);
            Game = pixelFightGame();
        }
        private string pixelFightGame()
        {
            throw new NotImplementedException();
        }
        private string netWorkService(string ip, string port)
        {
            throw new NotImplementedException();
        }
    }
}