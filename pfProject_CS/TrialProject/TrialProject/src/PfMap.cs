using System;
using Newtonsoft.Json;

namespace TrialProject.src{
    public class PixelMap{
        private String height;
        private string width;
        private string gridMap;
        public PixelMap(String _info, String mapHeight, String mapWidth, bool _isJson = false){
            if (_isJson){
                ParseJson(_info);
            }
            else {
                Height = mapHeight;
                Width = mapWidth;
                GridMap = null;
            }
        }
        public PixelMap() { }
        public string Height { get => height; set => height = value; }
        public string Width { get => width; set => width = value; }
        public string GridMap { get => gridMap; set => gridMap = value; }
        public string tmpMapList;
        private void ParseJson(String _s) {
            PixelMap tmp_r = JsonConvert.DeserializeObject<PixelMap>(_s);
            this.height = tmp_r.Height;
            this.width = tmp_r.Width;
            this.tmpMapList = tmp_r.GridMap;
        }
        private string DumpJson() {
            return JsonConvert.SerializeObject(this);
        }
    }
}