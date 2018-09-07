
using System;
using System.Collections.Generic;
using System.Text;

namespace TrialProject.src {
    public class GridTag{
        public static string typeLand = "Land";
        public static string attributionEmpty = "Empty";
    }
    public class PixelGrid {
        private string type;
        private string attribution;
        private int value;
        public PixelGrid() { }
        public PixelGrid(String ptype = "Land", String attribution = "empty", int value = 1){
            Type = ptype;
            Attribution = attribution;
            Value = value;
        }
        public string Type { get => type; set => type = value; }
        public string Attribution { get => attribution; set => attribution = value; }
        public int Value { get => value; set => this.value = value; }

        private string Dict()
        {
            return "abc";
        }
    }
}