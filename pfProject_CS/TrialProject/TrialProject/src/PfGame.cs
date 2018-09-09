using System;

namespace TrialProject.src
{
    public class PixelFightGame
    {
        private string gameRule;
        private string playerInfoList;
        private string pixelFightMap;
        private string perPosList;
        private string visionManager;
        private bool isPause;
        private bool isReady;
        private int gameRatio;
        private int roundCounter;
        private int _mw;
        private int _mh;
        public PixelFightGame()
        {
            GameRule = pixelFightRule(_mw = 30, _mh = 30);
            RoundCounter = 0;
            GameRatio = 0;
            PlayerInfoList = null;
            PixelFightMap = pixelMap();
            PerPosList = null;
            VisionManager = null;
            IsPause = false;
            IsReady = false;
        }
        private string pixelMap()
        {
            throw new NotImplementedException();
        }
        private string pixelFightRule(int _mw, int _mh)
        {
            throw new NotImplementedException();
        }

        public string GameRule { get => gameRule; set => gameRule = value; }
        public string PlayerInfoList { get => playerInfoList; set => playerInfoList = value; }
        public string PixelFightMap { get => pixelFightMap; set => pixelFightMap = value; }
        public string PerPosList { get => perPosList; set => perPosList = value; }
        public string VisionManager { get => visionManager; set => visionManager = value; }
        public bool IsPause { get => isPause; set => isPause = value; }
        public bool IsReady { get => isReady; set => isReady = value; }
        public int RoundCounter { get => roundCounter; set => roundCounter = value; }
        public int GameRatio { get => gameRatio; set => gameRatio = value; }

        
    }
}