using System;
using TrialProject.src;

namespace TrialProject {
    class Program {
        static void Main(string[] args) {
            Console.WriteLine("Test Code");
            // Test PfMessage.LoginRequest
            LoginRequest tmp_lr = new LoginRequest("ZJB");
            Console.WriteLine(tmp_lr.MsgType);
            Console.WriteLine(tmp_lr.UsrName);
            String json_info = tmp_lr.dumpJson();
            Console.WriteLine(json_info);
            LoginRequest tmp_lr2 = new LoginRequest(json_info, true);
            Console.WriteLine(tmp_lr2.MsgType);
            Console.WriteLine(tmp_lr2.UsrName);
            tmp_lr2.UsrName = "TC";
            Console.WriteLine(tmp_lr2.UsrName);
            Console.ReadKey();

        }
    }
}
