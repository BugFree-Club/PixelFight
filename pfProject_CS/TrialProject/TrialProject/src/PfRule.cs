using System;
using Newtonsoft.Json;

namespace TrialProject.src{
    public class PixelFightRule{
        private int maxRound;
        private int mapHeight;
        private int mapWidth;
        private int playerNum;
        private int emptyGridTime;
        private int playerGridTime;
        private int waitTime;
        public PixelFightRule() { }
        public PixelFightRule(int _mr = 1000, int _mh = 0, int _mw = 0, int _pn = 1, int _egt = 0, int _pgr = 0) {
            MaxRound = _mr;
            MapHeight = _mh;
            MapWidth = _mw;
            PlayerNum = _pn;
            EmptyGridTime = _egt;//占领网格时间
            PlayerGridTime = _pgr;//占领玩家网格时间
            WaitTime = 1;
        }
        public int MaxRound { get => maxRound; set => maxRound = value; }
        public int MapHeight { get => mapHeight; set => mapHeight = value; }
        public int MapWidth { get => mapWidth; set => mapWidth = value; }
        public int PlayerNum { get => playerNum; set => playerNum = value; }
        public int EmptyGridTime { get => emptyGridTime; set => emptyGridTime = value; }
        public int PlayerGridTime { get => playerGridTime; set => playerGridTime = value; }
        public int WaitTime { get => waitTime; set => waitTime = value; }

        private string DumpJson(){
            return JsonConvert.SerializeObject(this);
        }

        private void OutPut(){

        }

        private void Load(String _path)
        {
            PixelFightRule tmp_dic = JsonConvert.DeserializeObject<PixelFightRule>(_path);
            maxRound = tmp_dic.MaxRound;
            mapHeight = tmp_dic.MapHeight;
            mapWidth = tmp_dic.MapWidth;
            playerNum = tmp_dic.PlayerGridTime;
            emptyGridTime = tmp_dic.EmptyGridTime;
            playerGridTime = tmp_dic.PlayerGridTime;
        }
    }
}
