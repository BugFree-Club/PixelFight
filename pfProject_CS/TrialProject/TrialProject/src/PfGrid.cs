using System;
using System.Collections.Generic;
using System.Text;

namespace TrialProject.src {
    class PFGrid {
        private String type;
        private String attribution;
        private int value;

        public PFGrid() {

        }

        public PFGrid(String _t,String _a,int _v) {
            Type = _t;
            Attribution = _a;
            Value = _v;
        }

        public string Type { get => type; set => type = value; }
        public string Attribution { get => attribution; set => attribution = value; }
        public int Value { get => value; set => this.value = value; }
    }
}