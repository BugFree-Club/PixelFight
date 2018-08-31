using System;
using Newtonsoft.Json;
public class PixelFightRule {
    private string maxRound;
    private int mapHeight;
    private int mapWidth;
    private string playerNum;
    private string emptyGridTime;
    private string playerGridTime;
    public PixelFightRule(String _mr, String _pn, String _egt, String _pgr) {
        MaxRound = _mr;
        PlayerNum = _pn;
        EmptyGridTime = _egt;
        PlayerGridTime = _pgr;
    }
    public PixelFightRule(int _mh = 0, int _mw = 0) {
        MapHeight = _mh;
        MapWidth = _mw;
    }
    public PixelFightRule() { }
    public string MaxRound { get => maxRound; set => maxRound = value; }
    public string PlayerNum { get => playerNum; set => playerNum = value; }
    public string EmptyGridTime { get => emptyGridTime; set => emptyGridTime = value; }
    public string PlayerGridTime { get => playerGridTime; set => playerGridTime = value; }
    public int MapHeight { get => mapHeight; set => mapHeight = value; }
    public int MapWidth { get => mapWidth; set => mapWidth = value; }

    private void Dict() { }
    private void DumpJson() { }
    private void OutPut(String fName) { }
    private void Load(String _path) { }
}