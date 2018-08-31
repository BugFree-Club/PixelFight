using System;

public class PixelMap {
    private String height;
    private string width;
    private string gridMap;
    public PixelMap(String _h, String _w) {
        Height = _h;
        Width = _w;
        GridMap = null;
    }
    public PixelMap() { }
    public string Height { get => height; set => height = value; }
    public string Width { get => width; set => width = value; }
    public string GridMap { get => gridMap; set => gridMap = value; }
}